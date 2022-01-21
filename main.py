##############################################################
from random import seed, choice, sample, randint, shuffle
from personas import Cocinero, Repartidor, Cliente
from restaurante import Restaurante

## Si necesita agregar imports, debe agregarlos aquí arriba ##

### INICIO PARTE 4 ###

def lista_keys(dict):
    return [*dict]

def crear_cocineros():
    cocineros = []
    for i in range(5):
        cocineros.append(Cocinero(choice(NOMBRES),randint(20,30)))
        #print(f"Cocinero: {cocineros[-1].nombre}\tHabilidad: {cocineros[-1].habilidad}\tEnergia: {cocineros[-1].energia}")
    return cocineros

def crear_repartidores():
    repartidores = []
    for i in range(2):
        repartidores.append(Repartidor(choice(NOMBRES),randint(1,10)))
        #print(f"Reparto {i+1}: {repartidores[-1].nombre}\t Energia: {repartidores[-1].energia}\tTpoEntrega: {repartidores[-1].tiempo_entrega}")
    return repartidores

def crear_clientes():
    clientes = []
    for i in range(5):
        clientes.append(Cliente(choice(NOMBRES),sample(lista_keys(INFO_PLATOS),k = randint(1,5))))
        #print(clientes[-1].platos_preferidos)
    return clientes

def crear_restaurante():
    cocineros = crear_cocineros()
    repartidores = crear_repartidores()
    platos = INFO_PLATOS
    nombre = "El Bulli"
    restaurante = Restaurante(nombre,platos,cocineros,repartidores)
    return restaurante

### FIN PARTE 4 ###

################################################################
## No debe modificar nada de abajo en este archivo.
## Este archivo debe ser ejecutado para probar el funcionamiento
## de su programa orientado a objetos.
################################################################

INFO_PLATOS = {
    "Pepsi": ["Pepsi", "Bebestible"],
    "Coca-Cola": ["Coca-Cola", "Bebestible"],
    "Jugo Natural": ["Jugo Natural", "Bebestible"],
    "Agua": ["Agua", "Bebestible"],
    "Papas Duqueza": ["Papas Duqueza", "Comestible"],
    "Lomo a lo Pobre": ["Lomo a lo Pobre", "Comestible"],
    "Empanadas": ["Empanadas", "Comestible"],
    "Mariscos": ["Mariscos", "Comestible"],
}

NOMBRES = ["Amaia", "Cristian", "Maggie", "Pablo", "Catalina", "Juan", "Sergio"]

if __name__ == "__main__":

    ### Código para probar que tu miniproyecto esté funcionando correctamente  ###
    ### Corre directamente este archivo para que este código se ejecute ###
    seed("With Love")
    restaurante = crear_restaurante() # Crea el restaurante a partir de la función crear_restaurante()
    clientes = crear_clientes() # Crea los clientes a partir de la función crear_clientes()
    if restaurante != None and clientes != None:
        restaurante.recibir_pedidos(clientes) # Corre el método recibir_pedidos(clientes) para actualizar la calificación del restaurante
        print(
            f"La calificación final del restaurante {restaurante.nombre} "
            f"es {restaurante.calificacion}"
        )
    elif restaurante == None:
        print("la funcion crear_restaurante() no esta retornando la instancia del restaurante")
    elif clientes == None:
        print("la funcion crear_clientes() no esta retornando la instancia de los clientes")
