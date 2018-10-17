from InstagramAPI import InstagramAPI
from PageParser import Parser
from urllib.error import HTTPError
from time import sleep


class MassFollow:
    def __init__(self,username,password,delay,count):
        self.API = InstagramAPI(username,password)
        self.API.login()
        self.donors = {}
        self.donorsFollowers = {}
        self.delay = delay
        self.count = count

    def setDonors(self,*args):
        for donor in args:
            try:
                p = Parser(donor)
                self.donors[p.getUserId()] = ""
                sleep(1)
            except HTTPError:
                print("Bad username {}".format(donor))
        print("Donors has been setted: {}".format(self.donors))

    def getDonorsFollowers_all(self, next=''):
        if len(self.donors)>0:
            for donor in self.donors.keys():
                self.API.getUserFollowers(donor,next)
                followers = []
                try:
                    self.donors[donor] = self.API.LastJson['next_max_id']
                except KeyError:
                    print(donor)
                    self.donors[donor] = ''
                try:
                    for follower in self.API.LastJson['users']:
                        followers.append(follower['pk'])
                    self.donorsFollowers[donor] = followers
                except KeyError:
                    self.donorsFollowers[donor] = followers
        else:
            print("Error! You must set donors (MassFollow.setDonors(*args))!")

    def getDonorsFollowers(self):
        if len(self.donors) > 0:
            for donor in self.donors.keys():
                self.API.getUserFollowers(donor)
                followers = []
                for follower in self.API.LastJson['users']:
                    followers.append(follower['pk'])
                self.donorsFollowers[donor] = followers
        else:
            print("Error! You must set donors (MassFollow.setDonors(*args))!")

    def run(self):
        if len(self.donorsFollowers)>0:
            count = 0
            for donor in self.donors.keys():
                for follower in self.donorsFollowers[donor]:
                    self.API.follow(follower)
                    print("You are follow {}".format(follower))
                    sleep(self.delay)
                    count+=1
                    if count > self.count:
                        break
                #Get 200 followers yet from one account
                #if self.donors[donor] != '':
                    #self.getDonorsFollowers(self.donors[donor])
                #else:
                    #self.donors.pop(donor)
                    #self.donorsFollowers.pop(donor)
        else:
            print("Error! You must add donors followers (MassFollow.getDonorsFollowers())!")
