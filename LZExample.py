from math import floor, log2
def lzEncoder(s, input_alphabet = [0,1]):
    """ s = input string
        input_aplhabet = alphabet used for sting s, defalted to binary
        Takes in encoded string S and outputs decoded sring"""
    encode_length = length_for_binary(len(input_alphabet)) # set the inital encoding lenght to accomidate the inital alphabet

    dic = MakeBinaryDictionary(input_alphabet) # make the inital dictionary using the inital alphabet

    oupt = [dic[s[0]]] # inital encoding must be what we initaly have in the dictionary for the first charicter in s
    i=1
    curr = s[0] #current string which we are looking at
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
    return(oupt[1:])



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
    """ s = input string
        input_aplhabet = alphabet used for sting s, defalted to binary
        Takes in encoded string S and outputs decoded sring"""
    n = len(input_alphabet) # get the length of the current dictionary
    encode_length = length_for_binary(n) # set the inital encoding lenght to accomidate the inital alphabet

    dic = MakeBinaryDictionary_for_Decoder(input_alphabet) # make the inital dictionary using the inital alphabet
    return(LZDecoderhelper(n,s,dic,encode_length))
    
    
def LZExample(s , ia = [0,1]):
    print("==================")
    print("String to Encode: "+s)
    l1 = lzEncoder(s,input_alphabet=ia)
    print("Encoding List: "+str(l1))
    print("Encoding: "+"".join(l1))
    print("Decoded String:   "+LZDecoder("".join(l1), input_alphabet = ia))




#print(s)
#
#print(l1)


LZExample("000000")

LZExample("0100011011")

LZExample('TOBEORNOTTOBEORTOBEORNOT',ia=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"])

