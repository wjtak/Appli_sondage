from tkinter import *
from csv import writer


def insert() : 
    print('ok')
    code=eCode.get()
    commune=eCommune.get()
    type_commune=eType.get()
    nom_departement=eDepartement.get()
    departement=eDep.get()
    sexe=esex.get()
    age=eag.get()
    formation=eforma.get()
    profession=eprof.get()
    taille_org=etailleorg.get()
    position_gj=epos.get()


    row_contents = ['xxxx', code, commune,type_commune,nom_departement,departement,sexe,age,formation,profession,taille_org,position_gj]

    # Open file in append mode
    with open('users.csv', 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(row_contents)
    


fenetrePrincipale = Tk()
    
fenetrePrincipale.title("registration form")   
fenetrePrincipale.geometry("500x300") 

lCode = Label(fenetrePrincipale, text = "Code Postal")
eCode = Entry(fenetrePrincipale)

lCommune = Label(fenetrePrincipale, text = "Commune")
eCommune = Entry(fenetrePrincipale)

lType = Label(fenetrePrincipale, text = "Type Commune")
eType = Entry(fenetrePrincipale)

lDepartement = Label(fenetrePrincipale, text = "Nom departement")
eDepartement = Entry(fenetrePrincipale)

lDep = Label(fenetrePrincipale, text = "Département")
eDep = Entry(fenetrePrincipale)

lsex = Label(fenetrePrincipale, text = "Sexe")
esex = Entry(fenetrePrincipale)

lag = Label(fenetrePrincipale, text = "Âge")
eag = Entry(fenetrePrincipale)

lforma = Label(fenetrePrincipale, text = "Formation")
eforma = Entry(fenetrePrincipale)

lprof = Label(fenetrePrincipale, text = "Profession")
eprof = Entry(fenetrePrincipale)

ltailleorg = Label(fenetrePrincipale, text = "Taille de l'organisation")
etailleorg = Entry(fenetrePrincipale)

lpos = Label(fenetrePrincipale, text = "Position_gj")
epos = Entry(fenetrePrincipale)

b = Button(fenetrePrincipale, text="Submit", fg="Black", 
                            bg="Red", command=insert) 

lCode.pack()
eCode.pack()

lCommune.pack()
eCommune.pack()

lType.pack()
eType.pack()

lDepartement.pack()
eDepartement.pack()

lDep.pack()
eDep.pack()

lsex.pack()
esex.pack()

lag.pack()
eag.pack()

lforma.pack()
eforma.pack()

lprof.pack()
eprof.pack()

ltailleorg.pack()
etailleorg.pack()

lpos.pack()
epos.pack()

b.pack()

fenetrePrincipale.mainloop()