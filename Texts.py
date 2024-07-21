from exceedCv import google_CV as cv

j_path = "vision-project-207707-f84d39ceed76.json"

cv.google_auth(j_path)

cap = "texts.jpg"

texts, refPt = cv.detect_text(cap)
cv.display_allborders(refPt, cap)

for t in texts:
    print(t.description)
