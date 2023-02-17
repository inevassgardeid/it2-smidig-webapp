import json

def hent_books():
    fil = open("books.json")
    bøker = json.load(fil)
    fil.close()
    # for bok in bøker:
    #     bokliste = []
    #     bilde = bok["imageLink"]
    #     bokliste.append(bilde)
    #     return bokliste
    return bøker
