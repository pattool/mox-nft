import pytest
import boa
from script.deploy_workshop1_nft import deploy_basic_nft
from contracts import workshop1_nft

@pytest.fixture(scope="session")
def basic_nft():
    """Deploy NFT once for the entire test session (includes minting)."""
    return deploy_basic_nft()


@pytest.fixture(scope="function")
def fresh_nft_contract():
    """Deploy a fresh NFT contract for each test (no minting)."""
    return workshop1_nft.deploy()

