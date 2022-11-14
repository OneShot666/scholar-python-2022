import os


def Import_files(files: list):
    return files


def Find_word(word, find_one=False):
    Documents = []

    for mot in files:
        if mot == word:
            print("Trouvé !")
            if find_one:
                return mot
            else:
                Documents.append(mot)

    return Documents
