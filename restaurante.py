##############################################################
## Si necesita agregar imports, debe agregarlos aquí arriba ##
from personas import Repartidor, Cocinero, Cliente
from random import choice

### INICIO PARTE 3 ###
class Restaurante:
    def __init__(self, pNombre, pPlatos, pCocineros, pRepartidores):
        self.nombre = pNombre
        self.platos = pPlatos
        self.cocineros = pCocineros
        self.repartidores = pRepartidores
        self.calificacion = 0

    def validar_energia(self,personas):
        personas_2 = []    
        for persona in personas:
            if persona.energia > 0:
                personas_2.append(persona)
        if personas_2 != personas:
            personas = personas_2
            return personas
        else:
            return personas

    def recibir_pedidos(self,clientes):
        for cliente in clientes:
            pedidos = []
            for plato in cliente.platos_preferidos:
                if len(self.validar_energia(self.cocineros)) > 0:
                    cocinero = choice(self.validar_energia(self.cocineros))
                    #print(cocinero.nombre,cocinero.energia)#
                    pedidos.append(cocinero.cocinar(self.platos[plato]))
                else:
                    pass
            if len(self.validar_energia(self.repartidores)) > 0:
                repartidor = choice(self.validar_energia(self.repartidores))
                self.calificacion += cliente.recibir_pedido(pedidos,repartidor.repartir(pedidos))
            elif len(self.repartidores) == 0:
                self.calificacion += cliente.recibir_pedido([],0)
            #print(f"Cliente: {cliente.nombre}\tCalif: {self.calificacion}\n")#

        self.calificacion /= len(clientes)
            
            
### FIN PARTE 3 #

if __name__ == "__main__":

    ### Código para probar que tu clase haya sido creada correctamente  ###
    ### Corre directamente este archivo para que este código se ejecute ###
    try:
        PLATOS_PRUEBA = {
        "Pepsi": ["Pepsi", "Bebestible"],
        "Mariscos": ["Mariscos", "Comestible"],
        }
        un_restaurante = Restaurante("Bon Appetit", PLATOS_PRUEBA, [], [])
        print(f"El restaurante {un_restaurante.nombre}, tiene los siguientes platos:")
        for plato in un_restaurante.platos.values():
            print(f" - {plato[1]}: {plato[0]}")
    except TypeError:
        print("Hay una cantidad incorrecta de argumentos en algún inicializador y/o todavía no defines una clase")
    except AttributeError:
        print("Algún atributo esta mal definido y/o todavia no defines una clase")
