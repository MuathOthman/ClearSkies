def moneybudget(nimi):
    budget = "50"    #The amount of money will add if you get a new saatila
    sql = "update game set money = money + '" + budget + "'"        # Adding the amount into sql
    sql += " WHERE screen_name= '" + nimi + "'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    return

moneybudget(nimi) # This will go to function saa_tila when a new saatila is reached.

#mysql commands ALTER TABLE game add money int;