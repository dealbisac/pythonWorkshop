#Params

import requests

params = {"q" : "python"}
r = requests.get("https://www.google.com/search", params=params)

print("Status", r.status_code)

print(r.url)
print(r.text)


# saving code to the file
f = open("search.html", "w+");
f.write(r.text)
