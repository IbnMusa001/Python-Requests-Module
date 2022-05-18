import requests as req 
resp = req.get(input('Webpage to grab source from: '))

print(resp.text)