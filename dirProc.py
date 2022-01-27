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
      md5Hash = hashlib.md5(open(os.path.join(root,file),'rb').read())
      sha256Hash = hashlib.sha256(open(os.path.join(root,file),'rb').read())
      sha512Hash = hashlib.sha512(open(os.path.join(root,file),'rb').read())
      fuzzyHash = tlsh.hash(open(os.path.join(root,file), 'rb').read())
      filetype = magic.from_file(os.path.join(root,file)) #we need to cut this down to just the first word of the output
      
      #These two don't currently write to the summary file, but the data is picked up for each type.
      if filetype == "PDF document":
        pdf = PdfFileReader(file)
        info = pdf.getDocumentInfo()
        number_of_pages = pdf.getNumPages()
        author = info.author 
        creator = info.creator 
        title = info.title
        #(author,creator,title,number_of_pages)

      if filetype == "Microsoft Word 2007+":
        doc = docx.Document(file)
        metadata = {}
        properties = doc.core_properties
        metadata["author"] = properties.author
        metadata["language"] = properties.language
        metadata["version"] = properties.version
        metadata["modified"] = time.mktime
        (properties.modified.timetuple())

        #return metadata
        
      csvwriter.writerow([file, filetype, md5Hash,sha256Hash, sha512Hash, fuzzyHash])
