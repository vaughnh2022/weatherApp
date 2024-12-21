#if testing this code please login to weatherapi.com and get your own auth key

authkey="your_authetification_key"


#code is below


#imports

import requests
import json
import tkinter as tk
import time

#gui and url initialization

root = tk.Tk()
root.geometry('500x350')
url = "http://api.weatherapi.com/v1/current.json"
foreurl = "http://api.weatherapi.com/v1/forecast.json"


#json pull requests


def requestPull(name):
    paramz = {"key": authkey, "q": name}
    try:
        responce = requests.get(url, params=paramz)
        data = responce.json()
        if "error" in data:
            return None
        return data
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None
    
def forePull(name):
    paramz = {"key":authkey, "q": name}
    try:
        responce = requests.get(foreurl,params=paramz)
        data = responce.json()
        if "error" in data:
            return None
        return data
    except requests.exceptions.RequestException as e:
        return None


#home screen


def main():
    for widget in root.winfo_children():
        widget.destroy()
    frame = tk.Frame(root, width=500,height=350)
    frame.pack()
    
    lab=tk.Label(frame,text="Weather Main Page")
    lab.pack(pady=10)

    butt = tk.Button(frame,text="current weather",command=cityPrompt)
    butt.pack(pady=10)

    forebutt = tk.Button(frame,text="todays forecast",command=forePrompt)
    forebutt.pack(pady=10)


#current weather

def cityPrompt():
    for widget in root.winfo_children():
        widget.destroy()
    frame = tk.Frame(root, width=500,height=350)
    frame.pack()

    text = tk.Label(frame,text="input city for current weather")
    text.pack(pady=10)

    text_area = tk.Entry(frame, width=40)
    text_area.pack()

    result_label = tk.Label(frame,text="")
    result_label.pack(pady=10)

    enterButton = tk.Button(frame,text="enter",command=lambda: cityCheck(text_area.get(),result_label))
    enterButton.pack(pady=10)

    backButton = tk.Button(frame,text="back",command=main)
    backButton.pack(pady=10)



def cityCheck(name,result_label):
    citydata = requestPull(name)
    if citydata:
        cityDisplay(citydata)
    else:
        result_label.config(text="could not find city")


def cityDisplay(citydata):
    for widget in root.winfo_children():
        widget.destroy()
    frame = tk.Frame(root, width=500,height=350)
    frame.pack()

    text1 = tk.Label(frame,text=f"city: {citydata['location']['name']}")
    text1.pack(pady=2)
    text2 = tk.Label(frame,text=f"region: {citydata['location']['region']}")
    text2.pack(pady=2)
    text3 = tk.Label(frame,text=f"country: {citydata['location']['country']}")
    text3.pack(pady=2)
    text4 = tk.Label(frame,text=f"temp in F: {citydata['current']['temp_f']}")
    text4.pack(pady=2)
    text5 = tk.Label(frame,text=f"condition: {citydata['current']['condition']['text']}")
    text5.pack(pady=2)
    text6 = tk.Label(frame,text=f"local time: {citydata['location']['localtime']}")
    text6.pack(pady=2)
    text7 = tk.Label(frame,text=f"wind mph: {citydata['current']['wind_mph']}")
    text7.pack(pady=2)
    text8 = tk.Label(frame,text=f"humidity: {citydata['current']['humidity']}")
    text8.pack(pady=2)
    text9 = tk.Label(frame,text=f"feels like: {citydata['current']['feelslike_f']}")
    text9.pack(pady=2)
    text10 = tk.Label(frame,text=f"visibile miles: {citydata['current']['vis_miles']}")
    text10.pack(pady=2)
    backButton = tk.Button(frame,text="back",command=main)
    backButton.pack(pady=2)


#forecast


def forePrompt():
    for widget in root.winfo_children():
        widget.destroy()
    frame = tk.Frame(root, width=500,height=350)
    frame.pack()

    text = tk.Label(frame,text="input city for today's forecast")
    text.pack(pady=10)

    text_area = tk.Entry(frame, width=40)
    text_area.pack()

    result_label = tk.Label(frame,text="")
    result_label.pack(pady=10)

    enterButton = tk.Button(frame,text="enter",command=lambda: foreCheck(text_area.get(),result_label))
    enterButton.pack(pady=10)

    backButton = tk.Button(frame,text="back",command=main)
    backButton.pack(pady=10)

def foreCheck(name,result_label):
    citydata = forePull(name)
    if citydata:
        foreDisplay(citydata,0)
    else:
        result_label.config(text="could not find city")
def foreDisplay(citydata,hour):
    for widget in root.winfo_children():
        widget.destroy()
    num_hours = len(citydata["forecast"]["forecastday"][0]['hour'])
    frame = tk.Frame(root, width=500,height=350)
    frame.pack()
    text1 = tk.Label(frame,text=f"city: {citydata['location']['name']}")
    text1.pack(pady=2)
    text2 = tk.Label(frame,text=f"region: {citydata['location']['region']}")
    text2.pack(pady=2)
    text3 = tk.Label(frame,text=f"country: {citydata['location']['country']}")
    text3.pack(pady=2)

    forecast_day = citydata['forecast']['forecastday'][0]['hour'][hour]

    text4 = tk.Label(frame,text=f"date: {forecast_day['time']}")
    text4.pack(pady=2)
    text4 = tk.Label(frame,text=f"condition: {forecast_day['condition']['text']}")
    text4.pack(pady=2)
    text4 = tk.Label(frame,text=f"temp in f: {forecast_day['temp_f']}")
    text4.pack(pady=2)
    text4 = tk.Label(frame,text=f"wind mph: {forecast_day['wind_mph']}")
    text4.pack(pady=2)
    if hour==0:
        nextButton = tk.Button(frame,text="next",command=lambda: foreDisplay(citydata,hour+1))
        nextButton.pack(pady=10)
    elif hour==num_hours-1:
        prevButton = tk.Button(frame,text="prev",command=lambda: foreDisplay(citydata,hour-1))
        prevButton.pack(pady=10)
    else:
        nextButton = tk.Button(frame,text="next",command=lambda: foreDisplay(citydata,hour+1))
        nextButton.pack(pady=10)
        prevButton = tk.Button(frame,text="prev",command=lambda: foreDisplay(citydata,hour-1))
        prevButton.pack(pady=10)
    backButton = tk.Button(frame,text="back",command=main)
    backButton.pack(pady=10)

    




#init
main()
root.mainloop()





