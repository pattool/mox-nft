import pytest
import boa
import base64
from script.deploy_workshop1_nft import deploy_basic_nft
from script.deploy_mood_nft import deploy_mood, svg_to_base64_uri
from contracts import workshop1_nft
from contracts import mood_nft_contract



@pytest.fixture(scope="session")
def basic_nft():
    """Deploy NFT once for the entire test session (includes minting)."""
    return deploy_basic_nft()


@pytest.fixture(scope="function")
def fresh_nft_contract():
    """Deploy a fresh NFT contract for each test (no minting)."""
    return workshop1_nft.deploy()


@pytest.fixture(scope="session")
def mood_nft():
    return deploy_mood()


@pytest.fixture(scope="function")
def fresh_mood_contract():
    """Deploy a fresh Mood NFT contract for each test (no minting)."""
    # The mood_nft.vy contract expects base64-encoded data URIs directly
    # These are already properly formatted base64 data URIs for simple SVGs
    happy_svg_uri = "data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAwIiBoZWlnaHQ9IjIwMCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48Y2lyY2xlIGN4PSIxMDAiIGN5PSIxMDAiIHI9IjUwIiBmaWxsPSJ5ZWxsb3ciLz48L3N2Zz4="
    sad_svg_uri = "data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAwIiBoZWlnaHQ9IjIwMCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48Y2lyY2xlIGN4PSIxMDAiIGN5PSIxMDAiIHI9IjUwIiBmaWxsPSJibHVlIi8+PC9zdmc+"
    
    # Deploy the contract directly with the base64 URIs
    return mood_nft_contract.deploy(happy_svg_uri, sad_svg_uri)


@pytest.fixture(scope="function") 
def mood_contract_with_token(fresh_mood_contract):
    """Deploy contract and mint one token for testing."""
    contract = fresh_mood_contract
    # Mint token ID 0
    contract.mint_nft()
    return contract