## TO-DO: introdu calendar ca si intrare pentru a putea selecta ziua in care a venit

class Pacient:
    def __init__ (self, prenume, nume, anul, luna, ziua, telefon, cnp,  sex):
        self.prenume = prenume
        self.nume = nume
        self.anul = anul
        self.luna = luna
        self.ziua = ziua
        self.telefon = telefon
        self.cnp = cnp
        self.sex = sex

    def setNume(self, noulNume):
        self.nume = noulNume

    def getNume(self):
        return self.nume


