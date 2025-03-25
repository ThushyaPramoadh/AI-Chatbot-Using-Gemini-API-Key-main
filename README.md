# AI Chatbot Using Gemini API

## Overview
This project is an AI-powered chatbot utilizing Google's Gemini API. The chatbot processes user queries and generates intelligent responses in real-time.

## Features
- Integrates with Google's Gemini API for AI-powered responses
- User-friendly interface with Flask
- Supports text-based conversations

## Installation
### Prerequisites
- Python 3.x
- Flask
- A valid Gemini API Key

### Setup
1. Clone this repository:
   ```sh
   git clone https://github.com/ThushyaPramoadh/AI-Chatbot-Using-Gemini-API-Key-main.git
   cd AI-Chatbot-Using-Gemini-API-Key-main
   ```
2. Create and activate a virtual environment:
   - **Windows**:
     ```sh
     python -m venv venv
     venv\Scripts\activate
     ```
   - **MacOS/Linux**:
     ```sh
     python3 -m venv venv
     source venv/bin/activate
     ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Set up your Gemini API Key in an environment variable:
   - **Windows**:
     ```sh
     set GEMINI_API_KEY=your_api_key_here
     ```
   - **MacOS/Linux**:
     ```sh
     export GEMINI_API_KEY="your_api_key_here"
     ```
5. Run the application:
   ```sh
   python app.py
   ```
6. Open your browser and visit:
   ```
   http://127.0.0.1:5000
   ```

## Usage
- Enter a message in the chatbot interface.
- The chatbot will process your input and return AI-generated responses.

## Folder Structure
```
AI_Chatbot_Gemini/
├── app.py                  # Main Flask application
├── requirements.txt        # Dependencies
├── README.md               # Project documentation
├── templates/              # HTML templates
│   └── index.html
├── static/                 # Static files (CSS, JS, images)
│   ├── style.css
│   └── script.js
└── tests/                  # Unit tests
    └── test_app.py
```

## Contributing
1. Fork the repository.
2. Create a new branch:
   ```sh
   git checkout -b feature-branch
   ```
3. Commit your changes:
   ```sh
   git commit -m "Added new feature"
   ```
4. Push to the branch:
   ```sh
   git push origin feature-branch
   ```
5. Open a Pull Request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact
For any queries or issues, open an issue in the repository or contact the author.


1. **Clone the Repository**:
    ```bash
    git clone <repository_url>
    cd AI_Chatbot_Gemini
    ```

2. **Configure the Gemini API**:
   - Sign up for an API key at the [Gemini API](https://gemini.com/) website.
   - Replace `your_gemini_api_key_here` in `app.py` with your actual Gemini API key.

3. **Run the Flask Application**:
    ```bash
    python app.py
    ```

4. **Access the Chatbot**:
   - Open a browser and go to [http://127.0.0.1:5000](http://127.0.0.1:5000).

## Usage

1. Type your message in the input box on the webpage.
2. Click "Send" to get a response from the Gemini AI chatbot.
3. The conversation history will appear on the page.

## Files

- `app.py`: Main Flask application that routes requests, calls the Gemini API, and returns chatbot responses.
- `templates/index.html`: HTML file that contains the chatbot UI.
- `static/style.css`: Styles for the chatbot UI.
- `static/script.js`: JavaScript for sending and receiving messages asynchronously.

## License

This project is open-source and free to use.
