communication contract


requesting data in pipeline:

should contain string "request" followed by curly brackets and data separated by semicolons. if semicolons are beside each other or object ends early, nothing will be requested for those parameters.
requests must have data placed appropriately or will return nothing; for example, searching database for objects with 190 requires that 190 is placed after two semicolons / two undefined properties.
database and request structures can be changed without modifying code, all that needs to be altered within the program is the pipeline, database, and sleep time.

example request 1 (using information from example) database -
request
{string1;;190;}

example request 2 -
request
{string1;}

example request 3 -
request
{;;190;}



receiving data:

contains string "reply" followed by objects (one object per line), each contained in curly brackets and data separated by semicolons.

example reply for requests 1, 2, and 3 -
reply
{string1;string2;190;}
{string1;string3;190;}
{string1;string4;190;}
{string1;string5;190;}