"""
Nombres: Cristian David Santoyo Parra
         Michael Daniel Suárez Rivera
"""
import random
from behave import *

@given('una baraja')
def construir_baraja(context):
    b = []
    for i in range(0,4):
        for j in range(1,14):
            b.append(j)
    random.shuffle(b)
    return b

@when('reparto la carta')
def sacar_carta(context):
    baraja = construir_baraja(context)
    return baraja.pop()

@then('obtengo mano')
def repartir_mano(context):    
    return [sacar_carta(context), sacar_carta(context)]

def obtener_valor_mano(mano):
    val = 0
    b = False
    for i in mano:
        if (i == 1):
            b = True
            val += 11
        elif(i == 11 or i == 12 or i == 13):
            val +=10
        else:
            val +=i
    if (val > 21 and b):
        val-=10
    return val

def mostrar_mano(mano):
    val = []
    for i in mano:
        if (i == 1):
            val.append('A')
        elif(i == 11):
            val.append('J')
        elif(i == 12):
            val.append('Q')
        elif(i == 13):
            val.append('K')
        else:
            val.append(i)
    return val

def preguntar(mJugador, mCrupier):
    print("¿Desa sacar una carta? Si: s | No: n")
    r = input()
    while(r != 's' and r != 'n'):
        print("Entrada inválida")
        print("¿Desa sacar una carta? Si: s | No: n")
        r = input()
    
    if (r == 's'):
        mJugador.append(sacar_carta())
        print("Mano del jugador: ", mostrar_mano(mJugador))
        print("El valor de su mano es: ", obtener_valor_mano(mJugador))
        if (obtener_valor_mano(mJugador) > 21):
            print("Usted se pasó, Ha perdido ¬¬")
            return
        else:
            preguntar(mJugador, mCrupier)
    elif(r == 'n'):
        calcular_valores(mJugador, mCrupier)
        
def calcular_valores(mJugador, mCrupier):
    j = obtener_valor_mano(mJugador)
    c = obtener_valor_mano(mCrupier)

    while ((21 - j < 21 - c and c != 17) or c < 17):
        mCrupier.append(sacar_carta())
        c = obtener_valor_mano(mCrupier)

    print("J: ", j, " C: ", c)
    if (c > 21 and j < 22):
        print("Felicidades usted ha ganado")
        print("Mano del jugador: ", mostrar_mano(mJugador))
        print("El valor de su mano es: ", obtener_valor_mano(mJugador))
        print("Mano del Crupier: ", mostrar_mano(mCrupier))
        print("El valor de la mano del crupier: ", obtener_valor_mano(mCrupier))
        return    
    elif ((21 - j > 21 - c) or (j == c)):
        print("Usted ha perdido :(")
        print("Mano del jugador: ", mostrar_mano(mJugador))
        print("El valor de su mano es: ", obtener_valor_mano(mJugador))
        print("Mano del Crupier: ", mostrar_mano(mCrupier))
        print("El valor de la mano del crupier: ", obtener_valor_mano(mCrupier))
        return

def preguntar_juego_nuevo():
    print("¿Desa continuar jugando? Si: s | No: n")
    r = input()
    while(r != 's' and r != 'n'):
        print("Entrada inválida")
        print("¿Desa continuar jugando? Si: s | No: n")
        r = input()
    if (r == 's'):
        iniciar_juego()
    else:
        return

def iniciar_juego():
    print("Bienvenido al Juego de 21 :D")   

    mano_jugador = repartir_mano()
    mano_crupier = repartir_mano()

    print("Mano del jugador: ", mostrar_mano(mano_jugador))
    print("El valor de su mano es: ", obtener_valor_mano(mano_jugador))
    preguntar(mano_jugador, mano_crupier)
    preguntar_juego_nuevo()

