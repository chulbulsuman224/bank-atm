class Atm(object):
    def __init__(self,cashwithdrawal,currency,money_limit):
        self.cashwithdrawal=cashwithdrawal
        self.currency=currency
        self.money_limit=money_limit

    def start(self):
        print("started") 
    def cashwithdrawal1(self):
        print("cashwithdrawal")
    def stop(self):
        print("stop") 
    

Atm=Atm("atm","out","ruppees")
Atm.start()
Atm.cashwithdrawal1()
Atm.stop()
