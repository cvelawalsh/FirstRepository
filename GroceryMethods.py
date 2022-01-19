class Stock:

  category = 'Grocery Item'

  def __init__(self, stock_code, description, buy_price, mark_up):
      self.code = stock_code
      self.desc = description
      self.buy = buy_price
      self.margin = mark_up

  def sell_price(self):
      print('Retail price = $', round(self.buy * self.margin, 2))

  def sale(self, discount):
      print('The discounted price of {} is $'.format(C298.desc), round(self.buy * self.margin * (1-discount), 2))



# Creating an object

C298 = Stock('C298', 'Chicken Soup', 0.75, 1.553)

C298.sell_price()

C298.sale(.15)

#print(C298)
