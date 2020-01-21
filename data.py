# Super simple data loader

from zipfile import ZipFile
import numpy as np
import re

class Email:

    def __init__(self, text, label):
        self.words = re.findall(r'[a-zA-Z]{5,}', text)
        self.spam = True if label == "spam" else False

# Load emails (Bayes)
ham  = []
spam = []
with ZipFile("./spam_ham_dataset.csv.zip") as archive:
    with archive.open("spam_ham_dataset.csv") as f:
        for line in re.findall(r'\d+,(spam|ham),"([^"]+)",(0|1)', str(f.read())):
            label, text, _ = line
            email = Email(text, label)
            if email.spam:
                spam.append(email)
            else:
                ham.append(email)

# Generate SVM data
points = np.random.rand(500, 2) * 4 - 2
labels = np.zeros(500)
for (idx, p) in enumerate(points):
    if p[0]**2 + p[1]**2 <= 1:
        labels[idx] = +1
    else:
        labels[idx] = -1
