import os
import sys
import datetime

OUTFILE = "output1.txt"



def folder_cmp(dir1:str, dir2:str) -> list[str]:
    try:
        a = set(os.listdir(dir1))
        b = set(os.listdir(dir2))
        c = a.intersection(b)
        result = []

        for f in c:
            file1 = os.path.join(dir1, f)
            file2 = os.path.join(dir2, f)
            t1 = os.path.getctime(file1)
            t2 = os.path.getctime(file2)

            if t1 < t2:
                result.append(file1)
            else:
                result.append(file2)
        return result
    except Exception as e:
        print(e)
        return [""]


def find_all_files(dir):
    a = os.listdir(dir)
    files_lst1 = []
    for f1 in a:
        if os.path.isfile(f1):
            files_lst1.append(os.path.join(os.path.normpath(dir), f1))
        elif os.path.isdir(f1):
            files_lst1 += find_all_files()
    return files_lst1


def folder_cmp_3(dir1:str, dir2:str) -> list[str]:
    try:
        a = os.listdir(dir1)
        b = os.listdir(dir2)
        res1 = set()
        res2 = set()
        for f1 in a:
            path = os.path.split(f1)
            fname = path[-1]
            res1.add(fname)
        for f2 in b:
            path2 = os.path.split(f2)
            fname2 = path2[-1]
            res2.add(fname2)
        return list(res1.symmetric_difference(res2))

    except Exception as e:
        print(e)
        return [""]


if __name__ == '__main__':
    if len(sys.argv) < 3:
        DIR1 = input("First folder")
        DIR2 = input("Second folder")
    else:
        DIR1 = sys.argv[1]
        DIR2 = sys.argv[2]
        if len(sys.argv) >= 4:
            OUTFILE = sys.argv[3]

    out_old = sys.stdout

    with open(OUTFILE, "wt") as f:
        sys.stdout = f
        res = folder_cmp(DIR1, DIR2)
        for item in res:
            print(item)

    sys.stdout = out_old
