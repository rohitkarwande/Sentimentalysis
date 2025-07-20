# Sentimentalysis
This project is a web-based dashboard that analyzes and visualizes the sentiment of social media data in real-time. It uses a Python Flask backend to perform Natural Language Processing (NLP) and a dynamic frontend to display the results.

This project was created to demonstrate skills in backend development, data processing, and machine learning, as relevant for a Software Engineering role.

## Key Features
* **Real-time Simulation:** A backend API endpoint simulates a live data stream, providing new data every few seconds.
* **NLP-Powered Sentiment Analysis:** Uses the NLTK (Natural Language Toolkit) library's VADER model to accurately classify text as positive, negative, or neutral.
* **Dynamic Frontend:** The user interface, built with HTML, Tailwind CSS, and Chart.js, updates automatically without needing to refresh the page.
* **Clear Visualization:** A doughnut chart visualizes the overall distribution of sentiment, and a live-updating feed shows the most recent data points.

## Tech Stack
* **Backend:** Python, Flask
* **Machine Learning:** NLTK (VADER)
* **Frontend:** HTML, Tailwind CSS, Chart.js
* **Core Language:** Python

## How to Run Locally
1.  Clone the repository:
    ```bash
    git clone [https://github.com/rohitkarwande/Sentimentalysis.git](https://github.com/rohitkarwande/Sentimentalysis.git)
    cd Sentimentalysis
    ```
2.  Create a virtual environment and install dependencies:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```
3.  Run the Flask application:
    ```bash
    python app.py
    ```
4.  Open your web browser and navigate to `http://127.0.0.1:8080` to see the application running.
