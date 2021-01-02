creditos= ("Alberto","Oforte", 2016 )
def pedirtweet(usuario):
    tweet = None
    tweet = input("Que esta pasando= ")
    likes= 0
    retweets= 0 
    likes= int(input("Cuantos likes? "))
    retweets= int(input("Cuantos retweets? "))
    infotweet= {"Autor": usuario,"Mensaje": tweet, "Likes": likes, "Retweets": retweets}
    return infotweet
