from datetime import datetime, timedelta

Sunday = list()
Monday=list()
Tuesday = list()
Wednesday = list()
Thursday = list()
Friday = list()
Saturday = list()

# Функция основной программы
def get_birthdays_per_week(users):
    
    current_date = datetime.today().date()
    count = sum(isinstance(item, dict) for item in users)
    i=0
    while i<count:
        l = (users[i]["birthday"])
        l1 = l[:5]
        l_dat = datetime.strptime(l1, "%d-%m").date().replace(year=current_date.year)
        difference = l_dat-current_date
                
        if timedelta(days=0) <= difference < timedelta(days=7):
            day = l_dat.strftime("%A")
            sort_birthday(day,i)
        i+=1
    return print_users()

# Функция сортировки имен по дням недели
def sort_birthday(day,i):
    
    user = users[i]["name"]

    if day == "Sunday":
        Monday.append(user)
    elif day == "Monday":
        Monday.append(user)
    elif day == "Tuesday":
        Tuesday.append(user)
    elif day == "Wednesday":
        Wednesday.append(user)
    elif day == "Thursday":
        Thursday.append(user)
    elif day == "Friday":
        Friday.append(user)
    elif day == "Saturday":
        Monday.append(user)    

# Функция печати по дням недели
def print_users():
    
    if len(Monday) >0:
        print("Monday:", ", ".join(Monday))
    if len(Tuesday) >0:    
        print("Tuesday:", ", ".join(Tuesday))
    if len(Wednesday) >0:     
        print("Wednesday:", ", ".join(Wednesday))
    if len(Thursday) >0:
        print("Thursday:", ", ".join(Thursday))
    if len(Friday) >0:
        print("Friday:", ", ".join(Friday))        

# Cписок словарей users
users = [
    {"name":"Alex","birthday":"30-06-1982"},
    {"name":"Serj","birthday":"01-07-1976"},
    {"name":"Nikola","birthday":"02-07-1969"},
    {"name":"Yuriy","birthday":"03-07-1986"},
    {"name":"Olga","birthday":"04-07-1984"},
    {"name":"Andrey","birthday":"05-07-1985"},
    {"name":"Bogdan","birthday":"06-07-1982"}]

if __name__ == "__main__":
    get_birthdays_per_week(users)