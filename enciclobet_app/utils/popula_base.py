import csv
import pandas as pd
from enciclobet_app.utils import CONSTANTES
from enciclobet_app.utils import scripts

from enciclobet_app.utils.conexao import Conexao


con=Conexao()
con.criarTabelas()

with open('enciclobet_app\\utils\\dados_temporada_atual.csv', newline='', encoding='utf-8') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
    i=0

    jogosCadastrados = con.consultar("select id_jogo from jogos")

    loadingImpresso = 1
    for row in spamreader:
        i+=1
        if i < 2:
            continue

        loadingPorcentagem = i/len(jogosCadastrados) * 100
        if(loadingPorcentagem > loadingImpresso):
            print("loading ", loadingImpresso, "%")
            loadingImpresso+=1
            
        
        if row[CONSTANTES.Id_Jogo] not in jogosCadastrados:
        # if '/' in row[CONSTANTES.Season]:

            # Inserindo dados na tabela de gols
            golsA = row[CONSTANTES.Goals_A_Minutes].replace("[", "").replace("]", "").replace("\'", "").split(',')
            golsH = row[CONSTANTES.Goals_H_Minutes].replace("[", "").replace("]", "").replace("\'", "").split(',')

            minuto = '0'
            acrescimo = '0'

            if golsH[0]:
                for x in golsH:
                    if "+" in x:
                        minuto = x.split("+")[0]
                        acrescimo = x.split("+")[1]
                    else:
                        minuto = x

                    con.manipular(scripts.insertGols.format(
                            row[CONSTANTES.Id_Jogo],
                            "\'H\'",
                            "\'" + row[CONSTANTES.Home].replace("\'", "\'\'") + "\'",
                            minuto.strip(),
                            acrescimo.strip(),
                    ))

            minuto = '0'
            acrescimo = '0'

            if golsA[0]:
                for x in golsA:
                    if "+" in x:
                        minuto = x.split("+")[0]
                        acrescimo = x.split("+")[1]
                    else:
                        minuto = x

                    con.manipular(scripts.insertGols.format(
                            row[CONSTANTES.Id_Jogo],
                            "\'A\'",
                            "\'" + row[CONSTANTES.Away].replace("\'", "\'\'") + "\'",
                            minuto.strip(),
                            acrescimo.strip(),
                    ))
            
            
            # Inserindo dados na tabela de odds
            con.manipular(scripts.insertOdds.format(
                row[CONSTANTES.Id_Jogo].replace(",", "."),
                row[CONSTANTES.HT_Odds_H].replace(",", "."),
                row[CONSTANTES.HT_Odds_D].replace(",", "."),
                row[CONSTANTES.HT_Odds_A].replace(",", "."),
                row[CONSTANTES.HT_Odds_Over05].replace(",", "."),
                row[CONSTANTES.HT_Odds_Under05].replace(",", "."),
                row[CONSTANTES.HT_Odds_Over15].replace(",", "."),
                row[CONSTANTES.HT_Odds_Under15].replace(",", "."),
                row[CONSTANTES.HT_Odds_Over25].replace(",", "."),
                row[CONSTANTES.HT_Odds_Under25].replace(",", "."),
                row[CONSTANTES.FT_Odds_H].replace(",", "."),
                row[CONSTANTES.FT_Odds_D].replace(",", "."),
                row[CONSTANTES.FT_Odds_A].replace(",", "."),
                row[CONSTANTES.FT_Odds_Over05].replace(",", "."),
                row[CONSTANTES.FT_Odds_Under05].replace(",", "."),
                row[CONSTANTES.FT_Odds_Over15].replace(",", "."),
                row[CONSTANTES.FT_Odds_Under15].replace(",", "."),
                row[CONSTANTES.FT_Odds_Over25].replace(",", "."),
                row[CONSTANTES.FT_Odds_Under25].replace(",", "."),
                row[CONSTANTES.Odds_BTTS_Yes].replace(",", "."),
                row[CONSTANTES.Odds_BTTS_No].replace(",", "."),
                row[CONSTANTES.Odds_DuplaChance_1X].replace(",", "."),
                row[CONSTANTES.Odds_DuplaChance_12].replace(",", "."),
                row[CONSTANTES.Odds_DuplaChance_X2].replace(",", "."),
                row[CONSTANTES.Odds_Corners_H].replace(",", "."),
                row[CONSTANTES.Odds_Corners_D].replace(",", "."),
                row[CONSTANTES.Odds_Corners_A].replace(",", "."),
                row[CONSTANTES.Odds_Corners_Over75].replace(",", "."),
                row[CONSTANTES.Odds_Corners_Over85].replace(",", "."),
                row[CONSTANTES.Odds_Corners_Over95].replace(",", "."),
                row[CONSTANTES.Odds_Corners_Over105].replace(",", "."),
                row[CONSTANTES.Odds_Corners_Over115].replace(",", "."),
            ))


            # Inserindo dados na tabela de jogos
            con.manipular(scripts.insertJogos.format(
                row[CONSTANTES.Id_Jogo],
                "\'" + row[CONSTANTES.League] + "\'",
                "\'" + row[CONSTANTES.Season] + "\'",
                "\'" + row[CONSTANTES.Date] + "\'",
                row[CONSTANTES.Rodada],
                "\'" + row[CONSTANTES.Home].replace("\'", "\'\'") + "\'",
                "\'" + row[CONSTANTES.Away].replace("\'", "\'\'") + "\'",
                row[CONSTANTES.HT_Goals_H],
                row[CONSTANTES.HT_Goals_A],
                row[CONSTANTES.HT_TotalGoals],
                row[CONSTANTES.FT_Goals_H],
                row[CONSTANTES.FT_Goals_A],
                row[CONSTANTES.FT_TotalGoals],
                row[CONSTANTES.FT_Corners_H],
                row[CONSTANTES.FT_Corners_A],
                row[CONSTANTES.FT_TotalCorners],
                row[CONSTANTES.PPG_Home_Pre].replace(",", "."),
                row[CONSTANTES.PPG_Away_Pre].replace(",", "."),
                row[CONSTANTES.PPG_Home].replace(",", "."),
                row[CONSTANTES.PPG_Away].replace(",", "."),
                row[CONSTANTES.XG_Home_Pre].replace(",", "."),
                row[CONSTANTES.XG_Away_Pre].replace(",", "."),
                row[CONSTANTES.XG_Total_Pre].replace(",", "."),
                row[CONSTANTES.ShotsOnTarget_H],
                row[CONSTANTES.ShotsOnTarget_A],
                row[CONSTANTES.ShotsOffTarget_H],
                row[CONSTANTES.ShotsOffTarget_A],
                row[CONSTANTES.Shots_H],
                row[CONSTANTES.Shots_A],
            ))
    
    print('finalizado')

    con.fechar()