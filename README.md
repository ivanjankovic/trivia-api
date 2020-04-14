## Full Stack Trivia API Project 

- [Overview](#project-overview)
- [Getting Started](#Getting-Started)
- [Testing](#Testing)
- [API Documentation](#API-Documentation)

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

### Running Frontend in Dev Mode

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

## API Documentation

- [Endpoints](#Endpoints)
- [Error Handling](#Error-Handling)

### Endpoints

- [GET '/categories'](#GET-'/categories')
- [GET '/questions'](#GET-'/questions')
- [GET '/categories/{category_id}/questions'](#GET-'/categories/{category_id}/questions')
- [DELETE '/questions/{question_id}'](#DELETE-'/questions/{question_id}')
- [POST '/questions/search'](#POST-'/questions/search')
- [POST '/questions'](#POST-'/questions')
- [POST '/quizzes'](#POST-'/quizzes')

#### GET '/categories'

- Fetches a dictionary of categories in which the keys are the ids and the value is the corresponding string of the category
- Request Arguments: None
- Returns: An object with a single key, categories, that contains a object of id: category_string key:value pairs.
- Sample: `curl http//127.0.0.1:5000/categories`

```javascript
{
    'categories' : {
        '1' : "Science",
        '2' : "Art",
        '3' : "Geography",
        '4' : "History",
        '5' : "Entertainment",
        '6' : "Sports"
    },
    "success" : true
}
```

#### GET '/questions'

- Fetches a paginated view of all questions in the database ordered by category
- Request arguments: None
- Optional URL query: `?page={num}`
- Returns a json object with a list of paginated questions, total number of questions in the database, dictionary of the categories, current category displayed, and the number of questions currently displayed.
- Sample: `curl 127.0.0.1:5000/questions?page=2`

```javascript
{
  "categories": {
    "1": "Science", 
    "2": "Art", 
    "3": "Geography", 
    "4": "History", 
    "5": "Entertainment", 
    "6": "Sports"
  }, 
  "current_category": "None", 
  "questions": [
    {
      "answer": "Agra", 
      "category": 3, 
      "difficulty": 2, 
      "id": 15, 
      "question": "The Taj Mahal is located in which Indian city?"
    }, 
    {
      "answer": "Lake Victoria", 
      "category": 3, 
      "difficulty": 2, 
      "id": 13, 
      "question": "What is the largest lake in Africa?"
    }
  ],
  "success": true, 
  "total_questions": 19
}
```

#### GET '/categories/{category_id}/questions'

- Fetches all questions of a selected category
- Request args: None
- Returns a list of question objects, the current category, and the number of questions returned
- Sample: `curl 127.0.0.1:5000/categories/3/questions`

```javascript
{
  "current_category": "Geography", 
  "questions": [
    {
      "answer": "Agra", 
      "category": 3, 
      "difficulty": 2, 
      "id": 15, 
      "question": "The Taj Mahal is located in which Indian city?"
    },
    {
      "answer": "Charles Babbage",
      "category": 3,
      "difficulty": 1,
      "id": 25,
      "question": "Who is often called the father of the computer?"
    }
  ], 
  "success": true, 
  "total_questions": 2
}
```

#### DELETE '/questions/{question_id}'

- Deletes the question at the given `question_id`
- Request arguments: None
- Returns `id` of deleted question
- Sample: `curl -X DELETE http://127.0.0.1:5000/questions/12`

```javascript
{
  "deleted_question": 12, 
  "success": true
}
```

#### POST '/questions/search'

- Fetches all questions that contain search text
- Request arguments: `searchTerm`
- Returns questions which match the search, number of total questions returned, current category and search term
- Sample: `curl http://127.0.0.1:5000/questions/search -X POST -H "Content-Type: application/json" -d '{"searchTerm": "artist"}`


```javascript
{
  "current_category": null,
  "questions": [
    {
      "answer": "Escher",
      "category": 2,
      "difficulty": 1,
      "id": 16,
      "question": "Which Dutch graphic artist\u2013initials M C was a creator of optical illusions?"
    },
    {
      "answer": "Jackson Pollock",
      "category": 2,
      "difficulty": 2,
      "id": 19,
      "question": "Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?"
    }
  ],
  "search_term": "artist",
  "success": true,
  "total_questions": 2
}
```

#### POST '/questions'

- Adds a new question to the database
- Request arguments: 
  - `question`
  - `category` (`int` 1-5)
  - `difficulty` (`int` 1-5)
  - `answer`
- Returns new question id, new question, a list of questions objects and the number of all questions 
- Sample: `curl -X POST -H "Content-Type: application/json" -d '{"question": "Who is the father of the programmable computer." , "answer" : "Charles Babbage", "category" : "1", "difficulty" : "2"}' http://127.0.0.1:5000/questions`

```javascript
{
  "created": 26,
  "question_created": "Who is the father of the programmable computer.",
  "questions": [
    {
      "answer": "Apollo 13",
      "category": 5,
      "difficulty": 4,
      "id": 2,
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
    },
    {
      "answer": "Tom Cruise",
      "category": 5,
      "difficulty": 4,
      "id": 4,
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
    },
    ...
  ],
  "success": true,
  "total_questions": 19
}
```

#### POST '/quizzes'

- Fetches a random question from specific category, or all categories if category id is 0
- Request Arguments:
  - `quiz_category`: dictionary containing `id` and `type` of category
  - `previous_questions` : list of `id`s of previous questions of selected category
- Returns a question object to be displayed on the frontend
- Sample: `curl http://127.0.0.1:5000/quizzes -X POST -H "Content-Type: application/json" -d '{"previous_questions": [7, 8], "quiz_category": {"type": "Geography", "id": "3"}}'`

```javascript
{
  "question": {
    "answer": "Agra",
    "category": 3,
    "difficulty": 2,
    "id": 15,
    "question": "The Taj Mahal is located in which Indian city?"
  },
  "success": true
}
```

### Error Handling

Errors are returned as JSON objects in the following format:

```python
{
    "success": False, 
    "error": 400,
    "message": "Bad Request"
}
```

The API will return three error types when requests fail:

- 400: Bad Request
- 404: Resource Not Found
- 405: Not Allowed
- 422: Unprocessable Entity
- 500: Internal Service Error