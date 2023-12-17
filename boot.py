from tkinter import *
from tkinter import ttk
import os
import time
print("Booting...")
password = "H5gi5a6eb9()"
inf = "SYSTEM P (graphical), ver. 0.5"
rot = 0
def shutdown():
  print("Shutdown command has been sent from this console or remote terminal")
  exit()
def menu():
  consoleg = ttk.Button(text = 'Help', command = help)
  consoleg.pack()
def rot():
  rot = 1
def infh():
  print("Basic information about system 0.5:")
  print("System 0.5 is pythonm-based operating system for pupils an script-kiddies made for help them with hacking. System 1.0 will incluse most important programs like nmap, pentmenu, zphisher e.t.c I`ve made this system just for fun. Developing has been started in 2021 year. My name is John and I live in Russia. For contact information just type to me: johnwilsonEeEe@gmail.com. See you later in next releases! (It`s my birthday, I`ve got a brand new keyboard!!!)")
def sge():
  root = Tk()
  root.title("System P (graphical")
  shutdownbutton = ttk.Button(text="Shutdown", command = shutdown)
  menubutton = ttk.Button(text = 'Menu', command = menu)
  menubutton.pack()
  shutdownbutton.pack()
def help():
  labelt = ttk.Label()
  label = ttk.Label()
  label.pack()
  labelt.pack()
  label["text"] = 'ver - prints version of current software'
  labelt["text"] = 'exit - shutting down the system'
  cle = ttk.Button(text='clear', command = clear)
  cle.pack()
def clear():
  label.destroy()
  labelt.destroy()
print("Please enter the password for local account of adminisrtator (std)")
root = 0
com = 0
while com == 0:
  pas = input("? ")
  if pas == password:
    print("Done")
    print("Welcome, John!")
    com = 1
  else:
    print("Your password is incorrect")
print("To start System Graphical Envinronment (SGE) type sge")
print(inf, "<shell mode>")
while com == 1:
  if rot == 0:
    cmd = input("ADMINISTRATOR<s>~ ")
  else:
    cmd = input("ADMINISTRATOR<r>~ ")
  if cmd == 'ver':
    print(inf)
  if cmd == 'exit':
    shutdown()  
  if cmd == 'sge':
    print("Starting graphical environment")
    sge()
  if cmd == 'help':
    print("help - Displays basic information about commands and how to use it")
    print("ver - Displays basic info about this system")
    print("sge - starts graphical eninronment based on Tkinter")
    print()
    print("for more information type infh")
  if cmd == 'rtu':
    rot()
    print("Sucsessful")
  if cmd == 'infh':
    infh()
  if cmd == 'ddos':
    print("DDoS attack util (only for pentest!)")
    print()
    print("I'm sorry, but this feature does not works now. I'm working on it!")
