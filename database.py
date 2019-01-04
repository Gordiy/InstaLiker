import mysql.connector


class ConnectToDB():
    # create connection to the database
    def __init__(self, host, user, db_pswd, db):
        self.inst_db = mysql.connector.connect(
            host = host,
            user = user,
            password = db_pswd,
            database = db
        )

        # make cursor
        self.mycursor = self.inst_db.cursor()

    # set data to db
    def set_user(self, login, password):
        # make request to db
        sql = "INSERT INTO instagram_db (login, password) VALUES (%s, %s)"
        value = (login, password)
        # set data to db
        self.mycursor.execute(sql, value)
        # save data in db
        self.inst_db.commit()


    # get data from db
    def get_users(self):
        # make request to db
        self.mycursor.execute("SELECT * FROM instagram_db.instagram_db;")
        # get all elements in db
        result = self.mycursor.fetchall()
        return result


    # check if user created
    def get_certain_user(self, login):
        # make request to db, which return user
        result = self.mycursor.execute("SELECT * FROM instagram_db.instagram_db;")
        # get all elements in db
        result = self.mycursor.fetchall()

        # return True if user created
        for i in range(len(result)):
            if result[i][0] == login:
                return True
            else:
                return False


    def delete_user(self, login):
        # make request to db, which delete data from database
        sql = "DELETE FROM instagram_db WHERE login = '{0}'".format(login)
        # set data to db
        self.mycursor.execute(sql)
        # save data in db
        self.inst_db.commit()

