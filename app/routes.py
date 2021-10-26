from flask.globals import session
from app import db
from app.models.book import Book
from flask import Blueprint, jsonify, make_response, request

books_bp = Blueprint("books_bp", __name__,url_prefix="/books")

@books_bp.route("",methods=["POST", "GET"])
def handle_books():
    if request.method == "POST":
        request_body = request.get_json()
        if "title" not in request_body or "description" not in request_body:
            return make_response("Invalid Request", 400)
        
        new_book = Book(
        title = request_body["title"],
        description = request_body["description"]
    )
        db.session.add(new_book)
        db.session.commit()
        return make_response(
            f"Book {new_book.title} created",201)
    elif request.method == "GET":
        title_from_url = request.args.get("title")
        if title_from_url:
            books = Book.query.filter_by(title=title_from_url)
        else:
            books = Book.query.all()
        books_response = []
        for book in books:
            books_response.append(
                {
                "id": book.id,
                "title": book.title,
                "description": book.description
                }
            )
        return jsonify(books_response)

@books_bp.route("/<book_id>", methods = ["GET", "PUT", "DELETE"])
def handle_book(book_id):
    book = Book.query.get(book_id)
    if book == None:
        return {
            "message":"NOT FOUND"}, 404

    if request.method == "GET":
        return {
            "id": book.id,
            "title": book.title,
            "description": book.description
            }
    elif request.method == "PUT":
        request_body = request.get_json()
        try:
            book.title = request_body["title"]
            book.description = request_body["description"]

        # db.session.add(book)
            db.session.commit()
            return {
        "id": book.id,
            "title": book.title,
            "description": book.description
    },200
        except KeyError:
            return {
            "message": "Request is invalid"
        },400

    elif request.method == "DELETE":
        db.session.delete(book)
        db.session.commit()
        return {
            "message": f"Book with title {book.title} has been deleted"
        }, 200

