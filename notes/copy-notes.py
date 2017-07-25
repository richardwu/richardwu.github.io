import os
import filecmp
import shutil

BASE = os.path.join(os.environ['HOME'], "Dropbox", "uni-courses")
COURSES = {
            "2B": [
                "co250",
                "math239",
                "stat231",
            ]
        }

PDF_SUFFIX = "-notes.pdf"

for term, courses in COURSES.items():
    for course in courses:
        filename = course + PDF_SUFFIX
        origFpath = os.path.join(BASE, term, course.upper(), filename)

        # If file is outddated, do a copy
        if not filecmp.cmp(origFpath, filename):
            print("Outdated file: copying", origFpath)
            shutil.copyfile(origFpath, filename)
