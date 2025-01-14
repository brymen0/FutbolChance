class Apuesta:
    def __init__(self, eventosDeportivos, monto, valorCuota, eleccion):
        self.eventosDeportivos = eventosDeportivos
        self.eleccion = eleccion
        self.montoApostado = monto
        self.valorCuota = valorCuota
        self.ganacia = monto*valorCuota
        self.estado = "En juego"