#!/usr/bin/env python3
"""Calculates `md5` hash of the assets and writes it to `.checksum.md5` file.

Filenames are hashed too.
Hidden files (including `.checksum.md5` and `.travis.yml`) are ignored.
Python 3.5 required.
"""

import sys
import os
import hashlib
import glob
import argparse

assert sys.version_info >= (3, 5), f'{sys.version_info}'

parser = argparse.ArgumentParser()
parser.add_argument("-c", "--check", action='store_true')
args = parser.parse_args()

file_names = glob.glob(os.path.join('.', '**'), recursive=True)

constructor = hashlib.md5()
for file_name in file_names:
    if os.path.isfile(file_name):
        print(f"Hasing '{file_name}'...");
        constructor.update(file_name.encode())
        constructor.update(open(file_name, 'rb').read())

hash = constructor.hexdigest()
print(f'The hash is {hash}')

if args.check:
    print("Comparing the hash with `.checksum.md5`...")
    saved_hash = open('.checksum.md5').read().rstrip()
    if hash != saved_hash:
        exit("[ERROR] Hashes don't match!")
    print("Hashes match")
else:
    print("Updating `.checksum.md5`...")
    with open('.checksum.md5', mode='w') as f:
        f.write(hash + '\n')
