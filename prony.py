#card const is [rank,suit,[attrib1,attrib2...atribN]]
deck = [] 
for i in range (0, 14)
  for j in range(0, 4)
    deck.append([i,j,[]])
print(deck)
