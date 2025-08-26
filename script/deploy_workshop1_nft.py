from contracts import workshop1_nft
from moccasin.boa_tools import VyperContract

# Create metadata hash
"""
Key Steps:

First: Upload your image to IPFS → get image hash
Second: Create JSON with that image hash
Third: Upload JSON to IPFS → get metadata hash
Fourth: Use metadata hash as NFT tokenURI

"""

ST_BERNARD_URI= "QmSpWiq9VqdzdGJ382QZxzyrwQeNehmyQzf17sdcFSUSYy"

def deploy_basic_nft() -> VyperContract:
    contract_nft = workshop1_nft.deploy()
    print()
    print(f"Deployed basic NFT to {contract_nft.address}")
    
    contract_nft.mint(ST_BERNARD_URI)
    #contract.mint(BERNARD_URI)
    print(f"Minted Pug NFT with URI {contract_nft.tokenURI(0)}")
    print()
    return contract_nft


def moccasin_main():
    return deploy_basic_nft()