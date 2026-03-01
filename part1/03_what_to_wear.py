#Please write a program which asks for tomorrow's weather forecast and then suggests weather-appropriate clothing.
#The suggestion should change if the temperature (measured in degrees Celsius) is over 20, 10 or 5 degrees, and also if there is rain on the radar.

print("What is the weather forecast for tomorrow?")

temp = int(input("Temperature:"))
rain = input("Will it rain (yes/no):")

c1 = temp<=5 
c2 = 5<temp<=10
c3 = 10<temp<=20 
c4 = temp>20

c6 = rain == "yes"

if c1:
    print("Wear jeans and a T-shirt")
    print("I recommend a jumper as well")
    print("Take a jacket with you")
    print("Make it a warm coat, actually")
    print("I think gloves are in order")

if c2:
    print("Wear jeans and a T-shirt")
    print("I recommend a jumper as well")
    print("Take a jacket with you")

if c3:
    print("Wear jeans and a T-shirt")
    print("I recommend a jumper as well")

if c4:
    print("Wear jeans and a T-shirt")

if c6:
    print("Don't forget your umbrella!")