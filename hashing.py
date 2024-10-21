from cryptohashlib import sha256_hash, flip_bit, hamming_distance, find_collision, sha256_truncated, \
    find_collision_birthday


def main():
    # PART A -------------------------------------------------
    ex_string = "hello i am alive"
    hash_no_bit_flip = sha256_hash(ex_string)
    print(f"input string     : {ex_string}")
    print(f"SHA256 hash      : {hash_no_bit_flip}")

    # PART B -------------------------------------------------
    # flip different bits in string, observe the hamming distances
    flip_certain_bit(hash_no_bit_flip, ex_string, 8)
    flip_certain_bit(hash_no_bit_flip, ex_string, 21)
    flip_certain_bit(hash_no_bit_flip, ex_string, 100)

    # PART C -------------------------------------------------
    # can be any value between 8 and 50 bits
    truncate_bits = 8

    # Finding weak collision (H(m0) = H(m1))
    print("finding weak collision for m0...")
    m1, attempts = find_collision(ex_string, truncate_bits)
    print(f"Collision found after {attempts} attempts")
    print(f"input string     : {ex_string}")
    print(f"m1               : {m1}")
    print(f"H(m0) = H(m1)    : {sha256_truncated(ex_string, truncate_bits)}")

    # Finding collision using Birthday Paradox
    print("Finding collision using birthday paradox...")
    m1, m2, attempts = find_collision_birthday(truncate_bits)
    print(f"Collision found after {attempts} attempts")
    print(f"m1               : {m1}")
    print(f"m2               : {m2}")
    print(f"H(m1) = H(m2)    : {sha256_truncated(m1, truncate_bits)}")


def flip_certain_bit(original_hash, string, bit_pos):
    bit_flipped_string = flip_bit(string, bit_pos)
    print(f"flipped string   : {bit_flipped_string}")
    hash_with_bit_flip = sha256_hash(bit_flipped_string)
    print(f"flipped hash     : {hash_with_bit_flip}")

    distance = hamming_distance(original_hash, hash_with_bit_flip)
    print(f"hamming dist     : {distance}")


if __name__ == '__main__':
    main()
