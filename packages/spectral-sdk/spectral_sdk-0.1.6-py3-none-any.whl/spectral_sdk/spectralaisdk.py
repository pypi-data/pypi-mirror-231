from spectral_sdk.config_manager import ConfigManager
from functools import wraps
from tqdm import tqdm
from web3 import Web3
import click
import os
import requests
from . import CONFIG_PATH, ALCHEMY_URL, ABIS


from retrying import retry
config_manager = None
@retry(stop_max_attempt_number=3, wait_fixed=2000)
def fetch_from_ipfs(cid, filename, file_type = "File"):
    primary_source = "http://ipfs.io/ipfs/"
    url = primary_source + cid

    try:
        # Make the GET request to fetch the file content
        response = requests.get(url, timeout=(3,8), stream=True)
        
        # Check if the request was successful
        response.raise_for_status()
        
        total_size = int(response.headers.get('content-length', 0))
        block_size = 8192  # 8K
        progress_bar = tqdm(total=total_size, unit='iB', unit_scale=True)

        # Save the content to the specified file
        with open(filename, 'wb') as f:
            for chunk in response.iter_content(chunk_size=block_size):
                f.write(chunk)
                progress_bar.update(len(chunk))
        
        progress_bar.close()
        print(f"{file_type} successfully downloaded!")
        

    except requests.ReadTimeout as e:
        print("Failed to fetch the file from the official gateway. Trying another gateway...")
        response = requests.post("http://ipfs.dev.spectral.finance:5001/api/v0/cat?arg=" + cid)
        
        # Check if the request was successful
        response.raise_for_status()
        
        total_size = int(response.headers.get('content-length', 0))
        block_size = 8192  # 8K
        progress_bar = tqdm(total=total_size, unit='iB', unit_scale=True)
        
        # Save the content to the specified file
        with open(filename, 'wb') as f:
            for chunk in response.iter_content(chunk_size=block_size):
                f.write(chunk)
                progress_bar.update(len(chunk))
        
        progress_bar.close()
        print(f"{file_type} successfully fetched from the alternative gateway!")


@click.group()
def cli():
    """Modelers SDK provides tools to interact with Spectral platform and taking part in competitions."""
    pass

def ensure_global_config():
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            config_manager = ConfigManager(CONFIG_PATH)
            config_updated = False
            if config_manager.get('global', 'api_key') is None:
                click.echo("Input your Spectral API key.XD")
                click.echo("To get your Spectral API key, please visit https://app.spectral.dev/account")
                api_key = click.prompt("Spectral API key:")
                config_manager.set('global', 'api_key', api_key)
                config_updated = True
                click.echo("\n")
            if config_manager.get('global', 'alchemy_api_key') is None:
                click.echo("Input your Alchemy API key.")
                click.echo(
                    "To get your Alchemy API key, please visit https://www.alchemy.com/")
                alchemy_api_key = click.prompt("Alchemy API key:")
                config_manager.set('global', 'alchemy_api_key', alchemy_api_key)
                config_updated = True
                click.echo("\n")
            if config_manager.get('global', 'wallet_private_key') is None:
                click.echo(
                    "Paste your wallet private key. Why do we need it? Check out https://docs.spectral.dev/faq")
                click.echo(
                    "If you signed up using Privvy, please visit https://app.spectral.dev/account to get your private key.")
                api_key = click.prompt("Your Wallet's private key", hide_input=True)
                config_manager.set('global', 'wallet_private_key', api_key)
                config_updated = True
            if config_updated:
                click.echo("Your Spectral account has been configured.")
            return func(config_manager, *args, **kwargs)
        return wrapper
    return decorator

@cli.command()
@ensure_global_config()
def datawrappers_list(config_manager):
    """Configures datawrappers. To see available datawrappers run `spectral datawrappers`."""
    wrappers = ["spectral-credit-scoring", "another-datawrapper"]
    click.echo(
        f"Available datawrappers. {wrappers}. To (re)configurate datawrapper run `spectral datawrapper configure <wrapper_name>`")

@cli.command()
@ensure_global_config()
@click.argument('challenge_id')
def fetch_training_data(config_manager, challenge_id):
    """Configures datawrappers. To see available datawrappers run `spectral datawrappers`."""
    competition_abi = ABIS['Competition']
    web3_provider_api_key = config_manager.get('global', 'alchemy_api_key')
    w3 = Web3(Web3.HTTPProvider(ALCHEMY_URL + web3_provider_api_key))
    contract = w3.eth.contract(address=challenge_id, abi=competition_abi)
    ipfsTrainingDataset = contract.functions.ipfsTrainingDataset().call()
    filename = f"{challenge_id}_training_data.csv"
    fetch_from_ipfs(ipfsTrainingDataset, filename, "Training dataset")


@cli.command()
def update_contract():
    """setIP`."""
    token_abi = ABIS['Competition']
    token_address = "0x25170a5dE754C2B31289533d6E35188d6d0FC712"
    web3_provider_api_key = config_manager.get('global', 'alchemy_api_key')
    w3 = Web3(Web3.HTTPProvider((ALCHEMY_URL + web3_provider_api_key)))
    contract = w3.eth.contract(address=token_address, abi=token_abi)

    txn = contract.functions.setIPFSTrainingDataSet("123test").build_transaction(transaction={
        'chainId': 5,  # or whatever chain you're using
        'gas': 2000000,
        'gasPrice': w3.to_wei('1000', 'gwei'),
        'nonce': w3.eth.get_transaction_count("0xcE2734897240ff52c0cBE1c248A69F540502F0C4")
    })
    private_key = "xd"
    signed_txn = w3.eth.account.sign_transaction(txn, private_key)
    txn_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
    print('Transaction successful with hash:', txn_hash.hex())
    txn_receipt = w3.eth.wait_for_transaction_receipt(txn_hash)

    print('Transaction successful with hash:', txn_hash.hex())
    click.echo(f"Hello!")


@cli.command()
@ensure_global_config()
def configure(config_manager):
    """Configures datawrappers. To see available datawrappers run `spectral datawrappers`."""
    click.echo(f"Spectral SDK is configured!")

if __name__ == '__main__':
    cli()
    pass
