import doctest
import re
import pydoc

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
