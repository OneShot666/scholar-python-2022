# import os


# ! Waiting for upgrades
def import_file(file):
    return file


def find_word_in_file(word, file, find_one=False):
    Documents = []

    for mot, line in enumerate(import_file(file)):
        if mot == word:
            print(f"Word '{mot}' find at line {line} !")
            if find_one:
                return mot
            else:
                Documents.append(mot)

    if len(Documents) == 0:
        print(f"Aucun mot trouvé dans le fichier '{file}'")
    return Documents


if __name__ == "__main__":
    find_word_in_file('Nathan', 'a chemin projet test.txt', True)

quit()
