#Input: path
#Action: iterate over everything in directory, add filetype and hash info to a .csv
#Output: csv with file name, several hashes, file type
import os
import magic
import hashlib
import tlsh
import csv

with open('summary.csv', 'w') as csv_out:
  csvwriter = csv.writer(csv_out) #create csv writer object

  fields = ['filename', 'filetype', 'md5', 'sha256', 'sha512', 'fuzzy']

  path = input("Please enter a path: \n")

  #files = os.listdir(path)
  for root, dirs, files in os.walk(path, topdown=False):
    for file in files:
      #populate csv
      #print(magic.from_file("slightlyDiff.jpeg"))
      #md5Hash = hashlib.md5(open("calvinTrexPlane.jpeg", 'rb').read())
      #print(md5Hash.hexdigest())
      md5Hash = hashlib.md5(open((file),'rb').read())
      sha256Hash = hashlib.sha256(open((file),'rb').read())
      sha512Hash = hashlib.sha512(open((file),'rb').read())
      fuzzyHash = tlsh.hash(open(file, 'rb').read())
      filetype = magic.from_file(file) #we need to cut this down to just the first word of the output

      csvwriter.writerow([file, filetype, md5Hash,sha256Hash, sha512Hash, fuzzyHash])
