#!/usr/bin/python3
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import pandas as pd 
import os

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

def extract_names(file_content):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  # Extract the year using a regular expression
  year_match = re.search(r'Popularity in (\d{4})', file_content)
  year = year_match.group(1) if year_match else 'Unknown'
  
  # Extract the table rows using regular expressions
  rows = re.findall(r'<tr align="right"><td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>', file_content)
  
  # Create a summary text
  summary = f"{year}\n"
  for rank, male_name, female_name in rows:
      summary += f"{male_name} {rank}\n"
      summary += f"{female_name} {rank}\n"
  
  return summary

def process_file(filename, summaryfile):
    with open(filename, 'r', encoding='utf-8') as file:
        file_content = file.read()
    
    summary = extract_names(file_content)
    
    if summaryfile:
        filename_nohtml = filename[:-5]
        summary_filename = f"{filename_nohtml}.summary"
        with open(summary_filename, 'w', encoding='utf-8') as summary_file:
            summary_file.write(summary)
    else:
        print(summary)

def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print('usage: [--summaryfile] file [file ...]')
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    for filename in os.listdir("./"):
        if filename.endswith('.html'):
           process_file(filename, summary)

  # +++your code here+++
  # For each filename, get the names, then either print the text output
  # or write it to a summary file
  with open(args[0], 'r', encoding='utf-8') as file:
    file_content = file.read()
    print(extract_names(file_content))

if __name__ == '__main__':
  main()
