# 📰 Webpage Summarizer using OpenAI GPT

This Python script summarizes the main content of any public website using OpenAI's GPT model. It removes unnecessary page elements like navigation, images, scripts, and styles, and returns a clean, short markdown-formatted summary.

## 🚀 Features

* Fetches and parses a webpage using `requests` and `BeautifulSoup`
* Cleans and extracts the main text content
* Uses OpenAI's GPT model (`gpt-4o-mini`) to generate a concise summary
* Outputs the summary in markdown format
* Ignores navigation, ads, and irrelevant content

## 🛠️ Requirements

* Python 3.7+
* OpenAI API Key

## 📆 Installation

1. Clone the repository:

   ```bash
   git clone git@github.com:hariscoder3/webpage_summarizer.git
   cd webpage_summarizer
   ```

2. Create a virtual environment and activate it (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file and add your OpenAI API key:

   ```
   OPENAI_API_KEY=your_openai_api_key
   ```

## 📄 Usage

Update the target URL inside the `main()` function or modify the script to accept a URL from the command line:

```python
url = "https://linkedin.com"
```

Run the script:

```bash
python your_script_name.py
```

The summary will be printed in markdown format in the console.

## 📚 Example Output

```
## LinkedIn Summary

LinkedIn is a professional networking platform that connects employers and job seekers. Users can view job listings, connect with others in their industry, and publish content.
```

## 🧪 Dependencies

* `requests`
* `beautifulsoup4`
* `openai`
* `python-dotenv`

Install manually if needed:

```bash
pip install requests beautifulsoup4 openai python-dotenv
```

## 📂 Project Structure

```
webpage-summarizer/
├── webpage_summarizer.py     # Main script
├── requirements.txt          # Python dependencies
└── .env                      # Environment variables (not committed)
```

## 🛡️ License

This project is open-source and available under the MIT License.

