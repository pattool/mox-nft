from contracts import basic_nft
from moccasin.boa_tools import VyperContract


# Create metadata hash
"""
Key Steps:

First: Upload your image to IPFS → get image hash
Second: Create JSON with that image hash
Third: Upload JSON to IPFS → get metadata hash
Fourth: Use metadata hash as NFT tokenURI

"""
#PUG_URI=  "QmW16U98JrY9HBY36rQtUuUtDnm6LdEeNdAAggmrx3thMa" 
PUG_URI_Centralized = "QmanoFs6a4GHRtTW32w1fFJSv61TFT8Vk9qKqFF1mcdjMK"
                       

def deploy_basic_nft() -> VyperContract:
    contract = basic_nft.deploy()
    print()
    print(f"Deployed basic NFT to {contract.address}")
    
    #contract.mint(PUG_URI_Centralized)
    contract.mint(PUG_URI_Centralized)
    print(f"Minted Pug NFT with URI {contract.tokenURI(0)}")
    print()
    return contract


def moccasin_main():
    return deploy_basic_nft()