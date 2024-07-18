#!/usr/bin/python3
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import subprocess

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them
def get_special_paths(dir):
    result = []
    filenames = os.listdir(dir)
    for filename in filenames:
        if re.search(r'__\w+__', filename):
            result.append(os.path.abspath(os.path.join(dir, filename)))
    return result

def copy_to(paths, dir):
    if not os.path.exists(dir):
        os.makedirs(dir)
    for path in paths:
        shutil.copy(path, dir)

def zip_to(paths, zippath):
    base_name = os.path.splitext(zippath)[0]
    dir_name = os.path.dirname(zippath)
    temp_dir = os.path.join(dir_name, "temp_special")
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)

    try:
        for path in paths:
            shutil.copy(path, temp_dir)
        shutil.make_archive(base_name, 'zip', temp_dir)
    finally:
        shutil.rmtree(temp_dir)


def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print('usage: [--todir dir][--tozip zipfile] dir [dir ...]')
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  if not args: # A zero length array evaluates to "False".
    print('error: must specify one or more dirs')
    sys.exit(1)

  # +++your code here+++
  # Call your functions
  special_paths = []
  for dir in args:
    special_paths.extend(get_special_paths(dir))

  if todir:
    copy_to(special_paths, todir)

  if tozip:
    zip_to(special_paths, tozip)

  if not todir and not tozip:
    print('\n'.join(special_paths))

if __name__ == '__main__':
  main()
