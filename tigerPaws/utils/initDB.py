from datamanagement import *

def main():
    _filename = "..\data\courses.xlsx"
    df = getRows(_filename)
    loadData(df)
    return

if __name__ == "__main__":
    main()