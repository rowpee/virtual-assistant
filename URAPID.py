import pyttsx3
import speech_recognition as sr 
import datetime
import wikipedia
import webbrowser
import pyautogui
import tkinter as tk
import mysql.connector
import socket
import keyboard
import requests, json 
from tkinter import *
from tkinter import ttk
from playsound import playsound
from unittest import result
import os
import googletrans
from googletrans import Translator
import time
from email.mime import audio
from os import execl
import random
from threading import Timer



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[0].id)
voices = engine.getProperty('voices')

hal = ("hello","hii","hi","hey")
hal_response = ("hello sir","hii","how are you","hey there")


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


hostname = socket.gethostname()    
IPAddr = socket.gethostbyname(hostname)


send_url = "http://api.ipstack.com/check?access_key=ENTER_API"
geo_req = requests.get(send_url)
geo_json = json.loads(geo_req.text)
latitude = geo_json['latitude']
lan=str(latitude)
longitude = geo_json['longitude']
long=str(longitude)
city = geo_json['city']


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  


def takeCommand():
   
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        #speak("Listening")
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")



    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query
       
   
def taketemp():
 complete_url ="http://api.openweathermap.org/data/2.5/weather?"  + "appid=" + "ENTER_API" + "&q=" + city


 response = requests.get(complete_url) 

 x = response.json() 

 
 if x["cod"] != "404": 
     y = x["main"] 
     current_temperature = y["temp"] 
     current_pressure = y["pressure"] 
     current_humidiy = y["humidity"] 
     z = x["weather"] 
     upre = int(current_temperature)
     weather_description = z[0]["description"] 
     speak(" Temperature is " +
					str(upre-273) + "degree celsius")
                   
     print(" Temperature (in celsius unit) = " +
					str(upre-273))
 else: 
  print(" City Not Found ") 

def takeweather():
     complete_url ="http://api.openweathermap.org/data/2.5/weather?"  + "appid=" + "ENTER_API" + "&q=" + city


     response = requests.get(complete_url) 

     x = response.json() 

 
     if x["cod"] != "404": 
      y = x["main"] 
     current_temperature = y["temp"] 
     current_pressure = y["pressure"] 
     current_humidiy = y["humidity"] 
     z = x["weather"] 
     upre = int(current_temperature)
     weather_description = z[0]["description"] 

     speak("\n atmospheric pressure (in hPa unit) = " +
					str(current_pressure) +
		"\n humidity (in percentage) = " +
					str(current_humidiy) +
		"\n description = " +
					str(weather_description))  
                   
     print("\n atmospheric pressure (in hPa unit) = " +
					str(current_pressure) +
		"\n humidity (in percentage) = " +
					str(current_humidiy) +
		"\n description = " +
					str(weather_description))  




def takeAnswer():
       
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak Answer")
        #speak("Listening")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        tackle = r.recognize_google(audio, language='en-in')
        print(f"User said: {tackle}\n")



    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return tackle

def plays():
 pyautogui.moveTo(439,503)
 pyautogui.click()

def youthoob():
    pyautogui.moveTo(586,427)
    pyautogui.click()

def session():
    pyautogui.moveTo(1279,938)
    pyautogui.click()


wishMe()
speak("Hello Sir I am URAPID,How may I help you?")
while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
           speak("Searching Wikipedia")
           query = query.replace("wikipedia", "")
           results = wikipedia.summary(query, sentences=2)
           speak("According to Wikipedia")
           print(results)
           speak(results)

        elif 'open ' in query:
            j=query.replace("open" ,"")
            p=j.replace(" ","")
            webbrowser.open("www."+p+".com")

            
        elif 'temperature' in query:
            taketemp()

        elif 'awesome' in query:
            speak("Thank You Sir")

        elif 'great' in query:
            speak("It means a lot")

        elif 'wonderfull' in query:
            speak("Thanks for appreciation")

        elif 'hello' in query:
            speak(random.choice(hal_response))

        elif 'shutdown' in query:  
             os.system("shutdown /s /t 1") 

        elif 'weather' in query:
            takeweather()

        elif 'select all' in query:
           keyboard.press_and_release('control+a')

        elif 'copy' in query:
               keyboard.press_and_release('control+c')
               speak("Copied")
        
        elif 'notepad' in query:
           code = ('C:\WINDOWS\system32\\notepad.exe')
           os.startfile(code)

        elif 'paste' in query:
               keyboard.press_and_release('control+v')
               speak("Pasted")
        
        elif 'stop' in query:
            speak("Sorry Sir")
            exit()
        
        elif 'not talking to you' in query:
            speak("Sorry Sir for the confusion")

        elif 'ip address' in query:
            speak( "IP address is," +IPAddr)
        
        elif 'computer' in query:
            speak("Systems's name is," + hostname)

        elif 'how are you' in query:
            speak("fine sir, here to help you")

        elif 'translate' in query:
            translator = Translator()
            data = query.replace("translate" , "")
            translated = translator.translate(data, dest='en')
            speak(translated.text)
            print(translated.text)

        elif 'add list' in query:
            mydb = mysql.connector.connect(host='DATABASE-HOST',user='USER', password='#', database="#")
            cur=mydb.cursor()
            m = query.replace("add list", "")
            s = "INSERT INTO label(id,list) VALUES(%s,%s)"
            b1 = (1,m)
            cur.execute(s,b1)
            mydb.commit()
        
        elif 'speak list' in query:
            mydb = mysql.connector.connect(host='',user='', password='', database="")
            cur=mydb.cursor()
            s="SELECT * from label"
            cur.execute (s)
            result = cur.fetchall()
            for rec in result:
             values = ','.join(map(str, rec))
             li = values.replace("1", "")
             print(li)   
             speak(li)   
             

        elif 'delete' in query:
            mydb = mysql.connector.connect(host='',user='', password='', database="")
            cur=mydb.cursor()
            s ="delete from label where id=1"
            cur.execute(s)
            mydb.commit() 

        elif 'girl' in query:
            engine.setProperty('voice', voices[1].id)

        elif 'back' in query:
            engine.setProperty('voice', voices[0].id)

        elif 'rapid' in query:
            speak("Full form of URAPID is Unit for Registring and Prcocessing Information and data.I am an Virtual assistant on this Pc")
            

        elif 'exit' in query:
            speak("Exiting Now")
            exit()

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
        
        elif 'music' in query:
         webbrowser.open("https://www.youtube.com/watch?v=Kvgd6450Y28&list=RDMM&start_radio=1")

        elif 'google map' in query:
            plac=query.replace("search","")
            op=plac.replace("google map","")
            pp=op.replace(" ","")
            webbrowser.open("https://www.google.com/maps/place/"+pp)

        elif 'play' in query:
            r = query.replace("play ","")
            k = r.replace(" ","-")
            webbrowser.open("https://www.gaana.com/song/"+k)

        elif 'album' in query:
             rep = query.replace("album ","")
             kep = rep.replace(" ","-")
             webbrowser.open("https://www.gaana.com/album/"+kep)
             w = Timer(5.0 ,plays)
             w.start()
             
        elif 'youtube' in query:
            plo = query.replace("youtube", "")
            webbrowser.open("https://www.youtube.com/results?search_query="+plo+"&sp=EgIQAQ%253D%253D")
            a = Timer(5.0, youthoob)
            a.start()
            
         
        elif 'google' in query:
         sear = query.replace("google", "")
         webbrowser.open("https://www.google.com/search?sxsrf=ACYBGNRV2EMhWob__AMV0F_f_o9dcUeXNQ%3A1578132844246&source=hp&ei=bGUQXoGjDN7ez7sP8K6BmAY&q=" + sear + "&oq" + sear + "&gsl=psy-ab.3..35i39j0l9.2106.2839..3172...1.0..0.210.655.0j3j1......0....1..gws-wiz.......0i67j0i131.ep_CrQ-2NgM&ved=0ahUKEwiBidn82unmAhVe73MBHXBXAGMQ4dUDCAY&uact=5")
         
        elif 'reminder' in query:
          l = query.replace("set","")  
          t = l.replace("reminder for","")
          m = t.replace("minutes","")
          local_time = float(m)
          local_time = local_time * 60
          time.sleep(local_time)
          playsound('rip.mp3')
         
        
        elif 'close' in query:
            keyboard.press_and_release('alt+F4')

        elif 'play' in query:
            pyautogui.press('space')
        
        elif 'pause' in query:
            pyautogui.press('space') 

        elif 'full screen' in query:
            keyboard.press_and_release('f')

        elif 'app' in query:
            jol = query.replace("app ", "")
            keyboard.press_and_release('win')
            pyautogui.typewrite(jol)
            keyboard.press_and_release('enter')

        elif 'find path' in query:
            speak("say Starting Destination")
            print("Starting Destination")
            start = takeAnswer()
            if 'current location' in start:
                mui ="YOUR_LATITUDE, YOUR_LONGITUDE"
            else:
             mui = start.replace(" ","+") 
            speak("speak ending destination")
            print("Ending Destination")
            end = takeAnswer()
            nui = end.replace(" ","+")
            webbrowser.open("https://www.google.com/maps/dir/"+mui+"/"+nui)



        elif 'tab' in query:
            ko= query.replace('tab',"")
            ex = ("control+"+ko)
            print(ex)
            keyboard.press_and_release(ex)

        elif 'add' in query:
            print('speak number 1')
            speak('speak number 1')
            no1 = takeAnswer()
            print('speak number 2')
            speak('speak number 2')
            no2 = takeAnswer()
            nop=int(no1)
            noi=int(no2)
            print(nop+noi)

        
            
