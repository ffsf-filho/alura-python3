class Data:
    def __init__(self, dd = "01", mm = "01", yyyy = "1900"):
        self.dia = dd;
        self.mes = mm
        self.ano = yyyy

    def formatada(self):
        print(f"{self.dia}/{self.mes}/{self.ano}")