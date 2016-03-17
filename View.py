import Model
import Pickle_file

def Main_menu():
    print ("                 1. SHOW")
    print ("                 2. ADD")
    print ("                 3. DELETE")
    print ("                 4. CHANGE")
    print ("                 5. FIND")
    print ("                 6. EXIT")

def Date_menu():
    print ("                 1. DATE")
    print ("                 2. TEMPERATURE")
    print ("                 3. CLOUDS")
    print ("                 4. PRESSURE")

Main_menu()
while True:
    key = raw_input()
    if key == "1":
        #show
        Main_menu()
    elif key == "2":
        print ("Please enter data for the day")
        print ("Date: ")
        date = raw_input()
        print ("TEMPERATURE: ")
        temperature = raw_input()
        print ("Date: ")
        clouds = raw_input()
        print ("CLOUDS: ")
        pressure = raw_input()
        #add new dat
    elif key =="3":
        print ("Please enter date")
        date = raw_input()
        for day in Main_menu():
            if day.date == date:
                Main_menu().remove(day)
    elif key == "4":
        print ("Please enter date")
        #Date_menu()
        #change
    elif key == "5":
        print ("Please enter date")
        #find
    elif key == "6":
        print ("Goodbye")
        break





