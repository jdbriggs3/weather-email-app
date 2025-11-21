"""Configuration template for Weather Email App

Instructions:
1. Copy this file and rename it to 'config.py'
2. Fill in your actual credentials below
3. Never commit config.py to GitHub (it's in .gitignore)
"""

# OpenWeather API Key
# Get yours at: https://openweathermap.org/api
OPENWEATHER_API_KEY = "your_openweather_api_key_here"

# Gmail Settings
# Use your Gmail address and an App Password (not your regular password)
# Instructions: https://support.google.com/accounts/answer/185833
GMAIL_EMAIL = "your_email@gmail.com"
GMAIL_APP_PASSWORD = "your_gmail_app_password_here"

# Email Recipients
# Add all the email addresses you want to send weather updates to
RECIPIENTS = [
    "recipient1@gmail.com",
    "recipient2@gmail.com",
    "recipient3@gmail.com",
    "recipient4@gmail.com"
]

# Trip Date (Year, Month, Day)
# Change this to your actual departure date
TRIP_DATE = (2027, 1, 1)