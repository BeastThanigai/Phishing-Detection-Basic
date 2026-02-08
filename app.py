from flask import Flask, render_template, request, jsonify
import hashlib
import re

app = Flask(__name__)

# Load blacklisted URL hashes
def load_blacklist():
    with open("blacklist.txt", "r") as f:
        blacklist_hashes = {hashlib.sha256(line.strip().encode()).hexdigest() for line in f}
    return blacklist_hashes

BLACKLIST_HASHES = load_blacklist()

# Helper function to check for phishing keywords in messages
def detect_phishing_keywords(message):
    phishing_keywords = re.compile(r"verify|urgent|click here|login|password|account|update", re.IGNORECASE)
    return bool(phishing_keywords.search(message))

# Helper function to check if a URL is blacklisted
def is_phishing_url(url):
    url_hash = hashlib.sha256(url.encode()).hexdigest()
    return url_hash in BLACKLIST_HASHES

# Define the route for the home page
@app.route('/')
def index():
    return render_template('index.html')

# Define the API endpoint to check for phishing
@app.route('/check_phishing', methods=['POST'])
def check_phishing():
    data = request.form
    url = data.get("url", "")
    message = data.get("message", "")
    
    # Perform checks for phishing indicators
    url_phishing = is_phishing_url(url) if url else False
    message_phishing = detect_phishing_keywords(message) if message else False
    
    # Return the result as JSON
    result = {
        "url_phishing": url_phishing,
        "message_phishing": message_phishing,
        "phishing_detected": url_phishing or message_phishing
    }
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
