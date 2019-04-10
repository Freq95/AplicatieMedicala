## TO-DO:   1. Gandeste alta structura de tabele(ex: 2 tabele relationate ... fiecare pacient are mai multe inregistrari)
##            2. Adauga campuri unice
import sqlite3
import ClasaPacienti

# conn = sqlite3.connect('pacienti.db')
# c = conn.cursor()


class BazaDate(ClasaPacienti.Pacient):
    def __init__(self):
        conn = sqlite3.connect('pacienti.db')
        connProgramari = sqlite3.connect('programari.db')

        cursor = conn.cursor()
        cursorProgramari = connProgramari.cursor()

        self.connProgramari = connProgramari
        self.cursorProgramari = cursorProgramari

        self.conn = conn
        self.cursor = cursor

    def create_table(self):
        self.cursor.execute('CREATE TABLE IF NOT EXISTS pacientiDB\
        (ID INTEGER PRIMARY KEY AUTOINCREMENT,\
        Prenume TEXT NOT NULL,\
        Nume TEXT NOT NULL,\
        Varsta TEXT,\
        Sex TEXT)')

        self.cursorProgramari.execute('CREATE TABLE IF NOT EXISTS programariDB\
                                      (ID INTEGER PRIMARY KEY AUTOINCREMENT,\
                                      Tratament TEXT,\
                                      PDF TEXT,\
                                      Radiografie TEXT,\
                                      Nume_Pacient TEXT NOT NULL,\
                                      FOREIGN KEY(Nume_Pacient) REFERENCES pacientiDB(ID))')


    def introducere_pacient_db(self, pacient):
        self.cursor.execute('''INSERT INTO pacientiDB(Prenume, Nume, Varsta, Sex) VALUES(?, ?, ?, ?)''', (pacient.prenume, pacient.nume, pacient.varsta, pacient.sex))
        self.conn.commit()

    def introducere_programare_db(self, programare): ## comm out programare.tratament
        self.cursorProgramari.execute('''INSERT INTO programariDB(Tratament, PDF, Radiografie, Nume_Pacient) VALUES(?, ?, ?, ?)''', (programare.tratament, programare.pdf, programare.radiografie, programare.numePacient))
        self.connProgramari.commit()

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

    def cautare_prenume_pacient_DB(self, preumeCautat):
        self.cursor.execute("SELECT * FROM pacientiDB WHERE prenume=?", (preumeCautat,))
        rows = self.cursor.fetchall()

        for row in rows:
            print(row)

    def CheckExistentaPacientInDB(self, prenumePacient, numePacient):
        self.cursor.execute("SELECT * FROM pacientiDB WHERE prenume=?", (prenumePacient,))
        flagPrenume = self.cursor.fetchall()

        self.cursor.execute("SELECT * FROM pacientiDB WHERE nume=?", (numePacient,))
        flagNume = self.cursor.fetchall()

        if flagPrenume.__len__() > 0 and flagNume.__len__() > 0:
            print('In baza de date acest pacient exista')
            return True
        else:
            print('Pacient Nou')
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