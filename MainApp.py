# TO-DO: make an executable for test
# nu lasa introducerea multipla a aceleiasi persoane
# !!!! repara introducerea de pdf in baza de date - check -  daca e necesar sa-l introduci sau e dee ajuns sa-l salvvezi local in proiect, same shit si cu imaginea + adauga data
import ClasaDB
import ClasaPacienti
import ClasaProgramari
import os
import PyPDF2

from PIL import Image

import Tkinter
import tkFileDialog

def mainApplication():
    Pacient = ClasaPacienti.Pacient('Marinica', 'Novac', '23', 'M')

    PacientDB = ClasaDB.BazaDate()
    PacientDB.create_table()
    PacientDB.introducere_pacient_db(Pacient)

    #PacientDB.afisare_tabel()

    PacientDB.cautare_pacient_DB('Paul')
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
    tratament = raw_input("tratament: ")
    id_pacient = raw_input("id_pacient: ")

    #PDF citire
    Tkinter.Tk().withdraw()  # Close the root window
    in_path = tkFileDialog.askopenfilename(title = "Select file",filetypes = (("pdf files","*.pdf"),("all files","*.*")))
    print in_path

    objPDF = open(in_path, 'rb')
    pdf = PyPDF2.PdfFileReader(objPDF)
    print(pdf.numPages)
    os.startfile(in_path)

    #Radiografie citire + afisare
    Tkinter.Tk().withdraw()  # Close the root window
    in_path1 = tkFileDialog.askopenfilename(title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
    print in_path1
    radiografie = Image.open(in_path1).convert('L')
    radiografie.show()

    #Adaugare programare noua
    newProgramare = ClasaProgramari.Programare(tratament, pdf, radiografie, id_pacient)
    DataBase.introducere_programare_db(newProgramare)

    DataBase.close_DB()


if __name__ == '__main__':


    formularPacient()
