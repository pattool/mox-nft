# Moccasin Project

🐍 Welcome to my Moccasin NFT project!

## Build 2 NFTs

1. Basic NFT + workshop1_nft
2. Dynamic NFT, one where the mood can be changed, and the image be changed.

## Quickstart

1. Deploy to a fake local network that titanoboa automatically spins up!

```bash
mox run deploy
```

2. Run tests

```
mox test
```

## What is the TokenURI?

A "uniform resource identifier". Like:

"ipfs://QmW16U98JrY9HBY36rQtUuUtDnm6LdEeNdAAggmrx3thMa" 

    -> ipfs = Interplanetary File System
 
    1.baseURI: ipfs://

    2._tokenURI: QmW16U98JrY9HBY36rQtUuUtDnm6LdEeNdAAggmrx3thMa
 
or

"https://some-website.com/some-json.json"

## What does the data look like?

```json
{
    "name": "PUG",
    "description": "An adorable PUG pup!",
    "image": "ipfs://QmSsYRx3LpDAb1GZQm7zZ1AuHZjfbPkD6J7s9r41xu1mf8", # note: return an image.
    "attributes": [
        {
            "trait_type": "cuteness",
            "value": 100
        }        
    ]
}
```

_For documentation, please run `mox --help` or visit [the Moccasin documentation](https://cyfrin.github.io/moccasin)_


## Create metadata hash

Key Steps:

1. First: Upload your image to IPFS → get image hash
2. Second: Create JSON with that image hash
3. Third: Upload JSON to IPFS → get metadata hash
4. Fourth: Use metadata hash as NFT tokenURI


## Prefix Base64 code data
data:image/svg+xml;base64,