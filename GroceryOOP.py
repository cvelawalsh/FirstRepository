class Stock:

  category = 'Grocery Item'

  def __init__(self, stock_code, description, buy_price, mark_up):
      self.code = stock_code
      self.desc = description
      self.buy = buy_price
      self.margin = mark_up

# Creating an object

C298 = Stock('C298', 'Chicken Soup', 0.75, 1.553)

print("Hello, world")

print(C298)
print(dir(C298), '\n')

print(C298.category)
print(C298.desc)
print(C298.buy)
print(C298.margin)
print(C298.code, '\n')

print('In the {} category we have {} at a cost price of ${}.'.format(C298.category, C298.desc, C298.buy))
