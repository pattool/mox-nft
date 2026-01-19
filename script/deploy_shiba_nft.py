from contracts import shiba_nft
from moccasin.boa_tools import VyperContract

# Create metadata hash
"""
Key Steps:

First: Upload your image to IPFS → get image hash
Second: Create JSON with that image hash
Third: Upload JSON to IPFS → get metadata hash
Fourth: Use metadata hash as NFT tokenURI

"""


SHIBA_URI = "QmWfiatRkpYe1jh7XTEzJR18aYXtHbVAWfSNcPW8TvZRsS"

def deploy_basic_nft() -> VyperContract:
    contract_nft = shiba_nft.deploy()
    print()
    print(f"Deployed Shiba NFT to {contract_nft.address}")
    
    contract_nft.mint(SHIBA_URI)
    print(f"Minted Shiba NFT with URI {contract_nft.tokenURI(0)}")
    print()
    return contract_nft


def moccasin_main():
    return deploy_basic_nft()