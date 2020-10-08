import os
import re
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dir", "-d", type=str, required=True)
    args = parser.parse_args()
    try:
        for root, dirs, files in os.walk(args.dir):
            for file in files:
                if file.endswith(".ini"):
                    print("Found: ", os.path.join(root, file))
                    path = (os.path.join(root, file))
                    with open(path) as f:
                        st = f.read()
                        srt = re.sub(r"\W", "", st)
                        if 'canarytokens' in srt:
                            print("Canary token detected in file: ", path)
    except OSError:
        print("error")


if __name__ == "__main__":
    main()
