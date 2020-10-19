import tkinter as tk
from tkinter import ttk
win = tk.Tk()

win.title("Python GUI")
e = tk.StringVar()
e_entry = tk.Entry(win, width=68, textvariable=e)
e_entry.pack()

def conversion(e):
	
	try:
		lenth=len(e)
		al_number=int(e)
		if lenth in units:
			tmp,tmp_number=lenth,al_number
	except:
		assert "Invalid input format"
win.mainloop()
