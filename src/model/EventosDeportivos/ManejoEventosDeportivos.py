import pickle
from src.model.EventosDeportivos.EventoDeportivo import EventoDeportivo
from src.model.Cuotas.Cuota import Cuota

class ManejoEventosDeportivos:
    def __init__(self):
        cuotas = [Cuota("Ganar",[2.86,3.50,2.86]),Cuota("Ganar",[2.25,2.90,3.00]),Cuota("Ganar",[1.75,4.00,6.00]),Cuota("Ganar",[2.50,2.00,3.00]),
                  Cuota("Ganar",[1.25,4.50,8.00])]
        self.eventos = [
            EventoDeportivo("Fútbol", "España", "La Liga", "FC Barcelona", "Real Madrid", "Jornada 20","14/01/2025","14:00",cuotas[0]),
            EventoDeportivo("Fútbol", "Internacional", "Champions League", "Inter Milan", "PSG", "Cuartos de Final - Ida","15/01/2025","20:00",cuotas[1]),
            EventoDeportivo("Fútbol", "España", "La Liga", "Atletico de Madrid", "Sevilla", "Jornada 20","15/01/2025","21:00",cuotas[2]),
            EventoDeportivo("Fútbol", "Inglaterra", "Premier League", "Liverpool", "Manchester City", "Jornada 25","16/01/2025","22:00",cuotas[3]),
            EventoDeportivo("Fútbol", "Alemania", "Bundesliga", "Bayern Munich", "Ausburgo", "Jornada 17","17/01/2025","14:00",cuotas[4])
        ]
        self.cargarEventos()

    def guardarEventos(self):
        with open('.../data/eventosDeportivos.dat', 'wb') as f:
            pickle.dump(self.eventos, f, pickle.HIGHEST_PROTOCOL)

    def cargarEventos(self):
        try:
            with open('.../data/eventosDeportivos.dat', 'rb') as f:
                self.eventos = pickle.load(f)
                #return self.eventos
        except FileNotFoundError: print("No existe el archivo eventosDeportivos, se creará uno")
        except EOFError: print("Archivo vacío")
        #return self.eventos

'''
if __name__ == "__main__":
    cuotas = [Cuota("Ganar",[2.86,3.50,2.86]),Cuota("Ganar",[2.25,2.90,3.00]),Cuota("Ganar",[1.75,4.00,6.00]),Cuota("Ganar",[2.50,2.00,3.00]),
              Cuota("Ganar",[1.25,4.50,8.00])]
    eventos = [
        EventoDeportivo("Fútbol", "España", "La Liga", "FC Barcelona", "Real Madrid", "Jornada 20","14/01/2025","14:00",cuotas[0]),
        EventoDeportivo("Fútbol", "Internacional", "Champions League", "Inter Milan", "PSG", "Cuartos de Final - Ida","15/01/2025","20:00",cuotas[1]),
        EventoDeportivo("Fútbol", "España", "La Liga", "Atletico de Madrid", "Sevilla", "Jornada 20","15/01/2025","21:00",cuotas[2]),
        EventoDeportivo("Fútbol", "Inglaterra", "Premier League", "Liverpool", "Manchester City", "Jornada 25","16/01/2025","22:00",cuotas[3]),
        EventoDeportivo("Fútbol", "Alemania", "Bundesliga", "Bayern Munich", "Ausburgo", "Jornada 17","17/01/2025","14:00",cuotas[4])
    ]

    manejp = ManejoEventosDeportivos()
    manejp.guardarEventos()  # Guardamos los eventos en el archivo
    manejp.cargarEventos()
    eventos_cargados = manejp.eventos
    for evento in eventos_cargados:
        print(evento.liga)

'''

