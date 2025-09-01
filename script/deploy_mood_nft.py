import base64
from contracts import mood_nft_contract


def svg_to_base64_uri(svg):
    svg_bytes = svg.encode("utf-8")
    base64_svg = base64.b64encode(svg_bytes).decode("utf-8")
    return f"data:image/svg+xml;base64,{base64_svg}"
                

def deploy_mood():
    happy_svg_uri = ""
    sad_svg_uri = ""

    with open("./images/dynamic/happy.svg", "r") as f:
        happy_svg = f.read()
        happy_svg_uri = svg_to_base64_uri(happy_svg)
        #print(happy_svg_uri)

    with open("./images/dynamic/sad.svg", "r") as f:
        sad_svg = f.read()
        sad_svg_uri = svg_to_base64_uri(sad_svg)
        #print(sad_svg_uri)

    mood_contract = mood_nft_contract.deploy(happy_svg_uri, sad_svg_uri)
    mood_contract.mint_nft()
    #mood_contract.flip_mood(0)
    print(f"TokenUri: {mood_contract.tokenURI(0)}")
    return mood_contract


def moccasin_main():
    return deploy_mood()
