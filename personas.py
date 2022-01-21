##############################################################
from random import randint
from platos import Comestible, Bebestible
## Si necesita agregar imports, debe agregarlos aquí arriba ##

### INICIO PARTE 2.1 ###
class Persona:
    def __init__(self, pNombre):
        self.nombre = pNombre

### FIN PARTE 2.1 ###

### INICIO PARTE 2.2 ###
class Repartidor(Persona):
    def __init__(self, pNombre, tpo_entrega = randint(20,30)):
        super().__init__(pNombre)
        self.tiempo_entrega = tpo_entrega
        self.energia = randint(75,100)

    def repartir(self,pedido):
        if len(pedido)<=2:
            factor_tamano = 5
            factor_velocidad = 1.25
        else:
            factor_tamano = 15
            factor_velocidad = 0.85
        self.energia -= factor_tamano
        #print(f"Reparto: {self.nombre}\n\tTpo: {self.tiempo_entrega}s\tTamño: {factor_tamano}\tVeloc: {factor_velocidad}\tEnerg: {self.energia}")#
        return self.tiempo_entrega*factor_velocidad
    
### FIN PARTE 2.2 ###

### INICIO PARTE 2.3 ###
class Cocinero(Persona):
    def __init__(self, pNombre, pHabilidad = randint(1,10)):
        super().__init__(pNombre)
        self.habilidad = pHabilidad
        self.energia = randint(50,80)

    def cocinar(self,informacion_plato):
        #print(f"Cocinero: {self.nombre}\tHabilidad: {self.habilidad}\tEnergia: {self.energia}")#
        if informacion_plato[1] == "Bebestible":
            bebestible = Bebestible(informacion_plato[0])
            if bebestible.tamano == "Pequeño":
                self.energia -= 5
            elif bebestible.tamano == "Mediano":
                self.energia -= 8
            else:
                self.energia -= 10

            if bebestible.dificultad > self.habilidad:
                bebestible.calidad *= 0.7
            else:
                bebestible.calidad *= 1.5
            return bebestible
        
        elif informacion_plato[1] == "Comestible":
            comestible = Comestible(informacion_plato[0])
            self.energia -= 15
            if comestible.dificultad > self.habilidad:
                comestible.calidad *= 0.7
            else:
                comestible.calidad *= 1.5
            return comestible
    
### FIN PARTE 2.3 ###

### INICIO PARTE 2.4 ###
class Cliente(Persona):
    def __init__(self, pNombre, pPlatos):
        super().__init__(pNombre)
        self.platos_preferidos = pPlatos

    def recibir_pedido(self,pedido,demora):
        calificacion = 10
        if len(pedido)<len(self.platos_preferidos) or demora >= 20:
            calificacion *= 0.5
        for plato in pedido:
            #print(plato.nombre,plato.calidad)
            if plato.calidad >= 11:
                calificacion += 1.5
            elif plato.calidad <= 8:
                calificacion -=3
            else:
                pass
            #print(f"\t{plato.nombre}\tCalidad: {plato.calidad:.2f}\tCalif: {calificacion}\tTiempo: {demora:.2f}")#
        return calificacion
        
### FIN PARTE 2.4 ###

if __name__ == "__main__":

    ### Código para probar que tu clase haya sido creada correctamente  ###
    ### Corre directamente este archivo para que este código se ejecute ###
    try:
        PLATOS_PRUEBA = {
        "Jugo Natural": ["Jugo Natural", "Bebestible"],
        "Empanadas": ["Empanadas", "Comestible"],
        }
        un_cocinero = Cocinero("Cristian", randint(1, 10))
        un_repartidor = Repartidor("Tomás", randint(20, 30))
        un_cliente = Cliente("Alberto", PLATOS_PRUEBA)
        print(f"El cocinero {un_cocinero.nombre} tiene una habilidad: {un_cocinero.habilidad}")
        print(f"El repatidor {un_repartidor.nombre} tiene una tiempo de entrega: {un_repartidor.tiempo_entrega} seg")
        print(f"El cliente {un_cliente.nombre} tiene los siguientes platos favoritos:")
        for plato in un_cliente.platos_preferidos.values():
            print(f" - {plato[1]}: {plato[0]}")
    except TypeError:
        print("Hay una cantidad incorrecta de argumentos en algún inicializador y/o todavía no defines una clase")
    except AttributeError:
        print("Algún atributo esta mal definido y/o todavia no defines una clase")
