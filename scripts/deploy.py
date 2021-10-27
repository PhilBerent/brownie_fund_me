from brownie import FundMe, MockV3Aggregator, accounts, config, network
from scripts.helpful_scripts import (
    get_account,
    deploy_mocks,
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
    # db
    # testIt,
    # ed
)
from web3 import Web3


def deploy_fund_me():
    account = get_account()

    # if we are on a persistant network like kovan the use the associated address
    # otherwise, deploy mocks
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
    else:
        print("Mocks Deployed!")
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address
        # db
        print(f"price_feed_address from deploy is {price_feed_address}")
        # ed

    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": account},
        # following line could also be
        # publish_source=config["networks"][network.show_active()]["verify"]
        # but using get means that it wont crash if I have forgotten to put verify for this network in brownie-config
        publish_source=config["networks"][network.show_active()].get("verify"),
    )
    print(f"Contract deployed to {fund_me.address}")
    # db
    # testIt()
    # ed

    print("Hey, Hey, Phil Phil Phil2")
    return fund_me


def main():
    deploy_fund_me()
