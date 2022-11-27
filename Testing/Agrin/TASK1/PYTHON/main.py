def moneybudget(nimi):
    budget = 50     #The amount of money will add if you get a new saatila
    budget1 = str(budget)
    sql = "UPDATE game set money= '" + budget1 + "'"    # Adding the amount into sql
    sql += "Where screen_name = '" + nimi + "'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    return


moneybudget(nimi) # This will go to function saa_tila when a new saatila is reached.