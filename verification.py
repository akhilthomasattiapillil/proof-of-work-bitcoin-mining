import hashlib
max_nonce=1                                 #only 1 verification
def verification(message,solution,target): #inputs message and solution into hash function and target to compare
    for nonce in range(max_nonce):

        hash_result = hashlib.sha256((str(message) + str(solution)).encode('utf-8'))       #hashfunction
        hex_dig = hash_result.hexdigest()
        hash_bin = str(bin(int(hex_dig,16)))
        hash_bin=hash_bin[2:]
        hash_10 = int(hash_bin,2)
        target_10 = int(target,2)
        print ('solution value is:',hash_10)
        if hash_10 <= target_10:
            print(" ")
            print('The final hash value is verified or solution is 1')      #1 if correct

        else:
            print('The solution is 0 ')                                     #0 if incorrect

if __name__ == "__main__":

    target_r = open("C:\\Users\\Akhil\\Desktop\\1 fall sem courses\\data security and privacy\\project 4\\target.txt", "r", encoding='utf-8')
    target_in = target_r.read()
    print("target is",target_in)

    input_r = open("C:\\Users\\Akhil\\Desktop\\1 fall sem courses\\data security and privacy\\project 4\\input.txt", "r", encoding='utf-8')
    input_in = input_r.read()
    print("input is",input_in)

    solution_r = open("C:\\Users\\Akhil\\Desktop\\1 fall sem courses\\data security and privacy\\project 4\\solution.txt",
                   "r", encoding='utf-8')
    solution_in = solution_r.read()
    print("solution in decimal  is", solution_in)

    print("Starting verification...")

    f = verification(input_in, solution_in,target_in)

    print(" ")
    print("Execution completed")



