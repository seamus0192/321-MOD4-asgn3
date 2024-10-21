from Crypto.Hash import SHA256


# function that hashes a string and returns the digest
def sha256_hash(string):
    bytes = bytearray(string.encode('utf-8'))

    # create a SHA256 hash object with passed bytes
    hash_object = SHA256.new()
    hash_object.update(bytes)

    # get the hex digest
    return hash_object.hexdigest()


# function that given a string and a bit position, flips specified bit in string
def flip_bit(string, bit_position):
    # Convert the string to a list of bytes
    bytes = bytearray(string.encode('utf-8'))

    # find byte contains bit to flip, and bit's position within byte
    byte_idx = bit_position // 8
    bit_idx = bit_position % 8

    # flip the bit
    bytes[byte_idx] ^= (1 << bit_idx)

    return bytes.decode('utf-8')


# given 2 hashes, finds the hamming distance (# of different bits) between hashes
def hamming_distance(hash1, hash2):
    # convert the hashes back to binary format
    bin1 = bin(int(hash1, 16))[2:].zfill(256)
    bin2 = bin(int(hash2, 16))[2:].zfill(256)

    # Count the number of differing bits
    return sum(b1 != b2 for b1, b2 in zip(bin1, bin2))
