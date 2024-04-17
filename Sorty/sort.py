import json
from util import *
import time

def main():
    directory = "./raw/"
    start = time.time()
    with open(('./regex.json'), encoding="utf-8") as f:
        regex = json.load(f)

    files = take_file_list(directory)
    
    amount = sortRegex(files, regex)

    print(f"Moved {amount} files. It's done in {time.time() - start} seconds")
    
if __name__ == "__main__":
    main()