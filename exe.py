import hashlib


key_list = []
hash_list = []



# use wordList File
def read_word_list():
    print('reading from  list')
    with open('wordlist.txt') as word_list:
        words = word_list.readlines()
        for strings in words :
            key_list.append( strings.strip() )






def MY24SHA( key ):

    hash_digest = hashlib.sha1(str(key).encode()).hexdigest()

    return hash_digest[:6]




def MY60SHA( key ):

    hash_digest = hashlib.sha1(str(key).encode('utf-8')).hexdigest()

    return hash_digest[:15]


#a



def collision(func):


   
    for key in key_list:

        key_obj = {
                'hash': func(key),
                'word': key
        }

        hash_list.append(key_obj )


    for word_hash in hash_list:
            
        check = word_hash
        found = False
        count = 0

        for hashes in hash_list:
            if hashes['word'] != check['word'] and hashes['hash'] == check['hash'] :
                print(f'6nibbs Collision for {hashes["word"]} and {check["word"]}  ')
                found = True
                break
        
        
    if not found :
        print('No Collision Found')







#check for collision
if len(key_list) == 0 :
    read_word_list()

#collision(MY24SHA)
collision(MY60SHA)













# collition   str(a) != str(b)    but hashFunc(str(a)) == hashFunc(str(b))








