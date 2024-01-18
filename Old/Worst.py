from LZCompression import *
#testing to make sure it is the wo
"""for n in range(1000):
    n += 1
    wst = Worst4(n)
    rnd = randomBinary(n)
    wstComp = lzEncoder(wst)
    rndComp = lzEncoder(rnd)
    if len(wstComp) < len(rndComp):
        print(len(wstComp), len(rndComp))
        print(wst[:100], rnd[:100])"""
# make worst csv
f = open("worst4_1.csv", "w")
f.write("n,len(lz(worst(n))),delta ,encod \n")
pre = 0
for n in range(1,100):
    print(n)
    encod = lzEncoder(Worst4(n))
    delta = len(''.join(encod)) - pre
    pre = len(''.join(encod))
    encwords = len(encod)
    if n < 3:
        f.write(f"{n},{pre},{delta},[{'  '.join(encod)}]\n")
        #f.write(f"{n},{pre},{delta},{encwords},[{'  '.join(encod)}]\n")
    else:
        f.write(f"{n},{pre},{delta},[{'  '.join(encod)}]\n")
        #f.write(f"{n},{pre},{delta},{encwords},[{'  '.join(encod[-3:])}]\n")
f.close()

# f = open("worst4.txt", "w")
# f.write("n,len(lz(worst(n)))\n")
# for n in range(1,200):
#     encod = lzEncoder(Worst4(n))
#     f.write(f"{encod}\n")
# f.close()