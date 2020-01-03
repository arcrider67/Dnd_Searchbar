import requests
import string
import json



class shuttle:

    __url = ""

    def hitApi(self,url, search):
        response = requests.get(url + search)
        if (response.ok):
            requestDataJson = json.loads(response.text)

        return(requestDataJson)
        
    def dataProcess(self, parameter_list):
            raise NotImplementedError


class shuttleSpell(shuttle):

    __url = "http://dnd5eapi.co/api/spells/?name="

    def hitApi(self,search):
        return shuttle.hitApi(self, self.__url, search)
        
    #handle a spell search
    def dataProcess(self, parameter_list):
        pass





