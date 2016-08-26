@REM **************
@echo off
if "%1"=="" echo usage: test.bat (firstname) (lastname)
if "%1"=="" goto :EOF
echo SELECT > myquery.sql
echo presapp_researchpresentation.id, >> myquery.sql
echo presapp_researchpresentation.research, >> myquery.sql
echo presapp_author.firstname, >> myquery.sql
echo presapp_author.lastname, >> myquery.sql
echo presapp_unit.name, >> myquery.sql
echo presapp_conference.end_date >> myquery.sql
echo FROM >> myquery.sql
echo presapp_researchpresentation_authors>> myquery.sql
echo INNER JOIN presapp_researchpresentation ON presapp_researchpresentation.id = presapp_researchpresentation_authors.researchpresentation_id >> myquery.sql
echo INNER JOIN presapp_author ON presapp_author.id = presapp_researchpresentation_authors.author_id >> myquery.sql
echo INNER JOIN presapp_unit ON presapp_unit.id = presapp_author.unit_id >> myquery.sql
echo INNER JOIN presapp_conference ON presapp_researchpresentation.conference_id = presapp_conference.id >> myquery.sql
echo WHERE >> myquery.sql
echo presapp_author.firstname LIKE '%%%1%%' and presapp_author.lastname LIKE '%%%2%%' and strftime('%%Y',presapp_conference.end_date)='2015'; >> myquery.sql;
sqlite3 db.sqlite3 ".read myquery.sql"
del myquery.sql
@REM **************
