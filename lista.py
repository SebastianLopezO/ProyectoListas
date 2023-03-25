from nodo import Nodo
from colores import Colors as Clr


class Lista:
    def __init__(self, Name):
        self.punta = None
        self.cola = None
        self.name = Name
        self.method = "empty"

    # Metodos

    def insert_end(self,dato):
        if self.punta is None:
            X = Nodo(dato)
            X.liga_i = X
            X.liga_d = X
            self.punta = X
            self.cola = X
        else:
            X = Nodo(dato)
            X.liga_i=self.Cola
            X.liga_d=self.punta
            self.punta.liga_i = X
            self.cola.liga_d = X
            self.cola = X

    def show_list_details(self):
        msj = f"{Clr.BG_BL}\n{self.name}: [ "
        P = self.punta
        if self.punta != None:
            while True:
                msj += f"{{ {Clr.BG_G}{P.liga_i}{Clr.BG_BL} | {Clr.BG_Y} {P.dato} {Clr.BG_BL} | {Clr.BG_G}{P.liga_d}{Clr.BG_BL} }}  => "
                P = P.liga_d
                if P == self.punta:
                    break
        msj += " ]\n\n" + Clr.RT
        print(msj)


