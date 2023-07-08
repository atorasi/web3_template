from random import randint
from time import sleep

from config import SLEEP_ACCS, SLEEP_ACCS_FROM, SLEEP_ACCS_TO, SLEEP_AKTIVE, SLEEP_AKTIVE_FROM, SLEEP_AKTIVE_TO


def newersleep_accs() -> int:
    if SLEEP_ACCS:
        time = randint(SLEEP_ACCS_FROM, SLEEP_ACCS_TO)
        sleep(time)
    return time

def newersleep_accs() -> int:
    if SLEEP_AKTIVE:
        time = randint(SLEEP_AKTIVE_FROM, SLEEP_AKTIVE_TO)
        sleep(time)
    return time
