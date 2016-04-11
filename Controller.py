import doctest
import re
import pydoc
import Model


# function to display second menu


def Date_menu():
    print ("                 1. TEMPERATURE")
    print ("                 2. CLOUDS")
    print ("                 3. PRESSURE")
    print ("                 4. EXIT")


# function to display all days


def showAllDays(diary):
    if (len(diary) == 0):
        print ("Error! Diary is empty")
    else:
        for i in diary:
            i.displayDayInfo()
            print ("------------------------")


# input date


def Input_date():
    while True:
        print ("DATE (in dd.mm.yyyy): ")
        date = input()
        if (checkingDate(date)):
            return date

# input temperature


def Input_temperature():
    while True:
        print ("TEMPERATURE (in Celsiuses (-60 to +60)): ")
        temperature = input()
        if (checkingTemperature(temperature)):
            return temperature

# input clouds


def Input_clouds():
    while True:
        print ("CLOUDS (clear, sunny, cloudy, fog, rain): ")
        clouds = input()
        if (checkingClouds(clouds)):
            return clouds

# input pressure


def Input_pressure():
    while True:
        print ("PRESSURE (value of 700 to 800): ")
        pressure = input()
        if (checkingPressure(pressure)):
            return pressure


# function to add a new day


def addDay(diary):
    date = Input_date()
    temperature = Input_temperature()
    clouds = Input_clouds()
    pressure = Input_pressure()
    for i in diary:
        if i.date == date:
            print("Error! Date already exists")
    else:
        diary.append(Model.CalendarDay(date, temperature, clouds, pressure))

# function to delete a day


def delDay(diary):
    date = Input_date()
    for day in Model.diary:
        if day.date == date:
            Model.diary.remove(day)
            break
    else:
        print ("Error! Date not found")


# function to find a day


def findDay(diary):
    date = Input_date()
    for day in Model.diary:
        if day.date == date:
            day.displayDayInfo()
            break
    else:
        print ("Error! Date not found")


# function to change a day


def changeDay(diary):
    Date_menu()
    while True:
        key = input()
        if key == "1":
            temperature = Input_temperature()
            day.setNewTemperature(temperature)
            Date_menu()
            temperature = None
        elif key == "2":
            clouds = Input_clouds()
            day.setNewClouds(clouds)
            Date_menu()
            clouds = None
        elif key == "3":
            pressure = Input_pressure()
            day.setNewPressure(pressure)
            Date_menu()
            pressure = None
        elif key == "4":
            Main_menu()
            break

# checking date on correct


def checkingDate(date):
    """

    >>> checkingDate('12.02.2015')
    1
    """
    if (len(date) == 10):
        if ((date[0] == '1') or (date[0] == '2')):
            if (date[3] == '1'):
                p = re.compile(r"^[0-2][0-9][.][1][0-2][.][0-9][0-9][0-9][0-9]$")
            if (date[3] == '0'):
                p = re.compile(r"^[0-2][0-9][.][0][0-9][.][0-9][0-9][0-9][0-9]$")
        if (date[0] == '3'):
            if (date[3] == '1'):
                p = re.compile(r"^[03][0-1][.][1][0-2][.][0-9][0-9][0-9][0-9]$")
            if (date[3] == '0'):
                p = re.compile(r"^[3][0-1][.][0][0-9][.][0-9][0-9][0-9][0-9]$")
        if p.search(date):
            return 1

# checking temperature on correct


def checkingTemperature(temperature):
    """

    >>> checkingTemperature(2)
    1
    """
    a = int(temperature)
    if ((a >= -60) and (a <= 60)):
        return 1

# checking clouds on correct


def checkingClouds(clouds):
    """
    ;param checkingClouds: contact temperature
    >>> checkingClouds('clear')
    1
    """
    reserved_clouds = ['clear', 'sunny', 'cloudy', 'fog', 'rain']
    for i in reserved_clouds:
        if i == clouds:
            return 1

# checking pressure on correct


def checkingPressure(pressure):
    """
    ;param checkingPressure: contact temperature
    >>> checkingPressure(750)
    1
    """
    a = int(pressure)
    if ((a >= 700) and (a <= 800)):
        return 1

if (__name__ == '__main__'):
    import doctest
    doctest.testmod()
