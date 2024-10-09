```markdown
# Joke Generator App

This project is a web application built with Flask that generates jokes using OpenAI's GPT-4 model based on a user-provided topic. Users can view jokes, rate them (like or dislike), and store them in an SQLite database.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Endpoints](#endpoints)
- [Database](#database)
- [Environment Variables](#environment-variables)
- [License](#license)

## Features

- Generate jokes based on a specific topic using OpenAI's GPT-4.
- Store generated jokes in a local SQLite database.
- Allow users to like or dislike jokes.
- Dynamic web page rendering with Flask and Jinja templates.

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/kempsly/GPT-LLM-Simple-Joke-Generator-App.git
    cd joke-generator-app
    ```

2. **Create a virtual environment:**

    If you’re using `conda`:

    ```bash
    conda create -p venv python=3.10 -y
    conda activate ./venv
    ```

    If you’re using `virtualenv`:

    ```bash
    python -m venv venv
    source venv/bin/activate   # On macOS/Linux
    .\venv\Scripts\activate    # On Windows
    ```

3. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up your environment variables:**

    - Create a `.env` file in the root directory and add your OpenAI API key:

    ```bash
    OPENAI_API_KEY=your-openai-api-key-here
    ```

5. **Initialize the SQLite database:**

    The app automatically creates a `database.db` file in the root folder if it doesn't exist.

## Usage

1. **Run the application:**

    ```bash
    python app.py
    ```

2. Open your browser and go to `http://127.0.0.1:5000/`.

3. Enter a topic (e.g., "computers") and the app will generate three jokes related to that topic using OpenAI's API.

4. You can like or dislike jokes. The joke ratings are updated in the SQLite database.

## Endpoints

- `GET /`: Renders the main page where users can input a topic to generate jokes.
- `POST /generate_jokes`: Accepts a topic via form data, calls the OpenAI API to generate jokes, and returns them to the user.
- `POST /rate_joke`: Allows users to rate jokes by liking or disliking them. Updates the joke's rating in the SQLite database.

## Database

The app uses SQLite to store jokes and their ratings (likes and dislikes). The table schema is as follows:

- **jokes table**:
    - `id`: Auto-incremented primary key.
    - `joke`: The joke text.
    - `likes`: Number of likes.
    - `dislikes`: Number of dislikes.

## Environment Variables

Make sure to set the following environment variables in a `.env` file:

```bash
OPENAI_API_KEY=your-openai-api-key-here
```

You can obtain your OpenAI API key by signing up at [OpenAI](https://openai.com/).

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
```