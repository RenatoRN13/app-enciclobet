selectGolsByFiltros = """
select 
    j.id_jogo, j.league, j.season, j.date, j.home, j.away, g.mando_campo, g.minuto, g.acrescimo, j.ft_goals_h, j.ft_goals_a
from gols g 
inner join jogos j on j.id_jogo = g.id_jogo 
inner join odds o on o.id_jogo = g.id_jogo
where 1=1
and o.ft_odds_a > {0} and o.ft_odds_a < {1}
and (j.home ilike '%{2}%' or j.away ilike '%{3}%')
and j.league ilike '%{4}%'
and j.season like '%{5}%'
order by g.id_jogo, g.minuto, g.acrescimo
"""

selectJogosByLeague = """
select j.*, o.ft_odds_h, o.ft_odds_d, o.ft_odds_a, o.ft_odds_under25, o.odds_btts_yes from jogos j 
inner join odds o on o.id_jogo = j.id_jogo 
where league ilike '%{0}%'
"""

selectJogosByEquipeCasa = """
select j.*, o.ft_odds_h, o.ft_odds_d, o.ft_odds_a, o.ft_odds_under25, o.odds_btts_yes from jogos j 
inner join odds o on o.id_jogo = j.id_jogo 
where home ilike '%{0}%'
"""
selectJogosByEquipeVisitante = """
select j.*, o.ft_odds_h, o.ft_odds_d, o.ft_odds_a, o.ft_odds_under25, o.odds_btts_yes from jogos j 
inner join odds o on o.id_jogo = j.id_jogo 
where away ilike '%{0}%'
"""
selectJogosByOddCasa = """
select j.*, o.ft_odds_h, o.ft_odds_d, o.ft_odds_a, o.ft_odds_under25, o.odds_btts_yes from jogos j 
inner join odds o on o.id_jogo = j.id_jogo 
where o.ft_odds_h > {0} and o.ft_odds_h < {1}
"""
selectJogosByOddVisitante = """
select j.*, o.ft_odds_h, o.ft_odds_d, o.ft_odds_a, o.ft_odds_under25, o.odds_btts_yes from jogos j 
inner join odds o on o.id_jogo = j.id_jogo 
where o.ft_odds_a > {0} and o.ft_odds_a < {1}
"""



createTableGols =  """
                    create table if not exists gols (
                        id_jogo int,
                        mando_campo char,
                        equipe text,
                        minuto int,
                        acrescimo int,
                        PRIMARY KEY (id_jogo, mando_campo, minuto, acrescimo)
                    )
                    """

createTableOdds =  """
            create table if not exists odds (
              id_jogo int PRIMARY KEY,
              HT_Odds_H decimal,
              HT_Odds_D decimal,
              HT_Odds_A decimal,
              HT_Odds_Over05 decimal,
              HT_Odds_Under05 decimal,
              HT_Odds_Over15 decimal,
              HT_Odds_Under15 decimal,
              HT_Odds_Over25 decimal,
              HT_Odds_Under25 decimal,
              FT_Odds_H decimal,
              FT_Odds_D decimal,
              FT_Odds_A decimal,
              FT_Odds_Over05 decimal,
              FT_Odds_Under05 decimal,
              FT_Odds_Over15 decimal,
              FT_Odds_Under15 decimal,
              FT_Odds_Over25 decimal,
              FT_Odds_Under25 decimal,
              odds_BTTS_Yes decimal,
              odds_BTTS_No decimal,
              odds_DuplaChance_1X decimal,
              odds_DuplaChance_12 decimal,
              odds_DuplaChance_X2 decimal,
              odds_Corners_H decimal,
              odds_Corners_D decimal,
              odds_Corners_A decimal,
              odds_Corners_Over75 decimal,
              odds_Corners_Over85 decimal,
              odds_Corners_Over95 decimal,
              odds_Corners_Over105 decimal,
              odds_Corners_Over115 decimal
            )
            
            """

createTableJogos =  """
            create table if not exists jogos (
              id_jogo int PRIMARY KEY,
              league text,
              season text,
              date text,
              rodada int,
              home text,
              away text,
              HT_Goals_H int,
              HT_Goals_A int,
              HT_TotalGoals int,
              FT_Goals_H  int,
              FT_Goals_A  int,
              FT_TotalGoals  int,
              FT_Corners_H  int,
              FT_Corners_A  int,
              FT_TotalCorners  int,
              PPG_Home_Pre  decimal,
              PPG_Away_Pre  decimal,
              PPG_Home  decimal,
              PPG_Away  decimal,
              XG_Home_Pre  decimal,
              XG_Away_Pre  decimal,
              XG_Total_Pre  decimal,
              shotsOnTarget_H  int,
              shotsOnTarget_A  int,
              shotsOffTarget_H  int,
              shotsOffTarget_A  int,
              shots_H  int,
              shots_A  int
            )
            """

insertGols = """
                insert into gols values (
                    {0},
                    {1},
                    {2},
                    {3},
                    {4}
                )
            """

insertJogos = """
                insert into jogos values (
                    {0},
                    {1},
                    {2},
                    {3},
                    {4},
                    {5},
                    {6},
                    {7},
                    {8},
                    {9},
                    {10},
                    {11},
                    {12},
                    {13},
                    {14},
                    {15},
                    {16},
                    {17},
                    {18},
                    {19},
                    {20},
                    {21},
                    {22},
                    {23},
                    {24},
                    {25},
                    {26},
                    {27},
                    {28}
                )
            """

insertOdds = """
                insert into odds values (
                    {0},
                    {1},
                    {2},
                    {3},
                    {4},
                    {5},
                    {6},
                    {7},
                    {8},
                    {9},
                    {10},
                    {11},
                    {12},
                    {13},
                    {14},
                    {15},
                    {16},
                    {17},
                    {18},
                    {19},
                    {20},
                    {21},
                    {22},
                    {23},
                    {24},
                    {25},
                    {26},
                    {27},
                    {28},
                    {29},
                    {30},
                    {31}
                )
            """
