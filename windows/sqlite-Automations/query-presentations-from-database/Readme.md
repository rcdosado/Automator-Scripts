What is it
=========


It allows you to query the sqlite database with parameters from a text file
it uses batch script to do this. The query from the example is from my own db
but it simply list an individual and all their research presentation for the year 2015

what are these
--------------

list.txt contains people names in strictly 2 words, first name and last name
it searches this person in the database and the output can be redirected to file.
the people are dummy names btw, replace it with your own list

test.bat is a batch file the recreates a query file, the contains different person
every time it is created.

loops.bat this file calls test.bat and gives person names as paramters from list.txt
you can redirect the output so you can dump the list as file.

Requirements
------------
sqlite3.exe
your sqlite3 database


How to use
---------
setup your query in test.bat
then simply call

`loops.bat > output.txt`

it assumes sqlite3.exe is PATH and db.sqlite3 is in the current directory

