class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower
        
class Wheel:
    def __init__(self, size):
        self.size = size

class Car:
    def __init__(self, make, brand, horsepower, wheel_size):
        self.make = make
        self.brand = brand
        self.engine = Engine(horsepower)
        self.wheels = [Wheel(wheel_size) for _ in range(4)]

    def car_info(self):
        return (f"Car: {self.brand} {self.make}\n"
                f"Engine Horsepower: {self.engine.horsepower}\n"
                f"Wheel Size: {self.wheels[0].size} (x4)")

    def __str__(self):
        return self.car_info()


if __name__ == "__main__":
    # Create a sample car
    my_car = Car(make="Model S", brand="Tesla", horsepower=670, wheel_size=19)
    # Display car information
    print(my_car)
