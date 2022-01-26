from datetime import date


print("welcome.")
m = input("enter your birth month: >")
d = input("enter your birth day: >")
y = input("enter your birth year: >")

print("you were born on", m, d, y)
print("happy birthday" * 3)

td = date.today()
print(td)