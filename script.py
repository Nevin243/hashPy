import sys
import hashlib as hash

# Specifies the size of blocks to read the file as
BLOCKSIZE = 65536

def hash_select(selection):

    hash_select = {
        'md5' : hash.md5,
        'sha1' : hash.sha1,
        'sha256' : hash.sha256,
        'sha512' : hash.sha512,
    }

    # gets the funciton defaults to md5 if none selected
    func = hash_select.get(selection, lambda: hash.md5)

    return func()

# Filename from args
filename = sys.argv[2]

# Hash type from args
hasher = hash_select(sys.argv[1])

print ("Filepath: " + filename)

with open(filename, 'rb') as hash_file:
    file_buffer = hash_file.read(BLOCKSIZE)   
    while len(file_buffer) > 0:
        hasher.update(file_buffer)
        file_buffer = filename.read(BLOCKSIZE)

hash_out = hasher.hexdigest()

# Final print out
print ('Hash: ' + hash_out)

if len(sys.argv) > 3:
    if sys.argv[3] == hash_out:
        print ('Good hash')
    else:
        print('Bad hash')
    