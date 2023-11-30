"""
task 21_1
"""
import re

TEXTFILE2 = r"example2.txt"
TEXTFILE = r"example.txt"
OUTFILE = r"output.txt"

PATTERN1 = r"\d{1,2}\.\d{1,2}\.\d{4}"
PATTERN2 = r"(\d{4})/(\d{1,2})/(\d{1,2})"
PATTERN = f"{PATTERN1}|{PATTERN2}"
PATTERN3 = r"[A-Z].*?[\.!?]"
PATTERN4 = r"(\d{4})-(\d{1,2})-(\d{1,2})"
def task21_1():
    global TEXTFILE
    with open(TEXTFILE, encoding="UTF-8") as f, open(OUTFILE, "wt") as g:
        for line in f:
            txt = re.sub(PATTERN2, r"\3.\2.\1", line)
            g.write(txt)

def task21_2():
    global TEXTFILE2
    with open(TEXTFILE2, encoding="UTF-8") as f:
        text = " ".join([s.rstrip() for s in f.readlines()])
        print (text)
        sentences = re.findall(PATTERN3, text)
        for i in sentences:
            print (i)


date1 = r"\b(?P<year1>\d{4})/(?P<month1>\d{1,2})/(?P<day1>\d{1,2})"
date2 = r"\b(?P<day2>\d{1,2})\.(?P<month2>\d{1,2})\.(?P<year2>\d{4})"
date3 = r"\b(?P<year3>\d{4})\-(?P<month3>\d{1,2})\-(?P<day3>\d{1,2})"

DATE = date1 + "|" + date2 + "|" + date3

def change_dates(string):
    def _change_date(match):
        date = match.group()
        if '/' in date:
            k = '1'
        elif '.' in date:
            k = '2'
        else:
            k = '3'

        year = match.group('year' + k)
        month = match.group('month' + k)
        day = match.group('day' + k)

        if len(month) != 2:
            month = "0" + month
        if len(day) != 2:
            day = "0" + day

        return "/".join((year, month, day))

    return re.sub(DATE, _change_date, string)





if __name__ == "__main__":

    task21_2()
    with open("input.txt", "r", encoding="UTF-8") as inp:
        s = inp.read()
        s = change_dates(s)
    with open("output.txt", "w", encoding="UTF-8") as out:
        out.write(s)
