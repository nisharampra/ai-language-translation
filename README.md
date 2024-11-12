# ai-language-translation

# Translation App Using LangChain and Node.js

ThiThis application translates text from one language to another using a combination of a Node.js backend and a Python script with LangChain and Ollama. The Python script handles the translation logic, while the Node.js server acts as an interface to interact with the user through a simple web interface.

Prerequisites
Before running the application, make sure you have the following installed:

Node.js (v14 or later)
Python 3.x
Required Python libraries (langchain_ollama, OllamaLLM, etc.)

How It Works
The user enters text and a target language in the front-end form.
The form sends a POST request to the Node.js backend (server.js).
The Node.js server executes the translate.py Python script, passing the text and target language as arguments.
The Python script uses the LangChain and Ollama model to translate the text and returns the result.
The backend sends the translated text back to the front end, where it is displayed to the user.
Example
Frontend Input
Text: Hello, how are you?
Target Language: Spanish
Translation Output
Translated Text: Hola, ¿cómo estás?
