import time
import datetime

x = input("Podaj czas; ")

x = time.strptime(x, "%H:%M")
print(type(x))
x = list(x)
print(x)
