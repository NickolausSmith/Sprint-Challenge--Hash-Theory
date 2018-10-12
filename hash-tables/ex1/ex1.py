def get_indices_of_item_weights(weights, limit):
    #initialize hashtable
    pair = ()
    
    hashTable = {}

    for i, v in enumerate(weights):
        difference = limit - v
        
        if (check_valid(hashTable, difference)):
            
            if (hashTable[difference] > i):
                pair = (hashTable[difference], i)
            else:
                pair = (i, hashTable[difference])
        
        hashTable[v] = i

    return pair


def check_valid(hashtable, key):
    try:
        hashtable[key]
        return True
    except:
        return False


if __name__ == '__main__':
    # You can write code here to test your implementation using the Python repl
    pass