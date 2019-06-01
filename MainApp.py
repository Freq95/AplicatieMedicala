# TO-DO: make an executable for test --->>> [done once - it works but the code had some errors]
# nu lasa introducerea multipla a aceleiasi persoane
# !!!! repara introducerea de pdf in baza de date - check -  daca e necesar sa-l introduci sau e dee ajuns sa-l salvvezi local in proiect, same shit si cu imaginea + adauga data
import ClasaDB
import ClasaPacienti
import ClasaProgramari
import sys
import os
import PyPDF2
from PIL import Image
import tkinter
from tkinter import filedialog
from tkinter import *
import webbrowser as wb



def runGui():
    print('mainGui')
    window = Tk()

    window.title("Aplicatie Medicala")

    window.geometry('350x200')

    ## LABELS
    lblNume = Label(window, text="Nume: ")
    lblPrenume = Label(window, text="Prenume: ")
    lblVarsta = Label(window, text="Varsta: ")
    lblSex = Label(window, text="Sex: ")
    lblTratament = Label(window, text="Tratament: ")

    lblNume.grid(column=0, row=0)
    lblPrenume.grid(column=0, row=1)
    lblVarsta.grid(column=0, row=2)
    lblSex.grid(column=0, row=3)
    lblTratament.grid(column=0, row=4)

    ## TEXT INPUTS
    txtNume = Entry(window, width=10)
    txtPrenume = Entry(window, width=10)
    txtVarsta = Entry(window, width=10)
    txtSex = Entry(window, width=10)
    txtTratament = Entry(window, width=10)

    txtNume.grid(column=1, row=0)
    txtPrenume.grid(column=1, row=1)
    txtVarsta.grid(column=1, row=2)
    txtSex.grid(column=1, row=3)
    txtTratament.grid(column=1, row=4)

    ## ACTIUNE BUTOANE
    def clicked():
        #lbl.configure(text="Button was clicked !!")
        ## aici ai ramas
        ##Pacient = ClasaPacienti.Pacient(txtNume.get(), txtPrenume.get(), txtVarsta.get(), txtSex.get())
        print("First Name: %s\nLast Name: %s" % (txtNume.get(), txtPrenume.get()))
        Pacient = ClasaPacienti.Pacient(txtNume.get(), txtPrenume.get(), txtVarsta.get(), txtSex.get())
        mainApplication(Pacient)

    def programare():
        print("Programare Noua")
        formularPacient(txtTratament.get(), txtNume.get())

    def openPDF():
        print("Deschide PDF")
        deschidePDF(txtNume.get())
        #formularPacient("trat", "nume")

        #formularPacient(txtTratament.get(), txtNume.get())

    ## BUTOANE
    btnIntroducerePacient = Button(window, text="Introducere Pacient", command=clicked)
    btnIntroducerePacient.grid(column=2, row=0)

    btnAdaugaProgramare = Button(window, text="Programare Noua", command=programare)
    btnAdaugaProgramare.grid(column=2, row=2)

    btnPDF = Button(window, text="Deschide PDF", command=openPDF)
    btnPDF.grid(column=2, row=4)

    ## START GUI
    window.mainloop()


def deschidePDF(nume):
    ## deschidere pdf -- useless content below
    # objPDF = open(in_path, 'rb')
    # pdf = PyPDF2.PdfFileReader(objPDF)
    # print(pdf.numPages)W
    DataBase = ClasaDB.BazaDate()
    DataBase.create_table()
    pdfPath = DataBase.cautare_PDF_pacient(nume)



    ##refactor this and test it pentru mai multe programari
    ##investigate why for asd and nume from programariDB it opens the folder not the pdf
    ## implement checkboxes for pdf and image
    ## move pdf and images to a pdfs/images folder
    ## Rename pdf by pacient?

    [x[0] for x in pdfPath]
    pdfPath = [x[0] for x in pdfPath]
    #print(pdfPath.pop(0))



    #print(pdfPath.get(0))
    os.startfile(pdfPath.pop(0))


def mainApplication(Pacient):
    # cred ca merge sters
    Pacient = Pacient
    PacientDB = ClasaDB.BazaDate()
    PacientDB.create_table()

    # verificare daca exista pacient cu acelasi nume in DB
    existaPacient = PacientDB.CheckExistentaPacientInDB(Pacient.prenume, Pacient.nume)


    #Introducere in baza de date
    if existaPacient:
        print('Pacientul nu a fost introdus.')
    else:
        PacientDB.introducere_pacient_db(Pacient)

    #PacientDB.afisare_tabel()

    # cautare pacient
    #PacientDB.cautare_prenume_pacient_DB('Marinica')
    #PacientDB.cautare_nume_pacient_DB('Novac')


    PacientDB.close_DB()

    # print(Pacient.getNume())

def formularPacient(tratament, numePacient):
    #prenume = raw_input("Prenume: ")
    #nume = raw_input("Nume: ")
    #varsta = raw_input("Varsta: ")
    #sex = raw_input("Sex: ")
    #cnp = raw_input("CNP: ")
    #interventie = raw_input("Tip interventie: ")

    #Pacient = ClasaPacienti.Pacient(prenume, nume, varsta, sex)

    DataBase = ClasaDB.BazaDate()
    DataBase.create_table()

    ##Introducere pacient nou in baza de date:
    #PacientDB.introducere_pacient_db(Pacient)

    DataBase.afisare_tabel_pacienti()
    DataBase.afisare_tabel_programari()
    #DataBase.cautare_PDF_pacient("Novac")

    ##Cautare dupa nume:
    #PacientDB.cautare_pacient_DB('Paul')


    ##-------------- Adaugare Programare --------------##
    #tratament = input("Tratament: ")
    #numePacient = input("Nume Pacient: ")

    ##PDF citire ====================================
    tkinter.Tk().withdraw()  # Close the root window
    in_path = filedialog.askopenfilename(title = "Select file",filetypes = (("pdf files","*.pdf"),("all files","*.*")))


    ##Simply opens a pdf ====================================
    #wb.open_new(r'D:\__AplicatieMedicala\exemple.pdf')

    # print(in_path)



    #Radiografie citire + afisare ====================================
    tkinter.Tk().withdraw()  # Close the root window
    in_path1 = filedialog.askopenfilename(title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
    print(in_path1)

    #Afisare radiografie
    #radiografie = Image.open(in_path1).convert('L')
    #radiografie.show()

    #Adaugare programare noua
    newProgramare = ClasaProgramari.Programare(tratament, in_path, in_path1, numePacient)
    DataBase.introducere_programare_db(newProgramare)

    DataBase.close_DB()


if __name__ == '__main__':
    runGui()
    #mainApplication(Pacient)
    #formularPacient()

