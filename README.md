# Blood Analysis Hub

## Description

The Blood Analysis App is a web application designed to help users analyze and interpret their laboratory blood test results. It provides a user-friendly interface for inputting blood test data, visualizing results, and understanding the implications of these results for their health.

## Features

- Input and store blood test results.
- Visualize test results with charts and graphs.
- Interpret test results and provide explanations.
- Track historical test data over time.
- Secure and private data storage.

## Getting Started

### Prerequisites

- Python 3.11.2

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Connoisseur01/BloodAnalysis_Hub.git
    cd BloodAnalysis_Hub

2. Install dependencies:

    ```bash
    pip install -r requirements.txt

3. database migration:

    in python command line:
    ```python
    from . import db, create_app
    app = create_app()
    app.app_context().push()
    db.create_all()
    exit()

4. Run the application:

    ```bash
    python run.py

