# random code because stupid things are fun to do

"""
    code to find which github user has the given set of numbers as their id
    this code brings the user's info that could be found with the api + their avatar
"""

import requests

class GetTheUser():
    def __init__(self, user_input):
        self.id = user_input - 1
        self.set_avatar()

    def user_data(self):
        from json import loads
        url = f"https://api.github.com/users?since={self.id}"
        response = requests.get(url)
        res = loads(response.content.decode("utf8"))
        user_data = res[0]
        return user_data

    def set_avatar(self):
        user_data = self.user_data()
        from PIL import Image
        avatar_url = user_data['avatar_url']
        self.img = Image.open(requests.get(avatar_url, stream=True).raw)

user_input = int(input('Enter numbers: '))
gt = GetTheUser(user_input)
print(gt.user_data())
gt.img.show()
