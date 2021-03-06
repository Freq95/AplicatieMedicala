import sqlite3
import datetime
import os, operator

import ClasaPacienti
import ClasaDocuments

from PyQt5.QtGui import QStandardItemModel 
from PyQt5 import QtCore
from PyQt5.QtWidgets import QListWidgetItem
from PyQt5.QtGui import QColor
from collections import Counter
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QTableView

class BazaDate(ClasaPacienti.Pacient):
    def __init__(self):
        conn = sqlite3.connect('pacienti.db')
        connProgramari = sqlite3.connect('programari.db')
        connDocs = sqlite3.connect('docs.db')

        cursor = conn.cursor()
        cursorProgramari = connProgramari.cursor()
        cursorDocs = connDocs.cursor()

        self.connProgramari = connProgramari
        self.cursorProgramari = cursorProgramari
        
        self.conn = conn
        self.cursor = cursor

        self.connDocs = connDocs
        self.cursorDocs = cursorDocs

    def create_table(self):
        self.cursor.execute('CREATE TABLE IF NOT EXISTS pacientiDB\
                            (ID INTEGER PRIMARY KEY AUTOINCREMENT,\
                            Prenume TEXT NOT NULL,\
                            Nume TEXT NOT NULL,\
                            Anul TEXT,\
                            Luna TEXT,\
                            Ziua TEXT,\
                            Telefon TEXT,\
                            CNP TEXT,\
                            Sex TEXT)')

        self.cursorProgramari.execute('CREATE TABLE IF NOT EXISTS programariDB\
                                      (ID INTEGER PRIMARY KEY AUTOINCREMENT,\
                                      Interventie TEXT,\
                                      Data TEXT,\
                                      Ora TEXT,\
                                      Prenume TEXT,\
                                      Nume TEXT NOT NULL,\
                                      NotaProgramare TEXT,\
                                      FOREIGN KEY(Nume) REFERENCES pacientiDB(ID) ON DELETE CASCADE)')

        self.cursorDocs.execute('CREATE TABLE IF NOT EXISTS docsDB\
                                      (ID INTEGER PRIMARY KEY AUTOINCREMENT,\
                                      Prenume TEXT,\
                                      Nume TEXT,\
                                      Document TEXT,\
                                      FOREIGN KEY(Nume) REFERENCES pacientiDB(ID) ON DELETE CASCADE)')


    def introducere_pacient_db(self, pacient):
        self.cursor.execute('''INSERT INTO pacientiDB(Prenume, Nume, Anul, Luna, Ziua, Telefon, CNP, Sex) VALUES(?, ?, ?, ?, ?, ?, ?, ?)''', (pacient.prenume, pacient.nume, pacient.anul, pacient.luna, pacient.ziua, pacient.telefon, pacient.cnp, pacient.sex))
        self.conn.commit()

    def introducere_programare_db(self, programare): ## comm out programare.tratament
        self.cursorProgramari.execute('''INSERT INTO programariDB(Interventie, Data, Ora, Prenume, Nume, NotaProgramare) VALUES(?, ?, ?, ?, ?, ?)''', (programare.interventie, str(programare.data), programare.ora.toString('hh:mm'), programare.prenume, programare.nume, programare.notaProgramare))
        self.connProgramari.commit()

    def introducere_docs_db(self, docs):
        self.cursorDocs.execute('''INSERT INTO docsDB(Prenume, Nume, Document) VALUES(?, ?, ?)''', (docs.prenume, docs.nume, docs.document))
        self.connDocs.commit()


    def afisare_tabel_programari(self):
        self.cursorProgramari.execute("SELECT * FROM programariDB")
        rows = self.cursorProgramari.fetchall()

        for row in rows:
            print(row)

    def afisare_tabel_pacienti(self):
        self.cursor.execute("SELECT * FROM pacientiDB")
        rows = self.cursor.fetchall()

        for row in rows:
            print(row)
    
    def afisare_tabel_docs(self):
        self.cursorDocs.execute("SELECT * FROM docsDB")
        rows = self.cursorDocs.fetchall()

        for row in rows:
            print(row)

    def cautare_prenume_pacient_DB(self, preumeCautat):
        self.cursor.execute("SELECT * FROM pacientiDB WHERE prenume=?", (preumeCautat,))
        rows = self.cursor.fetchall()

        for row in rows:
            print(row)

    def cautare_PDF_pacient(self, numeCautat):
        #self.cursor.execute("SELECT PDF FROM programariDB WHERE Nume_Pacient=?", (numeCautat,))
        self.cursorProgramari.execute("SELECT PDF FROM programariDB WHERE Nume_Pacient=?", (numeCautat,))
        rows = self.cursorProgramari.fetchall()
        #print(rows[0])

        #return rows[rows.__len__() - 1] ## returneaza ultimul pdf incarcat
        return rows

    def CheckExistentaPacientInDB(self, prenumePacient, numePacient):
        self.cursor.execute("SELECT * FROM pacientiDB WHERE prenume=?", (prenumePacient,))
        flagPrenume = self.cursor.fetchall()

        self.cursor.execute("SELECT * FROM pacientiDB WHERE nume=?", (numePacient,))
        flagNume = self.cursor.fetchall()

        if flagPrenume.__len__() > 0 and flagNume.__len__() > 0:
            print('In baza de date acest pacient exista.')
            return True
        else:
            print('Pacient Nou')
            return False

    def CheckExistentaDocumentInDB(self, document):
        self.cursorDocs.execute("SELECT * FROM docsDB WHERE Document=?", (document,))
        flagDocumente = self.cursorDocs.fetchall()

        if flagDocumente.__len__() > 0:
            print('In baza de date acest document exista.')
            return True
        else:
            print('Document nou')
            return False


    def cautare_nume_pacient_DB(self, numeCautat):
        self.cursor.execute("SELECT * FROM pacientiDB WHERE prenume=?", (numeCautat,))
        rows = self.cursor.fetchall()

        for row in rows:
            print(row)

    def close_DB(self):
        self.cursor.close()
        self.conn.close()

        self.cursorProgramari.close()
        self.connProgramari.close()

    def afisare_pacienti_in_lista(self, widget):

        conn = sqlite3.connect('pacienti.db')
        #connProgramari = sqlite3.connect('programari.db')
        
        cursor = conn.cursor()
        self.cursor = cursor
        self.cursor.execute("SELECT Nume,Prenume FROM pacientiDB")
        rows = self.cursor.fetchall()

        for row in rows:
            print(row[0] + row[1])
            widget.addItem(row[1] + ' ' + row[0])

    def afisare_pacienti_in_lista_dupa_nume(self, listWidget, numeCautat):

        conn = sqlite3.connect('pacienti.db')
        #connProgramari = sqlite3.connect('programari.db')
        
        cursor = conn.cursor()
        self.cursor = cursor
        self.cursor.execute("SELECT Nume, Prenume FROM pacientiDB")
        rows = self.cursor.fetchall()

        listWidget.clear()
        numeCautat = numeCautat.lower()

        for row in rows:
            nume = row[0].lower()
            prenume = row[1].lower()
            if nume.startswith(numeCautat) or prenume.startswith(numeCautat):
                
                listWidget.addItem(row[1] + ' ' + row[0])             

    def CheckAndAddToListCurrentAppointment(self, listWidget, currentSelection):
        conn = sqlite3.connect('programari.db')
            #connProgramari = sqlite3.connect('programari.db')
            
        cursor = conn.cursor()
        self.cursor = cursor
        self.cursor.execute("SELECT * FROM programariDB")
        rows = self.cursor.fetchall()

        listWidget.clear()

        listOfAppoints = []
        for row in rows:
            if row[2] == currentSelection.isoformat():
                print('Adauga')
                numeP = str(row[4] + ' '  + row [5] + ' \n' + row[3] + '\n')
                listOfAppoints.append((numeP, datetime.datetime.strptime(row[3], '%H:%M')))
                   
        listOfAppoints.sort(key=operator.itemgetter(1))
        for appoint in range(listOfAppoints.__len__()):
            listWidget.addItem(listOfAppoints[appoint][0])
        
        return listWidget

    def UpdateListWithDocuments(self, listWidget, numePacient):
        conn = sqlite3.connect('docs.db')
            
        cursor = conn.cursor()
        self.cursor = cursor

        prenume =  numePacient.split(' ')[0]
        nume = numePacient.split(' ')[1]
        
        self.cursor.execute("SELECT * FROM docsDB WHERE prenume=? AND nume=?",  (prenume, nume))
        rows = self.cursor.fetchall()

        listWidget.clear()

        for row in rows:
            path, fileName = os.path.split(row[3])
            listWidget.addItem(fileName)
            print(listWidget.count())
        return listWidget

    def UpdateTable(self, tableWidget, numePacient):
        conn = sqlite3.connect('programari.db')     
        cursor = conn.cursor()
        self.cursor = cursor

        prenume =  numePacient.split(' ')[0]
        nume = numePacient.split(' ')[1]
        
        self.cursor.execute("SELECT * FROM programariDB WHERE prenume=? AND nume=?",  (prenume, nume))
        rows = self.cursor.fetchall()

        tableWidget.clear()
        numarProgramari = rows.__len__()
        
        
        # set row count
        tableWidget.setRowCount(numarProgramari)
        # set column count
        tableWidget.setColumnCount(4)

        tableWidget.setHorizontalHeaderItem(0, QTableWidgetItem("Data"))
        tableWidget.setHorizontalHeaderItem(1, QTableWidgetItem("Ora"))
        tableWidget.setHorizontalHeaderItem(2, QTableWidgetItem("Interventie"))
        tableWidget.setHorizontalHeaderItem(3, QTableWidgetItem("Nota Programare"))
        

        index = 0

        for row in rows:
            if(index < numarProgramari):
                tableWidget.setItem(index,0, QTableWidgetItem(row[2]))
                tableWidget.setItem(index,1, QTableWidgetItem(row[3]))
                tableWidget.setItem(index,2, QTableWidgetItem(row[1]))
                
                #daca contine si notaProgramare, afiseaza
                if (row.__len__() == 7):
                    tableWidget.setItem(index,3, QTableWidgetItem(row[6]))
                else:
                    tableWidget.setItem(index,3, QTableWidgetItem())

            index = index + 1
            
        return tableWidget

def IndexProgramare(self, infoPacient):
    #infoPacient - este rezultatul apelarii functiei InfoPacient
    for row in infoPacient:
            return (row[0])

def InfoPacient(self, prenumePacient, numePacient):
    conn = sqlite3.connect('pacienti.db')
            #connProgramari = sqlite3.connect('programari.db')
            
    cursor = conn.cursor()
    self.cursor = cursor
    
    self.cursor.execute("SELECT * FROM pacientiDB WHERE prenume=? AND nume=?",  (prenumePacient, numePacient))
    
    rows = self.cursor.fetchall()
    return rows

def InfoProgramare(self, prenumePacient, numePacient, dataProgramare, oraProgramare):
    conn = sqlite3.connect('programari.db')
            #connProgramari = sqlite3.connect('programari.db')
            
    cursor = conn.cursor()
    self.cursor = cursor
    data = dataProgramare.toString("yyyy-MM-dd")
    self.cursor.execute("SELECT * FROM programariDB WHERE prenume=? AND nume=? AND data=? AND ora=?",  (prenumePacient, numePacient, data, oraProgramare))
    
    rows = self.cursor.fetchall()
    return rows

def afisareInfoPacient(self, numePacient):
        conn = sqlite3.connect('pacienti.db')
            
        cursor = conn.cursor()
        self.cursor = cursor
        
        prenume =  numePacient.split(' ')[0]
        nume = numePacient.split(' ')[1]
    
        self.cursor.execute("SELECT * FROM pacientiDB WHERE prenume=? AND nume=?",  (prenume, nume))
        
        rows = self.cursor.fetchall()

        for row in rows:
            _translate = QtCore.QCoreApplication.translate
            self.label_15.setText(_translate("Form", row[1]))
            self.label_3.setText(_translate("Form", row[2]))
            dataNasterii = row[5]  +  '/'  +  row[4] +  '/'  +  row[3]
            self.label_14.setText(_translate("Form", dataNasterii))
            self.label_13.setText(_translate("Form", row[6]))
            self.label_12.setText(_translate("Form", row[7]))
            
            self.label_11.setText(_translate("Form", row[8]))

def updateNotaProgramareDB(self, Programare):
    # Update notaProgramare
    sql = ''' UPDATE programariDB
              SET Interventie = ? ,
                  Data = ? ,
                  Ora = ?,
                  Prenume = ?,
                  Nume = ?,
                  NotaProgramare = ?
              WHERE prenume=? AND nume=? AND data =? AND ora=?'''
    
    conn = sqlite3.connect('programari.db')    
    cursor = conn.cursor()
    self.cursor = cursor
    Programare = (
                Programare.interventie, 
                Programare.data, 
                Programare.ora, 
                Programare.prenume, 
                Programare.nume, 
                Programare.notaProgramare, 
                Programare.prenume,
                Programare.nume,
                Programare.data,
                Programare.ora
                )

    self.cursor.execute(sql, Programare)
    conn.commit()

def AdaugaDocumentInDB(Document):
    DocumentDB = BazaDate()
    DocumentDB.create_table()

    # verifica daca exista acelasi document in baza de date
    existaDcument = DocumentDB.CheckExistentaDocumentInDB(Document.document)

    #Introducere in baza de date
    if existaDcument:
        print('Documentul nu a fost introdus.')
    else:
        DocumentDB.introducere_docs_db(Document)

    DocumentDB.close_DB()

def AdaugarePacientDB(self, Pacient):
    PacientDB = BazaDate()
    PacientDB.create_table()

    # verificare daca exista pacient cu acelasi nume in DB
    existaPacient = PacientDB.CheckExistentaPacientInDB(Pacient.prenume, Pacient.nume)

    #Introducere in baza de date
    if existaPacient:
        print('Pacientul nu a fost introdus.')
    else:
        PacientDB.introducere_pacient_db(Pacient)

    PacientDB.close_DB()

def AdaugareProgramareDB(Programare):
    ProgramareDB = BazaDate()
    ProgramareDB.create_table()
    ProgramareDB.introducere_programare_db(Programare)
    ProgramareDB.close_DB()

def CheckAndAddToListCurrentAppointment(self, listWidget, currentSelection):
    conn = sqlite3.connect('programari.db')
        #connProgramari = sqlite3.connect('programari.db')
        
    cursor = conn.cursor()
    self.cursor = cursor
    self.cursor.execute("SELECT Data FROM programariDB")
    rows = self.cursor.fetchall()

    listWidget.clear()

    for row in rows:
        if row[0].startswith(numeCautat):
            self.cursor.execute("SELECT Prenume FROM pacientiDB WHERE Nume=?", (row[0],))
            prenume = self.cursor.fetchall()
            print(row[0], prenume[0][0])
            listWidget.addItem(row[0] + ' ' + prenume[0][0]) 

def UpdatePacientiProgramari(self, Pacient, Programare, indexPacient, indexProgramare):
    # Update lista Pacienti 
    sql = ''' UPDATE pacientiDB
              SET Prenume = ? ,
                  Nume = ? ,
                  Anul = ?,
                  Luna = ?,
                  Ziua = ?,
                  Telefon = ?,
                  CNP = ?,
                  Sex = ?
              WHERE id = ?'''
    
    conn = sqlite3.connect('pacienti.db')    
    cursor = conn.cursor()
    self.cursor = cursor
    Pacient = (
                Pacient.prenume, 
                Pacient.nume, 
                Pacient.anul, 
                Pacient.luna, 
                Pacient.ziua, 
                Pacient.telefon, 
                Pacient.cnp, 
                Pacient.sex,
                indexPacient
                )

    self.cursor.execute(sql, Pacient)
    conn.commit()

    # Update lista Programari
    sql2 = ''' UPDATE programariDB
              SET Interventie = ? ,
                  Data = ? ,
                  Ora = ?,
                  Prenume = ?,
                  Nume = ?
              WHERE id = ?'''
    
    connProgramari = sqlite3.connect('programari.db')    
    cursor2 = connProgramari.cursor()
    self.cursor2 = cursor2
    Programare = (
                Programare.interventie, 
                Programare.data.toString("yyyy-MM-dd"), 
                Programare.ora.toString("hh:mm"), 
                Programare.prenume, 
                Programare.nume, 
                indexProgramare
                )

    self.cursor2.execute(sql2, Programare)
    connProgramari.commit()

def StergePacient(self, indexPacient):
    sql = 'DELETE FROM pacientiDB WHERE id=?'
    conn = sqlite3.connect('pacienti.db')    
    cursor = conn.cursor()
    self.cursor = cursor
    self.cursor.execute(sql, (indexPacient,))
    conn.commit()

def StergeDocument(self, indexDocument):
    sql = 'DELETE FROM docsDB WHERE id=?'
    conn = sqlite3.connect('docs.db')    
    cursor = conn.cursor()
    self.cursor = cursor
    self.cursor.execute(sql, (indexDocument,))
    conn.commit()

def StergeProgramare(self, indexProgramare):
    sql = 'DELETE FROM programariDB WHERE id=?'
    conn = sqlite3.connect('programari.db')    
    cursor = conn.cursor()
    self.cursor = cursor
    self.cursor.execute(sql, (indexProgramare,))
    conn.commit()

def VerificaExistentaProgramare(self, data, ora):
    conn = sqlite3.connect('programari.db')            
    cursor = conn.cursor()
    self.cursor = cursor
    ora = ora.toString('hh:mm')
    data = data.toString("yyyy-MM-dd")

    self.cursor.execute("SELECT * FROM programariDB WHERE data=? AND ora=?",  (data, ora))
    rows = self.cursor.fetchall()

    return rows.__len__()

def GetInterventieProgramare(self, nume, prenume, data, ora):
    conn = sqlite3.connect('programari.db')            
    cursor = conn.cursor()
    self.cursor = cursor
    data = data.toString("yyyy-MM-dd")

    self.cursor.execute("SELECT * FROM programariDB WHERE prenume=? AND nume=? AND data=? AND ora=?",  (prenume, nume, data, ora))
    rows = self.cursor.fetchall()

    for row in rows:
        return row[1]

def GetAppiontmentsFromDB(self):
        conn = sqlite3.connect('programari.db')
            
        cursor = conn.cursor()
        self.cursor = cursor
        today = datetime.date.today()
        #date = str(today.year) + "-" + str(today.month) + "-" + str(today.day - 1)
        
        self.cursor.execute("SELECT * FROM programariDB")
        rows = self.cursor.fetchall()
        appointmentsList = []

        for row in rows:
            data_list = row[2].split('-')
            an = data_list[0]
            luna = data_list[1]
            zi = data_list[2]

            dbCurrentDate = datetime.date(int(an), int(luna), int(zi))

            test = []
            test.append((today, 5))
            if( dbCurrentDate >= today):
                appointmentsList.append(row[2])
        
        x = Counter(appointmentsList)
        
        # (date, data structure that contains date and how many occurance does that date have)
        return appointmentsList, x

    