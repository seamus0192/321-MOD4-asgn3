from dataclasses import dataclass
from typing import List

the_guys = {
    "Bilbo": "$2b$08$J9FW66ZdPI2nrIMcOxFYI.qx268uZn.ajhymLP/YHaAsfBGP3Fnmq",
    "Gandalf": "$2b$08$J9FW66ZdPI2nrIMcOxFYI.q2PW6mqALUl2/uFvV9OFNPmHGNPa6YC",
    "Thorin": "$2b$08$J9FW66ZdPI2nrIMcOxFYI.6B7jUcPdnqJz4tIUwKBu8lNMs5NdT9q",
    "Fili": "$2b$09$M9xNRFBDn0pUkPKIVCSBzuwNDDNTMWlvn7lezPr8IwVUsJbys3YZm",
    "Kili": "$2b$09$M9xNRFBDn0pUkPKIVCSBzuPD2bsU1q8yZPlgSdQXIBILSMCbdE4Im",
    "Balin": "$2b$10$xGKjb94iwmlth954hEaw3O3YmtDO/mEFLIO0a0xLK1vL79LA73Gom",
    "Dwalin": "$2b$10$xGKjb94iwmlth954hEaw3OFxNMF64erUqDNj6TMMKVDcsETsKK5be",
    "Oin": "$2b$10$xGKjb94iwmlth954hEaw3OcXR2H2PRHCgo98mjS11UIrVZLKxyABK",
    "Gloin": "$2b$11$/8UByex2ktrWATZOBLZ0DuAXTQl4mWX1hfSjliCvFfGH7w1tX5/3q",
    "Dori": "$2b$11$/8UByex2ktrWATZOBLZ0Dub5AmZeqtn7kv/3NCWBrDaRCFahGYyiq",
    "Nori": "$2b$11$/8UByex2ktrWATZOBLZ0DuER3Ee1GdP6f30TVIXoEhvhQDwghaU12",
    "Ori": "$2b$12$rMeWZtAVcGHLEiDNeKCz8OiERmh0dh8AiNcf7ON3O3P0GWTABKh0O",
    "Bifur": "$2b$12$rMeWZtAVcGHLEiDNeKCz8OMoFL0k33O8Lcq33f6AznAZ/cL1LAOyK",
    "Bofur": "$2b$12$rMeWZtAVcGHLEiDNeKCz8Ose2KNe821.l2h5eLffzWoP01DlQb72O",
    "Durin": "$2b$13$6ypcazOOkUT/a7EwMuIjH.qbdqmHPDAC9B5c37RT9gEw18BX6FOay"
}


@dataclass
class UserInfo:
    username: str
    algo: str
    work_factor: int
    salt: str
    hash: str

    def __repr__(self):
        return f"\n-----------------\nUSER - {self.username}\nALGO - {self.algo}\n" \
               f"WORK - {self.work_factor}\nSALT - {self.salt}\nHASH - {self.hash}"


def main():
    l: List[UserInfo] = []
    for guy in the_guys.keys():
        l.append(parse_user_info(guy, the_guys[guy]))
    print(l)


def parse_user_info(username: str, info: str) -> UserInfo:
    info = info.split("$")
    return UserInfo(username, info[1], int(info[2]), info[3][:20], info[3][20:])


if __name__ == '__main__':
    main()