import re
import docx

DOCFILE = "example.docx"
OUTFILE = "output.docx"

PATTERN1 = r"\d{1,2}\.\d{1,2}\.\d{4}"
PATTERN2 = r"(\d{4})/(\d{1,2})/(\d{1,2})"
PATTERN = f"{PATTERN1}|{PATTERN2}"
PATTERN3 = r"[A-Z].*?[\.!?]"
PATTERN4 = r"(\d{4})-(\d{1,2})-(\d{1,2})"

def convert_date(match):
    if match.group(2) is not None:
        return f"{match.group(3)}.{match.group(2)}.{match.group(1)}"
    elif match.group(5) is not None:
        return f"{match.group(5)}.{match.group(4)}.{match.group(6)}"

def task23_5():
    global DOCFILE
    doc = docx.Document(DOCFILE)
    for paragraph in doc.paragraphs:
        text = paragraph.text
        text = re.sub(PATTERN2, convert_date, text)
        text = re.sub(PATTERN4, r"\3.\2.\1", text)
        paragraph.text = text

    doc.save(OUTFILE)

if __name__ == "__main__":
    task23_5()
