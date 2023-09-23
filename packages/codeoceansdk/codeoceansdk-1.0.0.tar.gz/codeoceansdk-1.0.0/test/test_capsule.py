import json
import os
from pathlib import Path
from datetime import datetime
from time import mktime, sleep

import logging
import pandas as pd
import pytest
from codeoceansdk.Capsule import (
    Capsule,
    OriginalCapsuleInfo,
    UserPermission,
    EveryonePermission,
)
from codeoceansdk.Computation import File

p = Path(__file__).parent
with open(p / Path("config.json")) as handle:
    test_parameters = json.load(handle)


def test_get_capsule_runs():
    """
    Test previous runs. This capsule has three successful runs with results and six total runs. One run was run with parameters
    """
    capsule = Capsule(
        id="2f54bd66-d022-4cee-bf29-24f40beb425e",
        domain=test_parameters["DOMAIN"],
        api_key=os.environ["API_KEY"],
    )
    output_runs = capsule.get_capsule_runs()
    output_runs = pd.DataFrame(output_runs)
    assert 6 == len(output_runs)
    has_results = output_runs[output_runs["has_results"]]
    assert 3 == len(has_results)
    has_parameters = output_runs[output_runs["parameters"].apply(len) > 0]
    assert 1 == len(has_parameters)


def test_get_capsule():
    """Test retrieving capsule info. This capsule has been duplicated from the capsule used in test_get_capsule_runs"""
    capsule = Capsule(
        id="67369491-e18f-4596-b50c-8b18527ee1b3",
        domain=test_parameters["DOMAIN"],
        api_key=os.environ["API_KEY"],
    )
    capsule.get_capsule()
    original_capsule = OriginalCapsuleInfo(
        id="2f54bd66-d022-4cee-bf29-24f40beb425e",
        major_version=0,
        minor_version=0,
        name="test_previous_runs",
        created=int(
            mktime(
                datetime.strptime(
                    "Feb 16, 2023 16:16 10", "%b %d, %Y %H:%M %S"
                ).timetuple()
            )
        ),
        public=False,
    )
    assert capsule.original_capsule == original_capsule
    assert datetime.fromtimestamp(capsule.created) == datetime.strptime(
        "Feb 22, 2023 10:10 43", "%b %d, %Y %H:%M %S"
    )
    assert capsule.status == "non-published"
    assert capsule.owner == "1a091a69-17d2-4fd3-b8e6-cf0b091944b9"
    assert capsule.name == "test_duplicated"


def test_set_permissions():
    capsule = Capsule(
        id="67369491-e18f-4596-b50c-8b18527ee1b3",
        domain=test_parameters["DOMAIN"],
        api_key=os.environ["API_KEY"],
    )
    capsule.get_capsule()

    capsule.set_capsule_permissions(
        users=[UserPermission("june@codeocean.com", "owner")],
        everyone=EveryonePermission("none"),
    )
    # there's no actual way to check permissions, unfortunately, so we just have to run this and then switch back
    capsule.set_capsule_permissions(
        users=[UserPermission("june@codeocean.com", "owner")],
        everyone=EveryonePermission("viewer"),
    )


@pytest.mark.slow
def test_run_capsule_computation():
    """Runs the associated capsule,
    attaches test dataset, capsule copies it and parameter 1 to the output folder."""
    capsule = Capsule(
        id="543f15c6-a25e-4c24-895c-06ab2db78a49",
        domain=test_parameters["DOMAIN"],
        api_key=os.environ["API_KEY"],
    )
    parameters = ["test_parameter"]
    data_assets = [
        {"id": "c6f7b0ce-9d63-4b65-9b54-099d8e18c4e6", "mount": "test_mount"}
    ]
    computation = capsule.run_capsule_computation(parameters, data_assets)
    max_iter = 10
    i = 0
    while computation.state != "completed":
        computation.get_computation()
        assert max_iter > i, "Max iterations exceeded."
        sleep(5)
        i += 1
    assert computation.end_status == "succeeded"
    computation.get_computation()
    assert computation.has_results
    computation_results = computation.list_computation_result_files()
    assert computation_results == [
        File(name="output", path="output", type="file", size=101),
        File(name="test.tsv", path="test.tsv", type="file", size=27),
        File(
            name="test_parameter.txt", path="test_parameter.txt", type="file", size=15
        ),
    ]
