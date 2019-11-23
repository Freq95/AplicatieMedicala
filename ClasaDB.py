## TO-DO:     1. Gandeste alta structura de tabele(ex: 2 tabele relationate ... fiecare pacient are mai multe inregistrari)
##            2. Adauga campuri unice
import sqlite3
import ClasaPacienti
import ClasaDocuments

import datetime

# conn = sqlite3.connect('pacienti.db')
# c = conn.cursor()

# prenume, nume, anul, luna, ziua, telefon, cnp,  sex
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
                                      FOREIGN KEY(Nume) REFERENCES pacientiDB(ID))')

        #self.cursorProgramari.execute('CREATE TABLE IF NOT EXISTS programariDB\
        #                              (ID INTEGER PRIMARY KEY AUTOINCREMENT,\
        #                              Tratament TEXT,\
        #                              PDF TEXT,\
        #                              Radiografie TEXT,\
        #                              Nume_Pacient TEXT NOT NULL,\
        #                              FOREIGN KEY(Nume_Pacient) REFERENCES pacientiDB(ID))')

        self.cursorDocs.execute('CREATE TABLE IF NOT EXISTS docsDB\
                                      (ID INTEGER PRIMARY KEY AUTOINCREMENT,\
                                      Prenume TEXT,\
                                      Nume TEXT,\
                                      Document TEXT,\
                                      FOREIGN KEY(Nume) REFERENCES pacientiDB(ID))')


    def introducere_pacient_db(self, pacient):
        self.cursor.execute('''INSERT INTO pacientiDB(Prenume, Nume, Anul, Luna, Ziua, Telefon, CNP, Sex) VALUES(?, ?, ?, ?, ?, ?, ?, ?)''', (pacient.prenume, pacient.nume, pacient.anul, pacient.luna, pacient.ziua, pacient.telefon, pacient.cnp, pacient.sex))
        self.conn.commit()

    def introducere_programare_db(self, programare): ## comm out programare.tratament
        self.cursorProgramari.execute('''INSERT INTO programariDB(Interventie, Data, Ora, Prenume, Nume) VALUES(?, ?, ?, ?, ?)''', (programare.interventie, str(programare.data), programare.ora.toString(), programare.prenume, programare.nume))
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
            widget.addItem(row[0] + ' ' + row[1])

    def afisare_pacienti_in_lista_dupa_nume(self, listWidget, numeCautat):

        conn = sqlite3.connect('pacienti.db')
        #connProgramari = sqlite3.connect('programari.db')
        
        cursor = conn.cursor()
        self.cursor = cursor
        self.cursor.execute("SELECT Nume FROM pacientiDB")
        rows = self.cursor.fetchall()

        listWidget.clear()

        for row in rows:
            if row[0].startswith(numeCautat):
                self.cursor.execute("SELECT Prenume FROM pacientiDB WHERE Nume=?", (row[0],))
                prenume = self.cursor.fetchall()
                print(row[0], prenume[0][0])
                listWidget.addItem(row[0] + ' ' + prenume[0][0]) 

    def CheckAndAddToListCurrentAppointment(self, listWidget, currentSelection):
        conn = sqlite3.connect('programari.db')
            #connProgramari = sqlite3.connect('programari.db')
            
        cursor = conn.cursor()
        self.cursor = cursor
        self.cursor.execute("SELECT * FROM programariDB")
        rows = self.cursor.fetchall()

        listWidget.clear()

        for row in rows:
            if row[2] == currentSelection.isoformat():
                #self.cursor.execute("SELECT Prenume FROM pacientiDB WHERE Nume=?", (row[0],))
                #prenume = self.cursor.fetchall()
                #print(row[0], prenume[0][0])
                #listWidget.addItem(row[0] + ' ' + prenume[0][0]) 
                print('Adauga')
                #listWidget.addItem(row[4] + row [5] + ' : ' + '\n' + row[3])
                listWidget.addItem(row[4] + row [5] + ' - ' + row[3])
            






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
