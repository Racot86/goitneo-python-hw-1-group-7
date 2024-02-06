from pathlib import Path

def load_contacts():
    if Path.is_file(Path('contacts.txt')):
        with open('contacts.txt', 'r') as fh:
            print (fh.read())
    else:
        return []
