listOne = [ 1, 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 ,10]
listTwo = [2, 4, 6 , 8 ,10, 12 , 14 ,16 ,18 ,20]
#listOne = [ '1', '2' , '3', '4','5' , '6', '7' , '8', '9' ,'10']
#listTwo = ['2','4','6','8','10','12','14','16','18','20']
def addAndDisplayLists(listOne, listTwo):
    for x in range (len(listOne)):
        print (listOne[x], '+' , listTwo[x] , '=' ,  (listOne[x] + listTwo[x]))

def substractAndDisplayLists(listOne, listTwo):
    for x in range (len(listOne)):
        print (listOne[x], '-' , listTwo[x] , '=' ,  (listOne[x] - listTwo[x]))

def multiplyAndDisplayLists(listOne, listTwo):
    for x in range (len(listOne)):
        print (listOne[x], '*' , listTwo[x] , '=' ,  (listOne[x] * listTwo[x]))

def divideAndDisplayLists(listOne, listTwo):
    for x in range (len(listOne)):
        print (listOne[x], '/' , listTwo[x] , '=' ,  (listOne[x] / listTwo[x]))

addAndDisplayLists(listOne, listTwo)
substractAndDisplayLists(listOne, listTwo)
multiplyAndDisplayLists(listOne, listTwo)
divideAndDisplayLists(listOne, listTwo)