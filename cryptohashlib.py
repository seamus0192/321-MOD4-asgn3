import string
import random
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


# hashes string with SHA256 and truncates the result to truncate_bits amount
def sha256_truncated(string, num_bits=32):
    hash_object = bytes.fromhex(sha256_hash(string))

    # Convert the hash to an integer, and truncate to the desired number of bits
    hash_int = int.from_bytes(hash_object, byteorder='big')

    # apply truncation by taking the remainder of division by 2^truncate_bits
    return hash_int % (2 ** num_bits)


# generate a random string of specified len
# random string generator from:
# https://stackoverflow.com/questions/2257441/random-string-generation-with-upper-case-letters-and-digits
def random_string(length=10):
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))


# find m1 such that H(m0) = H(m1), return m1 and # of attempts
def find_collision(m0, truncate_bits=32):
    hash_m0 = sha256_truncated(m0, truncate_bits)

    attempts = 0
    while True:
        m1 = random_string()

        # ensure m1 is not the same as m0
        if m1 == m0:
            continue

        hash_m1 = sha256_truncated(m1, truncate_bits)
        attempts += 1

        # Check for a collision
        if hash_m0 == hash_m1:
            return m1, attempts


# birthday paradox concept for finding a collision
def find_collision_birthday(truncate_bits=32):
    # dict to store the truncated hashes
    hash_table = {}

    attempts = 0
    while True:
        m = random_string()

        truncated_hash = sha256_truncated(m, truncate_bits)
        attempts += 1

        # check if this hash already exists in the table (signifies collision)
        if truncated_hash in hash_table:
            return hash_table[truncated_hash], m, attempts

        # store the truncated hash with corresponding rand string
        hash_table[truncated_hash] = m
