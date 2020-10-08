from os import path
import os
import argparse
import zipfile




def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", "-f", type=str, required=True)
    args = parser.parse_args()
    try:
        if path.exists(args.file):
            os.rename(args.file, 'temp.zip')
            orgf = args.file
            with zipfile.ZipFile('temp.zip', 'r') as zip_ref:
                zip_ref.extractall("temp")
                tokenfile = os.path.join(os.getcwd(), ".\\temp\\word\\footer2.xml")
                print(tokenfile)
            with open(tokenfile) as f:
                if "canary" in f.read():
                    print("Canarytoken detected")
            os.rename("temp.zip", orgf)

    except OSError:
        print("error")

if __name__ == "__main__":
    main()
