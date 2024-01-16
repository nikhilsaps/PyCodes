import  requests
import json


responce =requests.get("https://api.jikan.moe/v4/anime?q=frierend%20no%20sousao&sfw")
print(responce.content)
