from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


def get_youtube_transcript(video_url):
    # Your existing transcript extraction code goes here
    # Return the transcript as a string
    pass


def login_to_chatgpt(driver):
    # Open the ChatGPT login page
    driver.get("https://chat.openai.com/")

    # Wait for the page to load (adjust time if needed)
    time.sleep(5)

    # If you're not already logged in, you will need to handle the login process here
    # This will depend on your login flow (e.g., using Google, email, etc.)
    # For simplicity, this assumes you're already logged in


def ask_chatgpt_to_summarize(driver, transcript):
    # Find the input box and send the transcript to ChatGPT
    input_box = driver.find_element(By.TAG_NAME, 'textarea')
    input_box.send_keys(f"Please summarize this transcript:\n{transcript}")
    input_box.send_keys(Keys.RETURN)

    # Wait for the model to process (adjust timing as needed)
    time.sleep(10)

    # Get the response
    response = driver.find_element(By.CSS_SELECTOR, ".result-streaming").text
    return response


if __name__ == "__main__":
    # Get the YouTube transcript (replace with actual implementation)
    video_url = input("Please enter the YouTube video URL: ")
    transcript = get_youtube_transcript(video_url)

    if "An error occurred" not in transcript:
        # Set up the Selenium driver (make sure ChromeDriver is in your PATH)
        driver = webdriver.Chrome()

        try:
            # Log into ChatGPT
            login_to_chatgpt(driver)

            # Ask ChatGPT to summarize the transcript
            summary = ask_chatgpt_to_summarize(driver, transcript)

            # Output the summary
            print("Summarized Transcript:\n", summary)

        finally:
            # Close the browser window
            driver.quit()
    else:
        print(transcript)
