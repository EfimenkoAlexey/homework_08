from datetime import datetime
import collections


def get_birthdays_per_week(users):
    
    # birthday = datetime.weekday()
    Users = collections.namedtuple("Users",["name","birthday"])
    # users = Users("Alex","Monday")
    # for keys, value in users.items():
    
    # d = datetime.strptime(users[0][0], "%d-%m-%Y")
    # print(d.strptime("%A"))
    print(users[0])


users = [
    {"name":"Alex","birthday":"27-01-1982"},
    {"name":"Serj","birthday":"04-09-2010"},
    {"name":"Nikola","birthday":"17-12-1969"},
    {"name":"Yuriy","birthday":"11-12-2016"},
    {"name":"Olga","birthday":"10-12-1984"},
    {"name":"Andrey","birthday":"30-03-1985"},
    {"name":"Bogdan","birthday":"26-04-1995"}]
print(get_birthdays_per_week(users))