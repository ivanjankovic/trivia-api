## Full Stack Trivia API Project 

### Project Overview 

Trivia API is a backend web development project created for the Full Stack Developer Nanodegree at Udacity. The goal of the project was to:

* Create all necessary endpoints on the backend to serve the frontend, enabling the visitor of the website to:
    * View all trivia questions stored in a database
    * View trivia questions based on their category
    * Add and delete questions to the database
    * Play trivia in a chosen category, getting random questions from the database
* Apply test-driven development, writing unit tests for each endpoint
* Make modifications to the frontend and database if necessary

### Game Overview 

This Trivia project allows users to play a trivia game and test their general knowledge either for themselves or against friends. The project task was to create and API and unit test for implementing the application allowing it to do the following:

1. Display questions - both all questions and by category. Questions should show the question, category and difficulty rating by default and can show/hide the answer.
2. Delete questions.
3. Add questions and require that they include question and answer text.
4. Search for questions based on a text query string.
5. Play the quiz game, randomizing either all questions or within a specific category.

### Tech stack

* **SQLAlchemy ORM** as the ORM library
* **PostgreSQL** for the database
* **Python3** and **Flask** as the server language and server framework
* **HTML**, **CSS**, and **Javascript** with **Node.js** and **React** for the frontend

## Getting Started

### Database Setup
With Postgres running, restore a database using the trivia.psql file provided. From the backend folder in terminal run:
```bash
psql trivia < trivia.psql
```

### Backend Dependencies
Once you have your virtual environment setup and running, install dependencies by navigating to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```
### Running the server
From within the `backend` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```

### Frontend dependencies
#### Node

This project depends on Nodejs and Node Package Manager (NPM). Find and download Node and npm (which is included) at: [https://nodejs.com/en/download](https://nodejs.org/en/download/).
#### NPM
This project uses NPM to manage software dependencies. NPM Relies on the package.json file located in the `frontend` directory of this repository. After cloning, open your terminal and run:

```bash
npm install
```

## Running Your Frontend in Dev Mode

The frontend app was built using create-react-app. In order to run the app in development mode use ```npm start```. You can change the script in the ```package.json``` file. 

Open [http://localhost:3000](http://localhost:3000) to view it in the browser. The page will reload if you make edits.<br>

```bash
npm start
```

## Testing
To run the tests, run
```
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
``` 