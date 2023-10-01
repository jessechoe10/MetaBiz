from flask import Flask, render_template, request, jsonify
from metaphor_python import Metaphor

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data = request.json
        search_term = data.get('search', "")
        
        metaphor = Metaphor("c9494bd2-cdef-43ae-ad06-f340de23b201")
        response = metaphor.search(
            search_term,
            num_results=10,
            use_autoprompt=True,
        )
        articles = response.results
        return jsonify(articles)
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)