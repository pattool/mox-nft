import boa
from script.deploy_workshop1_nft import deploy_basic_nft, moccasin_main, ST_BERNARD_URI
from moccasin.boa_tools import VyperContract


def test_basic_deployment(basic_nft):
        """Test that the contract deploys successfully with correct initial state."""
        contract = basic_nft
        
        # Test contract deployment
        assert contract.address is not None
        assert len(contract.address) == 42  # Ethereum address format        
        print(f"✅ Contract deployed successfully at: {contract.address}")


def test_contract_deployment(fresh_nft_contract):
        """Test that the contract deploys successfully with correct initial state."""
        contract = fresh_nft_contract
        
        # Test contract deployment
        assert contract.address is not None
        assert len(contract.address) == 42  # Ethereum address format
        assert contract.address.startswith('0x')
        
        print(f"✅ Contract deployed successfully at: {contract.address}")


def test_contract_name_and_symbol(fresh_nft_contract):
        """Test that the contract has the correct name and symbol."""
        contract = fresh_nft_contract
        
        # Test ERC721 metadata
        assert contract.name() == "St. Bernard NFT"
        assert contract.symbol() == "BNFT"
        
        print(f"✅ Contract name: {contract.name()}")
        print(f"✅ Contract symbol: {contract.symbol()}")


def test_base_uri(fresh_nft_contract):
        """Test that the base URI is set correctly."""
        contract = fresh_nft_contract
        
        expected_base_uri = "https://gateway.pinata.cloud/ipfs/"
        assert contract.get_base_uri() == expected_base_uri
        
        print(f"✅ Base URI: {contract.get_base_uri()}")


def test_initial_ownership(fresh_nft_contract):
        """Test that the deployer becomes the owner of the contract."""
        contract = fresh_nft_contract
        
        # The deployer (boa.env.eoa) should be the owner
        deployer = boa.env.eoa
        owner = contract.owner()
        
        assert owner == deployer
        assert owner != "0x0000000000000000000000000000000000000000"  # Not zero address
        
        print(f"✅ Contract owner: {owner}")
        print(f"✅ Deployer address: {deployer}")
        print(f"✅ Ownership verification: {owner == deployer}")


def test_moccasin_main_function():
        """Test the moccasin_main function - THIS COVERS LINE 30."""
        # This test specifically covers line 30: return deploy_basic_nft()
        contract = moccasin_main()
        
        # Verify it returns the same as deploy_basic_nft
        assert isinstance(contract, VyperContract)
        assert contract.address is not None
        
        # Verify the NFT was minted
        assert contract.totalSupply() == 1
        assert contract.ownerOf(0) == boa.env.eoa
        
        # Verify the token URI
        expected_uri = f"https://gateway.pinata.cloud/ipfs/{ST_BERNARD_URI}"
        assert contract.tokenURI(0) == expected_uri
        
        print(f"✅ moccasin_main() executed successfully")
        print(f"✅ Contract deployed at: {contract.address}")
        print(f"✅ Line 30 coverage achieved: return deploy_basic_nft()")



    