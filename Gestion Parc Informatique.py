from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import tkinter.font as font
from PIL import Image, ImageTk
import sqlite3
import os
from datetime import datetime

IMAGE_PATH_FIRST = "assets/first-page.jpg"
IMAGE_PATH_OTHERS = "assets/other-pages.jpg"
BUTTON_FONT = None
WIDTH = 1200
HEIGTH = 800
LARGEFONT =("Verdana", 35)
MIDFONT =("Verdana", 25)
SMALLFONT =("Verdana", 18)


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

conn = sqlite3.connect(resource_path('laptops.db'))



class BkgrFrame(tk.Frame):
    def __init__(self, parent, file_path, width, height):
        super(BkgrFrame, self).__init__(parent, borderwidth=0, highlightthickness=0)

        self.canvas = tk.Canvas(self, width=width, height=height)
        self.canvas.pack()

        pil_img = Image.open(file_path)
        self.img = ImageTk.PhotoImage(pil_img.resize((width, height), Image.ANTIALIAS))
        self.bg = self.canvas.create_image(0, 0, anchor=tk.NW, image=self.img)

    def add(self, widget, x, y):
        canvas_window = self.canvas.create_window(x, y, anchor=tk.NW, window=widget)
        return widget


class tkinterApp(tk.Tk):
     
    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
         
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)

        self.title("Gestion des laptops")
        self.geometry("1200x800")
        # creating a container

        # button to show frame 2 with text
        # layout2
        BUTTON_FONT = font.Font(family='Helvitica', size=20)
        container = tk.Frame(self) 
        container.pack(side = "top", fill = "both", expand = True)
        self.resizable(width=0, height=0)

        container.grid_rowconfigure(0, weight = 3)
        container.grid_columnconfigure(0, weight = 3)

  
        # initializing frames to an empty array
        self.frames = {} 
  
        # iterating through a tuple consisting
        # of the different page layouts
        for F in (Acceuil, Ajouter, Rechercher_laptop_nom_app, Rechercher_laptop_user, Rechercher_laptop_vcn):
  
            frame = F(container, self)
  
            # initializing frame of that object from
            # startpage, Ajouter, Rechercher_laptop_nom_app respectively with
            # for loop
            self.frames[F] = frame
  
            frame.grid(row = 0, column = 0, sticky ="nsew")
  
        self.show_frame(Acceuil)
  
    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


# second window frame Ajouter
class Ajouter(tk.Frame):
     
    def __init__(self, parent, controller):

        def check_number(entry):
            try:
                float(entry.get())
                return True
            except ValueError:
                return False

        def validate(entry):
            try:
                datetime.strptime(entry.get(), "%d-%m-%Y")
                return True
            except ValueError:
                return False

        def clear():
            
            # clear the content of text entry box
            nom_appareil_field.delete(0, END)
            marque_field.delete(0, END)
            date_achat_field.delete(0, END)
            date_exp_field.delete(0, END)
            prix_achat_field.delete(0, END)
            date_compta_field.delete(0, END)
            # ammort_mensuel_field.delete(0, END)
            utilisateur_field.delete(0, END)
            date_affect_field.delete(0, END)
            date_fin_field.delete(0, END)
            Message.config(text = "")

        def validate_fields():
            if (check_number(prix_achat_field) and
                validate(date_achat_field) and
                validate(date_exp_field) and
                validate(date_compta_field) and
                validate(date_affect_field) and
                validate(date_fin_field)) :

                return True
            else : 
                return False

        # Function to take data from GUI
        # window and write to an excel file
        def insert():
            elements = []
            
            # if user not fill any entry
            # then print "empty input"
            if (nom_appareil_field.get() == "" and
                marque_field.get() == "" and
                date_achat_field.get() == "" and
                date_exp_field.get() == "" and
                prix_achat_field.get() == "" and
                date_compta_field.get() == "" and
                utilisateur_field.get() == "" and
                date_affect_field.get() == "" and
                date_fin_field.get() == ""):

                messagebox.showinfo(title="Alerte", message= "Valeurs vides")

            else:
                if (validate_fields()) :
                    elements.append(nom_appareil_field.get())
                    elements.append(marque_field.get())
                    elements.append(date_achat_field.get())
                    elements.append(date_exp_field.get())
                    elements.append(prix_achat_field.get())
                    elements.append(date_compta_field.get())
                    elements.append((float(prix_achat_field.get())*0.30)/12)
                    elements.append(utilisateur_field.get())
                    elements.append(date_affect_field.get())
                    elements.append(date_fin_field.get())
                    elements.append(0)
                    elements.append(0)


                    rqst = """INSERT INTO laptops
                            (Nom_appareil, 
                            Marque, 
                            Date_achat, 
                            Date_exp, 
                            Prix_achat, 
                            Date_compta, 
                            Amortissement_mensuel, 
                            Utilisateur, 
                            Date_affectation, 
                            Date_fin, 
                            Dot_ammortissement_mensuel,
                            VCN ) 
                            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"""

                    cursor = conn.cursor()
                    cursor.execute(rqst, elements)
                    conn.commit()

                    # set focus on the nom_appareil_field box
                    nom_appareil_field.focus_set()

                    # call the clear() function
                    msg = "laptop " + nom_appareil_field.get() + " ajouté"
                    messagebox.showinfo(title="Ajout d'un laptop", message= msg)
                    clear()
                else :
                    Message.config(text = "Valeur incorrect")
                    if not check_number(prix_achat_field) : prix_achat_field.config(fg='red')
                    if not validate(date_achat_field) : date_achat_field.config(fg='red')
                    if not validate(date_exp_field) : date_exp_field.config(fg='red')
                    if not validate(date_compta_field) : date_compta_field.config(fg='red')
                    if not validate(date_affect_field) : date_affect_field.config(fg='red')
                    if not validate(date_fin_field) : date_fin_field.config(fg='red')


        # Function to set focus (cursor)
        def focus1(event):
            marque_field.focus_set()


        # Function to set focus
        def focus2(event):
            date_achat_field.focus_set()


        # Function to set focus
        def focus3(event):

            if validate(date_achat_field):
                date_exp_field.focus_set()
                date_achat_field.config(fg='black')
                Message.config(text = "")
            else: 
                Message.config(text = "Format date achat incorrecte dd-mm-yyyy")
                date_achat_field.focus_set()

            

        # Function to set focus
        def focus4(event):
            if validate(date_exp_field):
                prix_achat_field.focus_set()
                date_exp_field.config(fg='black')
                Message.config(text = "")
            else: 
                Message.config(text = "Format date d'expiration incorrecte dd-mm-yyyy")
                date_exp_field.focus_set()


        # Function to set focus
        def focus5(event):
            if check_number(prix_achat_field):
                date_compta_field.focus_set()
                prix_achat_field.config(fg='black')
                Message.config(text = "")
            else: 
                Message.config(text = "Prix d'achat invalide")
                prix_achat_field.focus_set()


        # Function to set focus
        def focus6(event):
            if validate(date_compta_field):
                utilisateur_field.focus_set()
                date_compta_field.config(fg='black')
                Message.config(text = "")
            else: 
                Message.config(text = "Format date d'comptabilisation incorrecte dd-mm-yyyy")
                date_compta_field.focus_set()


        # Function to set focus
        def focus7(event):
            date_affect_field.focus_set()

        # Function to set focus
        def focus8(event):
            if validate(date_affect_field):
                date_fin_field.focus_set()
                date_affect_field.config(fg='black')
                Message.config(text = "")
            else: 
                Message.config(text = "Format date d'affectation incorrecte dd-mm-yyyy")
                date_affect_field.focus_set()

        # Function to set focus
        def focus9(event):
            if validate(date_fin_field):
                date_fin_field.config(fg='black')
                Message.config(text = "")
            else: 
                Message.config(text = "Format date de fin incorrecte dd-mm-yyyy")
                date_fin_field.focus_set()

        def entries_black():
            prix_achat_field.config(fg='black')
            date_achat_field.config(fg='black')
            date_exp_field.config(fg='black')
            date_compta_field.config(fg='black')
            date_affect_field.config(fg='black')
            date_fin_field.config(fg='black')


        tk.Frame.__init__(self, parent)

        bkrgframe = BkgrFrame(self, resource_path(IMAGE_PATH_OTHERS), WIDTH, HEIGTH)
        bkrgframe.pack()

        Titre = bkrgframe.add(Label(self, text ="Gestion des laptops", bg="#DEC6FA", font = LARGEFONT)
                            , 300, 100)

        Message = bkrgframe.add(Label(self, text="", bg="#DEC6FA", fg='red')
                            , 400, 220)

        nom_appareil = bkrgframe.add(Label(self, text="Nom de l'appareil", bg="#DEC6FA")
                            , 200, 240)

        marque = bkrgframe.add(Label(self, text="Marque", bg="#DEC6FA")
                            , 200, 260)

        date_achat = bkrgframe.add(Label(self, text="Date de l'achat", bg="#DEC6FA")
                            , 200, 280)

        date_exp = bkrgframe.add(Label(self, text="Date d'expiration", bg="#DEC6FA")
                            , 200, 300)

        prix_achat = bkrgframe.add(Label(self, text="Prix d'achat", bg="#DEC6FA")
                            , 200, 320)

        date_compta = bkrgframe.add(Label(self, text="Date comptabilisation", bg="#DEC6FA")
                            , 200, 340)

        #ammort_mensuel = bkrgframe.add(Label(self, text="Ammortissement mensuel", bg="#DEC6FA"), 200, 360)

        utilisateur = bkrgframe.add(Label(self, text="Utilisateur", bg="#DEC6FA")
                            , 200, 360)

        date_affect = bkrgframe.add(Label(self, text="Date affectation", bg="#DEC6FA")
                            , 200, 380)

        date_fin = bkrgframe.add(Label(self, text="Date de fin", bg="#DEC6FA")
                            , 200, 400)



        

        # create a text entry box
        # for typing the information
        nom_appareil_field = bkrgframe.add(Entry(self, width= 40, fg='black'), 400, 240)
        marque_field = bkrgframe.add(Entry(self, width= 40, fg='black'), 400, 260)
        date_achat_field = bkrgframe.add(Entry(self, width= 40, fg='black'), 400, 280)
        date_exp_field = bkrgframe.add(Entry(self, width= 40, fg='black'), 400, 300)
        prix_achat_field = bkrgframe.add(Entry(self, width= 40, fg='black'), 400, 320)
        date_compta_field = bkrgframe.add(Entry(self, width= 40, fg='black'), 400, 340)
        #ammort_mensuel_field = bkrgframe.add(Entry(self, width= 40), 400, 360)
        utilisateur_field = bkrgframe.add(Entry(self, width= 40, fg='black'), 400, 360)
        date_affect_field = bkrgframe.add(Entry(self, width= 40, fg='black'), 400, 380)
        date_fin_field = bkrgframe.add(Entry(self, width= 40, fg='black'), 400, 400)

        
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

        date_fin_field.bind("<Return>", focus9)

        entries_black()

        submit = bkrgframe.add(tk.Button(self, 
                            text ="Ajouter",
                            command=insert,
                            bg='#45b592',
                            fg='#ffffff',
                            bd=0,
                            font=BUTTON_FONT,
                            height=2,
                            width=15
                            )
                            , 530, 430)

        button1 = bkrgframe.add(tk.Button(self, 
                            text ="Retour",
                            command = lambda : [entries_black(), clear(), controller.show_frame(Acceuil)] ,
                            bg='#FFCE5F',
                            fg='#ffffff',
                            bd=0,
                            font=BUTTON_FONT,
                            height=2,
                            width=15
                            )
                            , 700, 550)
        

# second window frame Ajouter
class Acceuil(tk.Frame):
     
    def __init__(self, parent, controller):

        def diff_month(d1, d2):
            return (d1.year - d2.year) * 12 + d1.month - d2.month

        def get_dot_ammort_mensuel(date_achat, ammort_mesnuel):
            val_ammort_mesnuel = float(ammort_mesnuel)
            nb_months = diff_month(datetime.now(), datetime.strptime(date_achat, "%d-%m-%Y"))
            return nb_months*val_ammort_mesnuel

        def update_rows():
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM laptops")
            rows = cursor.fetchall()
            for row in rows :  
                val_dot_ammort_mensuel = get_dot_ammort_mensuel(row[2], row[6])
                val_vcn = float(row[4])-val_dot_ammort_mensuel
                cursor.execute("UPDATE laptops SET dot_ammortissement_mensuel=?, VCN=? WHERE Nom_appareil=? ", (val_dot_ammort_mensuel, val_vcn, row[0]))
                conn.commit()

         
        tk.Frame.__init__(self, parent)

        # button to show frame 2 with text
        # layout2
        bkrgframe = BkgrFrame(self, resource_path(IMAGE_PATH_FIRST), WIDTH, HEIGTH)
        bkrgframe.pack()
        

        button1 = bkrgframe.add(tk.Button(self, 
                            text ="Ajouter",
                            command = lambda : controller.show_frame(Ajouter),
                            bg='#45b592',
                            fg='#ffffff',
                            bd=0,
                            font=BUTTON_FONT,
                            height=2,
                            width=15
                            ), 550, 400)

        button2 = bkrgframe.add(tk.Button(self, 
                            text ="Rechercher par nom d'appareil",
                            command = lambda : controller.show_frame(Rechercher_laptop_nom_app),
                            bg='#45b592',
                            fg='#ffffff',
                            bd=0,
                            font=BUTTON_FONT,
                            height=2,
                            width=30
                            ), 500, 450)

        button3 = bkrgframe.add(tk.Button(self, 
                            text ="Rechercher par utilisateur",
                            command = lambda : controller.show_frame(Rechercher_laptop_user),
                            bg='#45b592',
                            fg='#ffffff',
                            bd=0,
                            font=BUTTON_FONT,
                            height=2,
                            width=30
                            ), 500, 500)

        button4 = bkrgframe.add(tk.Button(self, 
                            text ="Rechercher par VCN",
                            command = lambda : controller.show_frame(Rechercher_laptop_vcn),
                            bg='#45b592',
                            fg='#ffffff',
                            bd=0,
                            font=BUTTON_FONT,
                            height=2,
                            width=30
                            ), 500, 550)

        button5 = bkrgframe.add(tk.Button(self, 
                            text ="MAJ Valeurs",
                            command = update_rows,
                            bg='#FFCE5F',
                            fg='#ffffff',
                            bd=0,
                            font=BUTTON_FONT,
                            height=2,
                            width=20
                            ), 1025, 737)

# second window frame Rechercher_laptop_nom_app
class Rechercher_laptop_nom_app(tk.Frame):
     
    def __init__(self, parent, controller):

        def clear():
            
            # clear the content of text entry box
            nom_appareil_recherche_field.delete(0, END)
            nom_appareil_field.delete(0, END)
            marque_field.delete(0, END)
            date_achat_field.delete(0, END)
            date_exp_field.delete(0, END)
            prix_achat_field.delete(0, END)
            date_compta_field.delete(0, END)
            ammort_mensuel_field.delete(0, END)
            utilisateur_field.delete(0, END)
            date_affect_field.delete(0, END)
            date_fin_field.delete(0, END)
            dot_ammort_mensuel_field.delete(0, END)
            vcn_field.delete(0, END)

        def change_text(entry,txt):
            entry.delete(0,END)
            entry.insert(0,txt)

        def clear_text(entry):
            entry.delete(0,END)

        def diff_month(d1, d2):
            return (d1.year - d2.year) * 12 + d1.month - d2.month

        def get_dot_ammort_mensuel(date_achat, ammort_mesnuel):
            val_ammort_mesnuel = float(ammort_mesnuel)
            nb_months = diff_month(datetime.now(), datetime.strptime(date_achat, "%d-%m-%Y"))
            return nb_months*val_ammort_mesnuel

        def recherche(name):
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM laptops where Nom_appareil=?", (name,))
            row = cursor.fetchone()

            if row :
                val_dot_ammort_mensuel = get_dot_ammort_mensuel(row[2], row[6])
                change_text(nom_appareil_field,row[0])
                change_text(marque_field,row[1])
                change_text(date_achat_field,row[2])
                change_text(date_exp_field,row[3])
                change_text(prix_achat_field,row[4])
                change_text(date_compta_field,row[5])
                change_text(ammort_mensuel_field,row[6])
                change_text(utilisateur_field,row[7])
                change_text(date_affect_field,row[8])
                change_text(date_fin_field,row[9])
                change_text(dot_ammort_mensuel_field, row[10])
                change_text(vcn_field, row[11])

            else :
                clear_text(nom_appareil_field)
                clear_text(marque_field)
                clear_text(date_achat_field)
                clear_text(date_exp_field)
                clear_text(prix_achat_field)
                clear_text(date_compta_field)
                clear_text(ammort_mensuel_field)
                clear_text(utilisateur_field)
                clear_text(date_affect_field)
                clear_text(date_fin_field)
                clear_text(dot_ammort_mensuel_field)
                clear_text(vcn_field)

                

        tk.Frame.__init__(self, parent)

        bkrgframe = BkgrFrame(self, resource_path(IMAGE_PATH_OTHERS), WIDTH, HEIGTH)
        bkrgframe.pack()

        Titre = bkrgframe.add(Label(self, text ="Rechercher un laptop par nom d'appareil", bg="#DEC6FA", font = MIDFONT)
                            , 300, 100)
        
        # recherche section

        nom_appareil_recherche = bkrgframe.add(Label(self, text="Tapez le nom de l'appareil :", bg="#DEC6FA")
                            , 300, 200)

        nom_appareil_recherche_field = bkrgframe.add(Entry(self), 500, 200)

        Recherchebtn = bkrgframe.add(tk.Button(self, 
                            text ="Rechercher",
                            command = lambda : recherche(nom_appareil_recherche_field.get()),
                            bg='#45b592',
                            fg='#ffffff',
                            bd=0,
                            font=BUTTON_FONT,
                            height=2,
                            width=15
                            )
                            , 700, 190)


        # affichage section

        nom_appareil = bkrgframe.add(Label(self, text="Nom de l'appareil", bg="#DEC6FA")
                            , 300, 280)

        marque = bkrgframe.add(Label(self, text="Marque", bg="#DEC6FA")
                            , 300, 300)

        date_achat = bkrgframe.add(Label(self, text="Date de l'achat", bg="#DEC6FA")
                            , 300, 320)

        date_exp = bkrgframe.add(Label(self, text="Date d'expiration", bg="#DEC6FA")
                            , 300, 340)

        prix_achat = bkrgframe.add(Label(self, text="Prix d'achat", bg="#DEC6FA")
                            , 300, 360)

        date_compta = bkrgframe.add(Label(self, text="Date comptabilisation", bg="#DEC6FA")
                            , 300, 380)

        ammort_mensuel = bkrgframe.add(Label(self, text="Ammortissement mensuel", bg="#DEC6FA")
                            , 300, 400)

        utilisateur = bkrgframe.add(Label(self, text="Utilisateur", bg="#DEC6FA")
                            , 300, 420)

        date_affect = bkrgframe.add(Label(self, text="Date affectation", bg="#DEC6FA")
                            , 300, 440)
        
        date_fin = bkrgframe.add(Label(self, text="Date de fin", bg="#DEC6FA")
                            , 300, 460)

        dot_ammort_mensuel = bkrgframe.add(Label(self, text="Dotation aux amortissements", bg="#DEC6FA")
                            , 300, 480)

        vcn = bkrgframe.add(Label(self, text="Valeure compatable nette", bg="#DEC6FA")
                            , 300, 500)

        

        # create a text entry box
        # for typing the information
        nom_appareil_field = bkrgframe.add(Entry(self), 450, 280)
        marque_field = bkrgframe.add(Entry(self), 450, 300)
        date_achat_field = bkrgframe.add(Entry(self), 450, 320)
        date_exp_field = bkrgframe.add(Entry(self), 450, 340)
        prix_achat_field = bkrgframe.add(Entry(self), 450, 360)
        date_compta_field = bkrgframe.add(Entry(self), 450, 380)
        ammort_mensuel_field = bkrgframe.add(Entry(self), 450, 400)
        utilisateur_field = bkrgframe.add(Entry(self), 450, 420)
        date_affect_field = bkrgframe.add(Entry(self), 450, 440)
        date_fin_field = bkrgframe.add(Entry(self), 450, 460)
        dot_ammort_mensuel_field = bkrgframe.add(Entry(self), 450, 480)
        vcn_field = bkrgframe.add(Entry(self), 450, 500)


        

        Retour = bkrgframe.add(tk.Button(self, 
                            text ="Retour",
                            command = lambda : [clear(), controller.show_frame(Acceuil)],
                            bg='#FFCE5F',
                            fg='#ffffff',
                            bd=0,
                            font=BUTTON_FONT,
                            height=2,
                            width=15
                            )
                            , 700, 550)


class Rechercher_laptop_user(tk.Frame):
     
    def __init__(self, parent, controller):

        def clear():
            
            # clear the content of text entry box
            nom_appareil_recherche_field.delete(0, END)
            nom_appareil_field.delete(0, END)
            marque_field.delete(0, END)
            date_achat_field.delete(0, END)
            date_exp_field.delete(0, END)
            prix_achat_field.delete(0, END)
            date_compta_field.delete(0, END)
            ammort_mensuel_field.delete(0, END)
            utilisateur_field.delete(0, END)
            date_affect_field.delete(0, END)
            date_fin_field.delete(0, END)
            dot_ammort_mensuel_field.delete(0, END)
            vcn_field.delete(0, END)
        
        def change_text(entry,txt):
            entry.delete(0,END)
            entry.insert(0,txt)

        def clear_text(entry):
            entry.delete(0,END)

        def diff_month(d1, d2):
            return (d1.year - d2.year) * 12 + d1.month - d2.month

        def get_dot_ammort_mensuel(date_achat, ammort_mesnuel):
            val_ammort_mesnuel = float(ammort_mesnuel)
            nb_months = diff_month(datetime.now(), datetime.strptime(date_achat, "%d-%m-%Y"))
            return nb_months*val_ammort_mesnuel

        def recherche(name):
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM laptops where Utilisateur=?", (name,))
            row = cursor.fetchone()

            if row :
                val_dot_ammort_mensuel = get_dot_ammort_mensuel(row[2], row[6])
                change_text(nom_appareil_field,row[0])
                change_text(marque_field,row[1])
                change_text(date_achat_field,row[2])
                change_text(date_exp_field,row[3])
                change_text(prix_achat_field,row[4])
                change_text(date_compta_field,row[5])
                change_text(ammort_mensuel_field,row[6])
                change_text(utilisateur_field,row[7])
                change_text(date_affect_field,row[8])
                change_text(date_fin_field,row[9])
                change_text(dot_ammort_mensuel_field, row[10])
                change_text(vcn_field, row[11])

            else :
                clear_text(nom_appareil_field)
                clear_text(marque_field)
                clear_text(date_achat_field)
                clear_text(date_exp_field)
                clear_text(prix_achat_field)
                clear_text(date_compta_field)
                clear_text(ammort_mensuel_field)
                clear_text(utilisateur_field)
                clear_text(date_affect_field)
                clear_text(date_fin_field)
                clear_text(dot_ammort_mensuel_field)
                clear_text(vcn_field)

                

        tk.Frame.__init__(self, parent)

        bkrgframe = BkgrFrame(self, resource_path(IMAGE_PATH_OTHERS), WIDTH, HEIGTH)
        bkrgframe.pack()

        Titre = bkrgframe.add(Label(self, text ="Rechercher un laptop par utilisateur", bg="#DEC6FA", font = MIDFONT)
                            , 300, 100)
        
        # recherche section

        nom_appareil_recherche = bkrgframe.add(Label(self, text="Tapez le nom de l'utilisateur :", bg="#DEC6FA")
                            , 300, 200)

        nom_appareil_recherche_field = bkrgframe.add(Entry(self), 500, 200)

        Recherchebtn = bkrgframe.add(tk.Button(self, 
                            text ="Rechercher",
                            command = lambda : recherche(nom_appareil_recherche_field.get()),
                            bg='#45b592',
                            fg='#ffffff',
                            bd=0,
                            font=BUTTON_FONT,
                            height=2,
                            width=15
                            )
                            , 700, 190)


        # affichage section

        nom_appareil = bkrgframe.add(Label(self, text="Nom de l'appareil", bg="#DEC6FA")
                            , 300, 280)

        marque = bkrgframe.add(Label(self, text="Marque", bg="#DEC6FA")
                            , 300, 300)

        date_achat = bkrgframe.add(Label(self, text="Date de l'achat", bg="#DEC6FA")
                            , 300, 320)

        date_exp = bkrgframe.add(Label(self, text="Date d'expiration", bg="#DEC6FA")
                            , 300, 340)

        prix_achat = bkrgframe.add(Label(self, text="Prix d'achat", bg="#DEC6FA")
                            , 300, 360)

        date_compta = bkrgframe.add(Label(self, text="Date comptabilisation", bg="#DEC6FA")
                            , 300, 380)

        ammort_mensuel = bkrgframe.add(Label(self, text="Ammortissement mensuel", bg="#DEC6FA")
                            , 300, 400)

        utilisateur = bkrgframe.add(Label(self, text="Utilisateur", bg="#DEC6FA")
                            , 300, 420)

        date_affect = bkrgframe.add(Label(self, text="Date affectation", bg="#DEC6FA")
                            , 300, 440)
        
        date_fin = bkrgframe.add(Label(self, text="Date de fin", bg="#DEC6FA")
                            , 300, 460)

        dot_ammort_mensuel = bkrgframe.add(Label(self, text="Dotation aux amortissements", bg="#DEC6FA")
                            , 300, 480)

        vcn = bkrgframe.add(Label(self, text="Valeure compatable nette", bg="#DEC6FA")
                            , 300, 500)

        

        # create a text entry box
        # for typing the information
        nom_appareil_field = bkrgframe.add(Entry(self), 450, 280)
        marque_field = bkrgframe.add(Entry(self), 450, 300)
        date_achat_field = bkrgframe.add(Entry(self), 450, 320)
        date_exp_field = bkrgframe.add(Entry(self), 450, 340)
        prix_achat_field = bkrgframe.add(Entry(self), 450, 360)
        date_compta_field = bkrgframe.add(Entry(self), 450, 380)
        ammort_mensuel_field = bkrgframe.add(Entry(self), 450, 400)
        utilisateur_field = bkrgframe.add(Entry(self), 450, 420)
        date_affect_field = bkrgframe.add(Entry(self), 450, 440)
        date_fin_field = bkrgframe.add(Entry(self), 450, 460)
        dot_ammort_mensuel_field = bkrgframe.add(Entry(self), 450, 480)
        vcn_field = bkrgframe.add(Entry(self), 450, 500)


        

        Retour = bkrgframe.add(tk.Button(self, 
                            text ="Retour",
                            command = lambda : [clear(), controller.show_frame(Acceuil)],
                            bg='#FFCE5F',
                            fg='#ffffff',
                            bd=0,
                            font=BUTTON_FONT,
                            height=2,
                            width=15
                            )
                            , 700, 550)



class Rechercher_laptop_vcn(tk.Frame):
     
    def __init__(self, parent, controller):


        def diff_month(d1, d2):
            return (d1.year - d2.year) * 12 + d1.month - d2.month

        def get_dot_ammort_mensuel(date_achat, ammort_mesnuel):
            val_ammort_mesnuel = float(ammort_mesnuel)
            nb_months = diff_month(datetime.now(), datetime.strptime(date_achat, "%d-%m-%Y"))
            return nb_months*val_ammort_mesnuel

        def update_rows():
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM laptops")
            rows = cursor.fetchall()
            for row in rows :  
                val_dot_ammort_mensuel = get_dot_ammort_mensuel(row[2], row[6])
                val_vcn = float(row[4])-val_dot_ammort_mensuel
                cursor.execute("UPDATE laptops SET dot_ammortissement_mensuel=?, VCN=? WHERE Nom_appareil=? ", (val_dot_ammort_mensuel, val_vcn, row[0]))
                conn.commit()

            
        def recherche(canvas):
            total_vcn = 0

            canvas.create_text(10, 10, text="Nom Appareil")
            canvas.create_text(100, 10, text="Utilisateur")
            canvas.create_text(200, 10, text="VCN")
            y= 30
            x1= 20
            x2= 100
            x3= 200
            update_rows()    

            cursor = conn.cursor()
            cursor.execute("SELECT * FROM laptops where VCN>0")
            rows = cursor.fetchall()

            for row in rows : 
                canvas.create_text(x1, y, text=row[0])
                canvas.create_text(x2, y, text=row[7])
                canvas.create_text(x3, y, text=row[11])
                total_vcn = total_vcn + float(row[11])
                y = y + 15

            total_vcn_msg = "Total VCN : " + str(total_vcn)
            total_laptops_msg = "Total laptops : " + str(len(rows))
            canvas.create_text(10, y+40, text=total_vcn_msg, font=SMALLFONT , anchor=tk.SW)
            canvas.create_text(10, y+80, text=total_laptops_msg, font=SMALLFONT , anchor=tk.SW)

        def clear_canavas():
             canvas_result.delete('all')   

        tk.Frame.__init__(self, parent)

        bkrgframe = BkgrFrame(self, resource_path(IMAGE_PATH_OTHERS), WIDTH, HEIGTH)
        bkrgframe.pack()

        Titre = bkrgframe.add(Label(self, text ="Rechercher un laptop par VCN", bg="#DEC6FA", font = MIDFONT)
                            , 300, 100)
        
        # recherche section

        canvas_result = bkrgframe.add(tk.Canvas(self, width=350, height=350,scrollregion=(0,0,500,500))
                            , 300, 200)

        clear_canavas()
        Recherchebtn = bkrgframe.add(tk.Button(self, 
                            text ="Rechercher",
                            command = lambda : [clear_canavas(), recherche(canvas_result)],
                            bg='#45b592',
                            fg='#ffffff',
                            bd=0,
                            font=BUTTON_FONT,
                            height=2,
                            width=15
                            )
                            , 700, 200)


        Retour = bkrgframe.add(tk.Button(self, 
                            text ="Retour",
                            command = lambda : [clear_canavas(), controller.show_frame(Acceuil)],
                            bg='#FFCE5F',
                            fg='#ffffff',
                            bd=0,
                            font=BUTTON_FONT,
                            height=2,
                            width=15
                            )
                            , 700, 550)


    
app = tkinterApp()
app.mainloop()