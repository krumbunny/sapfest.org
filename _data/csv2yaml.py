#!/usr/local/bin/python

import csv
import sys

src = csv.DictReader(sys.stdin)
for row in src:
  first = True
  for key in row:
    if first:
      print "- " + key + ": " + row[key]
      first = False
    else:
      print "  " + key + ": " + row[key]
