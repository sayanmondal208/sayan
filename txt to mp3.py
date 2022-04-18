from gtts import gTTS
import os
from win32com.client import Dispatch
import requests
import json
import time

print("1.COPY-PASTE\n2.UPLOAD\n3.NEWS")
choice=int(input("Choose any one option"))

if choice==1:
    mytext=input("Text here or paste any text :")
    print("Which voice you like to heared")
    print("1.MALE")
    print("2.FEMALE")
    voice=int(input("choose voice:"))
    if voice==1:
        speak=Dispatch("SAPI.spvoice")
        speak.speak(mytext)
    elif voice==2:
        language='en'
        output=gTTS(text=mytext,lang=language,slow=False)
        output.save("output.mp3")
        os.system("start output.mp3")
        
        
if choice==2:
    my_file=input("Enter your file name:")
    print("Which voice you like to heared")
    print("1.MALE")
    print("2.FEMALE")
    voice=input("choose voice:")

#female voice-----------
    if voice=="2":
        f=open(f"{my_file}.txt","r")
        mytext=f.read()
        language='en'
        output=gTTS(text=mytext,lang=language,slow=False)
        output.save("output.mp3")
        os.system("start output.mp3")

#male voice-----------
    if voice=="1":
        with open("short.txt")as f:
            file=f.read()
        def reader(str):
            sp=Dispatch("SAPI.spvoice")
            sp.speak(str)
        if __name__=="__main__":
            reader(file)
            
            
#News..............

if choice==3:
        print("1.All articles about Tesla from the last month\n2.Top business headlines in the US right now\n3.Top headlines from TechCrunch right now")
        ch=int(input("Choose any category from here:"))
        if ch==1:
            def speak(string):
                speak=Dispatch("SAPI.spvoice")
                speak.speak(string)
            if __name__=="__main__":
                speak("Please Wait news is loading.......its much time")
                time.sleep(5)
                #print("check here to get api--","https://newsapi.org/")
               # print("Todays news is")
                url="https://newsapi.org/v2/everything?q=tesla&from=2021-06-08&sortBy=publishedAt&apiKey=13fcaaeb981045ccb7eb74bedc7fd5c7"
                news=requests.get(url).text
                news_json=json.loads(news)
                art=news_json["articles"]
                for articles in art:
                    speak(articles["title"])
                    speak("Moving to next news please listen carefully!!")
                    time.sleep(2)
                print("thanks for listeng")
        elif ch==2:
            def speak(string):
                speak=Dispatch("SAPI.spvoice")
                speak.speak(string)
            if __name__=="__main__":
                speak("Please Wait news is loading.......its much time")
                time.sleep(5)
                #print("check here to get api--","https://newsapi.org/")
               # print("Todays news is")
                url="https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=13fcaaeb981045ccb7eb74bedc7fd5c7"
                news=requests.get(url).text
                news_json=json.loads(news)
                art=news_json["articles"]
                for articles in art:
                    speak(articles["title"])
                    speak("Moving to next news please listen carefully!!")
                    time.sleep(2)
                print("thanks for listeng")
        elif ch==3:
              def speak(string):
                speak=Dispatch("SAPI.spvoice")
                speak.speak(string)
              if __name__=="__main__":
                speak("Please Wait news is loading.......its much time")
                time.sleep(5)
                #print("check here to get api--","https://newsapi.org/")
               # print("Todays news is")
                url=f"https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=13fcaaeb981045ccb7eb74bedc7fd5c7"
                news=requests.get(url).text
                news_json=json.loads(news)
                art=news_json["articles"]
                for articles in art:
                    speak(articles["title"])
                    speak("Moving to next news please listen carefully!!")
                    time.sleep(2)
                print("thanks for listeng")

        
    

