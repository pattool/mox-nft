from contracts import picasso_nft
from moccasin.boa_tools import VyperContract

# Create metadata hash
"""
Key Steps:

First: Upload your image to IPFS → get image hash
Second: Create JSON with that image hash
Third: Upload JSON to IPFS → get metadata hash
Fourth: Use metadata hash as NFT tokenURI

"""


PICASSO_URI = "QmcjkSiLd95HQ5Xg3pcYMUFu9LV2q7QNYEj6GNjByowBUN"

def deploy_basic_nft() -> VyperContract:
    contract_nft = picasso_nft.deploy()
    print()
    print(f"Deployed Picasso NFT to {contract_nft.address}")
    
    contract_nft.mint(PICASSO_URI)
    print(f"Minted Picasso NFT with URI {contract_nft.tokenURI(0)}")
    print()
    return contract_nft


def moccasin_main():
    return deploy_basic_nft()