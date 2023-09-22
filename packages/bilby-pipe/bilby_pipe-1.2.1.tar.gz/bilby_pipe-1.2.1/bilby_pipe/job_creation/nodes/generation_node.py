import os

from ...utils import DataDump, default_frame_type, log_function_call, logger
from ..node import Node


class GenerationNode(Node):
    def __init__(self, inputs, trigger_time, idx, dag, parent=None):
        """
        Node for data generation jobs

        Parameters:
        -----------
        inputs: bilby_pipe.main.MainInput
            The user-defined inputs
        trigger_time: float
            The trigger time to use in generating analysis data
        idx: int
            The index of the data-generation job, used to label data products
        dag: bilby_pipe.dag.Dag
            The dag structure
        parent: bilby_pipe.job_creation.node.Node (optional)
            Any job to set as the parent to this job - used to enforce
            dependencies
        """

        super().__init__(inputs, retry=3)
        self.inputs = inputs
        self.trigger_time = trigger_time
        self.inputs.trigger_time = trigger_time
        self.idx = idx
        self.dag = dag
        self.request_cpus = 1

        self.setup_arguments()
        self.arguments.add("label", self.label)
        self.arguments.add("idx", self.idx)
        self.arguments.add("trigger-time", self.trigger_time)
        if self.inputs.injection_file is not None:
            self.arguments.add("injection-file", self.inputs.injection_file)
        if self.inputs.timeslide_file is not None:
            self.arguments.add("timeslide-file", self.inputs.timeslide_file)

        if self.inputs.transfer_files or self.inputs.osg:
            input_files_to_transfer = list()
            input_files_to_transfer.extend(self.resolve_frame_files)
            for attr in [
                "complete_ini_file",
                "prior_file",
                "injection_file",
                "gps_file",
                "timeslide_file",
            ]:
                if (value := getattr(self.inputs, attr)) is not None:
                    input_files_to_transfer.append(str(value))
            for value in [
                self.inputs.psd_dict,
                self.inputs.spline_calibration_envelope_dict,
            ]:
                input_files_to_transfer.extend(self.extract_paths_from_dict(value))
            input_files_to_transfer.extend(self.inputs.additional_transfer_paths)
            for ii, fname in enumerate(input_files_to_transfer):
                if fname.startswith(f"{self.inputs.data_find_urltype}://"):
                    input_files_to_transfer[ii] = f"igwn+{fname}"
            self.extra_lines.extend(
                self._condor_file_transfer_lines(
                    input_files_to_transfer,
                    [self._relative_topdir(self.inputs.outdir, self.inputs.initialdir)],
                )
            )
            self.arguments.add("outdir", os.path.relpath(self.inputs.outdir))

        self.extra_lines.extend(self.igwn_scitoken_lines)

        self.process_node()
        if parent:
            self.job.add_parent(parent.job)

    @property
    def resolve_frame_files(self):
        """
        Resolve frame files from frame_type_dict and data_dict.
        For each detector, if the frame filepath(s) is given
        return the filepath(s), otherwise use gwdatafind to
        resolve the frame files using the provided frame type.

        Returns:
        --------
        list: list of frame filepaths
        """
        from gwdatafind import find_urls
        from requests.exceptions import HTTPError

        data = dict()
        if self.inputs.frame_type_dict is not None:
            data = self.inputs.frame_type_dict
        if self.inputs.data_dict is not None:
            data.update(self.inputs.data_dict)
        output = list()
        for det in self.inputs.detectors:
            if det not in data:
                try:
                    data[det] = default_frame_type(det, self.trigger_time)
                except ValueError:
                    raise ValueError(
                        f"Detector {det} not found in frame_type_dict or data_dict "
                        "cannot resolve frame files."
                    )
            if isinstance(data[det], list):
                output.extend(data[det])
            elif os.path.exists(data[det]):
                output.append(data[det])
            else:
                start_time = self.inputs.start_time
                end_time = self.inputs.start_time + self.inputs.duration
                if self.inputs.psd_dict is None or not all(
                    det in self.inputs.psd_dict for det in self.inputs.detectors
                ):
                    start_time -= self.inputs.psd_duration
                kwargs = dict(
                    site=det[0],
                    frametype=data[det],
                    gpsstart=start_time,
                    gpsend=end_time,
                    urltype=self.inputs.data_find_urltype,
                    host=self.inputs.data_find_url,
                )
                log_function_call("gwdatafind.find_urls", kwargs)
                try:
                    output.extend(find_urls(**kwargs))
                except HTTPError:
                    logger.warning(f"Failed to resolve frame files for detector {det}")
        return output

    @staticmethod
    def extract_paths_from_dict(input):
        output = list()
        if isinstance(input, dict):
            for value in input.values():
                output.append(value)
        return output

    @property
    def executable(self):
        return self._get_executable_path("bilby_pipe_generation")

    @property
    def request_memory(self):
        return self.inputs.request_memory_generation

    @property
    def log_directory(self):
        return self.inputs.data_generation_log_directory

    @property
    def universe(self):
        if self.inputs.local_generation:
            logger.debug(
                "Data generation done locally: please do not use this when "
                "submitting a large number of jobs"
            )
            universe = "local"
        else:
            logger.debug(f"All data will be grabbed in the {self._universe} universe")
            universe = self._universe
        return universe

    @property
    def job_name(self):
        job_name = "{}_data{}_{}_generation".format(
            self.inputs.label, str(self.idx), self.trigger_time
        )
        job_name = job_name.replace(".", "-")
        return job_name

    @property
    def label(self):
        return self.job_name

    @property
    def data_dump_file(self):
        return DataDump.get_filename(self.inputs.data_directory, self.label)

    @property
    def igwn_scitoken_lines(self):
        permissions = list()
        if any(det in self.inputs.detectors for det in ["H1", "L1"]):
            permissions.append("read:/ligo")
        if "V1" in self.inputs.detectors:
            permissions.append("read:/virgo")
        if "K1" in self.inputs.detectors:
            permissions.append("read:/kagra")
        return [
            "use_oauth_services = igwn",
            f"igwn_oauth_permissions = {' '.join(permissions)}",
        ]
