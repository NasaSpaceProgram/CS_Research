from math import floor, log2


# =========================== Binary Numbers ===========================
def length_for_binary(n):
    """retunrs the lenght a binary string would need to be to encode the number n"""
    if log2(n) % 1 == 0:
        return(floor(log2(n)))
    else:
        return(floor(log2(n))+1)

def MakeBinaryDictionary(lst):
    """lst =  input alphabet
    Generates starting dictionary with lst as the keys and associated binary stings as the values"""
    if len(lst) == 0: # if our input alphabet is the empty set then we can just return an empty dictionary
        return({})

    l = length_for_binary(len(lst)) # set the length of all the binary strings to be 
    oupt = {}
    for i in range(len(lst)):
        oupt[str(lst[i])] = makeBinary_fixed(i,l) # for each value in the input alphabet make a dictionary entry and a corrisponding binary string
    return(oupt)

def MakeBinaryDictionary_for_Decoder(lst):
    """lst =  input alphabet
    Generates starting dictionary with binary strings as keys to values in the input alphabet"""
    if len(lst) == 0: # if our input alphabet is the empty set then we can just return an empty dictionary
        return({})

    l = length_for_binary(len(lst)) # set the length of all the binary strings to be 
    oupt = {}
    for i in range(len(lst)):
        oupt[makeBinary_fixed(i,l)] = str(lst[i]) # for each value in the input alphabet make a dictionary entry and a corrisponding binary string
    return(oupt)

def makeBinary_fixed(n,l):
    """returns a string representing an integer n in binary of length l 
    Note: """
    rem = n
    oupt = ""
    for i in range(l):
        if rem >= 2**(l-i-1):
            oupt += "1"
            rem -= 2**(l-i-1)
        else:
            oupt += "0"
    return(oupt)


# =========================== LZW Encod/Decod ===========================
def lzEncoder(s, input_alphabet = [0,1], input_dictionary = False, output_dictionary = False):
    """ Takes in string string s and encodes it into a list of strings
        s = input string
        input_aplhabet = list containing all elements of the alphabet used to begin encoding sting s
        input_dictionary = dictionary: used to secify input dictionary if it would be 
                          different from the one created by the inital alphabet
        output_dictionary = Boolian value: if true will output a tuple with the encoding 
                            and the dictionary, else will just output the encoding
    """
    encode_length = length_for_binary(len(input_alphabet)) # set the inital encoding lenght to accomidate the inital alphabet
    if not input_dictionary: # make the inital dictionary using the inital alphabet
        dic = MakeBinaryDictionary(input_alphabet)
    else:
        dic = input_dictionary

    oupt = [dic[s[0]]] # inital encoding must be what we initaly have in the dictionary for the first charicter in s
    i=1
    curr = s[0] #current charicter which we are looking at
    while i < len(s):
        old = curr 
        curr += s[i]
        
        if not curr in dic.keys(): #if the value is not in the current dictionary then we have to add it, otherwise we just need to keep adding to curr
            if length_for_binary(len(dic)) > encode_length: #Check if we need to update the dictionary to have larger binary strings
                encode_length = length_for_binary(len(dic))
                for j in range(len(dic)): #set all dictionary values to account for increased length of binary string
                    dic[list(dic.keys())[j]] = makeBinary_fixed(j,encode_length)
                dic[curr] = makeBinary_fixed(len(dic),encode_length) #update dictionary to include new value

            else:
                dic[curr] = makeBinary_fixed(len(dic),encode_length)#update dictionary to include new value
            curr = curr[-1] #change current so it is just the newest charicter
            oupt.append(dic[old])# Add the the encoding for the value that we did know
            
        i +=1

    oupt.append(dic[curr])# retreve the last part of the sequence
    if output_dictionary:
        return(oupt[1:],dic)
    else:
        return(oupt[1:])

    
def LZDecoderhelper(dictionary_Length,s,dic,encode_length,oupt = ""):
    if len(s) == encode_length:
        return(oupt + dic[s])
    curr = s[:encode_length] # get current encoding
    rest = s[encode_length:] # get the rest of the encoding
    oupt = oupt + dic[curr] # add the current encoding to the output string
    new_enc_len = length_for_binary(dictionary_Length+1)
    if new_enc_len > encode_length: #Check if we need to update the dictionary to have larger binary strings
        keys = list(dic.keys())
        new_dic = {}
        for j in range(dictionary_Length): #set all dictionary values to account for increased length of binary string
            new_dic[makeBinary_fixed(j,new_enc_len)] = dic.pop(keys[j])
        encode_length = new_enc_len
        curr = "0"+curr
        dic = new_dic
    if len(rest) >= encode_length: #check if we need another dicitonary value  
        new_dictionary_key = makeBinary_fixed(dictionary_Length,encode_length)# make the key for the new value for our dictionary
        dictionary_Length +=1 # update dictionary length
        dic[new_dictionary_key] = dic[curr] # we know our next value in our dictionary is going to be our last value with something else added on
        dic[new_dictionary_key] = dic[new_dictionary_key] + dic[rest[:encode_length]][0] # we know the missing value of our new dicitonary value is the first value in the next part
    return(LZDecoderhelper(dictionary_Length,rest,dic,encode_length,oupt = oupt))


    
def LZDecoder(s, input_alphabet = [0,1]):
    """ Takes in encoded string S and outputs decoded sring
        s = input string
        input_aplhabet = alphabet used for sting s, defalted to binary
        """
    n = len(input_alphabet) # get the length of the current dictionary
    encode_length = length_for_binary(n) # set the inital encoding lenght to accomidate the inital alphabet

    dic = MakeBinaryDictionary_for_Decoder(input_alphabet) # make the inital dictionary using the inital alphabet
    return(LZDecoderhelper(n,s,dic,encode_length))

# =========================== The Worst Sequence ===========================

def GetPossible(l, ls =[""], i=0):
    """Returns a list of all possible binary sequences of length l"""
    if i == l:
        return(ls)
    else:
        new_ls = []
        for j in ls:
            new_ls.append(j+"0")
            new_ls.append(j+"1")
        return(GetPossible(l, ls = new_ls, i = i+1))
    
def Worst(n):
    """Returns the sequence of length n with thw worst possible LZW encoding"""
    s = "0" #inital sequence starts at 0
    l = 2 #length of current strings to be added to dicitonary
    while len(s)<n: #we only need to continue to the given length
        possible =GetPossible(l) # get possible binary sequnces for current length
        sw0 = possible[:(len(possible)//2)] #split into vaules that start with 0 
        sw1 = possible[(len(possible)//2):] # and 1 respectivly
        
        i = 0
        while len(s)<n: #we only need to continue to the given length
            s += sw0[1+2*i][1:]+sw1[1+2*i][1:]+sw0[2*i][1:]+sw1[2*i][1:]#add "words" according to algorithum
            i+=1
            if i > 2**(l-2)-1:# ensure we are not reaching out of bounds in sw0 and sw1
                l += 1
                break
    return(s[:n])


def WorstLen(n):
  """Returns the LZW encoding length for the worst sequence of length n"""
  if n <= 4:
    return([1,2,5,7][n-1])
  i = 5 # iterator keeps track of where we are in the sequence
  Dict_word_Len = 2 #keeps track of the length of the words in the dictionary
  count = 7 # keeps track of current encoding length
  zeros_between_deltas = 1
  dict_len = 3
  for z in range(20):
    for d in range(2**(zeros_between_deltas+2)):
      dict_len += 1
      if i-1 >= n:
        return(count)
      elif floor(log2(dict_len)) - log2(dict_len) == 0 :
        for j in range(zeros_between_deltas):
          i += 1
        Dict_word_Len += 1
        count = count + 1 + Dict_word_Len
        i += 1
      else:
        for j in range(zeros_between_deltas):
          i += 1
        count = count + Dict_word_Len
        i += 1
    zeros_between_deltas += 1


# =========================== Mutual Information Definitions ===========================

def zipper(s1,s2):
    """Binary Zipper"""
    oupt = ""
    for i in range(len(s1)):
        oupt += str(int(s1[i])*1 + int(s2[i])*2)
    return(oupt)

def lzCompression_ratio(s, ia = [0,1]):
    return(len("".join(lzEncoder(s, input_alphabet = ia)))/len(s))


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

def Conditional_Comrpession(s2,s1):
    (s1Encoded,s1Dic) = lzEncoder(s1, output_dictionary = True)
    (s12Encoded,s12Dic) = lzEncoder(s2, input_dictionary = s1Dic, output_dictionary = True)
    return(len("".join(s12Encoded))/ len(s1))


def Mutual_Compression_ratio2(s1,s2):
    return(lzCompression_ratio(s2)-Conditional_Comrpession(s1,s2))




# =========================== New Definitionsß ===========================