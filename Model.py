class CalendarDay:

   def __init__(self, date, temperature, clouds, pressure):
       self.date = date
       self.temperature = temperature
       self.clouds = clouds
       self.pressure = pressure

   def displayDayInfo(self):
       print "Day date is ", CalendarDay.date
       print "Temperature - ", CalendarDay.temperature
       print "Clouds - ", CalendarDay.clouds
       print "Pressure - ", CalendarDay.pressure

   def setNewTemperature(temperature):
       self.temperature = temperature 

   def setNewClouds(clouds):
       self.clouds = clouds 

   def setNewPressure(pressure):
       self.pressure = pressure 

diary = []    
    
    