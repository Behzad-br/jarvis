import requests
import json
import pyttsx3

# Initialize TTS engine
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def latestnews():
    # API endpoint dictionary with placeholders for API key
    api_dict = {
        "business": "https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=YOUR_API_KEY",
        "entertainment": "https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=YOUR_API_KEY",
        "health": "https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=YOUR_API_KEY",
        "science": "https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=YOUR_API_KEY",
        "sports": "https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=YOUR_API_KEY",
        "technology": "https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=YOUR_API_KEY"
    }

    # Prompt user for news category
    speak("Which field news do you want? Options are: business, health, technology, sports, entertainment, science.")
    field = input("Type the field news that you want: ").strip().lower()

    # Validate and get the URL
    url = api_dict.get(field)
    if not url:
        speak("Sorry, the news category you requested is not available.")
        print("Sorry, the news category you requested is not available.")
        return

    # Fetch and process news
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        news = response.json()
        
        if 'articles' not in news:
            speak("No articles found.")
            print("No articles found.")
            return

        speak("Here is the first news.")
        articles = news["articles"]
        
        for article in articles:
            title = article.get("title")
            news_url = article.get("url")
            if title:
                print(title)
                speak(title)
                if news_url:
                    print(f"For more info visit: {news_url}")
            
            # User control to continue or stop
            a = input("[press 1 to continue] and [press 2 to stop]: ")
            if a == "2":
                break

        speak("That's all for now.")
    
    except requests.RequestException as e:
        speak("There was an error retrieving the news.")
        print(f"Error: {e}")

# Example usage
if __name__ == "__main__":
    latestnews()
