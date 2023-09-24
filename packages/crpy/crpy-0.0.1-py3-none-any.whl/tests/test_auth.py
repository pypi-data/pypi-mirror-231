import pytest

from crpy.registry import RegistryInfo


@pytest.mark.asyncio
async def test_auth():
    registry = RegistryInfo.from_url("alpine")
    token = await registry.auth()
    assert isinstance(token, str)
