from flask import Flask, render_template
from serpapi import GoogleSearch
import random 
app = Flask(__name__)

# Your SerpApi API key
API_KEY = "98f3960cc659239784d475245dfe43386f2b6332c4bb736d7e4f8b073adc29a3"

@app.route('/')
def index():
    # Define the parameters for the job search
    params = {
        "engine": "google_jobs",
        "q": "microbiologist",
        "location": "India",
        "hl": "en",
        "api_key": API_KEY
    }

    # Make the API request
    search = GoogleSearch(params)
    results = search.get_dict()

    # Extract the job results
    jobs_results = results.get("jobs_results", [])
    random.shuffle(jobs_results)
    return render_template('index.html', jobs=jobs_results)

if __name__ == '__main__':
    app.run(debug=True)
