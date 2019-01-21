import numpy as py
def main():
    no = input("enter the number of zeros:") # to enter no of zeros
    d=int(no)
    first = py.zeros(d, int)
    last = py.ones(256 - d, int)
    f = "".join(map(str, first))
    l = "".join(map(str, last))
    target = f + l              #concatenation ot two strings
    print(target)
    w1 = open("C:\\Users\\Akhil\\Desktop\\1 fall sem courses\\data security and privacy\\project 4\\target.txt" , "w+") #write file to target.txt
    w1.write(target)
    w1.close()

def main2():
    for no in range (21,27):            #to display targets with d from 21 to 26
        d=int(no)
        first = py.zeros(d, int)
        last = py.ones(256 - d, int)
        f = "".join(map(str, first))
        l = "".join(map(str, last))
        target2 = f + l
        print(target2)
        no+=1
        w2 = open("C:\\Users\\Akhil\\Desktop\\1 fall sem courses\\data security and privacy\\project 4\\targetforperformance.txt" , "w+")
        w2.write(target2)
        w2.close()


if __name__ == "__main__":
    main()
    print("Targets for performance reviews are shown below:")
    main2()
