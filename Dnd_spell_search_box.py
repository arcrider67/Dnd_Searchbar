import requests
import string
import json

def hitApi(name):
    response = requests.get("http://dnd5eapi.co/api/spells/?name="+name)
    if (response.ok):
        requestDataJson = json.loads(response.text)

        response = requests.get(requestDataJson["results"][0]["url"])
        return (response.text)

def main():
    done = False
    while(done == False):
        spell = str(input("type spell to search or done to exit"))

        if str(spell) == "done":
            done = True
        else:
            print(hitApi(spell))

main()