"""Weather app for Paris London Trip
    fetches today's weather and emails it to family"""
import requests
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime
import config  # Import configuration file


# -----------------------------------------------------
# Get weather data from OpenWeather
# -----------------------------------------------------
def get_weather(city, api_key):
    """Return formatted weather info for a city"""
    url = (
        f"http://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={api_key}&units=imperial"
    )
    response = requests.get(url)
    data = response.json()

    temp = data['main']['temp']
    temp_min = data['main']['temp_min']
    temp_max = data['main']['temp_max']
    description = data['weather'][0]['description'].title()
    return (
        f"{city}:\n"
        f" Current: {temp}°F\n"
        f" High: {temp_max}°F\n"
        f" Low: {temp_min}°F\n"
        f" Conditions: {description}"
    )


# -----------------------------------------------------
# Send email using Gmail
# -----------------------------------------------------
def send_email(subject, body, recipients):
    sender_email = config.GMAIL_EMAIL
    password = config.GMAIL_APP_PASSWORD

    # Build email
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = ", ".join(recipients)
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    # Connect to gmail SMTP
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()  # Secure the connection
        server.login(sender_email, password)
        server.sendmail(sender_email, recipients, msg.as_string())


# -----------------------------------------------------
# Main Program
# -----------------------------------------------------
if __name__ == "__main__":
    # Get today's date
    today = datetime.now().strftime("%A, %B %d, %Y")

    # Calculate days until trip
    trip_date = datetime(*config.TRIP_DATE)
    days_until_trip = (trip_date - datetime.now()).days

    # Get weather for both cities
    paris_weather = get_weather(city="Paris", api_key=config.OPENWEATHER_API_KEY)
    london_weather = get_weather(city="London", api_key=config.OPENWEATHER_API_KEY)

    # Build the message body with proper line breaks
    body = (
        "Good morning everyone! ☀️\n\n"
        f"🎊 Only {days_until_trip} days until our Paris & London adventure! 🎊\n\n"
        "Here is today's weather for our upcoming spring trip:\n\n"
        f"📅 Date: {today}\n\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        f"🗼 {paris_weather}\n\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        f"🏰 {london_weather}\n\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "Stay warm and start dreaming about croissants and tea! ☕🥐\n\n"
        "Love,\n"
        "Mimi 💕"
    )

    # Show preview of the email
    print("\n" + "=" * 70)
    print("EMAIL PREVIEW")
    print("=" * 70)
    print(f"Subject: Daily Paris and London Weather")
    print(f"\nTo: {', '.join(config.RECIPIENTS)}")
    print("\n" + "-" * 70)
    print(body)
    print("-" * 70)

    # Ask for confirmation before sending
    print("\n" + "=" * 70)
    confirm = input("\nType 'YES' to send this email, or anything else to cancel: ")

    if confirm.upper() == "YES":
        send_email("Daily Paris and London Weather", body, config.RECIPIENTS)
        print("\n✅ Weather email sent successfully!")
    else:
        print("\n❌ Email cancelled. No email was sent.")