# El usuario Jhon esta en una red social sus amigos son:
Jhon = {"Alice", "Bob", "Charlie", "David", "Eve"}

# La usuaria Jess Doe tiene los siguientes amigos
Jess = {"Alice", "Bob",  "Frank", "Grace"}

# ¿Tienen Jhon y Jess amigos en común?, ¿Cuales son?

comun = Jhon.intersection(Jess)

if comun:
    print('Los amigos en común que tienen son: ', comun)

else: 
    print('No tienen amigos en común')
