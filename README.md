# Moccasin Project

🐍 Welcome to my Moccasin NFT project!

## Build 2 NFTs

1. 4 Basic NFTs: Basic NFT - Workshop1 NFT - Shiba NFT - Picasso NFT
2. Dynamic NFT, one where the mood can be changed, and the image be changed.

## Installation
    - If you have an issue to run it, install virtual environment uv.
    - uv, is an extremely fast Python package and project manager, written in Rust.        
   - ### On macOS and Linux:
        curl -LsSf https://astral.sh/uv/install.sh | sh
       
        - Once install follow the next steps:
           - 1 uv venv
           - 2 uv sync
           - 3 source .venv/bin/activate

   - ### On Windows:
        powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

   - ### Documentation:
        - uv's documentation is available at docs.astral.sh/uv.
        - Additionally, the command line reference documentation can be viewed with uv help.

     
## Quickstart

1. Deploy to a fake local network that titanoboa automatically spins up!
    

```bash
- mox run deploy_basic_nft

- mox run deploy_mood_nft
```

2. Run tests

```
mox test
```

```
mox test --coverage
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


## License

uv is licensed under either of

    - Apache License, Version 2.0, (LICENSE-APACHE or 
      https://www.apache.org/licenses/LICENSE-2.0)
    - MIT license (LICENSE-MIT or https://opensource.org/licenses/MIT)
at your option.

Unless you explicitly state otherwise, any contribution intentionally submitted for inclusion in uv by you, as defined in the Apache-2.0 license, shall be dually licensed as above, without any additional terms or conditions.


