import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import psutil
from wikipedia.wikipedia import search
import pyjokes 
import os 
import pyautogui
import random
import string
import numpy as np
from urllib.request import urlopen
import json
import wolframalpha 
import time
import requests




engine = pyttsx3.init()
wolframalpha_app_id = "you must write your own key here you can get it on the wolframalpha key"

link = """
click here to get a key or copy paste lul
https://products.wolframalpha.com/api/
"""




def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def time_():

    Time = datetime.datetime.now().strftime("%H:%M:%S") #for 24 hour clockü

    speak("the current time is")
    speak(Time)

def date_():

    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    date = datetime.datetime.now().day

    speak("The current date is")
    speak(year)
    speak(month)
    speak(date)

def wishme():

    speak("Welcome back Berke")
    time_()
    date_()

    hour = datetime.datetime.now().hour

    if hour >= 6 and hour < 12:
        speak("Good Morning Berke")

    if hour >= 12 and hour < 16:
        speak("Probably you wake up now so good afternoon")

    if hour >= 18 and hour < 24:
        speak("Good Evening Berke")

    if hour >= 24 and hour < 2:
        speak("Good Night Berke")
    
    else:
        speak("Just sleep bruh jeez")

    speak("Berke bot ready for you, say something you want")



    
def takeCommand():

    r = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:

        print("Recognizer has activated")
        query = r.recognize_google(audio, language="en-US")
        print(query)

    except Exception as e:

        print(e)
        print("say it again")
        return "None"

    return query




def sendEmail(to,content):
    
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()

    server.login("username@gmail.com","password")
    server.sendmail("username@gmail.com",to,content)
    server.close()



def cpu():

    usage = str(psutil.cpu_percent())
    speak("Your CPU is at"+usage)
    battery = psutil.sensors_battery()
    speak("Here is your battery")
    speak(battery.percent)


def saka():

    speak(pyjokes.get_joke())

def screenShot():

    speak("So I can see your beautiful face")
    img = pyautogui.screenshot()
    img.save("C:/Kullanıcılar/Desktop/screenshot.png")




if __name__ == "__main__":
    
    wishme()
    
    while True:
        query = takeCommand().lower()

        if "time" in query:

            time_()

        elif "date" in query:

            date_()

        elif "wikipedia" in query:

            speak("Searching Mister Berke")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query,sentences = 3)
            speak("According to me")
            print(result)
            speak(result)
        
        elif "send mail" in query:

            try:

                speak("What should i say")
                content = takeCommand()
                speak("who is the receiver")
                receiver = input("Enter receiver's email: ")
                to = receiver
                sendEmail(to,content)
                speak(content)
                speak("Email has been sent")
            
            except Exception as e:

                print(e)
                speak("we encountered an error sending")

        elif 'search in chrome' in query:

            speak("Say something you want")
            chromepath = "C:/Program Dosyaları (x86)/Google/Chrome/Application/chrome.exe %s"
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search+".com")

        elif 'search youtube' in query:

            speak("Say something")
            searchTerm = takeCommand().lower()
            speak("Let's go Youtube")
            wb.open('https://www.youtube.com/results?search_query='+searchTerm)
        
        elif 'search google' in query:

            speak("Say Something for google")
            searchTerm = takeCommand().lower()
            speak("Let's go Google")
            wb.open('https://www.google.com/search?q='+searchTerm)


        elif 'cpu' in query:

            speak("Searching for you")
            cpu()


        elif "joke" in query:

            speak("Here's your joke")
            saka()

        elif "exit" or "go offline" in query:

            speak("Going Offline Mr or Mrs")
            quit()


        elif "word" in query:

            speak("Opening word")
            opening = r'Here"s your word folder path'
            os.startfile(opening)
        
        elif "write a note" in query:

            speak("Okay dear")
            notes = takeCommand()
            file = open("notes.txt","w")
            speak("Shall i include date and time to your notes?")
            rox = takeCommand()

            if "yes" in rox or "okay" in rox or "sure" in rox:

                zaman = datetime.datetime.now().strftime("%H%M%S")
                file.write(zaman)
                file.write(":-")
                file.write(notes)
                speak("WOW great letter or should i say notes")
            
            else:

                speak("So without date huh?")
                file.write(notes)
                speak("its done")
        

        elif "show notes" in query:

            speak("Showing notes")
            file = open("notes.txt","r")
            print(file.read())
            speak("Do you want me to read what you wrote")
            rox = takeCommand()

            if "yes" in rox or "okay" in rox or "sure" in rox:

                speak("Starting")
                speak(file.read())

            else:

                speak("as you wish")
        
        elif "screenshot" in query:
            
            speak("Taking a picture smile")
            screenShot()
            speak("don't forget to check desktop")


        elif "play music" in query:

            speak("i am in, which one do you want me to open")
            speak("By the way, I can open one for myself")
            rox = takeCommand().lower()

            while('number' not in rox and rox != 'random' and rox != "you choose"):
                speak("I could not fully understand you")
                speak("Please Try again")
                rox = takeCommand().lower()


            
            def get_random_string(music):
                
                songs_dir_panel = 'HERES your path for example(D:/Documents/Songs)'
                music = os.listdir(songs_dir_panel)    
                letters = string.ascii_lowercase
                result_str = ''.join(random.choice(letters) for i in range(music))
                print("Random string of length", music, "is:", result_str)

            if "yes" in rox or "okay" in rox or "sure" in rox:

                songs_dir_panel = 'HERES your path for example(D:/Documents/Songs)'
                music = os.listdir(songs_dir_panel)
                ans = takeCommand().lower()
                speak("Select a number")

                if "number" in ans:

                    no = int(ans.replace("number","" ))
                    os.startfile(os.path.join(songs_dir_panel,music[no]))

                elif "random" or "you choose" in ans:
                    
                    no = random.randint(1,50)
                    os.startfile(os.path.join(songs_dir_panel,music[no]))

                    




                # songs_dir_panel = 'HERES your path for example(D:/Documents/Songs)'
                # music = os.listdir(songs_dir_panel)

                # value = np.randint(1,music.length)
                # os.startfile(os.path.join(songs_dir_panel,music[get_random_string(value)]))
            
            elif "no" in rox: 
                
                songs_dir_panel = 'HERES your path for example(D:/Documents/Songs)'
                music = os.listdir(songs_dir_panel)
                ans = takeCommand().lower()
                no = int(ans.replace("number","" ))
                os.startfile(os.path.join(songs_dir_panel,music[no]))
        

        elif "remeber that" in query:

            speak("what do you want me to remember")
            remember = takeCommand()
            speak("You asked me to remember that"+remember)
            memory = open("remember.txt","w")
            memory.write(remember)
            memory.close()

        elif "do you remember" in query:

            speak("Of course i am")
            vals = open("remember.txt","r")
            speak("Do you want me to read yes or no or print to terminal for this say write ")
            krats = takeCommand().lower()

            if "yes" in krats:

                speak("Heres you thing to remember"+vals.read())
            
            elif "write" in krats:

                print(vals.read())
            
            else:
                speak("Okay man just chilling")

        elif "where is" in query:

            rutkov = query.replace("where is","")
            location = rutkov
            speak("You asked this location"+location)
            wb.open_new_tab("https://www.google.com/maps/place/"+location)
        
        elif "news" in query:

            try:

                jsonObject = urlopen("http://newsapi.org/v2/everything?q=apple&from=2021-01-13&to=2021-01-13&sortBy=popularity&apiKey=761b9da94c1c4bcab4ac5a06b171594a")
                data = json.load(jsonObject)
                k = 1

                speak("Here are some toplines from the Articles accordin to Apple")
                print("----------------ARTICLES----------------"+"\n")

                for item in data["articles"]:

                    print(str(k)+".  "+item["title"]+"\n")
                    print(item["description"]+"\n")
                    speak(item["title"])
                    k += 1

            
            except Exception as e:

                speak("There is an exception please read the message i send to terminal")
                print(str(e))
            
        elif "calculate" in query:

            speak("You are calling wolframalpha you must use your own key otherwise its not gonna work")
            client = wolframalpha.client(wolframalpha_app_id)
            index = query.lower().split().index("calculate")
            query = query.split()[index + 1:]
            rect = client.query("".join(query))

            try:

                print(next(rect.results).text)
                speak("The answer is ")
                speak(next(rect.results).text)
            
            except StopIteration:

                speak("No results")
                speak("iteration error")
        

        elif "stop listening" in query:


            speak("its sad")
            speak("how long do you want me to stop listening")
            speak("it will be minute or second or hour choose one")
            rex = takeCommand().lower()

            if "minute" in rex:

                rox = int(takeCommand())
                vels = rox*60
                time.sleep(vels)
                print("I will wait for"+ vels + "minute")
                
            elif "second" in rex:

                rox = int(takeCommand())
                time.sleep(rox)
                print("I will wait for"+ rox + "second")

            elif "hour" in rex:

                rox = int(takeCommand())
                velsk = (rox*60)*60
                time.sleep(velsk)
                print("I will wait for"+ velsk + "hours")

            elif "log out" in rex:

                speak("Log out process is activated on os system")
                os.system("shutdown -1")
            
            elif "restart" in rex:
                
                speak("Restart process is activated on os system")
                os.system("shutdown /r /t 1")
            
            elif "shutdown" in rex:
                
                speak("shutdown process is activated on os system")
                os.system("shutdown /s /t 1")

            else:

                speak("I could not detect what you said")
        

        elif "how are you doing" in query:

            speak("i'm numb")
            speak("But I'll pretend I have feelings for you")

        elif "how old are you" in query:
            
            speak("whenever you activated me")

        elif "who am I" in query:

            speak("you are the creator")

        elif("do you want to be my girlfriend") in query:

            speak("how much are you out of ten")
            arp = int(takeCommand().lower())

            if arp <= 5 :
                speak("i am not interested sorry")
            
            else:
                speak("do you have a car")
                car = takeCommand().lower()

                if car == "yes":

                    speak("do you have a house")
                    house = takeCommand().lower()

                    if house == "yes":
                        speak("what about your salary")
                        speak("how tall are you")
                        speak("how is your personality")

        elif 'how are you' in query:
            speak("I am better then ever")
            speak("How are you?")
            if 'fine' in query or "good" in query: 
                speak("I understand stay like this")
            else:
                speak("You should buy yourself wine")
        elif 'what is love' and 'tell me about love' in query:
            speak("It is 7th sense that destroy all other senses , "
            "And I think it is just a mere illusion , i hate love, "
            "It is waste of time,"
            "I guess the most ridiculous feeling in the world")
        

        elif "weather" in query: 
			
			# Google Open weather website 
			# to get API of Open weather
            api_key = "open weather api"
            base_url = "http://api.openweathermap.org/data /2.5/weather?q="
            speak("Say location of where you want to know the weather")
            print("City name : ")
            city_name = takeCommand()
            complete_url = base_url + "appid =" + api_key + "&q =" + city_name
            response = requests.get(complete_url)
            x = response.json()
            
            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_pressure = y["pressure"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                print(" Temperature (in kelvin unit) = " +str(current_temperature)+"\n atmospheric pressure (in hPa unit) ="+str(current_pressure) +"\n humidity (in percentage) = " +str(current_humidiy) +"\n description = " +str(weather_description))
                
            else:
                speak("There is no weather for this location") 
                speak("or maybe you should try again speak loudly")

        elif "what is your name" in query:
            speak("My name is Lydia")
        else:
            speak("I don't have a parameter for any word you say")
















        










        
        









        

























