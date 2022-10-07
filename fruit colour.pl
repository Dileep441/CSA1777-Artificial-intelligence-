colour(red).
colour(yellow).
colour(red).
colour(green).
colour(orange).

fruit(cherry).
fruit(banana).
fruit(apple).
fruit(apple).
fruit(orange).

item(cherry,red).
item(banana,yellow).


find(X,Y):-item(X,Y),colour(Y).
kiran(X,Y):-item(apple,Y),fruit(X).
