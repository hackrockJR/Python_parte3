def flistatweets(listatweet):
    for tweet in listatweet:
        print(str(tweet))
        likes = tweet['Likes']
        retweets = tweet['Retweets']
        if likes > 2:
            print("Su tweet tiene 'me gustas'")
        elif likes == 1:
            print("Su tweet solo tiene un me gusta")
        elif likes == 2:
            print("Su tweet solo tiene dos me gustas")
        else:
            print("Su tweet no tiene 'me gustas'")
        
        if (retweets > 0): print("Este tweet tiene retweets")
        
