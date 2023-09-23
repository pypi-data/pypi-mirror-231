import json
import os
from pathlib import Path
from datetime import datetime

import pandas as pd
from codeoceansdk.Computation import Computation

p = Path(__file__).parent
with open(p / Path("config.json")) as handle:
    parameters = json.load(handle)


def test_list_computation_result_files():
    computation = Computation(
        id="ad8a90de-9510-47f5-844c-288c9d36fafd",
        domain=parameters["DOMAIN"],
        api_key=os.environ["API_KEY"],
    )
    result_files = computation.list_computation_result_files()
    result_files = pd.DataFrame(result_files)
    assert 2 == len(result_files)
    assert 1 == len(result_files[result_files["path"] == "test.txt"])


def test_get_presigned_url():
    computation = Computation(
        id="ad8a90de-9510-47f5-844c-288c9d36fafd",
        domain=parameters["DOMAIN"],
        api_key=os.environ["API_KEY"],
    )

    presigned_url = computation.get_download_url("test.txt")
    assert presigned_url is not None


def test_get_computation():
    """This is a computation with 1 parameter"""
    computation = Computation(
        id="06bd58a0-a1e6-43cc-90c3-c87f87263f79",
        domain=parameters["DOMAIN"],
        api_key=os.environ["API_KEY"],
    )
    computation.get_computation()

    assert len(computation.parameters) == 1
    assert datetime.fromtimestamp(computation.created) == datetime.strptime(
        "Feb 17, 2023 12:55 1", "%b %d, %Y %H:%M %S"
    )
    assert computation.name == "Run With Parameters 6667301"
    assert computation.run_time == 3
    assert not computation.has_results
    assert computation.state == "completed"
    assert computation.end_status == "succeeded"
