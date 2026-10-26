from flask import Flask, request, redirect, render_template_string
import sqlite3
import os

app = Flask(__name__)

DB_PATH = os.environ.get("DB_PATH", "data/app.db")

def init_db():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, name TEXT)')
    conn.commit()
    conn.close()

@app.route("/", methods=["GET", "POST"])
def index():
    init_db()
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    
    if request.method == "POST":
        name = request.form.get("name")
        if name:
            c.execute('INSERT INTO items (name) VALUES (?)', (name,))
            conn.commit()
        return redirect("/")
    
    c.execute('SELECT name FROM items')
    items = c.fetchall()
    conn.close()

    html = """
    <h1>Lista de Compras</h1>
    <form method="POST">
        <input type="text" name="name" placeholder="Item" required />
        <button type="submit">Adicionar</button>
    </form>
    <ul>
        {% for item in items %}
            <li>{{ item[0] }}</li>
        {% endfor %}
    </ul>
    """
    return render_template_string(html, items=items)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)