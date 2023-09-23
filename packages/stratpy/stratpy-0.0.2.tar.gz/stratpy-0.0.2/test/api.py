from stratpy import *

game = Game("Prisoner's Dilemma")

# Create Players:
player1 = Player("South Korea")
player2 = Player("Japan")

# create utility:
a = Variable("A")
b = Variable("B")
c = Variable("C")
a > b == c


game + Decision(player1, "Commit")

print(game.root.name)

print(game.players)
print(game.title)
print(game.gametype)

print(f"{a.name} : {a.id}")
print(f"{b.name} : {b.id}")
print(f"{c.name} : {c.id}")
print("testing::")



print(b.lower)
print(b.equal)
print(b.higher)

# overload < > == to arrange variables

# a > b == c > d

# create a list with values over and values less
