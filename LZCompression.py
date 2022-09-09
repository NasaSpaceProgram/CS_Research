def isInDict(s,d):
    keys = d.keys()
    for key in keys:
        if d[key] == s:
            return((True,key))
    return((False,0))
    
def lzEndoder(s):
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



def lzDecoder(lst):
    dic = {0:lst[0]}
    oupt = lst[0]
    i=0
    curr = ""
    currenc = ""
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

def lzCompression_ratio(s):
    return(len("".join(lzEndoder(s)))/len(s))

def Mutual_Compression_ratio(s1,s2):
    s12 = zipper(s1,s2)
    return(lzCompression_ratio(s1)+lzCompression_ratio(s2)-lzCompression_ratio(s12))
    
#==============Testing LZ Algorithum ============================================
#s = "AABABBABBAABA"
#s = "Hello My name is Noah Nice To meet you"
#enc = lzEndoder(s)
#print("Length of string:" + str(len(s)))
#lenenc = 0
#for ele in enc:
#    lenenc = lenenc + len(ele)
#print("Length of encoded string:" + str(lenenc))
#print(lzDecoder(enc))

#=======================Testing mutual Compression Ratio ===========================
#s1 = "1101001001101"
#s2 = "1101001001101"

s1 = "101000101101111111000011011100011001010001010000101111000110"
s2 = "001010101110000100000111110000100001111000001110000111000100"
print(lzCompression_ratio(s1))
print(lzCompression_ratio(s2))
s12 = zipper(s1,s2)
print(lzCompression_ratio(s12))
print(Mutual_Compression_ratio(s1,s2))