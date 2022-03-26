from brownie import VianuToken, config, network
from scripts.helpful_scripts import (
    get_account,
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
)
from web3 import Web3

# setting initial supply to use as a constructor param when deploying the token
initial_supply = Web3.toWei(1000000, "ether")


def deploy_token():
    account = get_account()
    VianuToken.deploy(
        initial_supply,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify", False),
    )


def main():
    deploy_token()
