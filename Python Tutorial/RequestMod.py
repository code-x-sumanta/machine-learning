import requests
r=requests.get("Enter the url from google")
print(r.text)
print(r.status_code)