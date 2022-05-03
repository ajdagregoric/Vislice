STEVILO_DOVOLJENIH_NAPAK = 10
PRAVILNA_CRKA = '+'
PONOVLJENA_CRKA = 'o'
NAPACNA_CRKA = '-'
ZMAGA = 'W'
PORAZ = 'X'

class Igra:
    def __init__(self, geslo, crke=None):
        self.geslo = geslo.upper()
        if crke is not None:
            self.crke = crke
        else:
            self.crke = []

    def napacne_crke(self):
        return [crka for crka in self.crke if crka not in self.geslo]

    def pravilne_crke(self):
        return [crka for crka in self.crke if crka in self.geslo]
        
    def stevilo_napak(self):
        return len(self.napacne_crke())
    
    def zmaga(self):
        return len(set(self.geslo)) == len(self.pravilne_crke())
    
    def poraz(self):
        return self.stevilo_napak() > STEVILO_DOVOLJENIH_NAPAK

    def pravilni_del_gesla(self):
        niz = ''
        for crka in self.geslo:
            if crka in self.crke:
                niz += crka
            else:
                niz += '_'
        return niz
    
    def nepravilni_ugibi(self):
        return ' '.join(self.napacne_crke())

    def ugibaj(self, crka):

        #najprej preverimo ali je crka ponovljena, ker to stanja ne spremeni
        #ja -> vrnemo PONOVLJENA_CRKA
        #ne -> posodobimo stanje igre
        #       ali smo zmagali? ja -> vrnemo ZMAGA
        #       ali smo izgubili? ja -> vrnemo PORAZ
        #       ali je crka pravilna? ... pravilna
        #       nepravilna
        crka = crka.upper()

        if crka in self.crke:
            return PONOVLJENA_CRKA
        else:
            self.crke.append(crka)
            if self.zmaga():
                return ZMAGA
            elif self.poraz():
                return PORAZ
            elif crka in self.geslo:
                return PRAVILNA_CRKA
            else:
                return NAPACNA_CRKA

bazen_besed = []
with open('besede.txt', encoding='utf8') as d:
    for beseda in d:
        bazen_besed.append(beseda.strip())

import random

def nova_igra():
    geslo = random.choice(bazen_besed)
    return Igra(geslo)