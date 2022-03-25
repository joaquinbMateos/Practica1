# Adivina adivinador....
import random

numero_aleatorio = random.randrange(101)
gane = false
print('tenés 5 intentos para adivinar 0 entre 100')
intento = 1 
while intento < 6 and not gane:
    numero_ingresado = int(input('ingresa tu numero: '))
    if numero_ingresado == numero_aleatorio:
        print('GANASTE! y necesitaste {}intentos!!!'.format(intento))
        gane = true
    else:
        print('Mmmm...no..ese numero no es...Seguí intentando.')
        intento += 1
if not gane:
    print('/n Perdiste :(/n El numero era {}'.format(numero_aleatorio))