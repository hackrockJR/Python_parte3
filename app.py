from twitter.tweets.listar import flistatweets
from twitter.tweets.pedir import pedirtweet

infotweet = {}
listatweet = []
print("Bienvenidos a la aplicacion.")
usuario= input("Cual es tu usuario= ")
otro= "s"
i = 1 

while otro == "s":
    print("Tweet numero:", i)
    i += 1
    infotweet= pedirtweet(usuario)
    listatweet.append(infotweet)
    otro = input ("Desea introducir un nuevo tweet? s/n:")

flistatweets(listatweet)
print(dir())
print("Esta instuccion se va ejecutar siempre")
