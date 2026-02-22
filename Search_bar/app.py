from flask import Flask, request, jsonify, render_template
import sqlite3
import difflib
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, 'inventory.db')

def get_all_names():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT product_name FROM products")
    names = [row[0] for row in cursor.fetchall()]
    conn.close()
    return names

@app.route('/')
def index():
    # This serves your UI page
    return render_template('index.html')

@app.route('/search')
def search():
    # 1. Get what the user typed
    query = request.args.get('q', '').strip()
    if not query:
        return jsonify({'exact': [], 'fuzzy': []})
    
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    search_term = f"%{query}%"
    cursor.execute("SELECT product_name, price FROM products WHERE product_name LIKE ? LIMIT 5", (search_term,))
    exact_matches = [{'name': row[0], 'price': row[1]} for row in cursor.fetchall()]
    conn.close()

    fuzzy_matches = []
    if len(exact_matches) < 3:
        all_names = get_all_names()
        exact_names = [m['name'] for m in exact_matches]
        
        suggestions = difflib.get_close_matches(query, all_names, n=3, cutoff=0.5)        

        fuzzy_names = [s for s in suggestions if s not in exact_names]
        fuzzy_matches = [{'name': name} for name in fuzzy_names]

    return jsonify({
        'exact': exact_matches,
        'fuzzy': fuzzy_matches
    })

if __name__ == '__main__':

    app.run(debug=True)
