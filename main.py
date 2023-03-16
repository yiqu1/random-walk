import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
########### Challenge 4 - Random Walk ########

directions = [0, 90, 180, 270]

def random_color():
  r = random.randint(0, 255)
  g = random.randint(0, 255)
  b = random.randint(0, 255)
  random_color = (r, g, b)
  return random_color
  
tim.width(15)
tim.speed("fastest")

for _ in range(50):
  tim.color(random_color())
  tim.forward(30)
  tim.setheading(random.choice(directions))