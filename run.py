from follow import MassFollow
import settings

if __name__ == '__main__':
    m = MassFollow(settings.USERNAME,settings.PASSWORD)

    m.setDonors(
        'sayonaraboy',
        '_agentgirl_'
    )
    m.getDonorsFollowers()
    m.run()