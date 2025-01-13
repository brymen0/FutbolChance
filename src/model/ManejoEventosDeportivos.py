import pickle
from src.model.EventoDeportivo import EventoDeportivo

class ManejoEventosDeportivos:
    def __init__(self):
        self.eventos = []
        self.cargarEventos()

    def guardarEventos(self):
        with open('eventosDeportivos.dat', 'wb') as f:
            pickle.dump(self.eventos, f, pickle.HIGHEST_PROTOCOL)

    def cargarEventos(self):
        try:
            with open('eventosDeportivos.dat', 'rb') as f:
                self.eventos = pickle.load(f)
                #return self.eventos
        except FileNotFoundError: print("No existe el archivo eventosDeportivos, se creará uno")
        except EOFError: print("Archivo vacío")
        #return self.eventos

'''
if __name__ == "__main__":
    eventos = [
        EventoDeportivo("Fútbol", "España", "La Liga", "FC Barcelona", "Real Madrid", "Jornada 20"),
        EventoDeportivo("Fútbol", "Internacional", "Champions League", "Inter Milan", "PSG", "Cuartos de Final - Ida"),
        EventoDeportivo("Fútbol", "España", "La Liga", "Atletico de Madrid", "Sevilla", "Jornada 20"),
        EventoDeportivo("Fútbol", "Inglaterra", "Premier League", "Liverpool", "Manchester City", "Jornada 25"),
        EventoDeportivo("Fútbol", "Alemania", "Bundesliga", "Bayern Munich", "Ausburgo", "Jornada 17")
    ]

    manejp = ManejoEventosDeportivos()
    manejp.eventos = eventos  # Asignamos los eventos a la lista `self.eventos`
    manejp.guardarEventos()  # Guardamos los eventos en el archivo
    eventos_cargados = manejp.cargarEventos()  # Cargamos los eventos desde el archivo
    for evento in eventos_cargados:
        print(evento.deporte)

'''