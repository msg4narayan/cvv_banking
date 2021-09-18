import tkinter as tk
from tkinter import *
from tkinter import ttk,messagebox
import db
import util

bankAdminWindow = ""


def close():
	print("--- Entering bankAdminWindow close() ---")
	global bankAdminWindow
	bankAdminWindow.destroy()


#------To clear the Fields--------
def clearFields():
	print("--- Entering clearFields() ---")
	
#----------------------------------



#------To validate--------
def loadDashboard(uname):
	print("--- Entering dashboard module for ---"+str(uname))


	#get a DBConnection
	con = db.getDBConnection()
	cur = con.cursor()

	#fetch the customer id generated
	cur.execute("select concat(fname,' ',lname) as customer_name from customer where username=%s",(uname,))
	customer_name = cur.fetchone()[0]

	#Close the DB connection
	db.closeDBConnection(con)
	
	global bankAdminWindow
	bankAdminWindow = tk.Tk()
	bankAdminWindow.title("Welcome to Financial Crimes | Bank Admin")
	bankAdminWindow.state("zoomed")
	bankAdminWindow.columnconfigure(1, weight=6)

	#Logo
	logo = tk.Label(bankAdminWindow,text="Financial Crimes", font="Calibri 43")
	logo.grid(row=0,column=0,sticky="w", ipadx="2", columnspan=6)


	# Seperator object
	line_style = ttk.Style()
	line_style.configure("Line.TSeparator", background="#FF0000")
	separator = ttk.Separator(bankAdminWindow, orient='horizontal', style="Line.TSeparator")
	separator.grid(row=1,column=0,columnspan=6, sticky='ew')


	

	#Error and Message Row
	messageFrame = tk.Frame(bankAdminWindow)
	messageText = Label(messageFrame, text="Hi "+ customer_name, font="Calibri 16")
	messageSpacer = Label(messageFrame, text="  ", font="Calibri 16")
	messageFrame.grid(row=2,column=4,sticky="w")
	messageText.pack(side=TOP)
	messageSpacer.pack(side=TOP)



	#Admin Menu
	menuFrame = tk.Frame(bankAdminWindow,width=350, height=100)
	menuSpacer_1 = Label(menuFrame, text="  ", font="Calibri 16")
	menuSpacer_2 = Label(menuFrame, text="  ", font="Calibri 16")
	depositsButton = Button(menuFrame,text=" Deposits ", font="Calibri 12")
	reportsButton = Button(menuFrame,text=" Reports ", font="Calibri 12")
	fundTransferButton = Button(menuFrame,text=" Fund Transfer ", font="Calibri 12")


	menuFrame.grid(row=3,column=0,sticky="w")
	depositsButton.pack(side=LEFT)
	menuSpacer_1.pack(side=LEFT)
	reportsButton.pack(side=LEFT)
	menuSpacer_2.pack(side=LEFT)
	fundTransferButton.pack(side=LEFT)






	#BlankRow
	blankRow = Label(bankAdminWindow,text=" ", font="Calibri 12")
	blankRow.grid(row=7,column=0,sticky="e",columnspan=6)


	

	



		


	# Seperator object
	line_style = ttk.Style()
	line_style.configure("Line.TSeparator", background="#FF0000")
	separator = ttk.Separator(bankAdminWindow, orient='horizontal', style="Line.TSeparator")
	separator.grid(row=12,column=0,columnspan=6, sticky='ew', pady=10)











	bankAdminWindow.mainloop()