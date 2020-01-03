import requests
import string
import json
from item import shuttleSpell



def main():
    done = False
    while(done == False):
        
        shuttle = shuttleSpell()
        
        spell = str(input("type spell to search or done to exit"))

        if str(spell) == "done":
            done = True
        else:
            shuttle.hitApi(spell)
            print("successful")

main()