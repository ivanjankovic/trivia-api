import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from models import setup_db, Question, Category, db
import sys
import json

QUESTIONS_PER_PAGE = 10

# paginating questions
def paginate_questions(request, selection):
    page = request.args.get('page', 1, type=int)
    start = (page - 1) * QUESTIONS_PER_PAGE
    end = start + QUESTIONS_PER_PAGE

    questions = [question.format() for question in selection]
    current_questions = questions[start:end]

    return current_questions

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)

    # DONE 1: Set up CORS. Allow '*' for origins.
    # Delete the sample route after completing the TODOs
    CORS(app, resources={r"/api/*": {"origins": "*"}})


    # DONE 2: Use the after_request decorator to set Access-Control-Allow
    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Methods', 'GET, POST, DELETE')
        return response

    def all_categories():
        # get all categories and return dictionary
        categories = Category.query.all()
        return { category.id: category.type for category in categories }


# ----------------------------------------------------------------------------
# DONE 3: Create an endpoint to handle GET requests for all available categories.
# ----------------------------------------------------------------------------

    @app.route('/categories')
    def get_categories():
        categories_dict = all_categories()

        # abort if no categories
        if len(categories_dict) == 0:
            abort(404)

        # return category data to view
        return jsonify({
            'success': True,
            'categories': categories_dict,
        })

# ----------------------------------------------------------------------------
# DONE 4: Create an endpoint to handle GET requests for questions, 
# including pagination (every 10 questions). 
# This endpoint should return a list of questions, 
# number of total questions, current category, categories. 

# TEST: At this point, when you start the application
# you should see questions and categories generated,
# ten questions per page and pagination at the bottom of the screen for three pages.
# Clicking on the page numbers should update the questions. 
# ----------------------------------------------------------------------------

    @app.route('/questions')
    def get_questions():
        # get questions and paginate
        all_questions = Question.query.all()
        current_questions = paginate_questions(request, all_questions)
        
        # abort if no questions
        if len(current_questions) == 0:
            abort(404)
        
        # return all required data to view
        return jsonify({
            'success': True,
            'questions': current_questions,
            'total_questions': len(all_questions),
            'curret_category': request.args.get('category', 'None'),
            'categories': all_categories(),
        })

# ----------------------------------------------------------------------------
# DONE 5: Create an endpoint to DELETE question using a question ID.

# TEST: When you click the trash icon next to a question, the question will be removed.
# This removal will persist in the database and when you refresh the page. 
# ----------------------------------------------------------------------------

    @app.route('/questions/<int:id>', methods=['DELETE'])
    def delete_question(id):
        try:
            # get question by id, use one_or_none to only turn one result
            # or call exception if none selected
            question = Question.query.get(id)


            # abort if question not found
            if not question:
                abort(404)

            # delete and return success message
            question.delete()

            return jsonify({
                'success': True,
                'deleted_question_id': id
            })
        except:
            # abort if there's a problem deleting the question
            abort(422)

# ----------------------------------------------------------------------------
# DONE 6: Create an endpoint to POST a new question, 
# which will require the question and answer text, 
# category, and difficulty score.

# TEST: When you submit a question on the "Add" tab, 
# the form will clear and the question will appear at the end of the last page
# of the questions list in the "List" tab.  
# ----------------------------------------------------------------------------

    @app.route('/questions', methods=['POST'])
    def create_question():
        # load request body and data
        body = request.get_json()

        if not ('question' in body and 'answer' in body and
                'difficulty' in body and 'category' in body):
            abort(422)

        try:
            # Create and insert new question
            question = Question(body.get('question'),
                                body.get('answer'),
                                body.get('difficulty'),
                                body.get('category'))
            question.insert()

            # get all questions and paginate
            selection = Question.query.order_by(Question.id).all()
            current_questions = paginate_questions(request, selection)

            return jsonify({
                'success': True,
                'created': question.id,
                'question_created': question.question,
                'questions': current_questions,
                'total_questions': len(Question.query.all())
            })
        except:
            abort(422)

# ----------------------------------------------------------------------------
# DONE 7: Create a POST endpoint to get questions based on a search term. 
# It should return any questions for whom the search term 
# is a substring of the question.

# TEST: Search by any phrase. The questions list will update to include 
# only question that include that string within their question. 
# Try using the word "title" to start. 
# ----------------------------------------------------------------------------

    @app.route('/questions/search', methods=['POST'])
    def search_questions():
        # Get user input
        body = request.get_json()
        search_term = body.get('searchTerm', None)

        # If a search term has been entered, apply filter for question string
        # and check if there are results
        try:
            if search_term:
                search_results = Question.query.filter(Question.question.ilike
                                                (f'%{search_term}%')).all()

            # paginate and return results
            paginated = paginate_questions(request, search_results)

            return jsonify({
                'success': True,
                'questions':  paginated,
                'search_term': search_term,
                'total_questions': len(search_results),
                'current_category': None
            })
        except:
            abort(404)

# ----------------------------------------------------------------------------
# DONE 8: Create a GET endpoint to get questions based on category.

# TEST: In the "List" tab / main screen, clicking on one of the 
# categories in the left column will cause only questions of that 
# category to be shown. 
# ----------------------------------------------------------------------------

    @app.route('/categories/<int:id>/questions')
    def get_category_questions(id):
        # Get category by id, try get questions from matching category
        category = Category.query.filter_by(id=id).one_or_none()

        try:
            # get questions matching the category
            category_questions = Question.query.filter_by(category=category.id).all()

            if len(category_questions) == 0:
                abort(404)

            # paginate selected questions and return results
            page_questions = paginate_questions(request, category_questions)
            
            return jsonify({
                'success': True,
                'questions': page_questions,
                'total_questions': len(page_questions),
                'current_category': category.type
            })
        except:
            abort(400)

# ----------------------------------------------------------------------------
# DONE 9: Create a POST endpoint to get questions to play the quiz. 
# This endpoint should take category and previous question parameters 
# and return a random questions within the given category, 
# if provided, and that is not one of the previous questions. 

# TEST: In the "Play" tab, after a user selects "All" or a category,
# one question at a time is displayed, the user is allowed to answer
# and shown whether they were correct or not. 
# ----------------------------------------------------------------------------

    @app.route('/quizzes', methods=['POST'])
    def get_quiz():
        try:
            body = request.get_json()

            category = body.get('quiz_category')
            previous_questions = body.get('previous_questions')

            # If 'ALL' categories is 'clicked', filter available Qs
            if category['type'] == 'click':
                available_questions = Question.query.filter(
                    Question.id.notin_((previous_questions))).all()
            # Filter available questions by chosen category & unused questions
            else:
                available_questions = Question.query.filter_by(
                    category=category['id']).filter(
                        Question.id.notin_((previous_questions))).all()

            # randomly select next question from available questions
            new_question = available_questions[random.randrange(
                0, len(available_questions))].format() if len(
                    available_questions) > 0 else None

            return jsonify({
                'success': True,
                'question': new_question
            })
        except:
            abort(422)

# ----------------------------------------------------------------------------
# DONE 10: Create error handlers for all expected errors 
# including 404 and 422. 
# ----------------------------------------------------------------------------

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": "Bad Request"
        }), 400

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "Resource Not Found"
        }), 404

    @app.errorhandler(405)
    def method_not_allowed(error):
        return jsonify({
            "success" : False,
            "error" : 405,
            "message" : "Method Not Allowed"
        }), 405

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "Unprocessable Entity"
        }), 422

    @app.errorhandler(500)
    def internal_server_error(error):
        return jsonify({
            "success": False,
            "error": 500,
            "message": "Internal Server Error"
        }), 500

    return app
