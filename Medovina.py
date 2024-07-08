class Medovina():
    SUL = 0.3
    KVASINKY = 0.2

    def __init__(self, pozadovany_objem=10, sladkost=1):
        self.pozadovany_objem = pozadovany_objem
        self.sladkost = sladkost

    def kvas(self):
        return f"120g medu povařit 5-10 min v 1l vody."

    def recept(self):
        if self.pozadovany_objem>1 and self.sladkost == 1:
            med = (20.7*self.pozadovany_objem)/50
            voda = (35.6*self.pozadovany_objem)/50
            med_bez_kvasu = med - 0.12
            voda_bez_kvasu = voda - 1
            kvasinky = self.KVASINKY * self.pozadovany_objem
            zivna_sul = self.SUL * self.pozadovany_objem
            return f"Med: {round(med_bez_kvasu,1)} kg\nVoda: {round(voda_bez_kvasu,1)} l\nKvasinky: {round(kvasinky,1)} g\nŽivná sůl: {round(zivna_sul,1)} g\n\nPoměr med (kg):voda (l): 1.72\nObsah cukrů (kg/hl): 34\nKontrola moštoměrem (kg/hl): 30"

        elif self.pozadovany_objem>1 and self.sladkost == 2:
            med = (18.3*self.pozadovany_objem)/50
            voda = (37.3*self.pozadovany_objem)/50
            med_bez_kvasu = med - 0.12
            voda_bez_kvasu = voda - 1
            kvasinky = self.KVASINKY * self.pozadovany_objem
            zivna_sul = self.SUL * self.pozadovany_objem
            return f"Med: {round(med_bez_kvasu,1)} kg\nVoda: {round(voda_bez_kvasu,1)} l\nKvasinky: {round(kvasinky,1)} g\nŽivná sůl: {round(zivna_sul,1)} g\n\nPoměr med (kg):voda (l): 2.04\nObsah cukrů (kg/hl): 30\nKontrola moštoměrem (kg/hl): 26"

        elif self.pozadovany_objem>1 and self.sladkost == 3:
            med = (15.8*self.pozadovany_objem)/50
            voda = (39.1*self.pozadovany_objem)/50
            med_bez_kvasu = med - 0.12
            voda_bez_kvasu = voda - 1
            kvasinky = self.KVASINKY * self.pozadovany_objem
            zivna_sul = self.SUL * self.pozadovany_objem
            return f"Med: {round(med_bez_kvasu,1)} kg\nVoda: {round(voda_bez_kvasu,1)} l\nKvasinky: {round(kvasinky,1)} g\nŽivná sůl: {round(zivna_sul,1)} g\n\nPoměr med (kg):voda (l): 2.47\nObsah cukrů (kg/hl): 26\nKontrola moštoměrem (kg/hl): 22"

        elif self.pozadovany_objem>1 and self.sladkost == 4:
            med = (14.6*self.pozadovany_objem)/50
            voda = (39.9*self.pozadovany_objem)/50
            med_bez_kvasu = med - 0.12
            voda_bez_kvasu = voda - 1
            kvasinky = self.KVASINKY * self.pozadovany_objem
            zivna_sul = self.SUL * self.pozadovany_objem
            return f"Med: {round(med_bez_kvasu,1)} kg\nVoda: {round(voda_bez_kvasu,1)} l\nKvasinky: {round(kvasinky,1)} g\nŽivná sůl: {round(zivna_sul,1)} g\n\nPoměr med (kg):voda (l): 2.73\nObsah cukrů (kg/hl): 24\nKontrola moštoměrem (kg/hl): 20"

        else:
            return "Vyberte požadovanou chuť medoviny nebo zvyšte objem.\nMinimální objem kvasné nádoby je 2l."

