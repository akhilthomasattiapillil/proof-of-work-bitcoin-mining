import random
import hashlib
import time

max_nonce=2**256
def solution(input, target):
    for nonce in range(max_nonce):
        # to create random numbers of 256bit
        i = random.randint(0, pow(2, 256))
        hash_result = hashlib.sha256((str(input) + str(i)).encode('utf-8')) #SHA256encryption
        hex_dig = hash_result.hexdigest()                                   #converting to hexadecimal
        hash_bin = str(bin(int(hex_dig,16)))                                #converting to binary
        hash_bin=hash_bin[2:]
        hash_10 = int(hash_bin,2)                                           #converting nounce to decimal
        target_10 = int(target,2)                                           #converting target to decimal
        print ('Nounces:',hash_10)
        if hash_10 <= target_10:
            print(" ")
            print('The final hash value or solution is:',i)                 #solution
            return str(i)
        else:
            i+=1
        if i<= pow(2,256):
            i = 0

if __name__ == "__main__":

    target_r = open("C:\\Users\\Akhil\\Desktop\\1 fall sem courses\\data security and privacy\\project 4\\d24performance.txt", "r", encoding='utf-8')
    target_in = target_r.read()
    print("target is",target_in)

    input_r = open("C:\\Users\\Akhil\\Desktop\\1 fall sem courses\\data security and privacy\\project 4\\input.txt", "r", encoding='utf-8')
    input_in = input_r.read()
    print("input is",input_in)

    print("Starting search...")

    # checkpoint the current time
    start_time = time.time()

    f = solution(input_in, target_in )
    w1 = open("C:\\Users\\Akhil\\Desktop\\1 fall sem courses\\data security and privacy\\project 4\\solution.txt", "w+")
    w1.write(f)
    w1.close()

    print(" ")
    print("Execution completed")

    # checkpoint how long it took to find a result
    end_time = time.time()

    elapsed_time = end_time - start_time
    print("Elapsed Time: %.4f seconds" % elapsed_time)

