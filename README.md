# Python ScyllaDB Project

This project is a Python application that interfaces with [ScyllaDB](https://scylladb.com),
a high-performance NoSQL database, for basic CRUD (Create, Read, Update, Delete) operations.
It utilizes the `scylla-driver` library to interact with the database and demonstrates
operations like adding, reading, updating, and deleting user data.

## Prerequisites

Before you start, ensure you have the following installed:

- Python 3.x ([Python Installation Guide](https://www.python.org/downloads/))
- pip (usually installed with Python)
- Docker and Docker Compose ([Docker Install Documentation](https://docs.docker.com/get-docker/))

## Setting Up ScyllaDB with Docker Compose

To run ScyllaDB locally, you can use Docker Compose. Here's a simple setup:

1. **Run the ScyllaDB container**:

    ```bash
    docker-compose up -d
    ```

   This command will download the ScyllaDB image and start a ScyllaDB instance.

## Setting Up the Python Environment

1. **Create a virtual environment (recommended)**:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

2. **Install dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

## Running the Python Application

To run the Python application:

1. **Execute the script**:

    ```bash
    python main.py
    ```

   This will start the application and perform the defined database operations.

## Environment Configuration

The application expects the ScyllaDB cluster IP to be configured in the script.
Replace `'localhost'` in the `Cluster` configuration with your ScyllaDB cluster IP.

## Contributing

Contributions to this project are welcome! Please fork the repository and submit a pull
request with your changes.

---
