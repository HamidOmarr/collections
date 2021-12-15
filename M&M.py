import random


MenMlistkleur = ['orangje','blauw', 'groen', 'bruin']

MenMDictionarykleur =	{
  "kleuren": ["rood" , "geel" , "groen" , "bruin"]

}



def MenMListbag(MenMlistkleur):
    RandomListMenM = []
    MenMListzak = int(input('Hoeveel M&M wil je?'))
    for x in range (MenMListzak):
        RandomListMenM.append(random.choice(MenMlistkleur))
        print (random.choice(MenMlistkleur))
    return RandomListMenM   


def MenMDictionaryBag(MenMDictionarykleur):
    RandomBagMenM = []
    MenMDictionaryzak = int(input('Hoeveel M&M wil je?'))
    for x in range (MenMDictionaryzak):
        RandomBagMenM.append(random.choice(MenMDictionarykleur["rood"]))
        print (random.choice(MenMDictionarykleur))



MenMDictionaryBag(MenMDictionarykleur)
