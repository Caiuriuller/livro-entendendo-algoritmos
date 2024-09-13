
def search(list, nameTosearch, searches=0):
   searches += 1
   indexOfMiddleArray = (int(len(list) / 2) - 1)
   nameInMiddleList = list[indexOfMiddleArray]
   
   if (nameInMiddleList == nameTosearch):
       return searches
   elif (nameTosearch < nameInMiddleList):
       return search(list[:indexOfMiddleArray], nameTosearch, searches)
   else:
       return search(list[indexOfMiddleArray+1:], nameTosearch, searches)