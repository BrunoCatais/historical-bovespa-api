# Stock API

This is a simple REST API for managing stocks. It provides CRUD operations for stocks and historical prices, as well as retrieval of stock data from the Ibovespa index.

## Installation

1. Clone this repository to your local machine
2. Install the required dependencies using pip:

```
pip install -r requirements.txt
```

## Usage

To start the application, run the following command:

```
uvicorn main:app --reload
```

This will start the application server and make it available at http://localhost:8000.

The API documentation is available at http://localhost:8000/docs
