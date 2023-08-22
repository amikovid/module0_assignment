cars=["toyota","bmw","chrysler","fiat","honda"]

def car_adder():
    inpu1= input("Which car do you want to add?")
    inpu1= str(inpu1)
    print(inpu1)
    cars.append(inpu1)
    print(cars)

car_adder()

