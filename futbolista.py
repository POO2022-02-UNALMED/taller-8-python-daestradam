from deportista import Deportista
from persona import Persona

class Futbolista(Persona, Deportista):
    _listaFutbolistas=[]
    def __init__(self, nombre, edad, altura, sexo, añosPracticando, golesMarcados, tarjetasRojas, piernaHabil):
        Persona.__init__(self, nombre, edad, altura, sexo)
        Deportista.__init__(self, "Futbol", añosPracticando)
        self._golesMarcados=golesMarcados
        self._tarjetasRojas=tarjetasRojas
        self._piernaHabil=piernaHabil
        self._listaFutbolistas.append(self)

    def getGolesMarcados(self):
        return self._golesMarcados
    def setGolesMarcados(self, golesMarcados):
        self._golesMarcados=golesMarcados
    def getTarjetasRojas(self):
        return self._tarjetasRojas
    def setTarjetasRojas(self, tarjetasRojas):
        self._tarjetasRojas=tarjetasRojas
    def getPiernaHabil(self):
        return self._piernaHabil
    def setPiernaHabil(self, piernaHabil):
        self._piernaHabil=piernaHabil

    def __str__(self):
        return "Mi nombre es "+Persona.nombre+" soy profesional en el deporte "+Deportista.deporte+" Tengo "+Persona.edad+" años de edad y llevo "+Deportista.añosParticipando+" años en el deporte"