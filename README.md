# Practical Task
This project is an API for createating Employee and Company detail from excel file.

This project can be run using either of the following methods:
1. Virtual Environment
2. Docker

## Pre Requirements
1. Python
2. Docker

## Steps To Clone Project
```bash
   git clone https://github.com/ThakkarUtsav369/PracticalTask.git
   cd PracticalTask/
```
## Steps to Run Project With Venv
Please Follow the below commnad to run the project:

1. Create a virtual environment:
```bash
   python -m venv env
```
2. Activate the virtual environment:
   
   On Windows:
  ```bash
      .\env\Scripts\activate
  ```
    On macOS and Linux:
  ```bash
    source env/bin/activate
  ```
3. Install dependencies:
  ```bash
       pip install -r requirements.txt
  ```
4. Run migrations:
   ```bash
   python manage.py migrate
   ```

5. Run server:
  ```bash
    python manage.py runserver
  ```

6. Open a postman and create a post request and use form-data for body http://localhost:8000/api/v1/uploadCsv/ to view the project.


## Steps to Run Project With Docker
Please Follow the below commnad to run the project:

1. Check if Docker and docker-compose is installed or not:

    for maccOS/linux use sudo for all the command:
  ```bash
      docker-compose --version
      docker --version
  ```
2. Create .env file from .env.example
3. Build the Docker Container
  ```bash
     docker-compose build
 ```
4. Run the Docker Container
```bash
  docker-compose up
```
5. Open a postman and create a post request and use form-data for body http://localhost:8000/api/v1/uploadCsv/ to view the project.




