# Cafe & Wifi API

A Flask-based RESTful API that allows users to explore, add, and manage cafes with details like location, amenities, and coffee prices.

## Technologies Used

- **Flask:** A lightweight WSGI web application framework for building web applications.
- **Flask-SQLAlchemy:** An extension for Flask that simplifies the use of SQLAlchemy in your Flask application.
- **SQLite:** A C-language library that provides a lightweight, serverless, self-contained SQL database engine.
- **Postman:** A popular API client used for testing web services.


## Features

- **Retrieve All Cafes:** List all cafes available in the database.
- **Retrieve a Random Cafe:** Get details of a random cafe.
- **Add a New Cafe:** Add a new cafe to the database.
- **Update Coffee Price:** Modify the coffee price of a specific cafe.
- **Report Closed Cafe:** Delete a specific cafe from the database.

## Endpoints

- `GET /all`: Fetch all cafes.
- `GET /random`: Fetch a random cafe.
- `POST /add`: Add a new cafe (requires form-data).
- `PATCH /update-price/<int:cafe_id>`: Update the coffee price of a specific cafe.
- `DELETE /report-closed/<int:cafe_id>`: Delete a specific cafe (requires API key).

## Setup

1. Clone the repository:  
   `git clone https://github.com/Developer122436/MyScrips.git`

2. Navigate to the project directory:  
   `cd My Projects on Data Science, Web and more/Section 66 - Advanced Build RESTful API`

3. Install the required packages:  
   `pip install -r requirements.txt`

4. Run the Flask application:  
   `flask run`

## Documentation

For detailed API documentation, visit [Postman Documentation](<https://documenter.getpostman.com/view/8808282/2s9YC2zDNg>).

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you'd like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
