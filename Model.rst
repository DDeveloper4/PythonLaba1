# class which contains constructor, destructor and methods

# for change attributes this class


class CalendarDay:
    def __init__(self, date, temperature, clouds, pressure):
        self.date = date
        self.temperature = temperature
        self.clouds = clouds
        self.pressure = pressure

    def displayDayInfo(self):
        print "Day date is ", self.date
        print "Temperature - ", self.temperature
        print "Clouds - ", self.clouds
        print "Pressure - ", self.pressure

    def setNewTemperature(self, temperature):
        self.temperature = temperature

    def setNewClouds(self, clouds):
        self.clouds = clouds

    def setNewPressure(self, pressure):
        self.pressure = pressure

diary = []
