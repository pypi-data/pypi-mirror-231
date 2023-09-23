import json
import os
from pathlib import Path

from codeoceansdk.CodeOcean import CodeOcean

p = Path(__file__).parent
with open(p / Path("config.json")) as handle:
    parameters = json.load(handle)


def test_check_domain_correct():
    correct_domain = CodeOcean(
        domain=parameters["DOMAIN"], api_key=os.environ["API_KEY"]
    )
    assert correct_domain.check_domain()


def test_check_domain_incorrect():
    correct_domain = CodeOcean(
        domain="https://notadomain.com", api_key=os.environ["API_KEY"]
    )
    assert not correct_domain.check_domain()
