from util import *

def main():
    print("BackTracking!!")
    files = take_file_list("./")
    files = [directory for directory in files if directory[0] != "./"]
    for file in files:
        fileDir = f"{file[0]}/{file[1]}"
        try:
            os.rename(fileDir, f"./raw/{file[1]}")
        except:
            continue
    
if __name__ == "__main__":
    main()