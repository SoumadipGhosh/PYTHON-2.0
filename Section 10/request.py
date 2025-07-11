import requests
# // get request
r = requests.get('https://api.github.com/events')

# print(r.text)

with open ("codesg.txt","w") as f:
    f.write(r.text)
    
# post request .    