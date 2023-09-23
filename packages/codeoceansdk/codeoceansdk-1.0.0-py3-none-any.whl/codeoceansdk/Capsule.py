import logging
from dataclasses import asdict, dataclass, field as dc_field
from enum import Enum
from typing import Optional

from codeoceansdk.CodeOcean import CodeOcean
from codeoceansdk.Computation import Computation

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class OriginalCapsuleInfo:
    id: str = None
    """Metadata id"""
    major_version: int = None
    """Major version number"""
    minor_version: int = None
    """Minor version number"""
    name: str = None
    """Name of original pipeline"""
    created: int = None
    """Creation time"""
    public: bool = None
    """Is original capsule public"""


@dataclass(frozen=True)
class SubmissionInfo:
    timestamp: int = None
    """Submission time"""
    commit: str = None
    """Submission commit hash"""
    verification_capsule: str = None
    """Verification capsule ID"""
    verified: bool = None
    """Indicates whether the capsule was verified"""
    verified_timestamp: int = None
    """Verification time"""


@dataclass(frozen=True, slots=True)
class Version:
    """Capsule version"""
    major_version: int
    """Major version"""
    minor_version: int
    """Minor version"""
    publish_time: int
    """Publish timestamp"""
    doi: str = None
    """Digital identifier for capsule"""


@dataclass(frozen=True, slots=True)
class Article:
    """If capsule is attached to a publication, what article is it attached to"""
    url: str = None
    """Article URL"""
    id: str = None
    """Article ID"""
    doi: str = None
    """Digital identifier for publication"""
    citation: str = None
    """Article citation"""
    state: Enum("state", ["in_review", "published"]) = None
    """Publication state (i.e., has it been published yet)"""
    name: str = None
    """Article name"""
    journal_name: str = None
    """Journal the article appears in"""
    publish_time: int = None
    """Publication timestamp"""


@dataclass(frozen=True, slots=True)
class UserPermission:
    """Permissions for specific user"""
    email: str
    """Email address for user"""
    role: Enum("role", ["owner, editor, viewer", "discoverable"])
    """Permission level to set for user"""


@dataclass(frozen=True, slots=True)
class GroupPermission:
    """Permissions for group of users"""
    group: str
    """Group name"""
    role: Enum("role", ["owner", "editor", "viewer", "discoverable"])
    """Permission level to set for group"""


@dataclass(frozen=True, slots=True)
class EveryonePermission:
    """Permission for all users"""
    role: Enum("role", ["viewer", "discoverable", "none"])
    """Permission level to set for everyone"""


@dataclass(kw_only=True)
class Capsule(CodeOcean):
    id: str
    """Capsule internal id"""
    created: int = 0
    """Capsule creation time"""
    name: str = ""
    """Capsule display name"""
    status: Enum(
        "status", ["non_published", "submitted", "publishing", "published", "verified"]
    ) = "non_published"
    """Whether or not capsule is published"""
    owner: str = ""
    """Capsule owner id"""
    slug: str = ""
    """Alternate capsule id"""
    field: Optional[str] = None
    """Capsule research field"""
    description: Optional[str] = None
    """Capsule description"""
    cloned_from_url: Optional[str] = None
    """If this is a capsule cloned from github, what url was it"""
    keywords: Optional[list[str]] = dc_field(default_factory=list)
    """Keywords describing capsule (optional)"""
    article: Optional[Article] = None
    """Capsule article info (optional)"""
    versions: Optional[list[Version]] = dc_field(default_factory=list)
    """Capsule versions (if published) (optional)"""
    published_capsule: Optional[str] = None
    """Published capsule id (separate from original)"""
    original_capsule: Optional[OriginalCapsuleInfo] = None
    """Original capsule info (if duplicated) (optional)"""
    submission: Optional[SubmissionInfo] = None
    """Submission info (if capsule submitted for publication) (optional)"""

    def __post_init__(self):
        super().__post_init__()
        self.capsule_url = f"{self.api_url}/capsules/{self.id}"

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

    def get_capsule_runs(self):
        """Get previous capsule runs

        :return: List of Computation objects.
        """
        input_url = f"{self.capsule_url}/computations"
        logger.debug(f"Input url: {input_url}")
        req = self.get(input_url)
        computations = self._parse_comp_response(computation_list=req.json())

        logger.info("Returned runs: {}".format(len(computations)))
        return computations

    def get_capsule(self):
        """
        Get capsule information
        """
        req = self.get(self.capsule_url)
        new_capsule = self.from_dict(req.json(), self.domain, self.api_key)
        self.__dict__.update(new_capsule.__dict__)

    @staticmethod
    def from_dict(capsule_dict, domain, api_key):
        """
        Parse dictionary to Capsule object

        :param domain: Code Ocean domain
        :param api_key: Capsule api.
        :param capsule_dict:  Input dictionary of capsule parameters.
        :return: Computation object.
        """
        if "article" in capsule_dict:
            capsule_dict["article"] = Article(**capsule_dict["article"])
        if "versions" in capsule_dict:
            capsule_dict["versions"] = [Version(**x) for x in capsule_dict["versions"]]
        if "original_capsule" in capsule_dict:
            capsule_dict["original_capsule"] = OriginalCapsuleInfo(
                **capsule_dict["original_capsule"]
            )
        if "submission" in capsule_dict:
            capsule_dict["submission"] = SubmissionInfo(**capsule_dict["submission"])

        capsule_dict["domain"] = domain
        capsule_dict["api_key"] = api_key
        return Capsule(**capsule_dict)

    def run_capsule_computation(
        self, parameters: list = None, data_assets: list = None
    ):
        """
        Run a capsule.

        :param parameters: List of parameters to pass to capsule.
        Should be the same order as in the App Panel.
        :param data_assets: List of dictionaries containing "id" and "mount" keys.
        id is the data asset id, mount is the location to mount it in the capsule.
        :return: Computation object.
        """
        logger.info(f"Running capsule computation on {self.id}")
        input_url = f"{self.api_url}/computations"

        logger.debug(f"Input url: {input_url}")
        logger.debug(f"Parameters {parameters}")
        logger.debug(f"Data assets {data_assets}")

        payload = {"capsule_id": self.id}
        if parameters:
            payload["parameters"] = parameters
        if data_assets:
            payload["data_assets"] = data_assets
        req = self.post(input_url, payload)
        return Computation.from_dict(req.json(), self.domain, self.api_key)

    def set_capsule_permissions(
        self,
        users: list[UserPermission] = None,
        groups: list[GroupPermission] = None,
        everyone: EveryonePermission = None,
    ):
        """

        :param users: User permissions to set
        :param groups: Group permissions to set
        :param everyone: Permissions for everyone with access to the capsule
        """
        input_url = f"{self.api_url}/capsules/{self.id}/permissions"

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
