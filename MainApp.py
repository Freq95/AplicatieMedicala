# TO-DO: make an executable for test --->>> [done once - it works but the code had some errors]
# nu lasa introducerea multipla a aceleiasi persoane
# !!!! repara introducerea de pdf in baza de date - check -  daca e necesar sa-l introduci sau e dee ajuns sa-l salvvezi local in proiect, same shit si cu imaginea + adauga data
import ClasaDB
import ClasaPacienti
import ClasaProgramari
import os
import PyPDF2
from PIL import Image
import tkinter
from tkinter import filedialog
import webbrowser as wb

def mainApplication():
    Pacient = ClasaPacienti.Pacient('Ion', 'Doi', '23', 'M')

    PacientDB = ClasaDB.BazaDate()
    PacientDB.create_table()

    # verificare daca exista pacient cu acelasi nume in DB
    existaPacient = PacientDB.CheckExistentaPacientInDB('Dolanescu', 'Doi')


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

def formularPacient():
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

    ##Cautare dupa nume:
    #PacientDB.cautare_pacient_DB('Paul')


    ##-------------- Adaugare Programare --------------##
    tratament = input("Tratament: ")
    numePacient = input("Nume Pacient: ")

    ##PDF citire ====================================
    tkinter.Tk().withdraw()  # Close the root window
    in_path = filedialog.askopenfilename(title = "Select file",filetypes = (("pdf files","*.pdf"),("all files","*.*")))


    ##Simply opens a pdf ====================================
    #wb.open_new(r'D:\__AplicatieMedicala\exemple.pdf')

    # print(in_path)

    ## deschidere pdf
    #objPDF = open(in_path, 'rb')
    #pdf = PyPDF2.PdfFileReader(objPDF)
    #print(pdf.numPages)
    #os.startfile(in_path)

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

    mainApplication()
    #formularPacient()

