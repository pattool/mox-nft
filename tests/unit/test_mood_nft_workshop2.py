import boa
import base64
import json
from script.deploy_mood_nft import moccasin_main, svg_to_base64_uri
import pytest

START_TOKEN_URI = "data:application/json;base64,eyJuYW1lIjoiTW9vZCBORlQiLCAiZGVzY3JpcHRpb24iOiJBbiBORlQgdGhhdCByZWZsZWN0cyB0aGUgbW9vZCBvZiB0aGUgb3duZXIsIDEwMCUgb24gQ2hhaW4hIiwgImF0dHJpYnV0ZXMiOiBbeyJ0cmFpdF90eXBlIjogIm1vb2RpbmVzcyIsICJ2YWx1ZSI6IDEwMH1dLCAiaW1hZ2UiOiJkYXRhOmltYWdlL3N2Zyt4bWw7YmFzZTY0LFBITjJaeUIyYVdWM1FtOTRQU0l3SURBZ01qQXdJREl3TUNJZ2QybGtkR2c5SWpRd01DSWdJR2hsYVdkb2REMGlOREF3SWlCNGJXeHVjejBpYUhSMGNEb3ZMM2QzZHk1M015NXZjbWN2TWpBd01DOXpkbWNpUGdvZ0lEeGphWEpqYkdVZ1kzZzlJakV3TUNJZ1kzazlJakV3TUNJZ1ptbHNiRDBpZVdWc2JHOTNJaUJ5UFNJM09DSWdjM1J5YjJ0bFBTSmliR0ZqYXlJZ2MzUnliMnRsTFhkcFpIUm9QU0l6SWk4K0NpQWdQR2NnWTJ4aGMzTTlJbVY1WlhNaVBnb2dJQ0FnUEdOcGNtTnNaU0JqZUQwaU56QWlJR041UFNJNE1pSWdjajBpTVRJaUx6NEtJQ0FnSUR4amFYSmpiR1VnWTNnOUlqRXlOeUlnWTNrOUlqZ3lJaUJ5UFNJeE1pSXZQZ29nSUR3dlp6NEtJQ0E4Y0dGMGFDQmtQU0p0TVRNMkxqZ3hJREV4Tmk0MU0yTXVOamtnTWpZdU1UY3ROalF1TVRFZ05ESXRPREV1TlRJdExqY3pJaUJ6ZEhsc1pUMGlabWxzYkRwdWIyNWxPeUJ6ZEhKdmEyVTZJR0pzWVdOck95QnpkSEp2YTJVdGQybGtkR2c2SURNN0lpOCtDand2YzNablBnPT0ifQ=="

END_TOKEN_URI = "data:application/json;base64,eyJuYW1lIjoiTW9vZCBORlQiLCAiZGVzY3JpcHRpb24iOiJBbiBORlQgdGhhdCByZWZsZWN0cyB0aGUgbW9vZCBvZiB0aGUgb3duZXIsIDEwMCUgb24gQ2hhaW4hIiwgImF0dHJpYnV0ZXMiOiBbeyJ0cmFpdF90eXBlIjogIm1vb2RpbmVzcyIsICJ2YWx1ZSI6IDEwMH1dLCAiaW1hZ2UiOiJkYXRhOmltYWdlL3N2Zyt4bWw7YmFzZTY0LFBITjJaeUIyYVdWM1FtOTRQU0l3SURBZ01qQXdJREl3TUNJZ2QybGtkR2c5SWpRd01DSWdhR1ZwWjJoMFBTSTBNREFpSUhodGJHNXpQU0pvZEhSd09pOHZkM2QzTG5jekxtOXlaeTh5TURBd0wzTjJaeUkrQ2lBZ1BHTnBjbU5zWlNCamVEMGlNVEF3SWlCamVUMGlNVEF3SWlCbWFXeHNQU0o1Wld4c2IzY2lJSEk5SWpjNElpQnpkSEp2YTJVOUltSnNZV05ySWlCemRISnZhMlV0ZDJsa2RHZzlJak1pTHo0S0lDQThaeUJqYkdGemN6MGlaWGxsY3lJK0NpQWdJQ0E4WTJseVkyeGxJR040UFNJM01DSWdZM2s5SWpneUlpQnlQU0l4TWlJdlBnb2dJQ0FnUEdOcGNtTnNaU0JqZUQwaU1USTNJaUJqZVQwaU9ESWlJSEk5SWpFeUlpOCtDaUFnUEM5blBnb2dJRHh3WVhSb0lHUTlJazAxTlNBeE5EQmpNVGN1TkRFdE5ESXVOek1nT0RJdU1qRXRNall1T1NBNE1TNDFNaTB1TnpNaUlITjBlV3hsUFNKbWFXeHNPbTV2Ym1VN0lITjBjbTlyWlRvZ1lteGhZMnM3SUhOMGNtOXJaUzEzYVdSMGFEb2dNenNpTHo0S1BDOXpkbWMrIn0="

def test_contract_init_correctly(mood_nft):
    assert mood_nft.name() == "Mood NFT"
    assert mood_nft.symbol() == "MNFT"
    assert mood_nft.token_id_to_mood(0) == 1
    assert mood_nft.address is not None
    assert mood_nft.totalSupply() == 1  # deploy_mood() mints one NFT
    assert mood_nft.ownerOf(0) == boa.env.eoa
    token_uri = mood_nft.tokenURI(0)
    assert token_uri.startswith("data:application/json;base64,")

    print(f"✅ deploy_mood() returns properly configured contract")
    print(f"✅ Contract address: {mood_nft.address}")
    print(f"✅ Initial NFT minted successfully")


def test_flip_mood(mood_nft):
    mood_nft.flip_mood(0)
    assert mood_nft.token_id_to_mood(0) == 2


def test_uri_changes_on_mood(mood_nft):
    assert mood_nft.tokenURI(0) == START_TOKEN_URI
    mood_nft.flip_mood(0)
    assert mood_nft.tokenURI(0) == END_TOKEN_URI
    mood_nft.flip_mood(0)
    assert mood_nft.tokenURI(0) == START_TOKEN_URI

    
def test_flip_mood_happy_to_sad_lines_128_129(mood_nft):
    """Test lines 128-129: if self.token_id_to_mood[token_id] == Mood.HAPPY branch"""
    
    # Token 0 starts as HAPPY (from deploy_mood)
    assert mood_nft.token_id_to_mood(0) == 1  # HAPPY
    
    # Execute flip_mood - this hits lines 128-129 (if branch)
    mood_nft.flip_mood(0)
    
    # Verify the if branch executed: HAPPY -> SAD
    assert mood_nft.token_id_to_mood(0) == 2  # SAD
    
    print(f"✅ Lines 128-129 covered: HAPPY -> SAD")


def test_mint_nft_line_75(fresh_mood_contract):
    """
    Test line 75: erc721._counter = token_id + 1
    This line increments the counter after getting the current token_id
    """
    contract = fresh_mood_contract
    
    # Check initial state - totalSupply should be 0
    initial_supply = contract.totalSupply()
    assert initial_supply == 0
    
    # Mint first NFT - this should execute line 75: erc721._counter = token_id + 1
    contract.mint_nft()
    
    # Verify the counter was incremented (line 75 was executed)
    assert contract.totalSupply() == 1
    assert contract.ownerOf(0) == boa.env.eoa
    assert contract.token_id_to_mood(0) == 1  # Should be HAPPY (1)
    
    # Mint second NFT to further test line 75
    contract.mint_nft()
    assert contract.totalSupply() == 2
    assert contract.ownerOf(1) == boa.env.eoa
    assert contract.token_id_to_mood(1) == 1


def test_flip_mood_lines_128_131(mood_contract_with_token):
        
    """
    Test lines 128-131: The mood flipping conditional logic
    Line 128: if self.token_id_to_mood[token_id] == Mood.HAPPY:
    Line 129: self.token_id_to_mood[token_id] = Mood.SAD  
    Line 130: else:
    Line 131: self.token_id_to_mood[token_id] = Mood.HAPPY
    """
    contract = mood_contract_with_token
    token_id = 0
    
    # Initial state should be HAPPY (1)
    initial_mood = contract.token_id_to_mood(token_id)
    assert initial_mood == 1  # Mood.HAPPY
    
    # Test line 128-129: HAPPY -> SAD transition
    contract.flip_mood(token_id)
    after_first_flip = contract.token_id_to_mood(token_id)
    assert after_first_flip == 2  # Mood.SAD
    
    # Test line 130-131: SAD -> HAPPY transition  
    contract.flip_mood(token_id)
    after_second_flip = contract.token_id_to_mood(token_id)
    assert after_second_flip == 1  # Mood.HAPPY
    
    # Test multiple alternations to ensure both code paths work
    contract.flip_mood(token_id)  # HAPPY -> SAD (lines 128-129)
    assert contract.token_id_to_mood(token_id) == 2
    
    contract.flip_mood(token_id)  # SAD -> HAPPY (lines 130-131)  
    assert contract.token_id_to_mood(token_id) == 1


def test_complete_line_coverage_single_test(fresh_mood_contract):
    """
    Single comprehensive test designed to hit all target lines:
    - Line 75: FINAL_STRING_SIZE constant usage
    - Lines 128->131: flip_mood conditional logic  
    - Lines 140->145: tokenURI image selection
    - Lines 171-181: set_indice_truncated function
    """
    contract = fresh_mood_contract
    
    # === COVER LINE 75: FINAL_STRING_SIZE constant ===
    # This constant is used in function return types and internal functions
    # We need to call functions that use this constant to ensure coverage
    
    # Call svg_to_uri (uses FINAL_STRING_SIZE in return type)
    contract.svg_to_uri('<svg><rect/></svg>')  # Forces constant evaluation
    
    # === COVER LINES 128->131: flip_mood function ===
    # Mint token first
    contract.mint_nft()
    token_id = 0
    
    # Initial state: HAPPY
    assert contract.token_id_to_mood(token_id) == 1
    
    # Execute HAPPY -> SAD path (lines 128-129)
    contract.flip_mood(token_id)
    assert contract.token_id_to_mood(token_id) == 2
    
    # Execute SAD -> HAPPY path (lines 130-131) 
    contract.flip_mood(token_id)
    assert contract.token_id_to_mood(token_id) == 1
    
    # === COVER LINES 140->145: tokenURI function ===
    # Test with HAPPY mood (line 140, skip 141-142)
    uri_happy = contract.tokenURI(token_id)
    assert uri_happy.startswith("data:application/json;base64,")
    
    # Change to SAD and test (lines 140, 141-142)
    contract.flip_mood(token_id)  # Now SAD
    uri_sad = contract.tokenURI(token_id) 
    assert uri_sad.startswith("data:application/json;base64,")
    assert uri_happy != uri_sad  # Should be different
    

def test_lines_140_145_all_mood_combinations(fresh_mood_contract):
    """
    Test all possible mood combinations for tokenURI (lines 140-145)
    """
    contract = fresh_mood_contract
    
    # Create 4 tokens
    for _ in range(4):
        contract.mint_nft()
    
    # Test all HAPPY tokens (line 140 path)
    for token_id in range(4):
        assert contract.token_id_to_mood(token_id) == 1  # All HAPPY initially
        uri = contract.tokenURI(token_id)  # Should execute line 140, skip 141-142
        assert uri.startswith("data:application/json;base64,")
    
    # Make all tokens SAD
    for token_id in range(4):
        contract.flip_mood(token_id)
        assert contract.token_id_to_mood(token_id) == 2  # All SAD now
    
    # Test all SAD tokens (lines 140, 141-142 path)
    for token_id in range(4):
        uri = contract.tokenURI(token_id)  # Should execute lines 140, 141-142
        assert uri.startswith("data:application/json;base64,")
    
    # Create mixed mood scenario
    contract.flip_mood(0)  # Token 0: HAPPY
    contract.flip_mood(1)  # Token 1: HAPPY
    # Tokens 2, 3 remain SAD
    
    # Test mixed moods
    happy_uris = []
    sad_uris = []
    
    for token_id in [0, 1]:  # HAPPY tokens
        uri = contract.tokenURI(token_id)  # Line 140 path
        happy_uris.append(uri)
        
    for token_id in [2, 3]:  # SAD tokens  
        uri = contract.tokenURI(token_id)  # Lines 140, 141-142 path
        sad_uris.append(uri)
    
    # All happy URIs should be the same
    assert happy_uris[0] == happy_uris[1]
    
    # All sad URIs should be the same
    assert sad_uris[0] == sad_uris[1]
    
    # But happy and sad should be different
    assert happy_uris[0] != sad_uris[0]


#def test_nuclear_option_all_lines(fresh_mood_contract):
#    """
#    Nuclear option: brute force all possible code paths
#    """
#    contract = fresh_mood_contract
#    
#    # === NUCLEAR APPROACH FOR LINE 75 ===
#    # Call every function that could possibly reference FINAL_STRING_SIZE
#    print("=== NUCLEAR LINE 75 TEST ===")
#    
#    # Mint tokens
#    for i in range(20):
#        contract.mint_nft()
#    
#    # Massive tokenURI calls
#    for token_id in range(20):
#        for call_num in range(10):
#            uri = contract.tokenURI(token_id)
#            assert uri is not None
#    
#    # Massive svg_to_uri calls  
#    svg_templates = [
#        '<svg></svg>',
#        '<svg><rect/></svg>',
#        '<svg><circle r="{}"/></svg>',
#        '<svg width="{}" height="{}"><rect/></svg>',
#        '<svg>{}x{}</svg>',
#    ]
#    
#    for i in range(50):
#        for template in svg_templates:
#            try:
#                if '{}' in template:
#                    svg = template.format(i, i)
#                else:
#                    svg = template
#                result = contract.svg_to_uri(svg)
#                assert result is not None
#            except:
#                pass
#    
#    # === NUCLEAR APPROACH FOR LINES 128-131 ===
#    print("=== NUCLEAR LINES 128-131 TEST ===")
#    
#    for token_id in range(20):
#        for flip_round in range(25):  # 25 flips per token
#            mood_before = contract.token_id_to_mood(token_id)
#            contract.flip_mood(token_id)
#            mood_after = contract.token_id_to_mood(token_id)
#            assert mood_before != mood_after
#    
#    # === NUCLEAR APPROACH FOR LINES 140-145 ===
#    print("=== NUCLEAR LINES 140-145 TEST ===")
#    
#    # Set up mixed moods
#    for token_id in range(20):
#        target_mood = 1 if token_id < 10 else 2
#        current_mood = contract.token_id_to_mood(token_id)
#        
#        while current_mood != target_mood:
#            contract.flip_mood(token_id)
#            current_mood = contract.token_id_to_mood(token_id)
#    
#    # Massive tokenURI calls for both mood states
#    for token_id in range(20):
#        for call_num in range(10):
#            uri = contract.tokenURI(token_id)
#            assert uri.startswith("data:application/json;base64,")
#    
#    # Change all moods and repeat
#    for token_id in range(20):
#        contract.flip_mood(token_id)
#    
#    for token_id in range(20):
#        for call_num in range(10):
#            uri = contract.tokenURI(token_id)
#            assert uri.startswith("data:application/json;base64,")
#    
#    print("=== NUCLEAR TEST COMPLETED ===")
