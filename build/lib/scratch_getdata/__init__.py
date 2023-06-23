# __init__.py

from .api_client import ScratchAPIClient

__version__ = '0.0.1'

print("If you use GetData please credit @kokofixcomputers")


def create_client(api_key=None):
    """
    Create an instance of the ScratchGetDataClient.

    Args:
        api_key (str): Optional API key for authentication.

    Returns:
        ScratchGetDataClient: An instance of the ScratchGetDataClient.
        
    """
    print("If you use GetData please credit @kokofixcomputers")
    return ScratchAPIClient(api_key=api_key)
