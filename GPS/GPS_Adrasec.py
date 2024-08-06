#!/usr/bin/python
#--------------------------------------
# Created by Raxgahrax
# Created for Adrasec 90/70
# Created : 24/06/19
# Revised : 21/02/20
# Source : https://github.com/hobuinc/mgrs
#--------------------------------------

import os
import sys
import random
import string 
from gps import *
from time import *
from math import floor
from time import strftime
import lcddriver
import time
import threading
import mgrs
import Adafruit_DHT

lcd = lcddriver.lcd()
m = mgrs.MGRS()
gpsd = None

class GpsPoller(threading.Thread):
   def __init__(self):
      threading.Thread.__init__(self)
      global gpsd
      gpsd = gps(mode=WATCH_ENABLE)
      self.current_value = None
      self.running = True
   def run(self):
      global gpsd
      while gpsp.running:
         gpsd.next()

gpsp = GpsPoller()
gpsp.start()

def printMessage_1():
   lcd.lcd_display_string("   Initialisation", 1)
   lcd.lcd_display_string("     Config du", 2)
   lcd.lcd_display_string("   recepteur GPS", 3)
   lcd.lcd_display_string("      en cours", 4)
   return
def printMessage_2():
   lcd.lcd_display_string("   Initialisation", 1)
   lcd.lcd_display_string("      Signaux", 2)
   lcd.lcd_display_string("    en cours de", 3)
   lcd.lcd_display_string("     reception", 4)
   return
def printMessage_3():
   random1=int(random.randint(1111111111111111,9999999999999999))
   a=str("  ")+str(random1)
   random2=int(random.randint(1111111111111111,9999999999999999))
   b=str("  ")+str(random2)
   random3=int(random.randint(1111111111111111,9999999999999999))
   c=str("  ")+str(random3)
   random4=int(random.randint(1111111111111111,9999999999999999))
   d=str("  ")+str(random4)
   lcd.lcd_display_string(a, 1)
   lcd.lcd_display_string(b, 2)
   lcd.lcd_display_string(c, 3)
   lcd.lcd_display_string(d, 4)
   return
def printMessage_4():
   random1=int(random.randint(1111111111111111,9999999999999999))
   a=str("  ")+str(random1)
   random2=int(random.randint(1111111111111111,9999999999999999))
   b=str("  ")+str(random2)
   random3=int(random.randint(1111111111111111,9999999999999999))
   c=str("  ")+str(random3)
   random4=int(random.randint(1111111111111111,9999999999999999))
   d=str("  ")+str(random4)
   lcd.lcd_display_string(a, 1)
   lcd.lcd_display_string(b, 2)
   lcd.lcd_display_string(c, 3)
   lcd.lcd_display_string(d, 4)
   return
def printMessage_5():
   lcd.lcd_display_string("    Piratage du", 1)  
   lcd.lcd_display_string("  reseau satellite", 2)
   lcd.lcd_display_string("    Cospas-Sarsat", 3)
   lcd.lcd_display_string("      en cours", 4)
   return
def printMessage_6():
   random1=int(random.randint(5,9))
   a=str("        0")+str(random1)+str(" %")
   lcd.lcd_display_string("  Donnees cryptees", 1)
   lcd.lcd_display_string("      en cours", 2)
   lcd.lcd_display_string("   d'acquisition", 3)
   lcd.lcd_display_string(a, 4)
   return
def printMessage_7():
   random1=int(random.randint(12,15))
   a=str("        ")+str(random1)+str(" %")  
   lcd.lcd_display_string("  Donnees cryptees", 1)
   lcd.lcd_display_string("      en cours", 2)
   lcd.lcd_display_string("   d'acquisition", 3)
   lcd.lcd_display_string(a, 4)   
   return
def printMessage_8():
   random1=int(random.randint(18,22))
   a=str("        ")+str(random1)+str(" %")    
   lcd.lcd_display_string("  Donnees cryptees", 1)
   lcd.lcd_display_string("      en cours", 2)
   lcd.lcd_display_string("   d'acquisition", 3)
   lcd.lcd_display_string(a, 4)
   return
def printMessage_9():
   random1=int(random.randint(30,37))
   a=str("        ")+str(random1)+str(" %")   
   lcd.lcd_display_string("  Donnees cryptees", 1)
   lcd.lcd_display_string("      en cours", 2)
   lcd.lcd_display_string("   d'acquisition", 3)
   lcd.lcd_display_string(a, 4)
   return
def printMessage_10():
   random1=int(random.randint(40,45))
   a=str("        ")+str(random1)+str(" %")   
   lcd.lcd_display_string("  Donnees cryptees", 1)
   lcd.lcd_display_string("      en cours", 2)
   lcd.lcd_display_string("   d'acquisition", 3)
   lcd.lcd_display_string(a, 4)
   return
def printMessage_11():
   random1=int(random.randint(70,85))
   a=str("        ")+str(random1)+str(" %")   
   lcd.lcd_display_string("  Donnees cryptees", 1)
   lcd.lcd_display_string("      en cours", 2)
   lcd.lcd_display_string("   d'acquisition", 3)
   lcd.lcd_display_string(a, 4)
   return
def printMessage_12():
   lcd.lcd_display_string("      Donnees", 1)
   lcd.lcd_display_string("   satellitaires", 2)
   lcd.lcd_display_string("      acquises", 3)
   lcd.lcd_display_string("    avec succes", 4)
   return 
def printMessage_13():
   random1=int(random.randint(1111,9999))
   a=str(" ")+str(random1)
   PID="  "+"Capture PID"+str(a)
   random2=int(random.randint(1,9))
   b=str(" ")+str(random2)
   random3=int(random.randint(10,99))
   c=str(random3)
   d=str(random.choice(string.ascii_letters))   
   Geosar="   GEOSAR v."+str(b)+"."+str(c)+str(d)
   lcd.lcd_display_string(PID, 1)
   lcd.lcd_display_string(Geosar, 2)   
   lcd.lcd_display_string(" Reception du flux", 3)
   lcd.lcd_display_string("  de donnees : OK", 4)  
   return

def printMessageTime():
   gpstime = gpsd.utc[0:4] + gpsd.utc[5:7] + gpsd.utc[8:10] + ' ' + gpsd.utc[11:19]
   os.system('sudo date -u --set="%s" > /dev/null 2>&1' % gpstime)
   textDate = strftime("%d.%m.%y", time.localtime())
   textTime = strftime("%H:%M", time.localtime())
   GPSLong = gpsd.fix.longitude
   GPSLat = gpsd.fix.latitude
   MGRS = m.toMGRS(GPSLat,GPSLong)
   textDateTime=("  "+textDate+" - "+textTime)   
   lcd.lcd_display_string("   ADRASEC 90/70", 1)  
   lcd.lcd_display_string(textDateTime, 2)   
   if (GPSLat > 0) and (GPSLong > 0): #Lat sup & long sup
      textGPSLat = str(GPSLat)[:8] 
      textGPSLong = str(GPSLong)[:7]
      textGPS=("  "+textGPSLat+"-"+textGPSLong)
      lcd.lcd_display_string(textGPS, 3)	  
   elif (GPSLat > 0) and (GPSLong < 0): #Lat sup & long inf
      textGPSLat = str(GPSLat)[:8] 
      textGPSLong = str(GPSLong)[:7]
      textGPS=("  "+textGPSLat+"-"+textGPSLong)
      lcd.lcd_display_string(textGPS, 3)	  
   elif (GPSLat < 0) and (GPSLong > 0): #Lat inf & long sup
      textGPSLat = str(GPSLat)[:8] 
      textGPSLong = str(GPSLong)[:7]
      textGPS=("  "+textGPSLat+"-"+textGPSLong)
      lcd.lcd_display_string(textGPS, 3)	  
   elif (GPSLat < 0) and (GPSLong < 0): #Lat inf & long inf
      textGPSLat = str(GPSLat)[:8] 
      textGPSLong = str(GPSLong)[:7]
      textGPS=("  "+textGPSLat+"-"+textGPSLong)
      lcd.lcd_display_string(textGPS, 3)	  
   a=(MGRS[:3])
   b=(MGRS[3:5])
   c=(MGRS[5:10])
   d=(MGRS[-5:])
   textMGRS=(" "+str(a)+"-"+str(b)+"-"+str(c)+"-"+str(d))
   lcd.lcd_display_string(textMGRS, 4)
   return
def printMessageAltitude():
   Alt = gpsd.fix.altitude
   GPSLong = gpsd.fix.longitude
   GPSLat = gpsd.fix.latitude
   MGRS = m.toMGRS(GPSLat,GPSLong)
   lcd.lcd_display_string("  Securite Civile", 1)
   if Alt < 0:
      AltFix=("Plouf   ")
      lcd.lcd_display_string("  "+"Altitude : "+(str(AltFix)), 2)
   elif Alt > 15500 :
      AltFix=("Espace !")
      lcd.lcd_display_string(" "+"Altitude : "+(str(AltFix)), 2)
   elif Alt > 9200 and Alt < 15500 :
      AltFix=("Avion ?!")
      lcd.lcd_display_string(" "+"Altitude : "+(str(AltFix)), 2)
   elif Alt > 999:
      AltFix=(str(Alt)[:4] + " m")
      lcd.lcd_display_string(" "+"Altitude : "+(str(AltFix)), 2)
   elif Alt > 99:
      AltFix=(str(Alt)[:3] + " m")
      lcd.lcd_display_string("  "+"Altitude : "+(str(AltFix)), 2)
   elif Alt > 9:
      AltFix=(str(Alt)[:2] + " m")
      lcd.lcd_display_string("  "+"Altitude : "+(str(AltFix)), 2)
   else:    
      AltFix=(str(Alt)[:1] + " m")
      lcd.lcd_display_string("   "+"Altitude : "+(str(AltFix)), 2)
   if (GPSLat > 0) and (GPSLong > 0): #Lat sup & long sup
      textGPSLat = str(GPSLat)[:8] 
      textGPSLong = str(GPSLong)[:7]
      textGPS=("  "+textGPSLat+"-"+textGPSLong)
      lcd.lcd_display_string(textGPS, 3)	  
   elif (GPSLat > 0) and (GPSLong < 0): #Lat sup & long inf
      textGPSLat = str(GPSLat)[:8] 
      textGPSLong = str(GPSLong)[:7]
      textGPS=("  "+textGPSLat+"-"+textGPSLong)
      lcd.lcd_display_string(textGPS, 3)	  
   elif (GPSLat < 0) and (GPSLong > 0): #Lat inf & long sup
      textGPSLat = str(GPSLat)[:8] 
      textGPSLong = str(GPSLong)[:7]
      textGPS=("  "+textGPSLat+"-"+textGPSLong)
      lcd.lcd_display_string(textGPS, 3)	  
   elif (GPSLat < 0) and (GPSLong < 0): #Lat inf & long inf
      textGPSLat = str(GPSLat)[:8] 
      textGPSLong = str(GPSLong)[:7]
      textGPS=("  "+textGPSLat+"-"+textGPSLong)
      lcd.lcd_display_string(textGPS, 3)
   a=(MGRS[:3])
   b=(MGRS[3:5])
   c=(MGRS[5:10])
   d=(MGRS[-5:])
   textMGRS=(" "+str(a)+"-"+str(b)+"-"+str(c)+"-"+str(d))    
   lcd.lcd_display_string(textMGRS, 4)
   return
def printMessageQTH():
   GPSLong = gpsd.fix.longitude
   GPSLat = gpsd.fix.latitude
   MGRS = m.toMGRS(GPSLat,GPSLong) 
   lat = gpsd.fix.latitude
   lon =  gpsd.fix.longitude
   # Constantes
   ASCII_0 = 48
   ASCII_A = 65
   ASCII_a = 97
   # Validation des entrees
   assert isinstance(lat, (int, float))
   assert isinstance(lon, (int, float))
   assert - 90.0 <= lat <= 90.0
   assert - 180.0 <= lon <= 180.0
   # Separation des champs, des carres et des sous-carres
   lon += 180
   lat += 90
   # Champs
   lon_field = int(floor(lon / 20))
   lat_field = int(floor(lat / 10))
   lon -= lon_field * 20
   lat -= lat_field * 10
   # Carres
   lon_sq = int(floor(lon / 2))
   lat_sq = int(floor(lat / 1))
   lon -= lon_sq * 2
   lat -= lat_sq * 1
   # Sous-carres
   lon_sub_sq = int(floor(lon / (5.0 / 60)))
   lat_sub_sq = int(floor(lat / (2.5 / 60)))
   lon -= lon_sub_sq * (5.0 / 60)
   lat -= lat_sub_sq * (2.5 / 60)
   # Carres etendus
   lon_ext_sq = int(round(lon / (0.5 / 60)))
   lat_ext_sq = int(round(lat / (0.25 / 60)))
   # Generation du QTH Locator
   qth_locator = ''
   qth_locator += chr(lon_field + ASCII_A)
   qth_locator += chr(lat_field + ASCII_A)
   qth_locator += chr(lon_sq + ASCII_0)
   qth_locator += chr(lat_sq + ASCII_0)
   if lon_sub_sq > 0 or lat_sub_sq > 0 or lon_ext_sq > 0 or lat_ext_sq > 0:
      qth_locator += chr(lon_sub_sq + ASCII_a)
   qth_locator += chr(lat_sub_sq + ASCII_a)
   if lon_ext_sq > 0 or lat_ext_sq > 0:
      qth_locator += chr(lon_ext_sq + ASCII_0)
   qth_locator += chr(lat_ext_sq + ASCII_0)
   textQTH=("   "+"QTH : "+(str(qth_locator)))
   if (GPSLat > 0) and (GPSLong > 0): #Lat sup & long sup
      textGPSLat = str(GPSLat)[:8] 
      textGPSLong = str(GPSLong)[:7]
      textGPS=("  "+textGPSLat+"-"+textGPSLong)
      lcd.lcd_display_string(textGPS, 3)	  
   elif (GPSLat > 0) and (GPSLong < 0): #Lat sup & long inf
      textGPSLat = str(GPSLat)[:8] 
      textGPSLong = str(GPSLong)[:7]
      textGPS=("  "+textGPSLat+"-"+textGPSLong)
      lcd.lcd_display_string(textGPS, 3)	  
   elif (GPSLat < 0) and (GPSLong > 0): #Lat inf & long sup
      textGPSLat = str(GPSLat)[:8] 
      textGPSLong = str(GPSLong)[:7]
      textGPS=("  "+textGPSLat+"-"+textGPSLong)
      lcd.lcd_display_string(textGPS, 3)	  
   elif (GPSLat < 0) and (GPSLong < 0): #Lat inf & long inf
      textGPSLat = str(GPSLat)[:8] 
      textGPSLong = str(GPSLong)[:7]
      textGPS=("  "+textGPSLat+"-"+textGPSLong)
      lcd.lcd_display_string(textGPS, 3)
   a=(MGRS[:3])
   b=(MGRS[3:5])
   c=(MGRS[5:10])
   d=(MGRS[-5:])
   textMGRS=(" "+str(a)+"-"+str(b)+"-"+str(c)+"-"+str(d))
   lcd.lcd_display_string("    - SWL9008 -", 1)
   lcd.lcd_display_string(textQTH, 2)
   lcd.lcd_display_string(textMGRS, 4)
   return
#def printMessageDHT():
#   humi, temp = dht.read_retry(dht.DHT22, 10)
#   Tempe = '%d' % temp
#   Humid = '%d' % humi
#   textTemp = str(Temp)
#   textHumi = str(Humi)   
#   if Tempe >= -40 and Tempe <= 80 :
#      lcd.lcd_display_string("    Temperature", 1)
#      lcd.lcd_display_string(""+(str(textTemp))+"'C", 2)
#      lcd.lcd_display_string("      Humidite", 3)	  
#      lcd.lcd_display_string(""+(str(textHumi))+" %", 4)	  
#   else:
#      lcd.lcd_display_string("    Temperature", 1)
#      lcd.lcd_display_string(" Sonde indisponible", 2)
#      lcd.lcd_display_string("      Humidite", 3)	  
#      lcd.lcd_display_string(""+(str(textHumi))+" %", 4)
#   if Humid >= 0 and Humid <= 100:
#      lcd.lcd_display_string("    Temperature", 1)
#      lcd.lcd_display_string(""+(str(textTemp))+"'C", 2)
#      lcd.lcd_display_string("      Humidite", 3)	  
#      lcd.lcd_display_string(""+(str(textHumi))+" %", 4)	  
#   else:
#      lcd.lcd_display_string("    Temperature", 1)
#      lcd.lcd_display_string(""+(str(textTemp))+"'C", 2)
#      lcd.lcd_display_string("      Humidite", 3)	  
#      lcd.lcd_display_string(" Sonde indisponible", 4)	  
#   return

def main():
   lcd.lcd_clear()
   printMessage_1()
   time.sleep(3)   
   lcd.lcd_clear()
   printMessage_2()
   time.sleep(2)   
   lcd.lcd_clear()
   printMessage_3()
   time.sleep(3)   
   lcd.lcd_clear()
   printMessage_4()
   time.sleep(3)   
   lcd.lcd_clear()
   printMessage_5()
   time.sleep(7)   
   lcd.lcd_clear()
   printMessage_6()
   time.sleep(3)   
   lcd.lcd_clear()
   printMessage_7()
   time.sleep(3)   
   lcd.lcd_clear()
   printMessage_8()
   time.sleep(3)   
   lcd.lcd_clear()
   printMessage_9()
   time.sleep(3)   
   lcd.lcd_clear()
   printMessage_10()
   time.sleep(5)   
   lcd.lcd_clear()
   printMessage_11()
   time.sleep(3)   
   lcd.lcd_clear()
   printMessage_12()
   time.sleep(5)
   printMessage_13()
   time.sleep(4)
# A decommenter si presence d'un module RTC & d'internet
#   response = os.system("ping -c 1 " + hostname)
#      if response == 0:
#         os.system(sudo hwclock --systohc) #OK
#      else:
#         os.system(sudo hwclock --hctosys) #KO	  
   while True:
      lcd.lcd_clear()
      printMessageTime()
      time.sleep(7)
      lcd.lcd_clear()
      printMessageAltitude()
      time.sleep(7)
      lcd.lcd_clear()
      printMessageQTH()
      time.sleep(7)
# A decommenter si presence d'un module DHT22
#      lcd.lcd_clear()
#      printMessageDHT()
#      time.sleep(5) 	  

if __name__ == '__main__':
   try:
      main()
   except (KeyboardInterrupt, SystemExit):
      gpsp.running = False
      gpsp.join()
