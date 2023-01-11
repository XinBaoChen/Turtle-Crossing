from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        self.x = 1
        
    def create_cars(self):
        #Generate random cars
        random_cars = random.randint(self.x,8)
        if random_cars < 5: 
            cars = Turtle("square")
            cars.shapesize(stretch_wid=1,stretch_len=2)
            cars.penup()
            cars.color(random.choice(COLORS))
            random_y = random.randint(-250,250) #The y axis is -300 to 300
            cars.goto(300,random_y)
            self.all_cars.append(cars)

    def more_cars(self):
        random_hard_cars = random.randint(self.x,15)
        if random_hard_cars < 10:
            cars = Turtle("square")
            cars.shapesize(stretch_wid=1,stretch_len=2)
            cars.penup()
            cars.color(random.choice(COLORS))
            random_y = random.randint(-250,250) #The y axis is -300 to 300
            cars.goto(300,random_y)
            self.all_cars.append(cars)

    def move_car(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
        if self.x < 5:
            self.x += 1
        if self.x == 4:
            self.more_cars()