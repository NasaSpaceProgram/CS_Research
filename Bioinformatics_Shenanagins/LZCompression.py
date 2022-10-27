from math import floor, log2

from random import randrange
def randomBinary(n):
    oupt = ""
    for i in range(n):
        oupt += str(randrange(0,2))
    return(oupt)
def makeBinary(n,l):
    """returns a string representing an integer in binary"""
    rem = n
    oupt = ""
    for i in range(l):
        #print(2**(l-i-1))
        if rem >= 2**(l-i-1):
            oupt += "1"
            rem -= 2**(l-i-1)
        else:
            oupt += "0"
    return(oupt)

def CHAMP(n):
    oupt = ""
    i = 0
    while len(oupt)< n:
        i += 1
        for j in range(2**i):
            oupt += makeBinary(j,i)
    oupt = oupt[:n]
    return(oupt)

#print(CHAMP(100000))


def isInDict(s,d):
    keys = d.keys()
    for key in keys:
        if d[key] == s:
            return((True,key))
    return((False,0))
    
def lzEncoder(s):
    """Takes in string S and outputs and ancoded sring"""
    dic = {}
    oupt = []
    i=0
    curr = ""
    currenc = ""
    while i <= len(s)-1:
        curr = curr + str(s[i])
        isin = isInDict(curr,dic)
        if isin[0]:
            i = i +1
            currenc = str(isin[1])
        else:
            enc = currenc + str(curr[-1])
            dic[len(dic)] = curr
            oupt.append(enc)
            curr = ""
            currenc = ""
            i = i +1
            #print(dic)
    return(oupt)



def lzEncoder1(s, dic):
    """Takes in string S and outputs and ancoded sring"""
    oupt = []
    i=0
    curr = ""
    currenc = ""
    while i <= len(s)-1:
        curr = curr + str(s[i])
        isin = isInDict(curr,dic)
        if isin[0]:
            i = i +1
            currenc = str(isin[1])
        else:
            enc = currenc + str(curr[-1])
            dic[len(dic)] = curr
            oupt.append(enc)
            curr = ""
            currenc = ""
            i = i +1
            #print(dic)
    return((oupt,dic))

def lzEncoder2(s, dic):
    """Takes in string S and outputs and ancoded sring"""
    oupt = []
    i=0
    curr = ""
    currenc = ""
    while i <= len(s)-1:
        curr = curr + str(s[i])
        isin = isInDict(curr,dic)
        if isin[0]:
            i = i +1
            currenc = str(isin[1])
        else:
            if currenc == "" or currenc == "0":
                enc = currenc + str(curr[-1])
            else:
                #print(int(currenc))
                l = floor(log2(int(currenc)))+1 #take out if not binary
                enc = makeBinary(int(currenc),l) + str(curr[-1]) # enc = currenc + str(curr[-1])
            dic[len(dic)] = curr
            oupt.append(enc)
            curr = ""
            currenc = ""
            i = i +1
            #print(dic)
    return((oupt,dic))


def lzDecoder(lst):
    dic = {0:lst[0]}
    oupt = lst[0]
    for ele in lst[1:]:
        if len(ele) > 1:
            enc = int(ele[:len(ele)-1])
            dec = dic[enc] + ele[-1]
        else:
            dec = ele
        oupt = oupt + dec
        dic[len(dic)] = dec
        #print(dic)
    return(oupt)



def zipper(s1,s2):
    oupt = ""
    i = 0
    while i < len(s1):
        oupt = oupt + s1[i]
        if i <len(s2):
            oupt = oupt + s2[i]
        i = i+ 1
    while i< len(s2):
        oupt = oupt + s2[i]
        i = i+ 1
    return(oupt)
#def zipper(s1,s2):
#    """Binary Zipper"""
#    oupt = ""
#    for i in range(len(s1)):
#        oupt += str(int(s1[i])*1 + int(s2[i])*2)
#    return(oupt)

def lzCompression_ratio(s):
    return(len("".join(lzEncoder(s)))/len(s))

def lzCompression_ratio_Binary(s):
    return(len("".join(lzEncoder2(s,{})[0]))/len(s))

def Mutual_Compression_ratio(s1,s2, zip = False):
    if zip:
        s12 = zipper(s1,s2)
    else:
        s12 = s1 + s2
    return(lzCompression_ratio(s1)+lzCompression_ratio(s2)-2*lzCompression_ratio(s12))

def Mutual_Compression_ratio2(s1,s2):
    return(lzCompression_ratio(s2)-Mutual_Compression_Crossed2(s1,s2))


def Mutual_Compression_Crossed(s1,s2):
    (s1Encoded,s1Dic) = lzEncoder1(s1, {})
    (s2Encoded,s2Dic) = lzEncoder1(s2, {})

    (s1Encoded2,s1Dic2) = lzEncoder1(s1, s2Dic)
    (s2Encoded2,s2Dic2) = lzEncoder1(s2, s1Dic)
    #s1Encoded2 = 

    return(
        (len("".join(s1Encoded2)) + len("".join(s2Encoded2)))/(len(s1+s2))# try deviding by n instead of 2n
    )

def Mutual_Compression_Crossed2(s1,s2):
    (s1Encoded,s1Dic) = lzEncoder1(s1, {})
    (s2Encoded,s2Dic) = lzEncoder1(s2, {})
    (s12Encoded,s12Dic) = lzEncoder1(s2, s1Dic)
    return(len("".join(s12Encoded))/ len(s1))


    #return(
    #    (len("".join(s1Encoded2)) + len("".join(s2Encoded2)))/(len(s1+s2))
    #)












    
#==============Testing LZ Algorithum ============================================
#s = "AABABBABBAABA"
#s = "Hello My name is Noah Nice To meet you"
#enc = lzEncoder(s)
#print("Length of string:" + str(len(s)))
#lenenc = 0
#for ele in enc:
#    lenenc = lenenc + len(ele)
#print("Length of encoded string:" + str(lenenc))
#print(lzDecoder(enc))

#=======================Testing mutual Compression Ratio ===========================
#s1 = "1101001001101"
#s2 = "1101001001101"

#s1 = "101000101101111111000011011100011001010001010000101111000110"
#s2 = "001010101110000100000111110000100001111000001110000111000100"
#s1 = randomBinary(100)
#s2 = randomBinary(100)
#s2 = s1
#print(lzCompression_ratio(s1))
#print(lzCompression_ratio(s2))
#s12 = zipper(s1,s2)
#print(lzCompression_ratio(s12))
#print(Mutual_Compression_ratio(s1,s2))

#print(lzEncoder1(s1, {}))



#=======================Testing mutual Compression Ratio 2 ===========================

#s1 = randomBinary(100)
#s2 = randomBinary(100)
#s2 = s1
#print(lzCompression_ratio(s1))
#print(lzCompression_ratio(s2))
#print(Mutual_Compression_Crossed(s1,s2))

#print(CHAMP(100000))
#print(lzCompression_ratio_Binary(CHAMP(100000)))