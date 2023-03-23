import pickle

from modules.islaidu_irasas import IslaiduIrasas
from modules.pajamu_irasas import PajamuIrasas


class Biudzetas:
    def __init__(self):
        self.zurnalas = self._gauti_zurnala()

    def _gauti_zurnala(self):
        try:
            with open("zurnalas.pkl", "rb") as file:
                zurnalas = pickle.load(file)
        except:
            with open("zurnalas.pkl", "wb") as file:
                zurnalas = []
        return zurnalas

    def _irasyti_zurnala(self):
        with open("zurnalas.pkl", "wb") as file:
            pickle.dump(self.zurnalas, file)

    def prideti_pajamu_irasa(self, suma, siuntejas, pap_informacija):

        irasas = PajamuIrasas(suma, siuntejas, pap_informacija)
        self.zurnalas.append(irasas)
        self._irasyti_zurnala()

    def prideti_islaidu_irasa(self, suma, atsiskaitymo_budas, isigyta_preke_paslauga):
        irasas = IslaiduIrasas(suma, atsiskaitymo_budas, isigyta_preke_paslauga)
        self.zurnalas.append(irasas)
        self._irasyti_zurnala()

    def gauti_balansa(self):
        suma1 = 0
        suma2 = 0
        for i in self.zurnalas:
            if isinstance(i, PajamuIrasas):
                suma1 += i.suma
            if isinstance(i, IslaiduIrasas):
                suma2 += i.suma

        balansas = suma1 - suma2
        print('%s' % (97 * '-'))
        print('|%s|%s|%s|%s|%s|%s|' % ("Pajamos:".ljust(10), str(suma1).center(20), "Islaidos:".ljust(10),
                                       str(suma2).center(20), "Balansas:".ljust(10), str(balansas).center(20)))
        print('%s' % (97 * '-'))

    def parodyti_ataskaita(self):
        sum = 0
        for i in self.zurnalas:
            sum += 1
            if isinstance(i, PajamuIrasas):
                print('%s' % (129 * '-'))
                print("|%s|%s|%s|%s|" % ("Pajamos:".ljust(12), str(i.suma).center(12), i.siuntejas.ljust(40),
                                         i.pap_informacija.ljust(60)))
                print('%s' % (129 * '-'))
            if isinstance(i, IslaiduIrasas):
                print('%s' % (129 * '-'))
                print("|%s|%s|%s|%s|" % ("Islaidos:".ljust(12), str(i.suma).center(12), i.atsiskaitymo_budas.ljust(40),
                                         i.isigyta_preke_paslauga.ljust(60)))
                print('%s' % (129 * '-'))
