import logging
from enum import Enum
from typing import Optional

from dataclasses import dataclass, field, asdict
from codeoceansdk.CodeOcean import CodeOcean

logger = logging.getLogger(__name__)


@dataclass(slots=True)
class DataSource:
    type: str


@dataclass(kw_only=True, slots=True)
class GCPCloudStorage(DataSource):
    """Google cloud data source"""

    bucket: str
    """GCP bucket"""
    prefix: str = None
    """GCP secret"""
    client_secret: Optional[str] = None
    """GCP secret key"""
    client_id: Optional[str] = None
    """GCP client id"""
    type: str = "gcp"


@dataclass(kw_only=True, slots=True)
class AWSS3(DataSource):
    """AWS S3 source"""

    bucket: str
    """AWS bucket"""
    keep_on_external_storage: bool = None
    """When this property is set to true, the data asset files will not be copied over to CO. Also the prefix 
    property will be ignored and the entire S3 bucket would be used. """
    prefix: str = None
    """AWS prefix"""
    index_data: bool = None
    """When this property is set to true, CO will index the files in the remote bucket, allowing to view 
    the file tree in the dataset and capsule pages. This is only relevant when keep_on_external_storage is set to 
    true (when keep_on_external_storage is false CO will always index the files) """
    access_key_id: Optional[str] = None
    """AWS ACCESS KEY ID (only needed when source bucket is private)"""
    secret_access_key: Optional[str] = None
    """AWS SECRET ACCESS KEY (only needed when source bucket is private)"""
    type: str = "aws"


@dataclass(kw_only=True, slots=True)
class ComputationSource(DataSource):
    """Result from computation source"""

    id: str
    """Metadata id for computation"""
    type: str = "computation"


@dataclass(frozen=True, slots=True)
class SourceBucket:
    """In the data asset, what was the original source"""

    bucket: str = None
    """original bucket’s name"""
    origin: Enum("origin", ["aws", "local", "gcp"]) = None
    """Which cloud did this come from (aws, local, gcp)."""
    prefix: str = None
    """Bucket prefix"""


@dataclass(frozen=True, slots=True)
class UpdateMetadataParams:
    name: str = None
    """Name of data asset to update"""
    description: str = None
    """Description of data asset to update"""
    mount: str = None
    """Mount point of data asset to update"""
    custom_metadata: Optional[dict] = field(default_factory=dict)
    """Custom metadata to update"""
    tags: Optional[list[str]] = field(default_factory=list)
    """Tags to update"""


@dataclass(frozen=True, slots=True)
class SearchRange:
    min: int = None
    """Minimum of the range"""
    max: int = None
    """Maximum of the range"""


@dataclass(frozen=True, slots=True)
class SearchFilter:
    key: str
    """Field key, can be each of title, description, tags, any custom field"""
    exclude: bool = None
    """Whether to include/exclude the field value"""
    value: Optional[str] = None
    """Field value to be included/excluded"""
    values: Optional[list[str]] = field(default_factory=list)
    """field values in case of multiple values"""
    range: Optional[SearchRange] = None
    """Field range to be included/excluded (one of min/max must be set)"""


@dataclass(frozen=True, slots=True)
class SearchParams:
    query: str = None
    """determines the search query. can be a free text or in the form of 'name:... tag:... run_script:... 
    commit_id:...' """
    offset: Optional[int] = None
    """If 30 items are returned and this is set to 10, the results 10-20 will be returned"""
    limit: Optional[int] = None
    """How many items to return"""
    sort_order: Optional[Enum("sort_order", ["asc", "desc"])] = None
    """Sort results by ascending or descending order"""
    sort_field: Optional[Enum("sort_field", ["created", "type", "name", "size"])] = None
    """Sort results by specified field"""
    type: Optional[Enum("type", ["dataset", "result"])] = None
    """If omitted results may include both datasets and results."""
    ownership: Optional[Enum("ownership", ["private", "created", "shared"])] = None
    """search data asset by ownership - created - only datasets created by the user, shared- datasets shared with 
    the user, private - datasets that the user has not shared"""
    favorite: Optional[bool] = None
    """Only search favorited data assets"""
    archived: Optional[bool] = None
    """Only search archived data assets"""
    origin: Optional[Enum("origin", ["internal", "external"])] = None
    """determines whether to get only external/local datasets"""
    filters: Optional[list[SearchFilter]] = field(default_factory=list)
    """List of fields to filter by."""


@dataclass(frozen=True, slots=True)
class SearchResults:
    has_more: bool
    """Indicates whether there are more results than those returned"""
    results: Optional[list] = field(default_factory=list)
    """DataAssets that match the search criteria"""


@dataclass(frozen=True, slots=True)
class PermissionGroup:
    """Add/update permissions for a group to give access to a data asset (only relevant with certain
    SSOs)"""

    name: str
    """Group name"""
    role: Enum("role", ["owner", "viewer"])
    """Role to set for group"""


@dataclass(frozen=True, slots=True)
class PermissionUser:
    email: str
    """User email"""
    role: Enum("role", ["owner", "viewer", "editor"])
    """Role to set for user"""


@dataclass(frozen=True, slots=True)
class PermissionParams:
    """Parameters to use to set permissions"""

    users: Optional[list[PermissionUser]] = field(default_factory=list)
    """Users to add/update permissions for"""
    groups: Optional[list[PermissionGroup]] = field(default_factory=list)
    """Group to add/update permissions for"""
    everyone: Optional[Enum("role", ["viewer", "none"])] = None
    """Set permissions for everyone. Can only be viewer or none"""


@dataclass(frozen=True, slots=True)
class Provenance:
    capsule: str = None
    """Source capsule"""
    commit: str = None
    """Git commit for result"""
    run_script: str = None
    """Script used to generate results"""
    docker_image: str = None
    """Environment docker image used for result"""
    data_assets: Optional[list[str]] = field(default_factory=list)
    """Data assets used to generate results"""


@dataclass(kw_only=True)
class DataAsset(CodeOcean):
    id: str
    """Metadata id"""
    created: int = 0
    """Data asset creation time"""
    description: str = ""
    """Description of the data asset."""
    files: int = 0
    """Number of files in the data asset. Not relevant if the data asset was created with keep_on_external_storage = 
    true and index_data = false. """
    last_used: int = 0
    """Time this data asset was last used"""
    size: int = 0
    """Size in bytes of the data asset. Not relevant if the data asset was created with keep_on_external_storage = 
    true and index_data = false. """
    sourceBucket: Optional[SourceBucket] = None
    """Info on bucket from which dataset was created"""
    tags: Optional[list[str]] = field(default_factory=list)
    """Keywords for searching the data asset by."""
    type: Enum("type", ["dataset", "result"]) = "DATA_ASSET_TYPE_DATASET"
    """Type of the data asset. (DATA_ASSET_TYPE_DATASET, DATA_ASSET_TYPE_RESULT)"""
    custom_metadata: dict = field(default_factory=dict)
    """Map of key value pairs, according to custom metadata fields defined by the admin and values that were set by 
    the user """
    app_parameters: Optional[list[dict]] = field(default_factory=list[dict])
    """Parameters used to generate the data asset"""
    provenance: Optional[Provenance] = None
    name: str = ""
    """Name of dataset"""
    state: Enum("state", ["draft", "ready", "failed"]) = "DATA_ASSET_STATE_DRAFT"
    """data asset creation state. Can be one of the following:
    DATA_ASSET_STATE_DRAFT - the data asset is still being created.
    DATA_ASSET_STATE_READY - the data asset is ready for use.
    DATA_ASSET_STATE_FAILED - the data asset creation failed."""

    def __post_init__(self):
        super().__post_init__()
        self.data_asset_url = f"{self.api_url}/data_assets/{self.id}"

    @staticmethod
    def from_dict(dataset_dict, domain, api_key):
        """

        :param dataset_dict: Dictionary containing Dataset parameters
        :param domain: Code Ocean Domain
        :param api_key: API key to access data asset
        :return: DataAsset
        """
        if "sourceBucket" in dataset_dict:
            dataset_dict["sourceBucket"] = SourceBucket(**dataset_dict["sourceBucket"])
        if "provenance" in dataset_dict:
            dataset_dict["provenance"] = Provenance(**dataset_dict["provenance"])
        dataset_dict["domain"] = domain
        dataset_dict["api_key"] = api_key
        return DataAsset(**dataset_dict)

    def get_data_asset(self):
        """
        Get data asset parameters for given data asset id.
        """
        logger.debug(f"Retrieving data asset from {self.data_asset_url}")
        req = self.get(self.data_asset_url)
        new_comp = self.from_dict(req.json(), self.domain, self.api_key)
        self.__dict__.update(new_comp.__dict__)

    def delete_data_asset(self):
        """Delete data asset"""
        logger.info(f"Deleting data asset {self.id}")
        self.delete(self.data_asset_url)

    @staticmethod
    def create_data_asset(
        name: str,
        tags: list[str],
        data_source: DataSource,
        mount: str,
        environment: CodeOcean,
        custom_metadata: dict = None,
        description: str = None,
    ):
        """
        Create data asset
        :param name: Data asset name
        :param tags: Data asset tags
        :param data_source: Data source, can be AWSSource, GCPSource, or DataSource
        :param mount: Mountpoint for data asset in capsule
        :param environment: CodeOcean environment to create data asset in.
        :param custom_metadata: Custom metadata values to set
        :param description: Description of data asset
        :return: DataAsset
        """
        input_url = f"{environment.api_url}/data_assets"
        data_source_dict = asdict(data_source)
        data_type = data_source_dict["type"]
        del data_source_dict["type"]
        payload = {
            "name": name,
            "tags": tags,
            "source": {data_type: data_source_dict},
            "mount": mount,
        }
        if custom_metadata:
            payload["custom_metadata"] = custom_metadata
        if description:
            payload["description"] = description
        logger.info(f"Creating data asset from {data_type}")
        response = environment.post(input_url, payload).json()
        new_data_asset = DataAsset.from_dict(
            response, environment.domain, environment.api_key
        )
        return new_data_asset

    def update_metadata(self, updated_parameters: UpdateMetadataParams):
        """
        Update metadata for data asset
        :param updated_parameters: DataAssetUpdateParams with updated values
        :return: Updated DataAsset object
        """
        logger.info(f"Updating metadata for asset {self.id}")
        response = self.put(self.data_asset_url, asdict(updated_parameters)).json()
        new_data_asset = DataAsset.from_dict(response, self.domain, self.api_key)
        return new_data_asset

    def archive_asset(self):
        """
        Archive data asset
        """
        logger.info(f"Unarchiving asset {self.id}")
        input_url = f"{self.data_asset_url}/archive"
        self.patch(input_url, params={"archive": True})

    def unarchive_asset(self):
        """
        Unarchive data asset
        """
        logger.info(f"Unarchiving asset {self.id}")
        input_url = f"{self.data_asset_url}/archive"
        self.patch(input_url, params={"archive": False})

    @staticmethod
    def search_data_assets(environment: CodeOcean, search_params: SearchParams):
        """
        Search data assets
        :param environment: CodeOcean environment
        :param search_params: DataAssetSearchParams object containing the search parameters
        :return: DataAssetSearchResults containing the found results
        """
        search_params = asdict(search_params)
        logger.info(f"Searching data assets assets")
        logger.debug(search_params)

        input_url = f"{environment.api_url}/data_assets/search"
        response = environment.post(input_url, search_params).json()
        search_response = SearchResults(
            has_more=response["has_more"],
            results=[
                DataAsset.from_dict(x, environment.domain, environment.api_key)
                for x in response["results"]
            ],
        )
        return search_response

    def set_permissions(self, permissions: PermissionParams):
        """
        Set permissions on Data Asset
        :param permissions: Permissions to add or update
        """
        logger.info(f"Setting permissions on {self.id}")
        permissions = asdict(permissions)
        logger.debug(permissions)
        input_url = f"{self.data_asset_url}/permissions"
        self.post(input_url, permissions)
