def countWord(word):
    if word[0] == " ":
        count = 0
    else:
        count = 1
    for i in range(len(word)-1):
        if word[i] == " " and word[i+1] != " ":
            count += 1
    return count

# print(countWord("   hello dsf   sdf   sdf sdf  sd f sd   sd f sdf  "))


def checkPrime(n): 
    if n < 2:
        return 0
    elif n < 4:
        return 1
    else:
        for i in range(2, n//2):
            if n % i == 0:
                return 0
    return 1
def calString(data):
    data += "h"
    data = list(data)
    cur = 0
    total = 0
    sign = 1
    for i in data:  
        if i.isdigit():
            cur = 10*cur + int(i)
        if i == "-":
            sign *= -1
        if i != "-" and i != "+" and (not i.isdigit()):
            print(sign*cur)
            if checkPrime(cur*sign):
                total += cur * sign
            cur = 0
            sign = 1
    return total

# print(calString("---37@bai5@nay1@2de-----3dung#31hong-12"))
        
def haha(data):
    data = list(data)
    for i in range(len(data)):
        if data[i].isalpha():
            data[i] = "+"
    hihi = "".join(data)
    return eval(hihi)
# print(haha("--38bai6nay12de-----3dung1hong-12"))
def twoSum(nums ,target):
        data = dict()
        for index, value in enumerate(nums):
            if (target - value) in data:
                return [index, data.get(target - value)]
            else:
                data[value] = index
  


#   __________________________________________

def solvePro(lst,target):
    for i in range(len(lst)):
        for j in range(i,len(lst)):
            if lst[i] + lst[j] == 9:
                return (i,j)
    return None

# print(solvePro([1,2,5,6,7], 9))
# print(twoSum([1,2,5,6,7], 9))
# _______________________________

def getMostt(data):
    data = data.lower().split()
    compare = dict()
    for val in data:
        compare[val] = compare.get(val, 0) +1
    
    result = sorted(compare.items(), key = lambda x : x[1], reverse = True)
    return result[0]

    # most = 0
    # res = None
    # for key, value in compare.items():
    #     if value > most:
    #         most = value
    #         res = key
    # return res, most
# _______________


def getMost(data):
    data = data.lower().split()
    result = dict()
    k = None
    Value = 0

    for val in data:
        result[val] = result.get(val,0) + 1
        if result[val] > Value:
            Value = result[val]
            k = val

    return (k, Value) 


# print(getMost("aa bb AA AA aa aa cc"))

# _____________________

def generateEmail(data):
    data = data.lower().split()
    res = data[-1]
    for i in range(len(data) -1):
        res += data[i][0]
    return res + "@gmail.com"

# print(generateEmail("Nguyen Vu Linh"))  

# ____________________
def twoSum(nums ,target):
        data = dict()
        for index, value in enumerate(nums):
            if (target - value) in data:
                return [index, data.get(target - value)]
            else:
                data[value] = index
# ----

def getDuplicate(lst):
    data = dict()
    for value in lst:
        if value in data:
            return value
        else:
            data[value] = value



# print(getDuplicate([1,2,1,2,3,3,2,1]))
# -----------------------


def getBiggestSequence(lst, n):
    maxval = None
    for i in range(len(lst) - n + 1):
        if maxval is None  or sum(lst[i:i+n]) > maxval:
            maxval = sum(lst[i:i+n])
    return maxval

# print(getBiggestSequence([1,2,3,4,5],2))

# tong cac chu so cua 1 so .

def getSumofDitgit(n):
    temp = 0
    while n > 9:
        for num in str(n):
            temp += int(num)
        n = temp
        temp = 0
    return n

print(getSumofDitgit(123456))