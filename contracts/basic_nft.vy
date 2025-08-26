# pragma version 0.4.1

# ------------------------------------------------------------------
#                             NATSPEC
# ------------------------------------------------------------------
"""
@license MIT
@title Puppy NFT
@notice My first NFT
"""


# ------------------------------------------------------------------
#                        IMPORT LIBRARIES
# ------------------------------------------------------------------
from snekmate.auth import ownable as ow
from snekmate.tokens import erc721


# ------------------------------------------------------------------
#                     IMPORT STORAGE VARIABLES
# ------------------------------------------------------------------
initializes: ow
initializes: erc721[ownable := ow]


# ------------------------------------------------------------------
#                         EXPORT FUNCTIONS
# ------------------------------------------------------------------
exports: erc721.__interface__


# ------------------------------------------------------------------
#                           CONSTANTS 
# ------------------------------------------------------------------
NAME: constant(String[25]) = "Puppy NFT"
SYMBOL: constant(String[5]) = "PNFT"
BASE_URI: public(constant(String[34])) = "https://gateway.pinata.cloud/ipfs/" 
#BASE_URI: public(constant(String[7])) ="ipfs://"
EIP_712_VERSION: constant(String[1]) = "1"


# ------------------------------------------------------------------
#                           CONSTRUCTOR
# ------------------------------------------------------------------
@deploy
def __init__():
    ow.__init__()
    erc721.__init__(NAME, SYMBOL, BASE_URI, NAME, EIP_712_VERSION)


# ------------------------------------------------------------------
#                            FUNCTIONS
# ------------------------------------------------------------------
@external
def mint(uri: String[432]):

    token_id: uint256 = erc721._counter
    erc721._counter = token_id + 1

    #  def _safe_mint(owner: address, token_id: uint256, data: Bytes[1_024])          
    erc721._safe_mint(msg.sender, token_id, b"")
    erc721._set_token_uri(token_id, uri)
    

@external
@view
def get_base_uri() -> String[34]:
    return BASE_URI









