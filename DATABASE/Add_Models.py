from Models import Session, Customer, Goods
Session1 = Session()
customer1 = Customer(customerId = 2228, customername = 'Kiborg', firstName = 'Andriy', lastName = 'Levitskiy', email = 'a_lrvitskiy22@gmail.com', password = '1143424', phone = '+380504658342')
goods1 = Goods(goodsId = 11, name = "Watch", price = 2750, status = 3)

Session1.add(customer1)
Session1.add(goods1)

Session1.commit()
Session1.close()
