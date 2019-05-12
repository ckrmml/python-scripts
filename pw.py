import random
import string
import argparse


__version__ = '0.0.1'


ALPHABET_LOWER = tuple(string.ascii_lowercase)
ALPHABET_UPPER = tuple(string.ascii_uppercase)
NUMERICAL = tuple(string.digits)
SPECIAL = ('!', '#', '$', '%', '&', '(', ')', '*', '+',
           ',', '-', '.', '/', ':', ';', '<', '=', '>',
           '?', '@', '[', ']', '_', '{', '|', '}')

SEQUENCE = list()
PW_BUFFER = list()

def generate_pw(length, sequence):
    password = list()

    while not len(password) == length:
        sc = random.choice(range(len(sequence)))
        cc = random.choice(sequence[sc])[0]
        if password:
            if password[-1] != cc:
                password.append(cc)
        else:
            password.append(cc)

    while _char_repeating(password):
        random.shuffle(password)

    if _check_sequences(password, sequence):
        return ''.join(password)
    else:
        return generate_pw(length, sequence)

def _char_repeating(password):
    for i,c in enumerate(password):
        if password[i] == password[i-1]:
            return True
    return False

def _check_sequences(password, sequence):
    sl = list()

    for char in password:
        for seq in sequence:
            if char in seq and seq not in sl: sl.append(seq)

    if len(sl) == len(sequence):
        return True
    return False

def _parse_args():
    parser = argparse.ArgumentParser(description = 'RndmPW (v{0}): just another python cmd-line password generator'.format(__version__),\
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    # count/length
    parser.add_argument(
        '-c',
        '--count',
        type=int,
        metavar='int',
        default=10,
        help='Number of passwords that get generated'
    )
    parser.add_argument(
        '-l',
        '--length',
        type=int,
        metavar='int',
        default=16,
        help='Length of passwords'
    )
    # chars to use
    parser.add_argument(
        '-a',
        '--alpha',
        type=str,
        metavar='l/u/b',
        default='b',
        help='Use alphabet (lower-case/upper-case/both)'
    )
    parser.add_argument(
        '-n',
        '--num',
        # default=True,
        action='store_true',
        help='Use numbers'
    )
    parser.add_argument(
        '-s',
        '--special',
        # default=True,
        action='store_true',
        help='Use special characters'
    )
    # debug/version
    parser.add_argument(
        '--debug',
        action='store_true',
        help='Enable debug logging'
    )
    parser.add_argument(
        '-v',
        '--version',
        action='version',
        version='%(prog)s {version}'.format(version=__version__))

    return parser.parse_args()

args = _parse_args()

if args.alpha == 'l':
    SEQUENCE.append(ALPHABET_LOWER)
elif args.alpha == 'u':
    SEQUENCE.append(ALPHABET_UPPER)
elif args.alpha == 'b':
    SEQUENCE.append(ALPHABET_LOWER)
    SEQUENCE.append(ALPHABET_UPPER)
if args.num:
    SEQUENCE.append(NUMERICAL)
if args.special:
    SEQUENCE.append(SPECIAL)

for _ in range(args.count):
    PW_BUFFER.append(generate_pw(args.length, SEQUENCE))

for pw in PW_BUFFER:
    print(pw)
