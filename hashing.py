from cryptohashlib import sha256_hash, flip_bit, hamming_distance


def main():
    ex_string = "hello i am alive"
    hash_no_bit_flip = sha256_hash(ex_string)
    print(f"example string is: {ex_string}")
    print(f"SHA256 hash is   : {hash_no_bit_flip}")

    # flip the 8th bit in the string
    bit_flipped_string = flip_bit(ex_string, 8)
    print(f"flipped string   : {bit_flipped_string}")
    hash_with_bit_flip = sha256_hash(bit_flipped_string)
    print(f"flipped hash     : {hash_with_bit_flip}")

    distance = hamming_distance(hash_no_bit_flip, hash_with_bit_flip)
    print(f"hamming dist     : {distance}")


if __name__ == '__main__':
    main()
