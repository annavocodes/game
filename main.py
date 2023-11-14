import random
from rpi_ws281x import PixelStrip, Color
import time

COUNT = 64
PIN   = 12
FREQ  = 800000
DMA   = 10
BRIGHTNESS = 50
INVERT = False
CHANNEL = 0

strip = PixelStrip(COUNT, PIN, FREQ, DMA, BRIGHTNESS, INVERT, CHANNEL)
strip.begin()

def color(strip, color):
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()

name = input("What is your name? ")
print("Welcome " + name + "! I'm thinking of a number between 1 and 100")

my_number = random.randint(1,100)
guess = []
for guess_number in range(1,11): 
  valid_guess = False
  while not valid_guess:
    try:
      user_guess = int(input("Take a guess...\n"))
      valid_guess = True
    except ValueError:
      print("Please provide a valid number.")
      
  difference = abs(my_number - user_guess)
  guess.append(user_guess)

  if user_guess < my_number and difference > 10: 
    print("Your guess is very low. Try again.")
  elif user_guess < my_number and difference < 10:
    print("Your guess is a little low. Try again.")
  elif user_guess > my_number and difference > 10:
    print("Your guess is very high. Try again.")
  elif user_guess > my_number and difference < 10:
    print("Your guess is a little high. Try again.")
  else:
    break
  color(strip, Color(255, 0, 0))

if user_guess == my_number:
  color(strip, Color(0, 255, 0))
  print("You won, " + name + "! You guessed my number in " + str(guess_number) + " guesses.")
  print("Your guesses were: " + " ".join(str(x) for i in guess))
  time.sleep(4)
  color(strip, Color(0,0,0))
else:
    print("Sorry! You didn't guess my number. The number I am thinking of is " + str(my_number))
    time.sleep(4)
    color(strip, Color(0,0,0))
  