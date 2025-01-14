import pickle
from src.model.Apuesta.Apuesta import Apuesta
class ManejoApuestas:
    def __init__(self):
        self.apuestas = []
        self.cargarApuestas()

    def guardarApuestas(self):
        with open('apuestas.dat','wb') as f:
            pickle.dump(self.apuestas,f,pickle.HIGHEST_PROTOCOL)

    def cargarApuestas(self):
        try:
            with open('apuestas.dat','rb') as f:
                self.apuestas = pickle.load(f)
        except FileNotFoundError: print("No existe el archivo, se creará uno")
        except EOFError: print("Archivo vacio")

    def crearApuesta(self, eventoDeportivo, monto, valorCuota, eleccion):
        self.apuestas.append(Apuesta(eventoDeportivo,monto,valorCuota, eleccion))
        self.guardarApuestas()
