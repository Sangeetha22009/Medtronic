# Flask App with Pytest Tests

This is a simple Flask application that demonstrates basic CRUD operations using a dummy dataset of flowers. The application includes pytest tests to ensure the functionality of the app.

## Usage

To start the Flask application, run the following command:

`python main.py`

The application will be accessible at [http://localhost:5000](http://localhost:5000).

## Running Tests

To run the pytest tests, use the following command:

`pytest`

This will execute all the test cases and provide a detailed report of the test results.

## Test fixture basic

to run this test

`pytest -k divisible -v`

## Test markers
to run this test

`pytest -m square -v` 

`pytest test_fixture_basic.py -m square -v`

`pytest -m others -v`

## Test Parameterizing

to run this test

`pytest -k multiplication -v`

## Test skip/Xfail
to run this test

`pytest test_skip_xfail.py -v`

## Exports Test Report

| File Format | Pytest Command                   |
|-------------|----------------------------------|
| XML         | pytest --junit-xml='<file_name>' |
| HTML        | pytest --html=<file_name>        |
| PDF         | python utils/report_to_pdf.py    |