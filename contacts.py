import json
import os

CONTACT_FILE = "data/contacts.json"


def load_contacts():

    if not os.path.exists(CONTACT_FILE):
        return {}

    with open(CONTACT_FILE, "r") as file:
        return json.load(file)


def get_email(name):

    contacts = load_contacts()

    return contacts.get(name.lower())


def list_contacts():

    return load_contacts()


if __name__ == "__main__":

    print(get_email("rahul"))