import os
import filecmp
import shutil

BASE = os.path.join(os.environ['HOME'], "Dropbox", "uni-courses")
COURSES = {
            "2b": [
                "co250",
                "math239",
                "stat231",
            ],

            "3b": [
                "stat331",
                "stat333",
                "math247",
                "cs442",
            ],

            "4a": [
                "stat433",
                "pmath351",
                "stat330",
                "cs466",
            ],
        }

PDF_SUFFICES = ["-notes.pdf", "-final-notes.pdf"]

for term, courses in COURSES.items():
    for course in courses:
        for PDF_SUFFIX in PDF_SUFFICES:
            filename = course + PDF_SUFFIX
            origFpath = os.path.join(BASE, term, course, filename)

            # If file does not exist, skip
            if not os.path.exists(origFpath):
                print("File not found:", origFpath)
                continue

            # If file is outddated (or not copied), do a copy
            if not os.path.exists(filename) or not filecmp.cmp(origFpath, filename):
                print("Outdated file: copying", origFpath)
                shutil.copyfile(origFpath, filename)
