states = ['Andhra','Telangana','Assam']
capitals = ['vizag','amaravathi','dispur']
ind = capitals.index('vizag')
print(states[ind])

# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' }
print(europe.keys())
print(europe.values())
print(europe['spain'])

lands = {'india':44,'pak':33,'srilanka':55}
lands['usa'] = 22
del lands['pak']
print(lands)
print(lands['india'])