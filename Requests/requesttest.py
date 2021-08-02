#requests

import  requests

r = requests.get("https://www.google.com/" )

print("Status", r.status_code)

print(r.url)
print(r.text)


# saving code to the file
f = open("pages.html", "w+");
f.write(r.text)
