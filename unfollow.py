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
        count = 0
        for follower in self.followers:
            #self.API.unfollow(follower)
            print('{} was unfollowed'.format(follower))
            #sleep(60)
            f = open('test.txt','a')
            f.write(str(follower)+'\n')
            f.close()
            count += 1
            if count > 999:
                break
        #self.getFollowers()
        #if len(self.followers)>0:
            #self.run()