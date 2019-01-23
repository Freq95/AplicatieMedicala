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
                                      PDF BLOB,\
                                      Radiografie BLOB,\
                                      Pacient_id INTEGER NOT NULL,\
                                      FOREIGN KEY(Pacient_id) REFERENCES pacientiDB(ID))')


    def introducere_pacient_db(self, pacient):
        self.cursor.execute('''INSERT INTO pacientiDB(Prenume, Nume, Varsta, Sex) VALUES(?, ?, ?, ?)''', (pacient.prenume, pacient.nume, pacient.varsta, pacient.sex))
        self.conn.commit()

    def introducere_programare_db(self, programare): ## comm out programare.tratament
        self.cursorProgramari.execute('''INSERT INTO programariDB(PDF, Radiografie, Pacient_id) VALUES(?, ?, ?)''', (programare.pdf, programare.radiografie, programare.id_pacient))
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

    def cautare_pacient_DB(self, NumeCautat):
        self.cursor.execute("SELECT * FROM pacientiDB WHERE prenume=?", (NumeCautat,))
        rows = self.cursor.fetchall()

        for row in rows:
            print(row)

    def close_DB(self):
        self.cursor.close()
        self.conn.close()

        self.cursorProgramari.close()
        self.connProgramari.close()








