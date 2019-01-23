## TO-DO: introdu calendar ca si intrare pentru a putea selecta ziua in care a venit

class Pacient:
    def __init__ (self, prenume, nume, varsta, sex):
        self.prenume = prenume
        self.nume = nume
        self.varsta = varsta
        self.sex = sex

    def setNume(self, noulNume):
        self.nume = noulNume

    def getNume(self):
        return self.nume


