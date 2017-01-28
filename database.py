class Lost:
    ID = 0
    def __init__(self, name=None, gender=None, age=None, eyeColor=None,
                ethnicity=None, hairColor=None, lipColor=None, hairLength=None,
                noseShape=None, eyeShape=None, chinShape=None, lipShape=None):

        self.ID += 1

        self.name = name
        self.age = age
        self.gender = gender
        self.ethnicity = ethnicity
        self.eyeColor = eyeColor
        self.eyeShape = eyeShape
        self.hairColor = hairColor
        self.hairLength = hairLength
        self.lipColor = lipColor
        self.lipShape = lipShape
        self.noseShape = noseShape
        self.chinShape = chinShape

        self.childData = {"name": name, "gender": gender, "age": age,
                        "ethnicity": ethnicity, "eyeColor": eyeColor,
                        "eyeShape": eyeShape, "hairColor": hairColor,
                        "hairLength": hairLength, "lipColor": lipColor,
                        "lipShape": lipShape, "chinShape": chinShape}

        self.contactData = {}

        self.status = "lost"

		self.photo = None


    def setContactInformation(self, location=None, date=None, officer=None,
                              samaritan=None):

        self.contactData = {"date": date, "location": location,
                            "officer": officer, "samaritan": samaritan}

    def getContactInformation(self):
        return self.contactData

    def getChildInformation(self):
        return self.childData

    def setStatus(self, s):
        self.status = s

    def getStatus(self):
        return self.status

    def getID(self):
        return self.ID

	def setPhoto(self, img):
		self.photo = img

	def getPhoto(self):
		return self.photo


class Database:
    def __init__(self):

        self.totalNumber = 0
        self.lostNumber = 0

        self.lostChildren = []
        self.foundChildren = []

        self.categories = ["name", "gender", "ethnicity", "eyeColor",
                            "eyeShape", "hairColor", "hairLength",
                            "lipColor", "lipShape", "noseShape"]

    def addLostChild(self, name=None, gender=None, age=None, eyeColor=None,
                ethnicity=None, hairColor=None, lipColor=None, hairLength=None,
                noseShape=None, eyeShape=None, chinShape=None, lipShape=None,
                location=None, date=None, officer=None, samaritan=None):

        child = Lost(name=name, gender=gender, age=age, ethnicity=ethnicity,
                    eyeShape=eyeShape, eyeColor=eyeColor, hairColor=hairColor,
                    hairLength=hairLength, lipShape=lipShape, lipColor=lipColor,
                    noseShape=noseShape, chinShape=chinShape)

        child.setContactInformation(location=location, date=date,
                                    officer=officer, samaritan=samaritan)

        child.setStatus("lost")

        (self.lostChildren).append(child)

        self.lostNumber += 1
        self.totalNumber += 1

        return child.getID()

    def removeLostChild(self, ID):
        self.lostNumber -= 1

        i = binSearch(self.lostList, ID)
        child = self.lostList[i]
        child.setStatus("found")
        self.lostList.pop(i)
        self.foundChildren.append(child)

    def getPossibleChildren(self, name=None, gender=None, age=None, eyeColor=None,
                ethnicity=None, hairColor=None, lipColor=None, hairLength=None,
                noseShape=None, eyeShape=None, chinShape=None, lipShape=None,
                lastSeenDate=None):

        possibleList = []

        for lostChild in self.lostChildren:
            lostChildData = lostChild.getData()
            score = 0
            if lostChildData["gender"] != gender:
                continue

            score += weightName(name, lostChildData["name"])
            score += weightAge(age, lostChildData["age"])
            score += weightEthnicity(ethnicity, lostChildData["ethnicity"])
            score += weightEyeColor(eyeColor, lostChildData["eyeColor"])
            score += weightEyeShape(eyeShape, lostChildData["eyeShape"])
            score += weightHairColor(hairColor, lostChildData["hairColor"])
            score += weightHairLength(hairLength, lostChildData["hairLength"])
            score += weightLipColor(lipColor, lostChildData["lipColor"])
            score += weightLipShape(lipShape, lostChildData["lipShape"])
            score += weightNoseShape(noseShape, lostChildData["noseShape"])
            score += weightChinShape(chinShape, lostChildData["chinShape"])
            score += weightDate(lastSeenDate, lostChild.getContactInformation["date"])

            if score >= 0:
                possibleList.append((score, lostChild))

        quicksort(possibleList)
        return possibleList


def weightSkinColor (x, y):
	if (x == y):
       return 1
	else :
       return -3

def weightEyeColor (x, y):
   if (x == y):
       return 1
   else :
       return -3

def weightHairColor (x, y):
   if (x == y):
       return 1
   else :
       return -3

def weightHairLength (x, y):
   if (x == y):
       return 0.5
   else :
       return 0

def weightNoseShape (x, y):
   if (x == y):
       return 1
   else :
       return -0.5

def weightEyeShape (x, y):
   if (x == y):
       return 2
   else :
       return -1

def weightChin (x, y):
   if (x == y):
       return 2
   else :
       return -1

def weightLipColor (x, y):
   if (x == y):
       return 0.5
   else :
       return -0.5

def weightGender (x, y):
   if (x == y):
       return 1
   else :
       return -9999999

def weightAge (x, y):
   return 1 - (abs(x-y)*0,75)

def weightLipShape (x, y):
   if (x == y):
       return 1
   else :
       return 0.5

# date format: dd-mm-yyyy
def weightlastDate (x, y):

   date1 = x.split("-")
   date2 = y.split("-")

   if (int(date1[2]) != int(date2[2])):
       return -2
   elif (int (date[1]) != int(date2[1])):
       return -2
   elif (abs((int date1[0]) - int(date[0])) <=2):
       return 3
   else
       return -2

def quicksort(aList, i):
    _quicksort(aList, 0, len(aList) - 1, i)

def _quicksort(aList, first, last, i):
    if first < last:
        pivot = partition(aList, first, last, i)
        _quicksort(aList, first, pivot - 1 , i)
        _quicksort(aList, pivot + 1, last, i)

def partition(aList, first, last, j):
    pivot = first + random.randrange(last - first + 1)
    swap(aList, pivot, last)
    for i in range(first, last):
        if GE(aList[i], aList[last]):
            swap(aList, i, first)
            first += 1
    swap(aList, first, last)
    return first

def swap(A, x, y):
    A[x],A[y]=A[y],A[x]

def GE (a, b):
    return a[0] >= b [0]


def binSearch(lostList, target):
    L = len(lostList)
    start = 0
    end = L
    while start < end:
        mid = start + (end - start)/2
        if int((lostList[mid]).getID()) == int(target):
            return mid
        elif int((lostList[mid]).getID()) < int(target):
            start = mid + 1
        else:
            end = mid
    return -1
