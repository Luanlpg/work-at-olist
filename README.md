# Library

## Requirements installation (REQUIRED: Python 3.6.0+)

- Create a virtual environment of your choice (Recommended / Optional)

- Clone the project: `git clone https://github.com/Luanlpg/work-at-olist.git`

- Access the repository: `cd work-at-olist/library/`

- Install the file `requirements.txt` using the command: `pip install -r requirements.txt`

## Persisting data from the csv file of authors

- Move the file with the names of the authors to the library folder and name it `authors.csv`

- After the first request made in the API the file will be processed and persisted

## Running the Flask

- Run the local server with: `python application.py`

## API routes

### GET `/api/author`
- Lists all authors

### POST `/api/author`
- Creates author
```
{
 "name": // Name of the author
}
```

### GET `/api/author/<NAME or ID>`
- List all authors by name or return the author corresponding to the id

### PUT `/api/author/<NAME or ID>`
- Edit author data (if name is used in the query string the name needs to be complete)
```
{
 "name": // Name of the author;
}
```

### DELETE `/api/author/<NAME or ID>`
- Remove author (if name is used in the query string the name needs to be complete)

### GET `/api/book`
- Lists all books

### POST `/api/book`
- Creates book
```
{
 "name": // Name of the book;
 "edition": // Edition number;
 "publication_year": // Publication year of the book;
 "authors": // List of author ids, same ids of previous imported data
}
```

### GET `/api/book/<NAME or ID>`
- List all books by name or return the book corresponding to the id

### PUT `/api/book/<NAME or ID>`
- Edit book data (if name is used in the query string the name needs to be complete)
```
{
 "name": // Name of the book(optional);
 "edition": // Edition number(optional);
 "publication_year": // Publication year of the book(optional)
}
```

### DELETE `/api/book/<NAME or ID>`
- Remove book (if name is used in the query string the name needs to be complete)

## Cloud project link
- `https://x-lib.herokuapp.com/`
