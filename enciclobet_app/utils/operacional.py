from enciclobet_app.utils import scripts
from enciclobet_app.utils.conexao import Conexao
from enciclobet_app.models import Infos



class Operacional:
    
    @staticmethod
    def atualizaFormaUltimos5Jogos(forma, casaOuVisitante, jogo):
        if(len(forma) == 5):
                forma = forma[1:5]
        if(jogo['golsCasa'] == jogo['golsVisitante']):               
            forma = forma + 'E'
        elif(jogo['golsCasa'] > jogo['golsVisitante']) and casaOuVisitante == 'casa':
            forma = forma + 'V'
        elif(jogo['golsCasa'] > jogo['golsVisitante']) and casaOuVisitante == 'visitante':
            forma = forma + 'D'
        elif(jogo['golsCasa'] < jogo['golsVisitante']) and casaOuVisitante == 'casa':
            forma = forma + 'D'
        elif(jogo['golsCasa'] > jogo['golsVisitante']) and casaOuVisitante == 'visitante':
            forma = forma + 'V'

        return forma

    @staticmethod
    def getPeriodosDeGol(mandoCampo, gols):
        periodoDeGols = {
            'gols0a15':  0,
            'gols16a30': 0,
            'gols31a45': 0,
            'gols46a60': 0,
            'gols61a75': 0,
            'gols76a90': 0
        }

        for gol in gols:
            if(gol['mando_campo'] == mandoCampo):
                if gol['minuto'] < 16:
                    periodoDeGols['gols0a15']+=1
                elif gol['minuto'] < 31:
                    periodoDeGols['gols16a30']+=1
                elif gol['minuto'] < 46:
                    periodoDeGols['gols31a45']+=1
                elif gol['minuto'] < 61:
                    periodoDeGols['gols46a60']+=1
                elif gol['minuto'] < 76:
                    periodoDeGols['gols61a75']+=1
                else:
                    periodoDeGols['gols76a90']+=1

        return periodoDeGols

    @staticmethod
    def getInfoTime(equipe, casaOuVisitante, jogos):
        marcouPrimeiroNoHT = 0
        marcouPrimeiro = 0
        marcouPrimeiroEVenceu = 0
        marcouPrimeiroENaoVenceu = 0

        sofreuPrimeiroNoHT = 0
        sofreuPrimeiro = 0
        sofreuPrimeiroEVenceu = 0
        sofreuPrimeiroENaoVenceu = 0

        mandoCampo = ''
        mandoCampoAdversario = ''
        golsFeitos = ''
        golsSofridos = ''

        numJogos = 0

        if casaOuVisitante == 'casa':
            mandoCampo = 'H'
            mandoCampoAdversario = 'A'
            golsFeitos = 'golsCasa'
            golsSofridos = 'golsVisitante'
        elif casaOuVisitante == 'visitante':
            mandoCampo = 'A'
            mandoCampoAdversario = 'H'
            golsFeitos = 'golsVisitante'
            golsSofridos = 'golsCasa'

        forma = ''
        periodoDeGols = {
            'gols0a15': 0,
            'gols16a30': 0,
            'gols31a45': 0,
            'gols46a60': 0,
            'gols61a75': 0,
            'gols76a90': 0
        }
        for j in jogos:
            if j[casaOuVisitante] != equipe:
                continue

            # if()
            numJogos+=1
            flagMarcouPrimeiro = False
            flagSofreuPrimeiro = False

            forma = Operacional.atualizaFormaUltimos5Jogos(forma, casaOuVisitante, j)
            periodoDeGols = Operacional.getPeriodosDeGol(mandoCampo, j['gols'])


            for gol in j['gols']:
                if gol['mando_campo'] == mandoCampo:
                    marcouPrimeiro+=1
                    flagMarcouPrimeiro = True
                    if gol['minuto'] <= 45:
                        marcouPrimeiroNoHT+=1
                elif gol['mando_campo'] == mandoCampoAdversario:
                    sofreuPrimeiro+=1
                    flagSofreuPrimeiro = True
                    if gol['minuto'] <= 45:
                        sofreuPrimeiroNoHT+=1
                break;
            
            if flagMarcouPrimeiro and j[golsFeitos] > j[golsSofridos]:
                marcouPrimeiroEVenceu+=1
            elif flagMarcouPrimeiro:
                marcouPrimeiroENaoVenceu+=1

            if flagSofreuPrimeiro and j[golsFeitos] > j[golsSofridos]:
                sofreuPrimeiroEVenceu+=1
            elif flagMarcouPrimeiro:
                sofreuPrimeiroENaoVenceu+=1
                
        result = Infos.Result()

        result.equipe = equipe

        result.marcouPrimeiroNoHT.valor = marcouPrimeiroNoHT
        result.marcouPrimeiroNoHT.porcentagem = marcouPrimeiroNoHT / numJogos
        result.marcouPrimeiroNoHT.oddJusta = 1 / (marcouPrimeiroNoHT / numJogos ) if marcouPrimeiroNoHT != 0 else 0

        result.marcouPrimeiro.valor = marcouPrimeiro
        result.marcouPrimeiro.porcentagem = marcouPrimeiro / numJogos
        result.marcouPrimeiro.oddJusta = 1 / (marcouPrimeiro / numJogos ) if marcouPrimeiro != 0 else 0

        result.marcouPrimeiroEVenceu.valor = marcouPrimeiroEVenceu
        result.marcouPrimeiroEVenceu.porcentagem = marcouPrimeiroEVenceu / numJogos
        result.marcouPrimeiroEVenceu.oddJusta = 1 / (marcouPrimeiroEVenceu / numJogos ) if marcouPrimeiroEVenceu != 0 else 0

        result.marcouPrimeiroENaoVenceu.valor = marcouPrimeiroENaoVenceu
        result.marcouPrimeiroENaoVenceu.porcentagem = marcouPrimeiroENaoVenceu / numJogos
        result.marcouPrimeiroENaoVenceu.oddJusta = 1 / (marcouPrimeiroENaoVenceu / numJogos ) if marcouPrimeiroENaoVenceu != 0 else 0

        result.sofreuPrimeiroNoHT.valor = sofreuPrimeiroNoHT
        result.sofreuPrimeiroNoHT.porcentagem = sofreuPrimeiroNoHT / numJogos
        result.sofreuPrimeiroNoHT.oddJusta = 1 / (sofreuPrimeiroNoHT / numJogos ) if sofreuPrimeiroNoHT != 0 else 0

        result.sofreuPrimeiro.valor = sofreuPrimeiro
        result.sofreuPrimeiro.porcentagem = sofreuPrimeiro / numJogos
        result.sofreuPrimeiro.oddJusta = 1 / (sofreuPrimeiro / numJogos ) if sofreuPrimeiro != 0 else 0

        result.sofreuPrimeiroEVenceu.valor = sofreuPrimeiroEVenceu
        result.sofreuPrimeiroEVenceu.porcentagem = sofreuPrimeiroEVenceu / numJogos
        result.sofreuPrimeiroEVenceu.oddJusta = 1 / (sofreuPrimeiroEVenceu / numJogos ) if sofreuPrimeiroEVenceu != 0 else 0

        result.sofreuPrimeiroENaoVenceu.valor = sofreuPrimeiroENaoVenceu
        result.sofreuPrimeiroENaoVenceu.porcentagem = sofreuPrimeiroENaoVenceu / numJogos
        result.sofreuPrimeiroENaoVenceu.oddJusta = 1 / (sofreuPrimeiroENaoVenceu / numJogos ) if sofreuPrimeiroENaoVenceu != 0 else 0

        result.numJogos = numJogos
        result.forma = forma

        result.gols0a15 = periodoDeGols['gols0a15']
        result.gols16a30 = periodoDeGols['gols16a30']
        result.gols31a45 = periodoDeGols['gols31a45']
        result.gols46a60 = periodoDeGols['gols46a60']
        result.gols61a75 = periodoDeGols['gols61a75']
        result.gols76a90 = periodoDeGols['gols76a90']

        return result

    @staticmethod
    def infoBackFavorito1T(filtros):
        con=Conexao()

        odd1, odd2, home, away, league, season = 1, 1000, '', '', '', ''

        # filtros = { 
        #     'odd1': 0, 
        #     'odd2': 0, 
        #     'home': 'novori', 
        #     'away': '', 
        #     'league': 'serie b', 
        #     'season': '2023'}

        # print(scripts.selectGolsByFiltros.format(
        #     filtros['odd1'] if filtros['odd1'] != 0 else odd1, 
        #     filtros['odd2'] if filtros['odd2'] != 0 else odd2, 
        #     filtros['home'] if filtros['home'] != '' else home, 
        #     filtros['away'] if filtros['away'] != '' else away, 
        #     filtros['league'] if filtros['league'] != '' else league,
        #     filtros['season'] if filtros['season'] != '' else season
        # ))

        result = con.consultar(scripts.selectGolsByFiltros.format(
            filtros['odd1'] if filtros['odd1'] != 0 else odd1, 
            filtros['odd2'] if filtros['odd2'] != 0 else odd2, 
            filtros['home'] if filtros['home'] != '' else home, 
            filtros['away'] if filtros['away'] != '' else away, 
            filtros['league'] if filtros['league'] != '' else league,
            filtros['season'] if filtros['season'] != '' else season
        ))

        jogos = []
        jogoIterado = 0
        indicePreenchido = -1
        for rs in result:
            if rs[0] != jogoIterado:
                jogoIterado = rs[0]
                # j.id_jogo, j.league, j.season, j.date, j.home, j.away, g.mando_campo, g.minuto, g.acrescimo, j.ft_goals_h, j.ft_goals_a
                # j.id_jogo, j.league, j.season, j.date, j.home, j.away, g.mando_campo, g.minuto, g.acrescimo, 
                jogos.append({
                                        'idJogo': rs[0], 
                                        'liga': rs[1], 
                                        'temporada': rs[2], 
                                        'data': rs[3], 
                                        'casa': rs[4], 
                                        'visitante': rs[5], 
                                        'gols': [],
                                        'golsCasa': rs[9], 
                                        'golsVisitante': rs[10]

                                    })
                indicePreenchido+=1

            jogos[indicePreenchido]['gols'].append({
                                                        'mando_campo': rs[6], 
                                                        'minuto': rs[7], 
                                                        'acrescimo': rs[8]
                                                        })

        infoResult = Infos()
        if filtros['home'] != '':
            infoResult.resultCasa = Operacional.getInfoTime(filtros['home'], 'casa', jogos) # vasco, casa, listaJogos
        if filtros['away'] != '':
            infoResult.resultVisitante = Operacional.getInfoTime(filtros['away'], 'visitante', jogos) # vasco, visitante, listaJogos

        # print(infoResult.resultVisitante)
        return infoResult

        

