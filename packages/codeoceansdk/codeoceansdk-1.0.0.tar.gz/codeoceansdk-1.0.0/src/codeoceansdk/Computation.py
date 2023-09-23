import logging
from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

from codeoceansdk.CodeOcean import CodeOcean

logger = logging.getLogger(__name__)


@dataclass(frozen=True, slots=True)
class Parameter:
    """
    Parameters used during computation
    """
    name: str = None
    """Parameter name"""
    value: str = None
    """Parameter value"""


@dataclass(frozen=True, slots=True)
class File:
    """
    File metadata
    """

    name: str
    """File name"""
    path: str
    """File full path"""
    type: Enum("type", ["file", "folder"])
    """File type (file or folder)"""
    size: int = None
    """Item size in bytes (only available for files)"""


@dataclass(kw_only=True)
class Computation(CodeOcean):
    """Computation from a capsule"""
    id: str
    """Computation internal id"""
    parameters: Optional[list[Parameter]] = field(default_factory=list)
    """List of run parameters"""
    created: int = 0
    """Computation creation time"""
    name: str = None
    """Display name of the computation"""
    run_time: int = 0
    """Total run time in seconds"""
    has_results: bool = False
    """Indicates whether the computation has results."""
    state: Enum(
        "state", ["initializing", "running", "finalizing", "completed"]
    ) = "completed"
    """Current status"""
    end_status: Enum("end_status", ["stopped", "failed", "succeeded"]) = None
    """Status after completion."""
    cloud_workstation: bool = None
    """Generated from cloud workstation"""

    def __post_init__(self):
        super().__post_init__()
        self.computation_url = f"{self.api_url}/computations/{self.id}"

    @staticmethod
    def from_dict(computation_dict: dict, domain: str, api_key):
        """
        Parse dictionary to Computation object

        :param api_key: Capsule API
        :param domain: Code Ocean domain
        :param computation_dict:  Input dictionary of computation parameters.
        :return: Computation object.
        """
        if "parameters" in computation_dict:
            computation_dict["parameters"] = [
                Parameter(**x) for x in computation_dict["parameters"]
            ]
        computation_dict["domain"] = domain
        computation_dict["api_key"] = api_key
        return Computation(**computation_dict)

    def list_computation_result_files(self):
        """
        List results for a particular computation.

        :return: List of files.
        """
        logger.debug(f"Retrieving all files from computation ${self.id}")
        input_url = f"{self.computation_url}/results"
        logger.debug(f"Input url: {input_url}")
        req = self.post(input_url).json()
        if "items" in req:
            return [File(**x) for x in req["items"]]
        else:
            return None

    def get_download_url(self, file_name: str):
        """Get download url for curr_id run.

        :param file_name: File name
        :return: Pre-signed url to data file.
        """
        logger.debug(f"Retrieving {file_name} from computation ${self.id}")
        input_url = f"{self.computation_url}/results/download_url?path={file_name}"
        logger.debug(f"Input url: {input_url}")

        req = self.get(input_url).json()

        if "url" in req.keys():
            return req["url"]
        else:
            logging.debug(f"Unable to retrieve {file_name}")
            return None

    def get_computation(self):
        """
        Get computation metadata.
        """
        logger.debug(f"Retrieving computation from {self.computation_url}")
        req = self.get(self.computation_url)
        new_comp = self.from_dict(req.json(), self.domain, self.api_key)
        self.__dict__.update(new_comp.__dict__)
