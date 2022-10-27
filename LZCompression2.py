def LZCompression(s, dictionary = {}):
    dic = dictionary


def zipper(s1,s2):
    """Binary Zipper"""
    oupt = ""
    for i in range(len(s1)):
        oupt += str(int(s1[i])*1 + int(s2[i])*2)
    return(oupt)

print(zipper("0101","0011"))