"""
Public function
"""
import requests

from requests.structures import CaseInsensitiveDict

from .metadata import Metadata

FETCH_TIMEOUT=30

class FetchException(Exception):
    """Exception raise when fetch function fail
    """

class BoxNameException(Exception):
    """Exception raise when box name have wrong character
    """

def fetch(url: str) -> Metadata:
    """
    Download metadata json for url and create Metadata class
    """
    headers = CaseInsensitiveDict()
    headers['Accept'] = "application/json"
    response = requests.get(url, headers=headers, timeout=FETCH_TIMEOUT)
    if not response.ok:
        raise FetchException(
            f'Impossible to fetch {url} (status code: {response.status_code})')
    return Metadata.from_json(response.content)  # pylint: disable=E1101


def forge_metadata_url(box_name: str) -> str:
    """
    Forge the metadata url from name
    """
    if not '/' in box_name:
        raise BoxNameException(f'box_name must contains "/" : {box_name}')
    user, name, *_ = box_name.split('/', maxsplit=2)
    return f'https://app.vagrantup.com/{user}/boxes/{name}'
