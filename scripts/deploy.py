from time import time
from brownie import accounts, FundMe ,network, config,MockV3Aggregator
import os,time
from scripts.helpfulScript import (
    get_account,
    deploy_mocks,
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
)

 

def deploy_fund_me():
    account = get_account()
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
    else:
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address

    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )
    print(f"Contract deployed to {fund_me.address}")
    return fund_me


def main():
    deploy_fund_me()
"""def deploy_fund_me():
    account = helpfulScript.get_account()
    if network.show_active() != "developement":
     print("hello")
     price_feed_address = config["networks"][network.show_active()][
         "0x8A753747A1Fa494EC906cE90E9f37563A8AF630e"
     ]
 
    fund_me = FundMe.deploy(
       price_feed_address,
       {"from": account},publish_source = True)
    time.sleep(1)    
    print(f"contract deployed to {fund_me.address}")
    



def main():
    deploy_fund_me()"""
