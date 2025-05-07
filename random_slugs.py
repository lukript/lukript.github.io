import random
import string
import os

SLUG_LENGTH = 8
SLUG_FILE = "used_slugs.txt"

def generate_random_slug(length=SLUG_LENGTH):
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))

def load_used_slugs():
    if not os.path.exists(SLUG_FILE):
        return set()
    with open(SLUG_FILE, "r") as file:
        return set(line.strip() for line in file)

def save_slug(slug):
    with open(SLUG_FILE, "a") as file:
        file.write(slug + "\n")

def get_unique_slug():
    used_slugs = load_used_slugs()
    while True:
        new_slug = generate_random_slug()
        if new_slug not in used_slugs:
            save_slug(new_slug)
            return new_slug

# Generate and print a unique slug
print(get_unique_slug())
