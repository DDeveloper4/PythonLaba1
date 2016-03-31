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
    print ("                 1. TEMPERATURE")
    print ("                 2. CLOUDS")
    print ("                 3. PRESSURE")
    print ("                 4. EXIT")

#Pickle_file.load_f()

Main_menu()
while True:
    key = raw_input()
    if key == "1":
        Pickle_file.showAllDays()
        Main_menu()
    elif key == "2":
        print ("Please enter data for the day")
        while True:
            print ("DATE (in dd.mm.yyyy): ")
            date = raw_input()
            if (Pickle_file.checkingDate(date)):
                break

        while True:
            print ("TEMPERATURE (in Celsiuses): ")
            temperature = raw_input()
            if (Pickle_file.checkingTemperature(temperature)):
                break

        while True:
            print ("CLOUDS (clear, sunny, cloudy, fog, rain): ")
            clouds = raw_input()
            if (Pickle_file.checkingClouds(clouds)):
                break

        while True:
            print ("PRESSURE (value of 700 to 800): ")
            pressure = raw_input()
            if (Pickle_file.checkingPressure(pressure)):
                break
        Pickle_file.addDay(date, temperature, clouds, pressure)
        date = None
        temperature = None
        clouds = None
        pressure = None
        Main_menu()
    elif key =="3":
        while True:
            print ("DATE (in dd.mm.yyyy): ")
            date = raw_input()
            if (Pickle_file.checkingDate(date)):
                break

        for day in Model.diary:
            if day.date == date:
                Model.diary.remove(day)
                break
        else:
            print ("Error! Date not found")
        date = None
        Main_menu()
    elif key == "4":
        while True:
            print ("DATE (in dd.mm.yyyy): ")
            date = raw_input()
            if (Pickle_file.checkingDate(date)):
                break

        for day in Model.diary:
            if day.date == date:
                Date_menu()
                while True:
                    key = raw_input()
                    if key == "1":
                        while True:
                            print ("TEMPERATURE (in Celsiuses): ")
                            temperature = raw_input()
                            if (Pickle_file.checkingTemperature(temperature)):
                                break
                        day.setNewTemperature(temperature)
                        Date_menu()
                        temperature = None
                    elif key == "2":
                        while True:
                            print ("CLOUDS (clear, sunny, cloudy, fog, rain): ")
                            clouds = raw_input()
                            if (Pickle_file.checkingClouds(clouds)):
                                break
                        day.setNewClouds(clouds)
                        Date_menu()
                        clouds = None
                    elif key == "3":
                        while True:
                            print ("PRESSURE (value of 700 to 800): ")
                            pressure = raw_input()
                            if (Pickle_file.checkingPressure(pressure)):
                                break
                        day.setNewPressure(pressure)
                        Date_menu()
                        pressure = None
                    elif key == "4":
                        Main_menu()
                        break

                break
            else:
                print ("Error! Date not found")
    elif key == "5":
        while True:
            print ("DATE (in dd.mm.yyyy): ")
            date = raw_input()
            if (Pickle_file.checkingDate(date)):
                break
        for day in Model.diary:
            if day.date == date:
                day.displayDayInfo()
                break
        else:
            print ("Error! Date not found")
        Main_menu()
    elif key == "6":
        print ("Goodbye")
        break

#Pickle_file.return_file()



