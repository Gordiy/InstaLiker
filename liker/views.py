from django.shortcuts import render
from .models import UserData
import mysql.connector


# create connection to the database
inst_db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "фвьшт",
    database = "instagram_db"
)

# make cursor
mycursor = inst_db.cursor()

# get user from db
def get_users():
    result = []
    # make request to db
    mycursor.execute("SELECT * FROM instagram_db.instagram_db;")
    # get all elements in db
    result = mycursor.fetchall()
    return result


# get_users()
print(get_users())

users = get_users()


def set_to_admin(request):
    users = get_users()

    # u = UserData.objects.order_by()

    for i in range(len(users)):
        if UserData.objects.filter(login = users[i][0]):
            print(users[i][0])
        else:
            UserData.objects.create(login=users[i][0], password=users[i][1])

    return render(request, "get_db.html")
