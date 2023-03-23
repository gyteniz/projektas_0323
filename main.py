from modules.biudzetas import Biudzetas


biudzetas = Biudzetas()
# biudzetas.prideti_pajamu_irasa(1000, "Pukuotukas", "uz grazias akis")

#
while True:
    pasirinkimas = int(input(
        "Pasirinkite:\t\n1 - prideti pajamu/islaidu irasa\n2 - gauti balansa\n3 - parodyti pajamu/islaidu ataskaita\n4 - iseiti is programos\n"))
    if pasirinkimas == 1:
        while True:
            alternatyva1 = int(input("Ka norite ivesti:\t\n1 - ivesti pajamas\n2 - ivesti islaidas\n3 - iseiti\n"))
            if alternatyva1 == 1:
                suma = int(input("Ivedame pajamas:\t"))
                siuntejas = input("Iveskite siunteja:\t")
                pap_informacija = input("Iveskite papildoma informacija:\t")
                biudzetas.prideti_pajamu_irasa(suma, siuntejas, pap_informacija)
            if alternatyva1 == 2:
                suma = int(input("Iveskite islaidas:\t"))
                atsiskaitymo_budas = input("Atsiskaitymo budas:\t")
                isigyta_preke_paslauga = input("Isigyta preke/paslauga:\t")
                biudzetas.prideti_islaidu_irasa(suma, atsiskaitymo_budas, isigyta_preke_paslauga)
            if alternatyva1 == 3:
                break

    if pasirinkimas == 2:
        biudzetas.gauti_balansa()
    if pasirinkimas == 3:
        biudzetas.parodyti_ataskaita()
    if pasirinkimas == 4:
        break
biudzetas.gauti_balansa()
biudzetas.parodyti_ataskaita()
