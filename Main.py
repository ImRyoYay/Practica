diccionario = {'pov': 'Punto de vista de algo o alguien',
            'waos': 'Expreción de sorpresa y/o asombro a una situación',
            'uwu': 'Nadie sabe que significa precisamente...',
            'boomer' : 'Persona que está lejos de la actualidad y de lo que está de moda',
            'hype' : 'Algo que crea expetación, o tiene buena pinta',
            'crush' : 'Amor platónico, felchazo',
            'lol' : 'Reírse a carcajadas de algo',
            'trolear' : 'Hacerle una broma o vacilar con alguien',
            'stalkear' : 'Cotillear la cuenta de alguna red social de alguien',
            'fachero' : 'Bueno, chulo'}

x = input('Ingresa una palabra que te gustaría conocer su significado: ')
if x in diccionario.keys():
    print(diccionario[x])
else:
    print('Esa palabra no está en nuestro diccionario...')
