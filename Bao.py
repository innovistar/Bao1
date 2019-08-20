import random

i = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

x =+1
y =+1
while True:
    line = input("Pick:")
    price = 25
    if line == "A":
        x = random.choice(i)
        y = random.choice(i)
        if x > y:
            outcome = (price*2)
            print (x, y)
            print ("WON", outcome)
        elif x < y:
            outcome = price*0
            print (x, y)
            print ("LOST", outcome)
        continue
    elif line == "B":
        x = random.choice(i)
        y = random.choice(i)
        if y > x:
            outcome = price*2
            print (x, y)
            print ("WON", outcome)
        elif y < x:
            outcome = price*0
            print (x, y)
            print ("LOST", outcome)
        continue
    elif line == "done":
        break
exit()
        


  

