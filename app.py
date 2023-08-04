from tkinter import *
import tkinter as tk
from tkinter import ttk
import tkinter.font as font
from PIL import Image, ImageTk

IMAGE_PATH_FIRST = 'C:\\Users\\Nader\\Documents\\projets_lotfi\\App-laptops\\first-page.jpg'
IMAGE_PATH_OTHERS = 'C:\\Users\\Nader\\Documents\\projets_lotfi\\App-laptops\\other-pages.jpg'
BUTTON_FONT = None
WIDTH = 1200
HEIGTH = 800

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
        for F in (Acceuil, Ajouter, Rechercher_laptop):
  
            frame = F(container, self)
  
            # initializing frame of that object from
            # startpage, Ajouter, Rechercher_laptop respectively with
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
                elements.append(ammort_mensuel_field.get())
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

        bkrgframe = BkgrFrame(self, IMAGE_PATH_OTHERS, WIDTH, HEIGTH)
        bkrgframe.pack()

            # create a Form label
        #heading = Label(self, text="Form", bg="light green")



        heading = bkrgframe.add(Label(self, text="Form", bg="#DEC6FA")
                            , 200, 210)

        nom_appareil = bkrgframe.add(Label(self, text="Nom de l'appareil", bg="#DEC6FA")
                            , 200, 240)

            # create a marque label
        marque = Label(self, text="Marque", bg="light green")

            # create a Date de l'achat label
        date_achat = Label(self, text="Date de l'achat", bg="light green")

            # create a date_exp label
        date_exp = Label(self, text="Date d'expiration", bg="light green")

            # create a prix_achat label
        prix_achat = Label(self, text="Prix d'achat", bg="light green")

            # create a Email id label
        date_compta = Label(self, text="Date comptabilisation", bg="light green")

            # create a ammort_mensuel label
        ammort_mensuel = Label(self, text="Ammortissement mensuel", bg="light green")

            # create a utilisateur label
        utilisateur = Label(self, text="Utilisateur", bg="light green")

            # create a date affectation label
        date_affect = Label(self, text="Date affectation", bg="light green")

            # grid method is used for placing
            # the widgets at respective positions
            # in table like structure .
        
        '''
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
        nom_appareil_field = Entry(self)
        marque_field = Entry(self)
        date_achat_field = Entry(self)
        date_exp_field = Entry(self)
        prix_achat_field = Entry(self)
        date_compta_field = Entry(self)
        ammort_mensuel_field = Entry(self)
        utilisateur_field = Entry(self)
        date_affect_field = Entry(self)

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

        # create a Submit Button and place into the self window
        submit = Button(self, text="Submit", fg="Black",
                                bg="Red", command=insert)
        submit.grid(row=10, column=1)


        button1 = ttk.Button(self, text ="Retour",
                                command = lambda : controller.show_frame(Page1))
     
        # putting the button in its place
        # by using grid
        button1.grid(row = 11, column = 1, padx = 10, pady = 10)
        '''

# second window frame Ajouter
class Acceuil(tk.Frame):
     
    def __init__(self, parent, controller):
         
        tk.Frame.__init__(self, parent)

        # button to show frame 2 with text
        # layout2
        bkrgframe = BkgrFrame(self, IMAGE_PATH_FIRST, WIDTH, HEIGTH)
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
                            ), 400, 400)

        button1 = bkrgframe.add(tk.Button(self, 
                            text ="Rechercher",
                            command = lambda : controller.show_frame(Rechercher_laptop),
                            bg='#45b592',
                            fg='#ffffff',
                            bd=0,
                            font=BUTTON_FONT,
                            height=2,
                            width=15
                            ), 800, 400)

# second window frame Ajouter
class Rechercher_laptop(tk.Frame):
     
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)

        bkrgframe = BkgrFrame(self, IMAGE_PATH_OTHERS, WIDTH, HEIGTH)
        bkrgframe.pack()

        button1 = bkrgframe.add(tk.Button(self, 
                            text ="Retour",
                            command = lambda : controller.show_frame(Ajouter),
                            bg='#45b592',
                            fg='#ffffff',
                            bd=0,
                            font=BUTTON_FONT,
                            height=2,
                            width=15
                            )
                            , 20, 10)


    
app = tkinterApp()
app.mainloop()