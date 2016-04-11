import Model
import Controller
import pip

# function to display first menu


def Main_menu():
    print ("                 1. SHOW")
    print ("                 2. ADD")
    print ("                 3. DELETE")
    print ("                 4. CHANGE")
    print ("                 5. FIND")
    print ("                 6. EXIT")

Main_menu()

while True:
    key = input()
    if key == "1":
        Controller.showAllDays(Model.diary)
        Main_menu()
    elif key == "2":
        print ("Please enter data for the day")
        Controller.addDay(Model.diary)
        Main_menu()
    elif key == "3":
        Controller.delDay(Model.diary)
        Main_menu()
    elif key == "4":
        date = Controller.Input_date()
        for day in Model.diary:
            if day.date == date:
                Controller.changeDay(Model.diary)
            else:
                print ("Error! Date not found")
                Main_menu()
    elif key == "5":
        Controller.findDay(Model.diary)
        Main_menu()
    elif key == "6":
        print ("Goodbye")
        break

if (__name__ == '__main__'):
    import doctest
    doctest.testmod()
