from tkinter import *
import tkinter as tk
import speech_recognition as s
from bs4 import BeautifulSoup
import requests
page = tk.Tk()
page.geometry("750x750")
page.title("Wikipedia Voice Search by Rahul Vijayakumar")
tk.Label(page, text="Search with your voice",
         fg="Black", font="Gabriola 45 bold").pack()
T = Text(page, height=30, width=85)
T.pack(expand=True)

def search():
    T.delete('1.0','end')
    recognizer = s.Recognizer()
    with s.Microphone() as source:
        txt = tk.StringVar(page)
        try:
            #print('ready')
            speech_input = recognizer.record(source,6)
            text = recognizer.recognize_google(speech_input)
            #print(text)
        except:
            print('Error')
        txt.set(text)
        e0 = tk.Entry(page, textvariable=txt).place(
            x=30, y=150, width=400, height=30)
        try:
            url = 'https://en.wikipedia.org/wiki/' + text
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            title = soup.title.get_text()
            x = soup.find_all('p')
            data = str()
            for i in x:
                data = data + i.get_text() + '\n'
            T.insert('end',data)
        except:
            print('Error while searching')

tk.Button(page, text="Speak", command=search).place(
    x=200, y=680, width=250, height=40)


page.mainloop()
