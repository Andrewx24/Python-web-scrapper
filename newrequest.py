
import requests 
URL = "https://realpython.github.io/fake-jobs//" 
r = requests.get(URL) 
print(r.text) 