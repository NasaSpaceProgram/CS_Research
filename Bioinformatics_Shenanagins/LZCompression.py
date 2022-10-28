from math import floor, log2

from random import randrange
def randomBinary(n):
    oupt = ""
    for i in range(n):
        oupt += str(randrange(0,2))
    return(oupt)
def makeBinary_fixed(n,l):
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

def makeBinary(n):
    if n == 0:
        return("0")
    l = floor(log2(n)) + 1 
    rem = n
    oupt = ""
    for i in range(l):
        if rem >= 2**(l-i-1):
            oupt += "1"
            rem -= 2**(l-i-1)
        else:
            oupt += "0"

    return(oupt)
def length_for_binary(n):
    if log2(n) % 1 == 0:
        return(floor(log2(n)))
    else:
        return(floor(log2(n))+1)

def MakeBinaryDictionary(lst):
    if len(lst) == 0:
        return({})
    l = length_for_binary(len(lst)) 
    oupt = {}
    for i in range(len(lst)):
        oupt[str(lst[i])] = makeBinary_fixed(i,l)
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

def isInDict(s,d):
    keys = d.keys()
    for key in keys:
        if d[key] == s:
            return((True,key))
    return((False,0))


def lzEncoder(s, input_alphabet = [0,1], input_dictionary = False, output_dictionary = False):
    """Takes in string S and outputs and ancoded sring"""
    encode_length = length_for_binary(len(input_alphabet))
    if not input_dictionary:
        dic = MakeBinaryDictionary(input_alphabet)
    else:
        dic = input_dictionary
    oupt = [dic[s[0]]]
    i=1
    curr = s[0]
    while i < len(s):
        old = curr
        curr += s[i]
        
        if not curr in dic.keys():
            if length_for_binary(len(dic)) > encode_length:
                encode_length = length_for_binary(len(dic))
                for j in range(len(dic)):
                    dic[list(dic.keys())[j]] = makeBinary_fixed(j,encode_length)
                dic[curr] = makeBinary_fixed(len(dic),encode_length)

            else:
                dic[curr] = makeBinary_fixed(len(dic),encode_length)
            curr = curr[-1]
            oupt.append(dic[old])
            
        i +=1

    oupt.append(dic[curr])
       
    if not output_dictionary:
        return(oupt[1:])
    else:
        return(oupt[1:],dic)




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


def Mutual_Compression_ratio(s1,s2, zip = False):
    if zip:
        s12 = zipper(s1,s2)
    else:
        s12 = s1 + s2
    return(lzCompression_ratio(s1)+lzCompression_ratio(s2)-2*lzCompression_ratio(s12))

def Mutual_Compression_ratio2(s1,s2):
    return(lzCompression_ratio(s2)-Mutual_Compression_Crossed2(s1,s2))


def Mutual_Compression_Crossed(s1,s2):
    (s1Encoded,s1Dic) = lzEncoder(s, input_alphabet = [0,1], input_dictionary = False, output_dictionary = True)
    (s2Encoded,s2Dic) = lzEncoder(s, input_alphabet = [0,1], input_dictionary = False, output_dictionary = True)

    (s1Encoded2,s1Dic2) = lzEncoder(s, input_alphabet = [0,1], input_dictionary = s2Dic, output_dictionary = True)
    (s2Encoded2,s2Dic2) = lzEncoder(s, input_alphabet = [0,1], input_dictionary = s1Dic, output_dictionary = True)

    return(
        (len("".join(s1Encoded2)) + len("".join(s2Encoded2)))/(len(s1+s2))# try deviding by n instead of 2n
    )

def Mutual_Compression_Crossed2(s1,s2):
    (s1Encoded,s1Dic) = lzEncoder(s1, output_dictionary = True)
    (s12Encoded,s12Dic) = lzEncoder(s2, input_dictionary = s1Dic, output_dictionary = True)
    return(len("".join(s12Encoded))/ len(s1))


A = ["#","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W", "X", "Y","Z"]
s = "TOBEORNOTTOBEORTOBEORNOT"
(lst,dic) = lzEncoder(s, input_alphabet = A, output_dictionary = True)
print(dic)
for i in lst:
    for key in dic.keys():
        if dic[key] == i:
            print(key)
print(lst)
print(len("".join(lst)))

