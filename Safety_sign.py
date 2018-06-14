# importation des modules
from tkinter import *
import datetime
from tkinter import font

# set-up des variables
debut = datetime.datetime.now()
record = datetime.timedelta(0, 0, 1)
jJanvier = 0
ActualTime = datetime.datetime.now()

class SafetyF(Frame, Toplevel):


    def bdate(self):
        """fichier texte qui garde en memoire le debut et le record"""
        with open("bddate.txt", "w") as f:
            f.write(debut)
            f.write (record)

    # initialisation de la class SafetyF
    def __init__(self, fenetre):
        """initialisation de la fenetre du logiciel"""
        Frame.__init__(self, fenetre)
        fenetre.geometry("706x529")
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.register # permet de garder en memoire les valeurs

        Button(fenetre, text="choose your resolution", borderwidth=2, background='violet').grid(row=1, column=0)
        Button(fenetre, text="706x526", command=self.resizeSmall, borderwidth=2, background='pink').grid(row=1, column=1)#Les boutons de cette liste servent a definir la taille de la fenetre
        Button(fenetre, text="1920x1080", command=self.resizeLarge, borderwidth=2, background='pink').grid(row=1, column=3)
        Button(fenetre, text="1600x900", command=self.resizeMedium, borderwidth=2, background='pink').grid(row=1, column=2)


    def resizeSmall(self):#petite fenetre
        fenetre.geometry("706x529")
        background_image = PhotoImage(file="C:\\Users\\EX_SDV\\PycharmProjects\\untitled1\\backgroundIsmall.PNG")
        background_label = Label(fenetre, image=background_image)
        background_label.image = background_image
        background_label.place(x=0, y=0, relwidth=1, relheight=1)#Activation de l'image de fond


        Button(fenetre, text='Start', command=self.Start, borderwidth=2, background='green').grid(row=1, column=1, sticky="nw")
        Button(fenetre, text='quitter', command=quit, borderwidth=2).grid(row=1, column=3, sticky="nw")
        Button(fenetre, text="+", command=self.jJ, borderwidth=2, background='red').grid(row=1, column=2, sticky="nw")
        Button(fenetre, bg='white', fg='black', justify='center', width=5, relief=FLAT, font=('Times', '22'), text=jJanvier).place(x=1360, y=280)

        Text(fenetre, bg='white', fg='black', width=18, height=2, relief=FLAT, font=('Times', '13')).place(x=120, y=90) #no accident this week
        Text(fenetre, bg='white', fg='black', width=18, height=2, relief=FLAT, font=('Times', '13')).place(x=423, y=90) #An accident accurred this week

        Entry(fenetre, bg='white', fg='black', justify='left', width=60, relief=FLAT, font=('Times', '12')).place(x=38, y=173) #ligne 1 (accident depuis le 1er janvier)
        Entry(fenetre, bg='white', fg='black', justify='left', width=60, relief=FLAT, font=('Times', '12')).place(x=38, y=240) #ligne 2 (nb jour sans accident)
        Entry(fenetre, bg='white', fg='black', justify='left', width=60, relief=FLAT, font=('Times', '12')).place(x=38, y=300) #ligne 3 (record jour sans accident)

        Text(fenetre, bg='white', fg='black', width=11, height=3, relief=GROOVE, borderwidth=3).place(x=150, y=357) #Basic rules to follow
        Text(fenetre, bg='white', fg='black', width=8, height=2, relief=GROOVE, borderwidth=3).place(x=182, y=476) #Message to read
        Entry(fenetre, bg='grey', fg='white', justify='center', width=65, relief=FLAT).place(x=260, y=485) #message du jour

    def resizeLarge(self):#grande fenetre
        fenetre.geometry("1920x1080")
        background_image = PhotoImage(file="C:\\Users\\EX_SDV\\PycharmProjects\\untitled1\\backgroundIhd.PNG")
        background_label = Label(fenetre, image=background_image)
        background_label.image = background_image
        background_label.place(x=0, y=0, relwidth=1, relheight=1)  # Activation de l'image de fond

        Button(fenetre, text='Start', command=self.Start, borderwidth=2, background='green').grid(row=1, column=1, sticky="nw")
        Button(fenetre, text='quitter', command=quit, borderwidth=2).grid(row=1, column=3, sticky="nw")
        Button(fenetre, text="+", command=self.jJ, borderwidth=2, background='red').grid(row=1, column=2, sticky="nw")

        Text(fenetre, bg='white', fg='black', width=25, height=4, relief=FLAT, font=('Times', '13')).place(x=290, y=185)  # no accident this week
        Text(fenetre, bg='white', fg='black', width=25, height=4, relief=FLAT, font=('Times', '13')).place(x=1150, y=185)  # An accident accurred this week

        Entry(fenetre, bg='white', fg='black', justify='left', width=90, relief=FLAT, font=('Times', '20')).place(x=140, y=355)  # ligne 1 (accident depuis le 1er janvier)
        Entry(fenetre, bg='white', fg='black', justify='left', width=90, relief=FLAT, font=('Times', '20')).place(x=140, y=470)  # ligne 2 (nb jour sans accident)
        Entry(fenetre, bg='white', fg='black', justify='left', width=90, relief=FLAT, font=('Times', '20')).place(x=140, y=600)  # ligne 3 (record jour sans accident)

        Text(fenetre, bg='white', fg='black', width=30, height=5, relief=GROOVE, borderwidth=3).place(x=450, y=730)  # Basic rules to follow
        Text(fenetre, bg='grey', fg='white', width=110, height=3, font=('Times', '19'), relief=FLAT).place(x=525, y=960)  # message du jour

    def resizeMedium(self):#fenetre moyenne
        fenetre.geometry("1600x900")
        background_image = PhotoImage(file="C:\\Users\\EX_SDV\\PycharmProjects\\untitled1\\backgroundImedium.PNG")
        background_label = Label(fenetre, image=background_image)
        background_label.image = background_image
        background_label.place(relx=0, rely=0)  # Activation de l'image de fond

        Button(fenetre, text='Start', command=self.Start, borderwidth=2, background='green').grid(row=1, column=1, sticky="nw")
        Button(fenetre, text='quitter', command=quit, borderwidth=2).grid(row=1, column=3, sticky="nw")
        Button(fenetre, text="add", command=self.jJ, borderwidth=2, background='red').grid(row=1, column=2, sticky="nw")

        Text(fenetre, bg='white', fg='black', width=25, height=4, relief=FLAT, font=('Times', '13')).place(relx=0.19, rely=0.1)  # no accident this week
        Text(fenetre, bg='white', fg='black', width=25, height=4, relief=FLAT, font=('Times', '13')).place(x=955, y=150)  # An accident accurred this week

        Entry(fenetre, bg='white', fg='black', justify='left', width=70, relief=FLAT, font=('Times', '20')).place(x=140, y=285)  # ligne 1 (accident depuis le 1er janvier)
        Entry(fenetre, bg='white', fg='black', justify='left', width=70, relief=FLAT, font=('Times', '20')).place(x=140, y=400)  # ligne 2 (nb jour sans accident)
        Entry(fenetre, bg='white', fg='black', justify='left', width=70, relief=FLAT, font=('Times', '20')).place(x=140, y=515)  # ligne 3 (record jour sans accident)

        Text(fenetre, bg='white', fg='black', width=30, height=5, relief=GROOVE, borderwidth=3).place(x=360, y=615)  # Basic rules to follow
        Text(fenetre, bg='grey', fg='white', width=100, height=3, font=('Times', '16'), relief=FLAT).place(x=435, y=813)  # message du jour

    def jJ(self):
        """ajoute 1 au nombre d accident depuis le premier janvier"""
        global jJanvier
        jJanvier += 1
        Button(fenetre, bg='white', fg='black', justify='center', width=5, relief=FLAT, font=('Times', '22'), text=jJanvier).place(x=1360, y=280)  # Jours accident depuis 1er janvier
        return

    def Start(self):
        """ Start gere le temps et le record"""
        global record
        global ActualTime
        ActualTime = datetime.datetime.now()
        delta = ActualTime - debut
        Button(fenetre, bg='white', fg='black', text=delta.seconds,justify='center', width=5, font=('Times', '22'), relief=FLAT).place(x=1360, y=387) # nb jours sans accident pour record
        if (ActualTime.second > record.seconds):
            record = ActualTime - debut
            Button(fenetre, bg='white', fg='black', justify='center', width=7, relief=FLAT, font=('Times', '22'), text=record.total_seconds()).place(x=1360, y=510) #record
        self.after(300, self.Start)
        return


#Fin du programme
fenetre = Tk()
fenetre.title('Safety First')
interface = SafetyF(fenetre)
interface.mainloop()

