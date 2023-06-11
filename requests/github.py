import requests
class Github:
    def __init__(self):
        self.api_url = "https://api.github.com"
        self.token = "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"
    def findUser(self,username):
        response = requests.get(self.api_url + '/users/' + username)
        return response.json()
    def getRepository(self,username):
        response = requests.get(self.api_url + "/users/" + username + "/repos")
        return response.json()
    def createRepo(self,reponame,username):
        self.data = {
            "name": reponame,
            "desription": "Python BTK",
            "private": False,
            "homepage": "https://instagram.com/emretkkn"
        }
        self.headers = {'Authorization': f'token {self.token}'}
        response = requests.post(self.api_url + '/users/' + username, data=self.data, headers=self.headers)
        return response.json()
repo = Github()

while True:
    choose = int(input("1- Find User\n2- Get Repos\n3- Create Repository\n4- Exit\nWrite Number: "))
    if choose == 4:
        break
    else:
        if choose == 1:
            username = input("Write Username: ")
            username.strip()
            result = repo.findUser(username)
            name = result["name"]
            location = result["location"]
            bio = result["bio"]
            followers = result["followers"]
            print(f"Name: {name}\nLocation: {location}\nBiography: {bio}\nFollowers: {followers}")
        elif choose == 2:
            username = input("Write Username: ")
            username.strip()
            result = repo.getRepository(username)
            for repo in result:
                name = repo["name"]
                id = repo["id"]
                print(f"{name} Id: {id}")
        elif choose == 3:
            username = input("Write Username: ")
            username.strip()
            reponame = input("Write New Repository Name: ")
            reponame.replace(" ","-")
            result = repo.createRepo(reponame,username)
            print(f"{result}")
        else:
            print("Undefined Value.")