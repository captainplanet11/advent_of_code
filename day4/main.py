import hashlib 
secrect_key = open("input.txt").read().strip()


number = 1

while True:
    #combine the secret key and the current number
    to_hash = f"{secrect_key}{number}"

    #compute the MD5 hash
    hash_result = hashlib.md5(to_hash.encode()).hexdigest()
    if hash_result.startswith("000000"):
        print(number)

    number += 1

