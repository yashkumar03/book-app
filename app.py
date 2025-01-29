from flask import Flask, render_template, request, jsonify
from books import Books

app = Flask(__name__)

@app.route('/', methods=['GET'])
def add_numbers():
    return render_template('index.html', result=None)

@app.route('/books', methods=['GET', 'POST'])
def getBook():
    id = request.args.get('id')
    title = request.args.get('title')
    genre = request.args.get('genre')
    year = request.args.get('year')
    author = request.args.get('author')

    if id:
        return jsonify({"data": Books[int(id) - 1]})

    queried_books = []

    if title:
        for book in Books:
            if book["title"] == title:
                queried_books.append(book)

    elif genre:
        for book in Books:
            if book["genre"] == genre:
                queried_books.append(book)
                
    elif year:
        for book in Books:
            if book["publication_year"] == int(year):
                queried_books.append(book)

    elif author:
        for book in Books:
            if book["author"] == author:
                queried_books.append(book)
    else:
        for book in Books:
            queried_books.append(book)
    
    if queried_books:
        return jsonify(queried_books), 200
    
    else:
        return jsonify({"Error": "No results found for provided filter"})
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)

