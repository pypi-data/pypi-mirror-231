from stratpy import Variable

#game = sp.Game("title", 2, type.Normal)
#print("hi")

#print(f"{game.title} {game.players} {game.gametype}")


#nash_game = [[10,-10,], [5, 5],
#             [0,0],     [15,18]]

#extenGame = Game(title="Game1", players=2,gametype=type.Normal, )



a = Variable("A")
b = Variable("B")
c = Variable("C")



print(f"{a.name} : {a.id}")
print(f"{b.name} : {b.id}")
print(f"{c.name} : {c.id}")
print("testing::")
a > b == c 
print(b.lower)
print(b.equal)
print(b.higher)


# overload < > == to arrange variables


# a > b == c > d

# create a list with values over and values less

