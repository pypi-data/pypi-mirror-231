import logging
from dataclasses import asdict, dataclass, field as dc_field
from enum import Enum
from typing import Optional

from codeoceansdk.Computation import Computation
from codeoceansdk.CodeOcean import CodeOcean
from codeoceansdk.Capsule import (
    SubmissionInfo,
    Version,
    Article,
    OriginalCapsuleInfo,
    UserPermission,
    GroupPermission,
    EveryonePermission,
)

logger = logging.getLogger(__name__)


@dataclass(kw_only=True)
class Pipeline(CodeOcean):
    id: str
    """Pipeline internal id"""
    created: int = 0
    """Pipeline creation time"""
    name: str = ""
    """Pipeline display name"""
    status: Enum(
        "status", ["non_published", "submitted", "publishing", "published", "verified"]
    ) = "non_published"
    """Whether or not pipeline is published"""
    owner: str = ""
    """Pipeline owner id"""
    slug: str = ""
    """Alternate pipeline id"""
    original_capsule: Optional[OriginalCapsuleInfo] = None
    """Original capsule info (if duplicated) (optional)"""
    published_capsule: str = None
    """Published capsule id (separate from original)"""
    submission: Optional[SubmissionInfo] = None
    """Submission info (if pipeline submitted for publication) (optional)"""
    versions: Optional[list[Version]] = dc_field(default_factory=list)
    """Pipeline versions (if published) (optional)"""
    description: Optional[str] = None
    """Capsule description"""
    field: Optional[str] = None
    """Pipeline research field"""
    keywords: Optional[list[str]] = dc_field(default_factory=list)
    """Keywords describing pipeline (optional)"""
    article: Optional[Article] = None
    """Pipeline article info (optional)"""
    cloned_from_url: Optional[str] = None
    """If this is a pipeline cloned from github, what url was it"""

    def __post_init__(self):
        super().__post_init__()
        self.pipeline_url = f"{self.api_url}/pipelines/{self.id}"

    def _parse_comp_response(self, computation_list: list):
        """
        Parse response from list of dictionaries containing
        computational parameters

        :param computation_list:  Input list of dictionary of computation parameters
        :return: list of Computation objects
        """
        computations = []
        for curr_dict in computation_list:
            computations.append(
                Computation.from_dict(
                    computation_dict=curr_dict, api_key=self.api_key, domain=self.domain
                )
            )
        return computations

    @staticmethod
    def from_dict(dataset_dict, domain, api_key):
        """

        :param dataset_dict: Dictionary containing Dataset parameters
        :param domain: Code Ocean Domain
        :param api_key: API key to access data asset
        :return: DataAsset
        """
        if "original_capsule" in dataset_dict:
            dataset_dict["original_capsule"] = OriginalCapsuleInfo(
                **dataset_dict["original_capsule"]
            )
        if "versions" in dataset_dict:
            dataset_dict["versions"] = [Version(**x) for x in dataset_dict["versions"]]

        dataset_dict["domain"] = domain
        dataset_dict["api_key"] = api_key
        return Pipeline(**dataset_dict)

    def get_pipeline(self):
        """
        Get pipeline metadata by ID

        :return: None
        """
        req = self.get(self.pipeline_url)
        new_pipeline = self.from_dict(req.json(), self.domain, self.api_key)
        self.__dict__.update(new_pipeline.__dict__)

    def get_pipeline_runs(self):
        """Get previous capsule runs

        :return: List of Computation objects.
        """
        input_url = f"{self.pipeline_url}/computations"
        logger.debug(f"Input url: {input_url}")
        req = self.get(input_url)
        computations = self._parse_comp_response(computation_list=req.json())

        logger.info("Returned runs: {}".format(len(computations)))
        return computations

    def set_capsule_permissions(
        self,
        users: list[UserPermission] = None,
        groups: list[GroupPermission] = None,
        everyone: EveryonePermission = None,
    ):
        """
        Set capsule permissions
        :param users: User permissions to set
        :param groups: Group permissions to set
        :param everyone: Permissions for everyone with access to the capsule
        """
        input_url = f"{self.api_url}/pipelines/{self.id}/permissions"

        logger.debug(f"Input url: {input_url}")
        logger.debug(f"Users {users}")
        logger.debug(f"groups {groups}")
        logger.debug(f"everyone {everyone}")

        payload = {}
        if users:
            payload["users"] = [asdict(x) for x in users]
        if groups:
            payload["groups"] = [asdict(x) for x in groups]
        if everyone:
            payload["everyone"] = asdict(everyone)["role"]

        self.post(input_url, payload)

    def run_pipeline_computation(self, data_assets: list = None):
        """
        Run a capsule.

        :param data_assets: List of dictionaries containing "id" and "mount" keys.
        id is the data asset id, mount is the location to mount it in the capsule.
        :return: Computation object.
        """
        logger.info(f"Running pipeline computation on {self.id}")
        input_url = f"{self.api_url}/computations"

        logger.debug(f"Input url: {input_url}")
        logger.debug(f"Data assets {data_assets}")

        payload = {"pipeline_id": self.id}

        if data_assets:
            payload["data_assets"] = data_assets
        req = self.post(input_url, payload)
        return Computation.from_dict(req.json(), self.domain, self.api_key)
