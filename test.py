from NMEA0183 import NMEA0183File

#Provides the required serial device info
nmea = NMEA0183File("plaka.log")

#Starts the serial connection
nmea.start()

#Checks if there is a valid connection
if nmea.exit == False:
   print 'Connection!'
   
   #More info on data names below
   #Different data types require different devices...obviously...
   #Some examples...
   
   #GPS data
   print nmea.data_gps['lat']
   print nmea.data_gps['lon']
   
   #Depth data
   print nmea.data_depth['feet']
   
   #Weather data
   print nmea.data_weather['wind_angle']
   print nmea.data_weather['water_temp']
   
   #Rudder data
   print nmea.data_rudder['stbd_angle']
   
   #Quit the NMEA connection
   nmea.quit()

else:
   print 'No connection!'
