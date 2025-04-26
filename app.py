from flask import Flask, request, render_template, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('search.html')

@app.route('/search')
def search():
    query = request.args.get('q')
    solr_url = f"http://localhost:8983/solr/mycollection/select?q=title:{query}&wt=json"
    response = requests.get(solr_url)
    results = response.json()['response']['docs']
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
