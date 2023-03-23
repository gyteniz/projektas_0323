from modules.irasas import Irasas


class PajamuIrasas(Irasas):
    def __init__(self, suma, siuntejas, pap_informacija):
        super().__init__(suma)
        self.siuntejas = siuntejas
        self.pap_informacija = pap_informacija
