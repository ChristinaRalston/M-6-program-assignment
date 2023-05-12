from datetime import datetime

today = datetime.today()
datestr = today.strftime("It's %A, %B %d, %Y")

with open ("today.txt", "w") as file:
    file.write(datestr)

today = open("today.txt", "r")
data = today.read()
print(data)

parseit = datetime.strptime(data, "It's %A, %B %d, %Y").date()

print(parseit)