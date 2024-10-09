from flask import Flask, render_template, request
import sqlite3
from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Configure OpenAI
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def create_connection():
    conn = sqlite3.connect('database.db')
    return conn

def create_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS jokes
                      (id INTEGER PRIMARY KEY AUTOINCREMENT, joke TEXT, likes INTEGER, dislikes INTEGER)''')
    conn.commit()
    conn.close()

create_table()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_jokes', methods=['POST'])
def generate_jokes():
    topic = request.form['topic']
    print("Calling OpenAI API...")
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {
                "role": "system",
                "content": [
                    {
                        "type": "text",
                        "text": f"Tell me three jokes about {topic}, separated by ---."
                    }
                ]
            }
        ],
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    
    jokes = [j.strip() for j in response.choices[0].message.content.strip().split("---") if j.strip()]

    print(jokes)

    joke_ids = []
    
    conn = create_connection()
    cursor = conn.cursor()
    for joke in jokes:
        cursor.execute("INSERT INTO jokes (joke, likes, dislikes) VALUES (?, ?, ?)", (joke, 0, 0))
        joke_id = cursor.lastrowid  # Get the last inserted id
        joke_ids.append(joke_id)  # Append the id to the list
    conn.commit()
    conn.close()

    # zip the jokes and joke_ids together
    jokes = zip(jokes, joke_ids)

    # Render HTML fragment
    return render_template('_jokes.html', jokes=jokes)


@app.route('/rate_joke', methods=['POST'])
def rate_joke():
    joke_id = request.form['id']
    rating = request.form['rating']
    
    conn = create_connection()
    cursor = conn.cursor()
    if rating == 'like':
        cursor.execute("UPDATE jokes SET likes = likes + 1 WHERE id = ?", (joke_id,))
    else:
        cursor.execute("UPDATE jokes SET dislikes = dislikes + 1 WHERE id = ?", (joke_id,))
    conn.commit()
    conn.close()
    
    # Return HTML to update the button
    if rating == 'like':
        return render_template('_like.html', joke_id=joke_id)
    else:
        return render_template('_dislike.html', joke_id=joke_id)

if __name__ == '__main__':
    app.run(debug=True)
