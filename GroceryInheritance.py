class Stock:

  category = 'Groceries'

  def __init__(self, stock_code, description, buy_price, mark_up):
      self.code = stock_code
      self.desc = description
      self.buy = buy_price
      self.margin = mark_up

  def sell_price(self):
      print('Retail price = $', round(self.buy * self.margin, 2))

  def sale(self, discount):
      print('The discounted price of {} is $'.format(C298.desc), round(self.buy * self.margin * (1-discount), 2))

class Canned(Stock):
    category = 'Cans'

    def __init__(self, stock_code, description, buy_price, mark_up, volume, manuf):
        Stock.__init__(self, stock_code, description, buy_price, mark_up)
        self.volume = volume
        self.manuf = manuf

    def multi_buy(self):
        print('Buy two {} of {} {} {} and get one free. Pay only ${}'.format(self.category, self.manuf,
                                                                            self.volume, self.desc,
                                                                        round(self.buy * self.margin, 2)))

class Meat(Stock):
    category = 'Meat'

    def __init__(self, stock_code, description, buy_price, mark_up, weight, use_by):
        self.kilo = weight
        self.expiry = use_by
        Stock.__init__(self, stock_code, description, buy_price, mark_up)

    def Label(self):
        print(self.desc, '\nWeight: ', self.kilo, 'kgs', '\nExpiry: ', self.expiry)
        self.sell_price()

    def Expiring(self, discount):
        print('Price reduced for quick sale: ${}'.format(round(self.buy * self.margin * (1 - discount), 2)))

C401 = Meat('C401', 'Sirloin Steak', 4.16, 1.654, .324, '15 June 2021')
C298 =  Canned('C298', 'Chicken Soup', 0.75, 1.553, '400 mls', 'Campbells')

C401.Label()
print()
C401.Expiring(.35)
print()
C298.multi_buy()
