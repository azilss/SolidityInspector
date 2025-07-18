import requests
import sys

ETHERSCAN_API_KEY = "YOUR_ETHERSCAN_API_KEY"

def fetch_abi(address):
    url = f"https://api.etherscan.io/api?module=contract&action=getabi&address={address}&apikey={ETHERSCAN_API_KEY}"
    response = requests.get(url).json()
    if response["status"] == "1":
        return response["result"]
    else:
        print("Error fetching ABI:", response["result"])
        return None

def basic_vulnerability_scan(abi_str):
    abi_lower = abi_str.lower()
    if "withdraw" in abi_lower:
        print("Potential reentrancy vulnerability: 'withdraw' function found.")
    if "owner" not in abi_lower:
        print("Warning: 'owner' pattern not found — contract might lack ownership checks.")

def main():
    if len(sys.argv) != 2:
        print("Usage: python solidity_inspector.py <contract_address>")
        return
    address = sys.argv[1]
    abi = fetch_abi(address)
    if abi:
        basic_vulnerability_scan(abi)

if __name__ == "__main__":
    main()
