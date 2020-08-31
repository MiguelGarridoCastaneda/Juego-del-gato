
def nuevaPartida(partida):
    
    partida['turno'] +=1
    while(True):  
        if (partida['turno'] > 9):
            partida['ganador'] = "E"
            break    
         
        if (partida['turno'] % 2 != 0):
            jugada = int(input("Es el turno del jugador X, ¿qué casilla marcarás?: "))
            if (jugada not in partida['registro']):
                partida['jX'].append(jugada)
                partida['registro'].append(jugada)
                break
            else:
                print("Esa casilla ya está ocupada")
        else:
            jugada = int(input("Es el turno del jugador O, ¿qué casilla marcarás?: "))
            if (jugada not in partida['registro']):
                partida['jO'].append(jugada)
                partida['registro'].append(jugada)
                break
            else:
                print("Esa casilla ya está ocupada")
        
    if (partida['turno'] >= 4):
        if (partida['turno'] % 2 != 0):
            if((1 in partida['jX'] and 2 in partida['jX'] and 3 in partida['jX']) or (4 in partida['jX'] and 5 in partida['jX'] and 6 in partida['jX'])
                or (7 in partida['jX'] and 8 in partida['jX'] and 9 in partida['jX']) or (1 in partida['jX'] and 4 in partida['jX'] and 7 in partida['jX'])
                or (2 in partida['jX'] and 5 in partida['jX'] and 8 in partida['jX']) or (3 in partida['jX'] and 6 in partida['jX'] and 9 in partida['jX'])
                or (1 in partida['jX'] and 5 in partida['jX'] and 9 in partida['jX']) or (3 in partida['jX'] and 5 in partida['jX'] and 7 in partida['jX'])):
                partida['ganador'] = 'X'
            
        else:
            if((1 in partida['jO'] and 2 in partida['jO'] and 3 in partida['jO']) or (4 in partida['jO'] and 5 in partida['jO'] and 6 in partida['jO'])
                or (7 in partida['jO'] and 8 in partida['jO'] and 9 in partida['jO']) or (1 in partida['jO'] and 4 in partida['jO'] and 7 in partida['jO'])
                or (2 in partida['jO'] and 5 in partida['jO'] and 8 in partida['jO']) or (3 in partida['jO'] and 6 in partida['jO'] and 9 in partida['jO'])
                or (1 in partida['jO'] and 5 in partida['jO'] and 9 in partida['jO']) or (3 in partida['jO'] and 5 in partida['jO'] and 7 in partida['jO'])):
                partida['ganador'] = 'O'
                         
    return partida

partida = {'jX':[], 'jO':[], 'registro':[], 'turno':0, 'ganador':""}
while(partida['ganador'] == ''):
    partida = nuevaPartida(partida)
print(partida)

