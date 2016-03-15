class CalendarDay:
   date = ''
   temperature = 0
   clouds = ''
   pressure = 0

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
