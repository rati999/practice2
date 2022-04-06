class fruits:
    def __init__(self, fruit_name, fruit_weight):
        self.fruit_name = fruit_name
        self.fruit_price = fruit_weight


f1 = fruits("watermelon", 20)

print("Fruit Name and weight : " + f1.fruit_name)
print(f1.fruit_price)