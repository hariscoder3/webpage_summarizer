import requests
import os 
from openai import OpenAI
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

class Website:
    def __init__(self, url):
        self.url = url
        headers = {
             "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
        }

        response = requests.get(url,headers)
        soup = BeautifulSoup(response.content, "html.parser")
        self.title = soup.title.string if soup.title else "no title found"
        self.text = soup.body.get_text(separator="/n",strip=True)

    def create_messages(self):
        system_prompt="""You are an assistant that analyzes the contents of a website
        and provides a short summary, ignoring text that might be navigation related.
        Respond in markdown."""

        user_prompt="""\nThe contents of this website is as follows; \
        please provide a short summary of this website in markdown. \
        If it includes news or announcements, then summarize these too.\n"""
    
        user_prompt += self.text

        return [
            {"role":"system","content":system_prompt},
            {"role":"user","content":user_prompt}
        ]
    
def main():
    url = "https://linkedin.com"
    data = Website(url)
    messages = data.create_messages()

    openai = OpenAI()

    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        temperature=0.7,
        max_tokens=100
    )
    print(response.choices[0].message.content)

if __name__=="__main__":
    main()