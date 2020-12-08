import requests

r = requests.get("https://www.google.com/logos/doodles/2020/december-holidays-days-2-30-6753651837108830.3-law.gif")

with open("google_20201208.gif", "wb") as f:
    f.write(r.content)
print("saved")