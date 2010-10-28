#!/usr/bin/env python

import datetime
import sys

def swapdate(file_contents):
    string = file_contents
    today = datetime.date.today()
    string = string.replace("&year", today.strftime("%Y"))
    return string

def swapnames(file_contents, names):
    namestring = ""
    for name,email in names:
        namestring += name + " <" + email + ">, "

    namestring = namestring[:-2]
    file_contents = file_contents.replace("&names", namestring)
    return file_contents

def author_split(authors):
    author_list = authors.split(",")
    author_result = []
    for i in xrange(1,len(author_list),2):
        author_result.append((author_list[i-1],author_list[i]))
    return author_result

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print "usage is ./licenseme <license> <authors> [outfile]"
        print "outfile defaults to LICENSE"
        print "authors should be a comma seperated list of name1,email1,name2,email2"
        exit(1)
    outfile = ""
    if len(sys.argv) == 3:
        outfile = "LICENSE"
    else:
        outfile = sys.argv[3]

    license = sys.argv[1]
    authors = sys.argv[2]
    author_pairs = author_split(authors)
    file_contents = open("/usr/share/licenseme/" + license + ".license").read()
    file_contents = swapdate(file_contents)
    file_contents = swapnames(file_contents,author_pairs)
    write_handle = open(outfile,"w")
    write_handle.write(file_contents)
    exit(0)

