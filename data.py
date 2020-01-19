# Super simple data loader

from zipfile import ZipFile
import re

class Email:

    def __init__(self, text, label):
        self.words = re.findall(r'[a-zA-Z]{5,}', text)
        self.spam = True if label == "spam" else False

# Load emails
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
