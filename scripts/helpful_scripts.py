from brownie import network, config, accounts, MockV3Aggregator
from web3 import Web3

# db
# from brownie import FundMe
# ed

DECIMALS = 8
STARTING_PRICE = 20000000000

FORKED_LOCAL_ENVIRONMENTS = ["mainnet-fork", "mainnet-fork-dev"]
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local"]


def get_account():
    print("into getaccount")
    if (
        network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS
        or network.show_active() in FORKED_LOCAL_ENVIRONMENTS
    ):
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def deploy_mocks():
    print(f"The active network is {network.show_active()}")
    print("Deploying Mocks...")
    if len(MockV3Aggregator) <= 1000:
        MockV3Aggregator.deploy(DECIMALS, STARTING_PRICE, {"from": get_account()})
    # db
    price_feed_address1 = MockV3Aggregator[-1].address
    print(f"price_feed address {price_feed_address1}")
    # ed
    print("Mocks Deployed!")
