def tracklist(**kwargs):
    for n in kwargs:
        print(n)
        for x in kwargs[n]:
            print("ALBUM: " + x + " TRACK: " + kwargs[n][x])
