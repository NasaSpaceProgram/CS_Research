from LZWMutInfo import *
def lzCompression_ratio(s, ia = [0,1]):
    return(len("".join(lzEncoder(s, input_alphabet = ia)))/len(s))

def Conditional_Comrpession(s2,s1):
    (s1Encoded,s1Dic) = lzEncoder(s1, output_dictionary = True)
    (s12Encoded,s12Dic) = lzEncoder(s2, input_dictionary = s1Dic, output_dictionary = True)
    return(len("".join(s12Encoded))/ len(s1))


def Mutual_Compression_ratio(s1,s2, zip = False):
    if zip:
        s12 = zipper(s1,s2)
        ia = [0,1,2,3]

    else:
        s12 = s1 + s2
        ia = [0,1]
    return(lzCompression_ratio(s1, ia = ia)+lzCompression_ratio(s2, ia= ia)-2*lzCompression_ratio(s12, ia = ia))

def Mutual_Compression_ratio1(s1,s2):
    ia = [0,1]
    return(lzCompression_ratio(s1, ia = ia)+lzCompression_ratio(s2, ia= ia)-Conditional_Comrpession(s1,s2))


def Mutual_Compression_Crossed(s1,s2):
    (s1Encoded,s1Dic) = lzEncoder(s1, input_alphabet = [0,1], input_dictionary = False, output_dictionary = True)
    (s2Encoded,s2Dic) = lzEncoder(s2, input_alphabet = [0,1], input_dictionary = False, output_dictionary = True)

    (s1Encoded2,s1Dic2) = lzEncoder(s1, input_alphabet = [0,1], input_dictionary = s2Dic, output_dictionary = True)
    (s2Encoded2,s2Dic2) = lzEncoder(s2, input_alphabet = [0,1], input_dictionary = s1Dic, output_dictionary = True)

    return(
        (len("".join(s1Encoded2)) + len("".join(s2Encoded2)))/(len(s1)+len(s2))# try deviding by n instead of 2n
    )

def Mutual_Compression_ratio_Crossed(s1,s2):
    ia = [0,1]
    return(lzCompression_ratio(s1, ia = ia)+lzCompression_ratio(s2, ia= ia)-Mutual_Compression_Crossed(s1,s2))



def Mutual_Compression_ratio2(s1,s2):
    return(lzCompression_ratio(s2)-Conditional_Comrpession(s1,s2))