from tkinter import *
import tkinter as tk
from tkinter import ttk
import tkinter.font as font
from PIL import Image, ImageTk
import sqlite3
import os

IMAGE_PATH_FIRST = "assets/first-page.jpg"
IMAGE_PATH_OTHERS = "assets/other-pages.jpg"
BUTTON_FONT = None
WIDTH = 1200
HEIGTH = 800
LARGEFONT =("Verdana", 35)
MIDFONT =("Verdana", 25)


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

conn = sqlite3.connect(resource_path('test.db'))



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
        for F in (Acceuil, Ajouter, Rechercher_laptop_nom_app, Rechercher_laptop_user):
  
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
            elements = []
            
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

                elements.append(nom_appareil_field.get())
                elements.append(marque_field.get())
                elements.append(date_achat_field.get())
                elements.append(date_exp_field.get())
                elements.append(prix_achat_field.get())
                elements.append(date_compta_field.get())
                elements.append((prix_achat_field.get()*0.30)/12)
                elements.append("test")
                elements.append("test")
                elements.append(utilisateur_field.get())
                elements.append(date_affect_field.get())
                elements.append("test")

                rqst = """INSERT INTO laptops
                          (Nom_appareil, Marque, Date_achat, Form_Number, Contact_Number, Email_id, Amortissement_mensuel, Dotation_amortissements, Valeure_compatable_nette, Utilisateur, Date_affectation, Date_fin) 
                          VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"""

                cursor = conn.cursor()
                cursor.execute(rqst, elements)
                conn.commit()

                # set focus on the nom_appareil_field box
                nom_appareil_field.focus_set()

                # call the clear() function
                clear()

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

        tk.Frame.__init__(self, parent)

        bkrgframe = BkgrFrame(self, resource_path(IMAGE_PATH_OTHERS), WIDTH, HEIGTH)
        bkrgframe.pack()

        Titre = bkrgframe.add(Label(self, text ="Gestion des laptops", bg="#DEC6FA", font = LARGEFONT)
                            , 300, 100)

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

        ammort_mensuel = bkrgframe.add(Label(self, text="Ammortissement mensuel", bg="#DEC6FA")
                            , 200, 360)

        utilisateur = bkrgframe.add(Label(self, text="Utilisateur", bg="#DEC6FA")
                            , 200, 380)

        date_affect = bkrgframe.add(Label(self, text="Date affectation", bg="#DEC6FA")
                            , 200, 400)

        

        # create a text entry box
        # for typing the information
        nom_appareil_field = bkrgframe.add(Entry(self, width= 40), 400, 240)
        marque_field = bkrgframe.add(Entry(self, width= 40), 400, 260)
        date_achat_field = bkrgframe.add(Entry(self, width= 40), 400, 280)
        date_exp_field = bkrgframe.add(Entry(self, width= 40), 400, 300)
        prix_achat_field = bkrgframe.add(Entry(self, width= 40), 400, 320)
        date_compta_field = bkrgframe.add(Entry(self, width= 40), 400, 340)
        ammort_mensuel_field = bkrgframe.add(Entry(self, width= 40), 400, 360)
        utilisateur_field = bkrgframe.add(Entry(self, width= 40), 400, 380)
        date_affect_field = bkrgframe.add(Entry(self, width= 40), 400, 400)

        
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

        ammort_mensuel_field.bind("<Return>", focus7)

        utilisateur_field.bind("<Return>", focus8)

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
                            command = lambda : controller.show_frame(Acceuil),
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

        button1 = bkrgframe.add(tk.Button(self, 
                            text ="Rechercher par nom d'appareil",
                            command = lambda : controller.show_frame(Rechercher_laptop_nom_app),
                            bg='#45b592',
                            fg='#ffffff',
                            bd=0,
                            font=BUTTON_FONT,
                            height=2,
                            width=30
                            ), 500, 450)

        button1 = bkrgframe.add(tk.Button(self, 
                            text ="Rechercher par utilisateur",
                            command = lambda : controller.show_frame(Rechercher_laptop_user),
                            bg='#45b592',
                            fg='#ffffff',
                            bd=0,
                            font=BUTTON_FONT,
                            height=2,
                            width=30
                            ), 500, 500)

# second window frame Rechercher_laptop_nom_app
class Rechercher_laptop_nom_app(tk.Frame):
     
    def __init__(self, parent, controller):
        
        def change_text(entry,txt):
            entry.delete(0,END)
            entry.insert(0,txt)

        def clear_text(entry):
            entry.delete(0,END)

        def recherche(name):
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM laptops where Nom_appareil=?", (name,))
            row = cursor.fetchone()

            if row :
                change_text(nom_appareil_field,row[0])
                change_text(marque_field,row[1])
                change_text(date_achat_field,row[2])
                change_text(date_exp_field,row[3])
                change_text(prix_achat_field,row[4])
                change_text(date_compta_field,row[5])
                change_text(ammort_mensuel_field,row[6])
                change_text(utilisateur_field,row[7])
                change_text(date_affect_field,row[8])
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


        

        Retour = bkrgframe.add(tk.Button(self, 
                            text ="Retour",
                            command = lambda : controller.show_frame(Acceuil),
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
        
        def change_text(entry,txt):
            entry.delete(0,END)
            entry.insert(0,txt)

        def clear_text(entry):
            entry.delete(0,END)

        def recherche(name):
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM laptops where Utilisateur=?", (name,))
            row = cursor.fetchone()

            if row :
                change_text(nom_appareil_field,row[0])
                change_text(marque_field,row[1])
                change_text(date_achat_field,row[2])
                change_text(date_exp_field,row[3])
                change_text(prix_achat_field,row[4])
                change_text(date_compta_field,row[5])
                change_text(ammort_mensuel_field,row[6])
                change_text(utilisateur_field,row[7])
                change_text(date_affect_field,row[8])
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


        

        Retour = bkrgframe.add(tk.Button(self, 
                            text ="Retour",
                            command = lambda : controller.show_frame(Acceuil),
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