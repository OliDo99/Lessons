from turtle import * 
from random import randint 
bgcolor('black') 
x = 1
y = 0
speed(0) 
while x < 500: 
  
 r = randint(0,255) 
 g = randint(0,255)  
 b = randint(0,255) 
  
 colormode(255)  
 pencolor(r,g,b) 
 fd(5 + x) 
 rt(90 + y) 
 x = x+1 
 y = y +0.001
  
exitonclick() 