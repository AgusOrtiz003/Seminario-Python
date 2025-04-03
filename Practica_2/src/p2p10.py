def imprimirRonda(ranking,numRonda):
    print(f'Ranking ronda {numRonda}:\n')
    print(f'Jugador{' '*3}Kills{' '*3}Asistencias{' '*3}Muertes{' '*3}MVPs{' '*3}Puntos')
    print('-'*55)
    for jugador in ranking:
        print(f'|{jugador}{' '*(6-len(jugador))}{' '*3}{ranking[jugador]['kills']}{' '*7}{ranking[jugador]['assists']}{' '*13}{ranking[jugador]['deaths']}{' '*9}{ranking[jugador]['mvps']}{' '*6}{ranking[jugador]['puntos']}{' '*4}|')
    print('-'*55)
    print('\n'*3)
    
def calcularPuntos(stats):
    puntos=0
    puntos+=3*stats['kills']
    puntos+=1*stats['assists']
    if stats['deaths']: puntos-=1
    return puntos

def procesarEstadisticas(nombre,stats,mvp,rankingFinal):
    for estadistica in stats:
        rankingFinal[nombre][estadistica]+=stats[estadistica]
    puntos=calcularPuntos(stats)
    if puntos>mvp['puntos']:
        mvp['nombre']=nombre
        mvp['puntos']=puntos
    rankingFinal[nombre]['puntos']+=puntos

def procesarRonda(ronda,numRonda,rankingFinal):
    mvp={'nombre':'','puntos':-1}
    for jugador in ronda:
        procesarEstadisticas(jugador,ronda[jugador],mvp,rankingFinal)
    rankingFinal[mvp['nombre']]['mvps']+=1
    rankingFinal=dict(sorted(rankingFinal.items(),key=lambda item:item[1]['puntos'],reverse=True))
    imprimirRonda(rankingFinal,numRonda)

def iniciarRanking(ronda,ranking):
    '''Toma una ronda para almacenar y inicializar las estadísticas de los jugadores'''
    for jugador in ronda:
        ranking[jugador]={}
        for estadistica in ronda[jugador]:
            ranking[jugador][estadistica]=0
        ranking[jugador]['mvps']=0
        ranking[jugador]['puntos']=0

def procesarPartida(rounds,rankingFinal):
    iniciarRanking(rounds[0],rankingFinal)
    for indice,ronda in enumerate(rounds):
        procesarRonda(ronda,(indice+1),rankingFinal)