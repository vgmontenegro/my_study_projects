from fazenda import Talhao, Product, ProductType

A1 = Talhao('A1',100)

p1 = Product('Match', ProductType.INSECTICIDE)
p2 = Product('Perito', ProductType.INSECTICIDE)

p1.add_product()
p2.add_product()