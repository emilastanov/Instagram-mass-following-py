from InstagramAPI import InstagramAPI
from time import sleep


class UnFollow:
    def __init__(self, username, password):
        self.API = InstagramAPI(username, password)
        self.API.login()
        self.followers = []

    def getFollowers(self):
        self.followers = []
        self.API.getSelfUsersFollowing()
        for follower in self.API.LastJson['users']:
            self.followers.append(follower['pk'])
        return self.followers

    def run(self):
        for follower in self.followers:
            self.API.unfollow(follower)
            print('{} was unfollowed'.format(follower))
            sleep(5)
        self.getFollowers()
        if len(self.followers)>0:
            self.run()
