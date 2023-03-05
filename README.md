# Brief 

<h3><b> Book Tracker Project </b></h3>

An app that allows users to add books to their reading wish list and track books they've completed.

<b> MVP </b>

- The app should allow the user to track books and authors they want to read and those they have read.
- The user should be able to create and edit authors.
- Each author should have one or more books.
- The user should be able to create and delete entries for books.
- The app should allow the user to mark books as read or still to read.


<b> Extensions </b>

- Have separate pages for books read and those still to be read.
- Add notes to individal books.


# Rules 

Built only using: 

- HTML / CSS
- Python
- Flask
- PostgreSQL and the psycopg


Must NOT use:

- Any Object Relational Mapper (e.g. ActiveRecord.
- JavaScript. At all. Don't even think about it. 
- Any pre-built CSS libraries, such as Bootstrap. 
- Authentication. Assume that the user already has secure access to the app. 


# Technologies Used

- HTML / CSS
- Python
- Flask
- PostgreSQL and the psycopg


# Running Instrictions

1. Clone and enter git repository 
```` terminal 
cd book_bucket_list
````
2. Install Requirements
```` terminal 
pip3 install Flask
````
3. Create Database

```` terminal 
createdb book_list
psql -d book_list -f db/book_list.sql
````

3. Run the app with Flask and open in web browser 
```` terminal 
flask run
````

# Screenshots

View all books in library:
<img width="1259" alt="main library page" src="https://user-images.githubusercontent.com/71439994/222966851-146d0897-b2e5-4d43-a0c3-2441d2672555.png">

Add book to library:
<img width="1260" alt="add book" src="https://user-images.githubusercontent.com/71439994/222967199-8ce02f12-8098-4ac9-b00a-1bb963038b64.png">

View all details of book/update book:
<img width="1260" alt="book details" src="https://user-images.githubusercontent.com/71439994/222967223-51bd2744-e1e5-4f8e-8676-dc4c4afebe77.png">

View all authors:
<img width="1259" alt="view all authors" src="https://user-images.githubusercontent.com/71439994/222967270-7049a831-624d-4439-8951-6f0daa326cbd.png">

Add author:
<img width="1259" alt="add author" src="https://user-images.githubusercontent.com/71439994/222967242-c3967008-8372-4707-a32e-b2c320e536f2.png">

View author details/update author: 
<img width="1268" alt="author detials" src="https://user-images.githubusercontent.com/71439994/222967379-439ebb8e-8ea3-4444-bad4-35af15575666.png">
