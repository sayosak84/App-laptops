# import openpyxl and tkinter modules
from openpyxl import *
from tkinter import *

# globally declare wb and sheet variable

# opening the existing excel file
wb = load_workbook('C:\\Users\\Nader\\Documents\\projets_lotfi\\App-laptops\\excel.xlsx')

# create the sheet object
sheet = wb.active


def excel():
	
	# resize the width of columns in
	# excel spreadsheet
	sheet.column_dimensions['A'].width = 30
	sheet.column_dimensions['B'].width = 10
	sheet.column_dimensions['C'].width = 10
	sheet.column_dimensions['D'].width = 20
	sheet.column_dimensions['E'].width = 20
	sheet.column_dimensions['F'].width = 40
	sheet.column_dimensions['G'].width = 50
	sheet.column_dimensions['H'].width = 50
	sheet.column_dimensions['I'].width = 50
	sheet.column_dimensions['J'].width = 50
	sheet.column_dimensions['K'].width = 50

	# write given data to an excel spreadsheet
	# at particular location
	sheet.cell(row=1, column=1).value = "Nom de l'appareil"
	sheet.cell(row=1, column=2).value = "Marque"
	sheet.cell(row=1, column=3).value = "Date de l'achat"
	sheet.cell(row=1, column=4).value = "Form Number"
	sheet.cell(row=1, column=5).value = "Contact Number"
	sheet.cell(row=1, column=6).value = "Email id"
	sheet.cell(row=1, column=7).value = "Amortissement mensuel"
	sheet.cell(row=1, column=8).value = "Dotation aux amortissements"
	sheet.cell(row=1, column=9).value = "Valeure compatable nette"
	sheet.cell(row=1, column=10).value = "Utilisateur"
	sheet.cell(row=1, column=11).value = "Date affectation"


# Function to set focus (cursor)
def focus1(event):
	# set focus on the marque_field box
	marque_field.focus_set()


# Function to set focus
def focus2(event):
	# set focus on the date_achat_field box
	date_achat_field.focus_set()


# Function to set focus
def focus3(event):
	# set focus on the date_exp_field box
	date_exp_field.focus_set()


# Function to set focus
def focus4(event):
	# set focus on the prix_achat_field box
	prix_achat_field.focus_set()


# Function to set focus
def focus5(event):
	# set focus on the date_compta_field box
	date_compta_field.focus_set()


# Function to set focus
def focus6(event):
	# set focus on the ammort_mensuel_field box
	ammort_mensuel_field.focus_set()

# Function to set focus
def focus7(event):
	# set focus on the utilisateur_field box
	utilisateur_field.focus_set()

# Function to set focus
def focus8(event):
	# set focus on the date_affect_field box
	date_affect_field.focus_set()


# Function for clearing the
# contents of text entry boxes
def clear():
	
	# clear the content of text entry box
	nom_appareil_field.delete(0, END)
	marque_field.delete(0, END)
	date_achat_field.delete(0, END)
	date_exp_field.delete(0, END)
	prix_achat_field.delete(0, END)
	date_compta_field.delete(0, END)
	ammort_mensuel_field.delete(0, END)
	utilisateur_field.delete(0, END)
	date_affect_field.delete(0, END)


# Function to take data from GUI
# window and write to an excel file
def insert():
	
	# if user not fill any entry
	# then print "empty input"
	if (nom_appareil_field.get() == "" and
		marque_field.get() == "" and
		date_achat_field.get() == "" and
		date_exp_field.get() == "" and
		prix_achat_field.get() == "" and
		date_compta_field.get() == "" and
		ammort_mensuel_field.get() == "" and
		utilisateur_field.get() == "" and
		date_affect_field.get() == ""):
			
		print("empty input")

	else:

		# assigning the max row and max column
		# value upto which data is written
		# in an excel sheet to the variable
		current_row = sheet.max_row
		current_column = sheet.max_column

		# get method returns current text
		# as string which we write into
		# excel spreadsheet at particular location
		sheet.cell(row=current_row + 1, column=1).value = nom_appareil_field.get()
		sheet.cell(row=current_row + 1, column=2).value = marque_field.get()
		sheet.cell(row=current_row + 1, column=3).value = date_achat_field.get()
		sheet.cell(row=current_row + 1, column=4).value = date_exp_field.get()
		sheet.cell(row=current_row + 1, column=5).value = prix_achat_field.get()
		sheet.cell(row=current_row + 1, column=6).value = date_compta_field.get()
		sheet.cell(row=current_row + 1, column=7).value = ammort_mensuel_field.get()
		sheet.cell(row=current_row + 1, column=10).value = utilisateur_field.get()
		sheet.cell(row=current_row + 1, column=11).value = date_affect_field.get()

		# save the file
		wb.save('C:\\Users\\Nader\\Documents\\projets_lotfi\\App-laptops\\excel.xlsx')

		# set focus on the nom_appareil_field box
		nom_appareil_field.focus_set()

		# call the clear() function
		clear()


# Driver code
if __name__ == "__main__":
	
	# create a GUI window
	root = Tk()

	# set the background colour of GUI window
	root.configure(background='light green')

	# set the title of GUI window
	root.title("registration form")

	# set the configuration of GUI window
	root.geometry("500x300")

	excel()

	# create a Form label
	heading = Label(root, text="Form", bg="light green")

	# create a nom_appareil label
	nom_appareil = Label(root, text="Nom de l'appareil", bg="light green")

	# create a marque label
	marque = Label(root, text="Marque", bg="light green")

	# create a Date de l'achat label
	date_achat = Label(root, text="Date de l'achat", bg="light green")

	# create a date_exp label
	date_exp = Label(root, text="Date d'expiration", bg="light green")

	# create a prix_achat label
	prix_achat = Label(root, text="Prix d'achat", bg="light green")

	# create a Email id label
	date_compta = Label(root, text="Date comptabilisation", bg="light green")

	# create a ammort_mensuel label
	ammort_mensuel = Label(root, text="Ammortissement mensuel", bg="light green")

	# create a utilisateur label
	utilisateur = Label(root, text="Utilisateur", bg="light green")

	# create a date affectation label
	date_affect = Label(root, text="Date affectation", bg="light green")

	# grid method is used for placing
	# the widgets at respective positions
	# in table like structure .
	heading.grid(row=0, column=1)
	nom_appareil.grid(row=1, column=0)
	marque.grid(row=2, column=0)
	date_achat.grid(row=3, column=0)
	date_exp.grid(row=4, column=0)
	prix_achat.grid(row=5, column=0)
	date_compta.grid(row=6, column=0)
	ammort_mensuel.grid(row=7, column=0)
	utilisateur.grid(row=8, column=0)
	date_affect.grid(row=9, column=0)

	# create a text entry box
	# for typing the information
	nom_appareil_field = Entry(root)
	marque_field = Entry(root)
	date_achat_field = Entry(root)
	date_exp_field = Entry(root)
	prix_achat_field = Entry(root)
	date_compta_field = Entry(root)
	ammort_mensuel_field = Entry(root)
	utilisateur_field = Entry(root)
	date_affect_field = Entry(root)

	# bind method of widget is used for
	# the binding the function with the events

	# whenever the enter key is pressed
	# then call the focus1 function
	nom_appareil_field.bind("<Return>", focus1)

	# whenever the enter key is pressed
	# then call the focus2 function
	marque_field.bind("<Return>", focus2)

	# whenever the enter key is pressed
	# then call the focus3 function
	date_achat_field.bind("<Return>", focus3)

	# whenever the enter key is pressed
	# then call the focus4 function
	date_exp_field.bind("<Return>", focus4)

	# whenever the enter key is pressed
	# then call the focus5 function
	prix_achat_field.bind("<Return>", focus5)

	# whenever the enter key is pressed
	# then call the focus6 function
	date_compta_field.bind("<Return>", focus6)

	utilisateur_field.bind("<Return>", focus7)

	date_affect_field.bind("<Return>", focus8)


	# grid method is used for placing
	# the widgets at respective positions
	# in table like structure .
	nom_appareil_field.grid(row=1, column=1, ipadx="100")
	marque_field.grid(row=2, column=1, ipadx="100")
	date_achat_field.grid(row=3, column=1, ipadx="100")
	date_exp_field.grid(row=4, column=1, ipadx="100")
	prix_achat_field.grid(row=5, column=1, ipadx="100")
	date_compta_field.grid(row=6, column=1, ipadx="100")
	ammort_mensuel_field.grid(row=7, column=1, ipadx="100")
	utilisateur_field.grid(row=8, column=1, ipadx="100")
	date_affect_field.grid(row=9, column=1, ipadx="100")

	# call excel function
	excel()

	# create a Submit Button and place into the root window
	submit = Button(root, text="Submit", fg="Black",
							bg="Red", command=insert)
	submit.grid(row=10, column=1)

	# start the GUI
	root.mainloop()
