import mysql.connector
lista_sql = []


def connect_db():
    return mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='ClearSkies',
        user='admin',
        password='12345',
        autocommit=True
    )

class Player:
    def __init__(self, id, consumed, budget, location, name, money):
        self.id = id
        self.consumed = consumed
        self.budget = budget
        self.location = location
        self.name = name
        self.money = money

    def datafromSQL(name):
        sql = f"select * from game where screen_name = '{name}'"
        cursor = connection.cursor()
        cursor.execute(sql)
        result_set = cursor.fetchone()
        if cursor.rowcount > 0:
            for i in result_set:
                lista_sql.append(i)

connection = connect_db()

nimi = input('Nimi: ')

Player.datafromSQL(nimi)

player = Player(lista_sql[0], lista_sql[1], lista_sql[2], lista_sql[3], lista_sql[4], lista_sql[5])
print(player.name)
print(player.id)
print(player.budget)

print(Player.nimi)