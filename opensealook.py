import requests

def get_owned_nfts(wallet_address, collection_slug):
    base_url = "https://api.opensea.io/api/v1/assets"
    params = {
        "owner": wallet_address,
        "collection": collection_slug,
        "order_direction": "desc",
        "offset": 0,
        "limit": 50  # Adjust this value based on your requirements, max is 50
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: Unable to fetch NFTs for wallet '{wallet_address}', status code {response.status_code}")
        return None

# Replace 'wallet_address' and 'collection_slug' with the actual values
wallet_address = "0xB99a55F4F9b49F3f88BcdC242194AED4E0756D25"
collection_slug = "asm-gen-ii-brains"

owned_nfts = get_owned_nfts(wallet_address, collection_slug)

if owned_nfts:
    token_ids = [nft["token_id"] for nft in owned_nfts["assets"]]
    print(token_ids)
