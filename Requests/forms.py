#request submission from the file

import requests

my_data ={
    "name" :"Ramesh Chaudhary",
    "email" : "ramesh@gmail.com"
}

url = "https://dipendrachand.com.np/demo/welcome.php"
r = requests.post(url, my_data)

myfile = open("form.html", "w+")
myfile.write(r.text)