import os , plyer , platform , subprocess
from tkinter import *

main_menu = Tk()

Label(main_menu,text="Notes Title: ").grid(row=0,column=0)

main_menu.mainloop()


#reminders
if platform.system() == "Windows":
	Title = ""
	Message = ""
elif platform.system() == "Linux":
	subprocess.call(['notify-send',title,message])
