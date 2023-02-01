import json
from random import choice
import argparse
import json
import os


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
                    prog = 'Words learning',
                    description = 'Helper for learning')
    parser.add_argument("-i", "--input", nargs="+")
    args = parser.parse_args()

    words = {}
    for f_path in args.input:
        with open(f_path, 'r') as f:
            words.update(json.load(f))

    while True:
        os.system("clear")
        show = choice(list(words.keys()))
        print(f"{show}")
        res = input()
        if res.lower() != words[show].lower():
            print("\033[1;31;40m Wrong \033[0m Correct answer is: " + words[show])
        else:
            print("\033[1;32;40m Correct \033[0m")
        print("Any key -> next")
        input()

