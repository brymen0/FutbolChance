import pickle


class ManejoCuotas:
    def __init__(self):
        self.cuotas = []
        self.cargarCuotas()

    def guardarCuotas(self):
        with open('../data/cuotas.dat', 'wb') as f:
            pickle.dump(self.eventos, f, pickle.HIGHEST_PROTOCOL)

    def cargarCuotas(self):
        try:
            with open('../data/cuotas.dat', 'rb') as f:
                self.eventos = pickle.load(f)
                #return self.eventos
        except FileNotFoundError: print("No existe el archivo cuotas, se creará uno")
        except EOFError: print("Archivo vacío")
        #return self.eventos



