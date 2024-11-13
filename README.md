
# NLP-to-SQL Query Project

This project allows users to convert natural language questions into SQL queries and retrieve data from a SQLite database. It uses the Google Gemini Large Language Model (LLM) to interpret the natural language input and generate corresponding SQL commands.

## Features

- Converts English questions into SQL queries
- Retrieves data from an SQLite database based on generated SQL queries
- Streamlit-based user interface for easy interaction

## Table of Contents

- [Installation]
- [Usage]
- [Environment Variables]
- [File Structure]
- [License]

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/GreenApple093/nlp-to-sql.git
   ```

2. **Install the required packages**:
   Make sure you have Python installed. Then, install the dependencies from `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up the SQLite database:**
   Run the `sql.py` script to create and populate the `STUDENT` table in `test.db`:
   ```bash
   python sql.py
   ```

4. **Set up environment variables:**
   Create a `.env` file in the root directory of your project with the following content:
   ```plaintext
   GOOGLE_API_KEY=your_actual_google_api_key
   ```
   Replace `your_actual_google_api_key` with your Google Gemini API key.

## Usage

1. **Start the Streamlit app:**
   Run the following command to launch the app:
   ```bash
   streamlit run app.py
   ```

2. **Interact with the app:**
   - Input a natural language question in the provided text input field.
   - Click the "Ask the question" button.
   - The application will generate a SQL query, execute it against the SQLite database, and display the results.

## Environment Variables

This project uses the `.env` file to manage environment variables. Ensure the following variable is set:

- `GOOGLE_API_KEY`: Your API key for Google Gemini LLM.

## File Structure

```plaintext
.
├── app.py               # Main Streamlit app code
├── sql.py               # Script to set up SQLite database
├── requirements.txt     # Python dependencies
├── .env                 # Environment variables (not included in version control)
├── .gitignore           # Git ignore file
└── README.md            # Project documentation
```

## Requirements

All required Python packages are listed in `requirements.txt`. To install them, use:

```bash
pip install -r requirements.txt
```


## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

