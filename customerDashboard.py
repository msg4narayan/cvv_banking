import tkinter as tk
from tkinter import *
from tkinter import ttk,messagebox
import db
import util

customerDashboardWindow = ""


def close():
	print("--- Entering customerDashboardWindow close() ---")
	global customerDashboardWindow
	customerDashboardWindow.destroy()


#------To clear the Fields--------
def clearFields():
	print("--- Entering clearFields() ---")
	
#----------------------------------



#------To validate--------
def loadDashboard(uname):
	print("--- Entering dashboard module for ---"+str(uname))
	
	global customerDashboardWindow
	customerDashboardWindow = tk.Tk()
	customerDashboardWindow.title("Welcome to Financial Crimes | Dashboard")
	customerDashboardWindow.state("zoomed")
	customerDashboardWindow.columnconfigure(1, weight=6)

	#Logo
	logo = tk.Label(customerDashboardWindow,text="Financial Crimes", font="Calibri 43")
	logo.grid(row=0,column=0,sticky="w", ipadx="2", columnspan=6)


	# Seperator object
	line_style = ttk.Style()
	line_style.configure("Line.TSeparator", background="#FF0000")
	separator = ttk.Separator(customerDashboardWindow, orient='horizontal', style="Line.TSeparator")
	separator.grid(row=1,column=0,columnspan=6, sticky='ew')


	

	#Error and Message Row
	messageFrame = tk.Frame(customerDashboardWindow)
	messageText = Label(messageFrame, text="Welcome   ", font="Calibri 16")
	messageSpacer = Label(messageFrame, text="  ", font="Calibri 16")
	messageFrame.grid(row=2,column=0,sticky="w")
	messageText.pack(side=TOP)
	messageSpacer.pack(side=TOP)

	

	



		


	# Seperator object
	line_style = ttk.Style()
	line_style.configure("Line.TSeparator", background="#FF0000")
	separator = ttk.Separator(customerDashboardWindow, orient='horizontal', style="Line.TSeparator")
	separator.grid(row=12,column=0,columnspan=6, sticky='ew', pady=10)











	customerDashboardWindow.mainloop()