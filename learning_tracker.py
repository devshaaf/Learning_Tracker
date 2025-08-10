import datetime as dt
import json
import re

class User: # class to create individual user obj
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.activities = []

    def to_dict(self):
        return {
            'username':self.username,
            'password':self.password,
            'activities': [{"topic":activity.topic, "time":activity.time, "note":activity.note, "date":activity.date} for activity in self.activities]
        }


class Activity: # class to create a complete activity of the user
    def __init__(self, topic, time, note):
        self.topic = topic
        self.time = time
        self.note = note
        self.date = str(dt.date.today())

users = [] # list where all the users will be stored inside.

def load_data():
    with open(r"D:\Python\JSONS\users.json", "r") as file:
        users_data = json.load(file)
    

    for user_dic in users_data: # loop to convert the user dict into user object
        user = User(user_dic["username"], user_dic["password"])
        activity_obj = [Activity(activity["topic"], activity["time"], activity["note"]) for activity in user_dic["activities"]] # list of the converted activity objs from dicts

        idx=0
        for activity in activity_obj:
            # activity.date = user_dic["date"] # change the updated date with the date in json file.
            # for idx in range(len(user_dic["activities"])):
            #     activity.date = user_dic["activities"][idx]["date"] # fetch the date on the specific index.
            activity.date = user_dic["activities"][idx]["date"]
            idx+=1

        user.activities.extend(activity_obj)
        users.append(user) # append all the converted users with converted activities into users list

load_data() # loads the data when the scripts run


def display_user_activities(user):
    for activity in user.activities:
        print("-"*30)
        print(f"Topic: {activity.topic}")
        print(f"Time: {activity.time} minutes")
        print(f"NOTE: {activity.note}")
        print(f"Date: {activity.date}")
        print("-"*30)


def output_message(message):
    print("-"*30 + "\n" + message + "\n" + "-"*30)

def log_activity(): # function to log the activity
            while True:
                try:
                    print("Enter your log activity:")
                    topic = input("Enter the topic:").lower()
                    time = int(input("Enter the time (Min): "))
                    note = input("Enter your NOTE: ")
                    newActivity = Activity(topic, time, note)
                    break
                except ValueError:
                    output_message("Enter the time in numbers!")

            return newActivity


def is_unique(username): # function to check if username exist or not
    for user in users:
        if(user.username == username):
            return False
    return True

def register_User(): # function to register new user
        try:
            username = input("Create a username: ")

            if(is_unique(username)): # check if the username exist or not
                password = input("Create a password: ")
                newUser = User(username, password)
                users.append(newUser)
                output_message("New user account has been created!")

            else:
                output_message("Username Already Exist!")

        except ValueError:
                output_message("Please enter numbers only for password!")


def display_filtrd_activities(filtrd_list): # display filtered activities by date or by topic
    for filtr_activity in filtrd_list:
        print("-"*30)
        print(f"Topic: {filtr_activity.topic}")
        print(f"Time: {filtr_activity.time} minutes")
        print(f"NOTE: {filtr_activity.note}")
        print(f"Date: {filtr_activity.date}")
        print("-"*30)

def filter_activities(user, filter_choice):
    pattern = r"^\d{4}-\d{2}-\d{2}$" # format yyyy-mm-dd

    if re.match(pattern, filter_choice):
        filtrd_by_date = [activity for activity in user.activities if activity.date == re.match(pattern, filter_choice).group()] # filtered activity objects by date

        display_filtrd_activities(filtrd_by_date)

    else:
        if "-" in filter_choice:
            print("Incorrect Format!")

        else:
            filtrd_by_topic = [activity for activity in user.activities if activity.topic == filter_choice] # filtered activity objects by topic.
            display_filtrd_activities(filtrd_by_topic)


def show_stats(user):
    total_time = 0

    for activity in user.activities: # adds all the time
        total_time+=activity.time

    total_activities = len(user.activities)

    avg_time_pr_act = total_time//total_activities

    print("-"*30, "\n"+"Your Stats:")
    print(f"You have spent a total of {total_time} minutes learning so far.")
    print(f"You have logged {total_activities} activities in total.")
    print(f"On average, each activity lasts around {avg_time_pr_act} minutes.")
    print("-"*30)


def user_menu(user):
    while True: # after log in loop
        try:
            user_choice = int(input("1) Log new Activity\n2) View all Activities\n3) Filter Activities\n4) Show Stats\n5) Save new data to file\n6) Log Out\n"))

            if(user_choice == 1): # add new activity
                newActivity = log_activity()
                user.activities.append(newActivity) # append to the activities list inside the User class
                output_message("Activity has been saved!")

            elif(user_choice == 2): # Display activities
                if(not user.activities): # check if there are activities logged or not
                    output_message("No Activities are logged yet!")

                else: # displaying all the activities of the user
                    display_user_activities(user)

            elif(user_choice == 3): # filter activities by date or topic
                filter_choice = input("Filter by date (YYYY-MM-DD) or topic: ").lower()
                filter_activities(user, filter_choice)

            elif(user_choice == 4): # show stats
                show_stats(user)
            
            elif(user_choice == 5): # save date to file
                save_data()

            elif(user_choice == 6): # log out
                output_message("Logged out successfully")
                break

        except ValueError:
                output_message("Enter a valid option!")

def user_input():
    try:
            username = input("Enter your username: ")
            password = input("Enter your password: ")
    except ValueError:
            output_message("Invalid input format. Please try again.")
    
    return username, password


def login_User(): # function to login user
    username, password = user_input()

    if(not users):
            output_message("No users found!")
    else:
            found_user = None
            attempts = 1

            while True: # authentication loop
                for user in users: # checking credentials
                    if user.username == username and user.password == password:
                        found_user = user
                        break
                # attempts+=1
            
                if found_user: # credentials matched
                    output_message(f"Hi {found_user.username}!\nWelcome Back")
                    user_menu(found_user)
                    break
                    
                elif attempts == 3: # attempts to login
                    output_message("Your Account has been locked due to unauthorized attempts!")
                    break

                else: #not matched
                    output_message("Credentials Not Matched!")
                    attempts+=1
                    username, password = user_input()
                


def save_data(): # function to save the data onto the JSON file
    users_list = [] # list containing converted user object into user dictionary
    for user in users:
        users_list.append(user.to_dict()) # convert each object into dictionary

    with open(r"D:\Python\JSONS\users.json", "w") as file:
        json.dump(users_list, file)

    output_message("Data has been saved to the file!")


def main_menu():
    while True: # main loop

        while True: # input validation loop
            try:
                user_choice = int(input("Welcome to the learning tracker app!\n1) Register\n2) Login\n3) Exit\n"))
                break
            except ValueError:
                output_message("Enter a valid option!")

        if(user_choice == 1): # register new user
            register_User()

        elif(user_choice == 2): # login to your account
            login_User()

        elif(user_choice == 3): # exit
            break


main_menu() # function to run the whole script


# few approches:
# remove all the parenthesis from if-else | done
# use **kwargs in User and Activity classes
# use @classmethod when making the returned data from json file back into objects