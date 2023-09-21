from .BacalhauProtocol import BacalhauProtocol
from .ErrorProtocol import ErrorProtocol
from .DeProtocol import DeProtocol
from typing import Iterable

def patch_ipfshttpclient():
    """Monkey patch ipfshttpclient to use newer versions of the
    ipfs protocol.
    """
    from ipfshttpclient import client

    old_assert_version = client.assert_version

    def patched_assert_version(
        version: str,
        minimum: str = "0.0.1",
        maximum: str = "0.100.0",
        blacklist: Iterable[str] = client.VERSION_BLACKLIST,
    ) -> None:
        return old_assert_version(version, "0.0.1", "0.100.0", blacklist)

    client.assert_version = patched_assert_version


patch_ipfshttpclient()