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
    return(oupt)

s = "AABABBABBAABA"
enc = lzEndoder(s)
print("Length of string:" + str(len(s)))
lenenc = 0
for ele in enc:
    lenenc = lenenc + len(ele)
print("Length of encoded string:" + str(lenenc))
print(lzDecoder(enc))
