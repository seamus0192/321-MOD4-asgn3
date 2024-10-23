from concurrent.futures import ThreadPoolExecutor

import bcrypt
import concurrent.futures
import nltk
import numpy as np

from nltk.corpus import words
from dataclasses import dataclass
from typing import Optional, Iterator

the_guys = {
    "Bilbo": b"$2b$08$J9FW66ZdPI2nrIMcOxFYI.qx268uZn.ajhymLP/YHaAsfBGP3Fnmq",
    "Gandalf": b"$2b$08$J9FW66ZdPI2nrIMcOxFYI.q2PW6mqALUl2/uFvV9OFNPmHGNPa6YC",
    "Thorin": b"$2b$08$J9FW66ZdPI2nrIMcOxFYI.6B7jUcPdnqJz4tIUwKBu8lNMs5NdT9q",
    "Fili": b"$2b$09$M9xNRFBDn0pUkPKIVCSBzuwNDDNTMWlvn7lezPr8IwVUsJbys3YZm",
    "Kili": b"$2b$09$M9xNRFBDn0pUkPKIVCSBzuPD2bsU1q8yZPlgSdQXIBILSMCbdE4Im",
    "Balin": b"$2b$10$xGKjb94iwmlth954hEaw3O3YmtDO/mEFLIO0a0xLK1vL79LA73Gom",
    "Dwalin": b"$2b$10$xGKjb94iwmlth954hEaw3OFxNMF64erUqDNj6TMMKVDcsETsKK5be",
    "Oin": b"$2b$10$xGKjb94iwmlth954hEaw3OcXR2H2PRHCgo98mjS11UIrVZLKxyABK",
    "Gloin": b"$2b$11$/8UByex2ktrWATZOBLZ0DuAXTQl4mWX1hfSjliCvFfGH7w1tX5/3q",
    "Dori": b"$2b$11$/8UByex2ktrWATZOBLZ0Dub5AmZeqtn7kv/3NCWBrDaRCFahGYyiq",
    "Nori": b"$2b$11$/8UByex2ktrWATZOBLZ0DuER3Ee1GdP6f30TVIXoEhvhQDwghaU12",
    "Ori": b"$2b$12$rMeWZtAVcGHLEiDNeKCz8OiERmh0dh8AiNcf7ON3O3P0GWTABKh0O",
    "Bifur": b"$2b$12$rMeWZtAVcGHLEiDNeKCz8OMoFL0k33O8Lcq33f6AznAZ/cL1LAOyK",
    "Bofur": b"$2b$12$rMeWZtAVcGHLEiDNeKCz8Ose2KNe821.l2h5eLffzWoP01DlQb72O",
    "Durin": b"$2b$13$6ypcazOOkUT/a7EwMuIjH.qbdqmHPDAC9B5c37RT9gEw18BX6FOay"
}


@dataclass
class UserInfo:
    username: Optional[str]
    algo: str
    work_factor: int
    salt: str
    hash: bytes

    def __repr__(self):
        return f"\n-----------------\nUSER - {self.username}\nALGO - {self.algo}\n" \
               f"WORK - {self.work_factor}\nSALT - {self.salt}\nHASH - {self.hash}"


def main():
    # download the word list corpus
    nltk.download('words')

    # get the list of words from the corpus
    word_list: Iterator[str] = filter(lambda x: 6 <= len(x) <= 10, words.words())

    for guy in the_guys.keys():
        attempt: int = 0
        user: UserInfo = parse_user_info(guy, the_guys[guy])
        print(f"Searching for {user.username}'s password...")

        # TODO broken. salt and hash and stuff are just jank.

        # Iterate through all words that are between 6 and 10 letters long
        for word in word_list:
            attempt += 1
            if bcrypt.hashpw(word.encode('utf-8'), bytearray(user.salt)) == user.hash:
                print(f"{user.username}'s passw ord has been cracked!\nPassword is {word}"
                      f"\nHash is {hash}\nAttempt num {attempt}")
                break


def parse_user_info(username: Optional[str], info: bytearray) -> UserInfo:
    info = info.split(b"$")
    return UserInfo(username, str(info[1]), int(info[2]), info[3][:22].decode('utf-8'), info[3][22:])


if __name__ == '__main__':
    main()
