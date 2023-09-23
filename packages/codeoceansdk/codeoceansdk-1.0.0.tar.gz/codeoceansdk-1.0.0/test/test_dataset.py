import json
import os
from pathlib import Path

import pandas as pd
from codeoceansdk.CodeOcean import CodeOcean
from codeoceansdk.DataAsset import (
    DataAsset,
    SourceBucket,
    AWSS3,
    UpdateMetadataParams,
    SearchParams,
    PermissionParams,
    PermissionUser,
)

p = Path(__file__).parent
with open(p / Path("config.json")) as handle:
    parameters = json.load(handle)


def test_get_data_asset():
    data_asset = DataAsset(
        id="ac1bba83-707f-4671-8a9e-55c9eee2510f",
        domain=parameters["DOMAIN"],
        api_key=os.environ["API_KEY"],
    )
    data_asset.get_data_asset()
    source_bucket = SourceBucket(bucket="", origin="local", prefix="")
    assert data_asset.sourceBucket == source_bucket


def test_get_data_asset_with_params():
    data_asset = DataAsset(
        id="c6f7b0ce-9d63-4b65-9b54-099d8e18c4e6",
        domain=parameters["DOMAIN"],
        api_key=os.environ["API_KEY"],
    )
    data_asset.get_data_asset()
    assert data_asset.app_parameters[0]["value"] == "test_parameter"


def test_create_and_delete_data_asset():
    data_asset = DataAsset.create_data_asset(
        name="test",
        tags=["unittest", "codeoceansdk"],
        data_source=AWSS3(
            bucket="codeocean-public-data",
            keep_on_external_storage=True,
            prefix="unit_test",
        ),
        mount="testsdk",
        description="Test for Code Ocean Python SDK",
        environment=CodeOcean(
            api_key=os.environ["API_KEY"], domain=parameters["DOMAIN"]
        ),
    )
    assert data_asset.description == "Test for Code Ocean Python SDK"
    assert data_asset.tags[0] == "unittest"
    assert data_asset.tags[1] == "codeoceansdk"
    data_asset.delete_data_asset()


def test_update_metadata():
    data_asset = DataAsset(
        id="6030d63b-e504-4253-b933-78f370811146",
        domain=parameters["DOMAIN"],
        api_key=os.environ["API_KEY"],
    )
    data_asset.get_data_asset()
    old_parameters = UpdateMetadataParams(
        name=data_asset.name,
        description=data_asset.description,
        tags=data_asset.tags,
        mount="test_mount",
        custom_metadata=data_asset.custom_metadata,
    )

    updated_parameters = UpdateMetadataParams(
        name="test_update_metadata",
        description="updated description",
        tags=["updated_tag1", "updated_tag2"],
        mount="updated_mount",
        custom_metadata={"Molecule Type": "DNA"},
    )

    new_data_asset = data_asset.update_metadata(updated_parameters)
    assert new_data_asset.description == "updated description"
    assert new_data_asset.tags[0] == "updated_tag1"
    assert new_data_asset.tags[1] == "updated_tag2"
    assert new_data_asset.custom_metadata["Molecule Type"] == "DNA"
    updated_data_asset = data_asset.update_metadata(old_parameters)
    assert updated_data_asset.description == old_parameters.description
    assert updated_data_asset.name == old_parameters.name
    assert all([a == b for a, b in zip(updated_data_asset.tags, old_parameters.tags)])
    old_metadata = old_parameters.custom_metadata
    updated_metadata = updated_data_asset.custom_metadata
    assert all(
        [old_metadata[key] == updated_metadata[key] for key in updated_metadata.keys()]
    )


def test_archive():
    data_asset = DataAsset(
        id="6030d63b-e504-4253-b933-78f370811146",
        domain=parameters["DOMAIN"],
        api_key=os.environ["API_KEY"],
    )
    data_asset.get_data_asset()
    data_asset.archive_asset()
    data_asset.unarchive_asset()


def test_search():
    search_params = SearchParams(
        query="test_update_metadata",
        ownership="private",
    )
    data_asset = DataAsset.search_data_assets(
        environment=CodeOcean(
            api_key=os.environ["API_KEY"], domain=parameters["DOMAIN"]
        ),
        search_params=search_params,
    )
    assert len(data_asset.results) == 1
    search_params = SearchParams(
        query="XXXX",
        ownership="private",
    )
    data_asset = DataAsset.search_data_assets(
        environment=CodeOcean(
            api_key=os.environ["API_KEY"], domain=parameters["DOMAIN"]
        ),
        search_params=search_params,
    )
    assert len(data_asset.results) == 0


def test_permissions():
    data_asset = DataAsset(
        id="6030d63b-e504-4253-b933-78f370811146",
        domain=parameters["DOMAIN"],
        api_key=os.environ["API_KEY"],
    )
    data_asset.get_data_asset()
    permissions = PermissionParams(everyone="viewer")
    data_asset.set_permissions(permissions)
    permissions = PermissionParams(everyone="none")
    data_asset.set_permissions(permissions)
    permissions = PermissionParams(
        users=[PermissionUser(email="june@codeocean.com", role="viewer")]
    )
    data_asset.set_permissions(permissions)
    permissions = PermissionParams(
        users=[PermissionUser(email="june@codeocean.com", role="owner")]
    )
    data_asset.set_permissions(permissions)
