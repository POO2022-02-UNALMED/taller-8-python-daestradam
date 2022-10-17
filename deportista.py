class Deportista():
    def __init__(self, deporte, añosPraticando):
        self._deporte=deporte
        self._añosPraticando=añosPraticando

    def getDeporte(self):
        return self._deporte
    def setDeporte(self, deporte):
        self._deporte=deporte
    def getAñosPraticando(self):
        return self._añosPraticando
    def setAñosPraticando(self, añosPraticando):
        self._añosPraticando=añosPraticando