from follow import MassFollow
from unfollow import UnFollow
import settings

while True:
    #Following
    m = MassFollow(settings.USERNAME,settings.PASSWORD)
    m.setDonors(
        'buzova86',
        'timatiofficial',
        'instagramru',
        'tnt_online',
        'pavelvolyaofficial'
    )
    m.getDonorsFollowers()
    m.run()

    print(
        "Following action has been finished!\n"
        "Starting unfollowing!"
    )

    #Write logs
    m.API.getSelfUsernameInfo()
    f = open('log.html', 'a')
    f.write(
        "<h4 style='margin: 0'>Bot finished task <i>'following'</i>!</h4>"
        "<p style='margin: 0'><b>{0}</b> have <b>{1}</b> followers</p><hr>\n"
        "".format(
            m.API.LastJson['user']['username'],
            m.API.LastJson['user']['follower_count']
        )
    )
    f.close()

    #Unfollowing
    u = UnFollow(settings.USERNAME,settings.PASSWORD)
    u.getFollowers()
    u.run()
    print(
        "Unfollowing action has been finished!\n"
        "Starting following!"
    )

    #Write logs
    m.API.getSelfUsernameInfo()
    f = open('log.html', 'a')
    f.write(
        "<h4 style='margin: 0'>Bot finished task <i>'unfollowing'</i>!</h4>"
        "<p style='margin: 0'><b>{0}</b> have <b>{1}</b> followers</p><hr>\n"
        "".format(
            m.API.LastJson['user']['username'],
            m.API.LastJson['user']['follower_count']
        )
    )
    f.close()



