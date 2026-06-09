Smart Email Writer is a simple Streamlit application that uses Google's Gemini AI model to generate professional emails and email replies. Users can enter a prompt, and the AI creates email content with appropriate tone adjustments and quick responses.

Features
Generate professional emails instantly.
Create email replies based on user input.
Tone adjustment for formal and informal communication.
Simple and user-friendly Streamlit interface.
Powered by Gemini 2.5 Flash AI model.
Technologies Used
Python
Streamlit
Google Generative AI (Gemini API)
Installation
Clone the repository:
git clone https://github.com/dharaneeshd600/email-ai-102
Navigate to the project folder:
cd smart-email-writer
Install required packages:
pip install streamlit google-generativeai
Add your Gemini API key:
gen.configure(api_key="YOUR_API_KEY")
Usage

Run the application:

streamlit run app.py

Enter your email request in the text box and click Submit. The AI will generate a professional email or reply based on your prompt.

Sample Prompt
Write a professional email requesting leave for two days.
Sample Output
Subject: Leave Request

Dear Manager,

I hope you are doing well. I would like to request leave for two days due to personal reasons...

Thank you for your consideration.

Regards,
Bharanitharan
Project Structure
smart-email-writer/
│
├── app.py
├── README.md
└── requirements.txt
Future Enhancements
Multiple tone options (Formal, Friendly, Professional).
Email templates.
Subject line generation.
Email export functionality.
Multi-language support.
