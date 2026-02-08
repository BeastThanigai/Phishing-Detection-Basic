**Phishing Detection System (Basic)
Flask-Based URL & Text Phishing Detection Using Blacklist and Keyword**

**📌 Project Overview**

This project is a basic Phishing Detection System developed using Python Flask.
It detects phishing attempts by analyzing URLs and text messages using:

Blacklist-based detection (SHA-256 hashed URLs)

Keyword-based detection (common phishing terms)

The project is designed for academic learning, cyber security fundamentals, and introductory phishing detection concepts, without using machine learning.

**🎯 Objective**

To understand how phishing attacks can be detected using simple techniques

To implement signature-based (blacklist) detection

To analyze suspicious text patterns using keywords

To build a basic Flask web application for security analysis

**🧠 Detection Techniques Used**
**1️⃣ Blacklist-Based URL Detection**

URLs are hashed using SHA-256

Hashes are compared with stored hashes in blacklist.txt

If a match is found → URL is marked as phishing

url_hash = hashlib.sha256(url.encode()).hexdigest()

**2️⃣ Keyword-Based Text Detection**

Detects common phishing terms such as:

verify

urgent

click here

login

password

account

update

**Regex is used for pattern matching:**

verify|urgent|click here|login|password|account|update

**⚙️ Features**

✅ URL phishing detection using blacklist signatures

✅ Message/text phishing detection using keywords

✅ SHA-256 hashing for secure comparison

✅ Flask web interface

✅ JSON-based response for detection results

✅ Simple and lightweight implementation


📂 Project Structure
PhishingDetectionBasic/
│── app.py
│── blacklist.txt
│── templates/
│   └── index.html
│── static/
│── .gitignore
│── README.md


app.py → Flask application logic

blacklist.txt → Contains blacklisted URL signatures

templates/ → HTML files for UI

static/ → CSS / JS (if any)

**▶️ How to Run the Project**
Step 1: Install Flask
pip install flask

Step 2: Navigate to project folder
cd PhishingDetectionBasic

Step 3: Run the application
python app.py

Step 4: Open browser
http://127.0.0.1:5000/

**🧪 Sample Detection**
Example 1: Phishing Text
Urgent! Verify your account now.


➡️ Phishing Detected: YES

Example 2: Normal Message
Meeting scheduled for tomorrow.


➡️ Phishing Detected: NO



**🚀 Future Enhancements**

Integrate Machine Learning models

Use real-time URL reputation APIs

Add email phishing detection

Store scan history in database

Deploy on cloud (Render / Heroku)

**📜 License**

This project is created for educational and academic purposes only.
