from follow import MassFollow
from unfollow import UnFollow
import settings

if __name__ == '__main__':
    """
    m = MassFollow(settings.USERNAME,settings.PASSWORD)

    m.setDonors(
        'sayonaraboy',
        '_agentgirl_'
    )
    m.getDonorsFollowers()
    #m.run()
    print(m.donorsFollowers)
    m.run()
    """
    u = UnFollow(settings.USERNAME,settings.PASSWORD)
    u.run()