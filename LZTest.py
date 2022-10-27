from LZCompression import *

def main(n, startLen, EndLen):
    f = open("Test.csv", "w")

    s1 = randomBinary(startLen)
    s2 = randomBinary(startLen)
    add_amount = (EndLen-startLen)//n
    if add_amount<1:
        add_amount = 1
    f.write("length of strings, compression ratio of s1, compression ratio of s2, mutual compression ratio, mutual compression ratio zipped, mutual compression ratio crossed, s1, s2 \n")
    for i in range(n):
        oupt = []
        oupt.append(str(len(s1)))
        oupt.append(str(lzCompression_ratio(s1)))
        oupt.append(str(lzCompression_ratio(s2)))
        oupt.append(str(Mutual_Compression_ratio(s1,s2)))
        oupt.append(str(Mutual_Compression_ratio(s1,s2, zip= True)))
        oupt.append(str(Mutual_Compression_Crossed(s1,s2)))
        oupt.append(s1)
        oupt.append(s2)
        f.write(",".join(oupt) + "\n")
        s1 += randomBinary(add_amount)
        s2 += randomBinary(add_amount)

    f.close()


def main2(n, startLen, EndLen):
    f = open("Retry_new_zip.csv", "w")

    s1 = randomBinary(startLen)
    s2 = randomBinary(startLen)
    add_amount = (EndLen-startLen)//n
    if add_amount<1:
        add_amount = 1
    f.write("length of strings, compression ratio of s1, compression ratio of s2, joint compression, joint compression zipped,Mutual compression ratio, Mutual compression ratio Zipped, s1, s2 \n")
    for i in range(n):
        oupt = []
        oupt.append(str(len(s1)))
        oupt.append(str(lzCompression_ratio(s1)))
        oupt.append(str(lzCompression_ratio(s2)))
        oupt.append(str(lzCompression_ratio(s1+s2)))
        s12 = zipper(s1,s2)
        oupt.append(str(lzCompression_ratio(s12)))
        oupt.append(str(Mutual_Compression_ratio(s1,s2)))
        oupt.append(str(Mutual_Compression_ratio(s1,s2, zip= True)))
        oupt.append(s1)
        oupt.append(s2)
        f.write(",".join(oupt) + "\n")
        s1 += randomBinary(add_amount)
        s2 += randomBinary(add_amount)

    f.close()


def CrossedPropertyTest1(n, startLen, EndLen):
    f = open("CrossedPropertyTest.csv", "w")

    s1 = randomBinary(startLen)
    s2 = randomBinary(startLen)
    add_amount = (EndLen-startLen)//n
    if add_amount<1:
        add_amount = 1
    f.write("length of strings, compression ratio of s1, compression ratio of s2 , joint compression , Mutual compression crossed(s1:s1), Mutual compression crossed(s2:s2), Mutual compression crossed(s1:s2), Mutual compression crossed(s1:s2), s1, s2 \n")
    for i in range(n):
        oupt = []
        oupt.append(str(len(s1)))
        oupt.append(str(lzCompression_ratio(s1)))
        oupt.append(str(lzCompression_ratio(s2)))
        oupt.append(str(lzCompression_ratio(s1+s2)))
        oupt.append(str(Mutual_Compression_Crossed(s1,s1)))
        oupt.append(str(Mutual_Compression_Crossed(s1,s2)))
        oupt.append(str(Mutual_Compression_Crossed(s1,s2)))
        oupt.append(str(Mutual_Compression_Crossed(s2,s1)))
        oupt.append(s1)
        oupt.append(s2)
        f.write(",".join(oupt) + "\n")
        s1 += randomBinary(add_amount)
        s2 += randomBinary(add_amount)

    f.close()

def Crossed2PropertyTest1(n, startLen, EndLen):
    f = open("Crossed2PropertyTest.csv", "w")

    s1 = randomBinary(startLen)
    s2 = randomBinary(startLen)
    add_amount = (EndLen-startLen)//n
    if add_amount<1:
        add_amount = 1
    f.write("length of strings, compression ratio of s1, compression ratio of s2 , joint compression , Mutual compression crossed(s1:s1), Mutual compression crossed(s2:s2), Mutual compression crossed(s1:s2), Mutual compression crossed(s2:s1), s1, s2 \n")
    for i in range(n):
        oupt = []
        oupt.append(str(len(s1)))
        oupt.append(str(lzCompression_ratio(s1)))
        oupt.append(str(lzCompression_ratio(s2)))
        oupt.append(str(lzCompression_ratio(s1+s2)))
        oupt.append(str(Mutual_Compression_Crossed2(s1,s1)))
        oupt.append(str(Mutual_Compression_Crossed2(s2,s2)))
        oupt.append(str(Mutual_Compression_Crossed2(s1,s2)))
        oupt.append(str(Mutual_Compression_Crossed2(s2,s1)))
        oupt.append(s1)
        oupt.append(s2)
        f.write(",".join(oupt) + "\n")
        s1 += randomBinary(add_amount)
        s2 += randomBinary(add_amount)

    f.close()

def CrossedPropertyTestBinary(n, startLen, EndLen):
    f = open("CrossedPropertyTest_withBinaryStrings.csv", "w")

    s1 = randomBinary(startLen)
    s2 = randomBinary(startLen)
    add_amount = (EndLen-startLen)//n
    if add_amount<1:
        add_amount = 1
    f.write("length of strings, compression ratio of s1, compression ratio of s2 , joint compression , Mutual compression crossed(s1:s1), Mutual compression crossed(s2:s2), Mutual compression crossed(s1:s2), Mutual compression crossed(s1:s2), s1, s2 \n")
    for i in range(n):
        oupt = []
        oupt.append(str(len(s1)))
        oupt.append(str(lzCompression_ratio_Binary(s1)))
        oupt.append(str(lzCompression_ratio_Binary(s2)))
        oupt.append(str(lzCompression_ratio_Binary(s1+s2)))
        oupt.append(str(Mutual_Compression_Crossed2(s1,s1)))
        oupt.append(str(Mutual_Compression_Crossed2(s1,s2)))
        oupt.append(str(Mutual_Compression_Crossed2(s1,s2)))
        oupt.append(str(Mutual_Compression_Crossed2(s2,s1)))
        oupt.append(s1)
        oupt.append(s2)
        f.write(",".join(oupt) + "\n")
        s1 += randomBinary(add_amount)
        s2 += randomBinary(add_amount)

    f.close()


main2(100, 10, 1000)