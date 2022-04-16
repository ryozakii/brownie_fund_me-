from brownie import FundMe, accounts
from eth_account import Account
from web3 import Web3

from scripts.helpfulScript import get_account   

def fund():
   fund_me = FundMe[-1]
   account = get_account()
   entrance_fee = fund_me.getEntranceFee()
   print(f"the current intrence fee is {entrance_fee}")
   print("funding")  
   fund_me.fund({"from":account,"value": entrance_fee})
   print(entrance_fee)
def withdraw():
    withdraw_me = FundMe[-1]
    account = get_account()
    withdraw_me.withdraw({"from":account})     
def main():
   fund()   
   #withdraw()