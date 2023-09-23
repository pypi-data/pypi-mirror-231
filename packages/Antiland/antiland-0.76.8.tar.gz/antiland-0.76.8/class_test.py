import requests

session_token="r:92fede4c6ad623f4dc2c41bf414fb19b"
dialogue="TOhmT4cR0d"

class Dialogue:
    def __init__(self, data):
        self.lang = data["lang"]
        self.groupAdmins = data.get("groupAdmins")
        self.lastmessage = data["lastmessage"]
        self.objectId = data["objectId"]
        self.guestname = data["guestname"]
        self.foundername = data["foundername"]
        self.founderId = data["founderId"]
        self.private = data.get("private")
        self.public = data.get("public")
        self.humanLink = data.get("humanlink")
        self.accepted = data["accepted"]
        self.flags = data["flags"]

def get_dialogue(dialogue,token):
        url="https://mobile-elb.antich.at/functions/getDialogue"
        json_payload={
            "dialogueId": dialogue,
            "v": 10001,
            "_ApplicationId": "fUEmHsDqbr9v73s4JBx0CwANjDJjoMcDFlrGqgY5",
            "_ClientVersion": "js1.11.1",
            "_InstallationId": "3e355bb2-ce1f-0876-2e6b-e3b19adc4cef",
            "_SessionToken": token
            }
        r=requests.post(url,json_payload)
        data = r.json()
        print(data)
        dialogue = Dialogue(data.get("result"))
        return dialogue.foundername

print(get_dialogue(dialogue,session_token))