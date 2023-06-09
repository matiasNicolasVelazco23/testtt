import pygame
from constantes import *


def crear_tarjeta(nombre_imagen: str, identificador: int, nombre_imagen_escondida: str, x: int, y: int) -> dict:
    '''
    Crea una nueva tarjeta
    Recibe como parametro el path donde estan los recursos, el nombre de la imagen y el tamaño que esta debera tener
    Retorna la tarjeta creada
    '''
    imagen = pygame.image.load(nombre_imagen)
    imagen_escalada = pygame.transform.scale(imagen,(ANCHO_TARJETA, ALTO_TARJETA))
    imagen_escondida = pygame.image.load(nombre_imagen_escondida)
    imagen_escondida_escalada =pygame.transform.scale(imagen_escondida,(ANCHO_TARJETA, ALTO_TARJETA))
    rectangulo_tarjeta= imagen_escalada.get_rect()
    rectangulo_tarjeta.x = x
    rectangulo_tarjeta.y = y
    flag_visible= False
    flag_descubierto = False
    # rectangulo_tarjeta.centerx = x
    # rectangulo_tarjeta.centery = y

    tarjeta = {
        "superficie" : imagen,
        "superficie_escondida" : imagen_escondida,
        "identificador" : identificador,
        "visible" : flag_visible,
        "descubierto" : flag_descubierto,
        "rectangulo" : rectangulo_tarjeta
    }
    
    return tarjeta


def obtener_cantidad_tarjetas_por_estado(lista_tarjetas: list[dict], estado: bool) -> int:
    '''
        Obtiene la cantidad de tarjetas que esten visibles y que esten o no cubiertas
        Recibe la lista de tarjetas y un estado (True o False) si es True me devuelve las cartas descubieras sino me devuelve las cubiertas.
        Retorna dicha cantidad
    '''
    cantidad = 0
    for tarjeta in lista_tarjetas:
        if (tarjeta["descubierto"] == estado and tarjeta["visible"]):
            cantidad += 1
    return cantidad


def descubrir_tarjetas(lista_tarjetas, identificador):
    '''
        Función que se encarga de cambiarme la bandera a las tarjetas a las que el usuario haya acertado en el memotest
        recibe la lista de tarjetas y el identificador a la que le va a reemplazar la bandera descubierto
        Uso una variable contador para evitar que el bucle se ejecute completo y ahorrar recursos si ya reemplazo a dos tarjetas no tiene sentido seguir iterando
    '''
    contador = 0
    for tarjeta in lista_tarjetas:
        if tarjeta["identificador"] == identificador and tarjeta["descubierto"] == False:
            tarjeta["descubierto"] = True
            contador += 1
        elif contador == 2:
            break
            
