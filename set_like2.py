from InstagramAPI import InstagramAPI
import time
from database import ConnectToDB


class SetLike():
    def __init__(self, login, password):
        self.login = login,
        self.password = password

    db = ConnectToDB("localhost", "root", "фвьшт", "instagram_db")
    users = db.get_users()


    def unliked_users(self):
        return {self.login: self.password}


    # funk which put like
    def put_like(self, Media, liker):
        # get media id
        MediaID = Media['id']

        # call like media method
        isLike = liker.like(mediaId=MediaID)

        if isLike:
            print("Your post {0} has been liked.".format(MediaID))
        else:
            print("Your media not liked.")


    def liking(self):
        for unliked_user in range(len(self.unliked_users())):
            # print(i, unliked_users.get(i))

            un_user = InstagramAPI(self.login[0], self.password)

            if un_user.login():
                print("Login unliked user( {0} ) success!!!".format(unliked_user))

                # check if user created before
                if self.db.get_certain_user(self.login[0]) == False:
                    # adding user to database
                    print('added')
                    self.db.set_user(self.login[0], self.password)

                # get Self user feed
                un_user.getSelfUserFeed()

                # get response json and assignment value to MediaList Variable
                # dict type data
                MediaList = un_user.LastJson

                # get count posts unliked user
                count_posts = MediaList['num_results']

                for i in range(len(self.users)):

                    user = InstagramAPI(self.users[i][0], self.users[i][1])

                    if user.login():
                        print("Liker login!!!")

                        # like post's unliked user
                        for i in range(count_posts):
                            Media = MediaList['items'][i]
                            time.sleep(1.1)
                            self.put_like(Media, user)
                    else:
                        print("Login {0} error!!!".format(str(self.users[i][0])))
                        self.db.delete_user(self.users[i][0])

            else:
                print("Error login unliked user: {0}!!!".format(self.login))
