communication contract


requesting data in pipeline:

should contain two lines in a text document. First line should be the string request second line should be a request in the format of your database. Database should be in the form of one json object per line in a text document. 
For example, a database like the following:

{"id": "001", "title": "Eragon", "author": "Christopher Paolini", "genre": "Fantasy", "year": 2002, "pages": 544}
{"id": "002", "title": "A Game of Thrones", "author": "George R. R. Martin", "genre": "Fantasy", "year": 1996, "pages": 694}
{"id": "003", "title": "Dune", "author": "Frank Herbert", "genre": "Science Fiction", "year": 1965, "pages": 412}
{"id": "004", "title": "The Lord of the Rings", "author": "J. R. R. Tolkien", "genre": "Fantasy", "year": 1954, "pages": 1178}
{"id": "005", "title": "Eldest", "author": "Christopher Paolini", "genre": "Fantasy", "year": 2005, "pages": 704}

would have a request for the object with id 003 like so:
request
{"id": "003", "title": "", "author": "", "genre": "", "year": "", "pages": ""}

or for the author Christopher Paolini:
request
{"id": "", "title": "", "author": "Christopher Paolini", "genre": "", "year": "", "pages": ""}

or for both:
request
{"id": "001", "title": "", "author": "Christopher Paolini", "genre": "", "year": "", "pages": ""}





receiving data:

contains two or more lines in a text document. First line is the string reply second line and on are objects in the database.
The following are the replies for the above example requests.
reply
{"id": "003", "title": "Dune", "author": "Frank Herbert", "genre": "Science Fiction", "year": 1965, "pages": 412}
reply
{"id": "001", "title": "Eragon", "author": "Christopher Paolini", "genre": "Fantasy", "year": 2002, "pages": 544}
{"id": "005", "title": "Eldest", "author": "Christopher Paolini", "genre": "Fantasy", "year": 2005, "pages": 704}
reply
{"id": "001", "title": "Eragon", "author": "Christopher Paolini", "genre": "Fantasy", "year": 2002, "pages": 544}



UML Diagram is included in the "CS361 Microservice 2 UML.png" file within the repository.
