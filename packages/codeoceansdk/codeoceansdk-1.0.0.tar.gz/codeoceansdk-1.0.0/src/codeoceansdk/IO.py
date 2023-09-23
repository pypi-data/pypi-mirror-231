from io import StringIO

import pandas as pd
import requests


def get_dataframe_from_url(url, sep="\t"):
    """Download delimited file from url and return pandas dataframe
    :param url: Pre-signed url
    :param sep: Text delimiter
    :return: pandas dataframe
    """
    req = requests.get(url)
    with StringIO(req.text) as handle:
        return pd.read_csv(handle, sep=sep)
