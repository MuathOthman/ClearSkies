class store:
    def __init__(self, money, co2):
        self.money = money
        self.co2 = co2

    def exchange(self):
        self.co2 = self.money / 2

    def info(self):
        print(f"RAHA {self.money} $ = {self.co2} KG, ")

wallet1 = store(50,0)
wallet1.exchange()
wallet1.info()

wallet2 = store(100,0)
wallet2.exchange()
wallet2.info()

wallet3 = store(150,0)
wallet3.exchange()
wallet3.info()

wallet4 = store(200,0)
wallet4.exchange()
wallet4.info()

wallet5 = store(250,0)
wallet5.exchange()
wallet5.info()

wallet6 = store(300,0)
wallet6.exchange()
wallet6.info()

wallet7 = store(350,0)
wallet7.exchange()
wallet7.info()

wallet8 = store(400,0)
wallet8.exchange()
wallet8.info()