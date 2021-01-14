from Models import Session, Customer, Goods
Session1 = Session()
customer1 = Customer(id = 118, customername = 'Kiborg', firstName = 'Andriy', lastName = 'Levitskiy', email = 'a_lrvitskiy22@gmail.com', password = '1143424', phone = '+380504658342')
customer2 = Customer(id = 128, customername = 'Lider', firstName = 'Bob', lastName = 'Vey', email = 'a_lrvitfjdefey22@gmail.com', password = '1143424', phone = '+380504658342')

goods1 = Goods(id = 111, name = "Watch", price = 2750, status = 3)
goods2 = Goods(id = 122, name = "Phone", price = 27000, status = 2)

Session1.add(customer1)
Session1.add(customer2)
Session1.add(goods1)
Session1.add(goods2)

Session1.commit()
Session1.close()
