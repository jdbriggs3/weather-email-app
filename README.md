# Paris & London Weather Email App

A Python script that sends daily weather updates to family members for our upcoming spring trip to Paris and London!

## What This Does

- Fetches current weather data for Paris and London from OpenWeather API
- Shows a countdown to your trip date
- Formats it into a nice, readable email with emojis
- Sends the email to family members via Gmail
- Shows a preview before sending so you can review it first

## Requirements

- Python 3.x
- `requests` library

## Installation

1. **Clone this repository**
```bash
   git clone https://github.com/yourusername/weather-email-app.git
   cd weather-email-app
```

2. **Install required library**
```bash
   pip install requests
```

3. **Set up your configuration file**
```bash
   # Copy the template
   cp config_template.py config.py
```

4. **Edit `config.py` with your credentials** (see Setup Instructions below)

## Setup Instructions

### 1. Get Your OpenWeather API Key
1. Go to https://openweathermap.org/
2. Sign up for a free account
3. Go to "API keys" in your account dashboard
4. Copy your API key (may take 10-15 minutes to activate)
5. Paste it into `config.py` as `OPENWEATHER_API_KEY`

### 2. Set Up Gmail App Password
1. Make sure 2-Step Verification is ON: https://myaccount.google.com/security
2. Go to https://myaccount.google.com/apppasswords
3. Select "Mail" and "Other (Custom name)"
4. Name it "Weather App" and click "Generate"
5. Copy the 16-character password (remove spaces)
6. Paste it into `config.py` as `GMAIL_APP_PASSWORD`

### 3. Configure Recipients and Trip Date
1. Open `config.py`
2. Add your Gmail address to `GMAIL_EMAIL`
3. Add family email addresses to the `RECIPIENTS` list
4. Set your trip departure date in `TRIP_DATE` as `(Year, Month, Day)`

## How to Run

### From Command Line/Terminal
```bash
# Windows
python weather_app.py

# Mac/Linux
python3 weather_app.py
```

### From PyCharm
1. Open the script in PyCharm
2. Click the green "Run" button
3. View the preview in the console
4. Type "YES" to send

## Daily Use

1. Set a calendar reminder for when you want to send the email
2. Run the script
3. Review the preview
4. Type "YES" to send, or anything else to cancel
5. Done!

## Example Output
```
Good morning everyone! ☀️

🎊 Only 112 days until our Paris & London adventure! 🎊

Here is today's weather for our upcoming spring trip:

📅 Date: Wednesday, November 20, 2025

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🗼 Paris:
 Current: 32.07°F
 High: 33.15°F
 Low: 29.79°F
 Conditions: Few Clouds

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🏰 London:
 Current: 35.19°F
 High: 37.15°F
 Low: 33.62°F
 Conditions: Broken Clouds

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Stay warm and start dreaming about croissants and tea! ☕🥐

Love,
Mimi 💕
```

## Customization

Want to change the email? Edit the `body` section in `weather_app.py`:
- Change the greeting message
- Modify or remove emojis
- Change the closing message
- Adjust the separator lines

To change cities, modify the `get_weather()` calls in the main program section.

## Troubleshooting

**"Invalid API key" error:**
- Wait 10-15 minutes after creating your OpenWeather account
- Double-check you copied the entire key with no extra spaces

**"Authentication failed" error:**
- Verify 2-Step Verification is ON in your Google Account
- Use the App Password, not your regular Gmail password
- Check that there are no spaces in the App Password

**"ModuleNotFoundError: No module named 'config'" error:**
- Make sure you created `config.py` from `config_template.py`
- Verify `config.py` is in the same folder as `weather_app.py`

## Files in This Repository

- `weather_app.py` - The main script
- `config_template.py` - Template for your configuration (copy to config.py)
- `.gitignore` - Prevents sensitive files from being committed
- `README.md` - This file (instructions)

**Note:** `config.py` is not included in the repository for security reasons. You must create it from the template.

## Security

- Never commit `config.py` to version control
- Keep your API keys and passwords private
- The `.gitignore` file protects your credentials automatically

## License

Free to use and modify for personal projects!

---

*Created with love by Mimi* 💕