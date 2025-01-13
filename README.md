# YouTube Video Summarizer

This project automatically summarizes YouTube videos using a combination of Python (Flask backend) and a Chrome extension. When you open a YouTube video, the extension fetches the transcript, sends it to the backend for summarization, and displays the summary in a popup.

---
![image](https://github.com/user-attachments/assets/b4306305-ebbd-4ce9-99b3-72381b6a6e8b)


## Features

- **Automatic Summarization**: Summarizes YouTube videos as soon as you open them.
- **Stylish Popup**: The summary is displayed in a clean, styled popup.
- **Non-Blocking**: The popup does not block interaction with the YouTube page.
- **Close Button**: Easily close the popup when done.

---

## Prerequisites

Before you begin, ensure you have the following installed:

1. **Python 3.8+**: [Download Python](https://www.python.org/downloads/)
2. **Google API Key**: Required for the Gemini model. [Get a Google API Key](https://developers.google.com/workspace/guides/create-credentials)
3. **Google Chrome**: The extension works on Chrome.

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/youtube-summarizer.git
cd youtube-summarizer
```

### 2. Set Up the Python Backend

1. Install the required Python libraries:

   ```bash
   pip install -r requirements.txt
   ```

2. Create a `.env` file in the `server/` directory and add your Google API key:

   ```plaintext
   GOOGLE_API_KEY=your_google_api_key_here
   ```

3. Start the Flask server:

   ```bash
   cd server
   python app.py
   ```

   The server will run at `http://localhost:5000`.

### 3. Load the Chrome Extension

1. Open Chrome and go to `chrome://extensions/`.
2. Enable **Developer Mode** (toggle in the top-right corner).
3. Click **Load unpacked** and select the `extension/` folder from this repository.

---

## Usage

1. Open a YouTube video in Chrome.
2. Click the extension.
3. The extension will fetch the transcript, summarize it, and display the summary in a popup
   
---

## Project Structure

```
youtube-summarizer/
├── extension/               # Chrome extension files
│   ├── manifest.json        # Extension manifest
│   ├── background.js        # Background script
│   ├── popup.js             # Popup JavaScript (formerly content.js)
│   ├── popup.css            # Popup CSS for styling
│   ├── popup.html           # Popup HTML
│   └── images/              # Extension icons
│       ├── icon16.png
│       ├── icon48.png
│       └── icon128.png
├── server/                  # Flask backend
│   ├── app.py               # Flask application
│   ├── summarize_youtube.py # Summarization logic
│   ├── .env                 # Environment variables
│   └── requirements.txt     # Python dependencies
├── .gitignore               # Git ignore file
└── README.md                # This file
```

---

## How It Works

1. **Popup Script (`popup.js`)**:
   - Automatically runs when a YouTube video page is loaded.
   - Sends the video URL to the background script.

2. **Background Script (`background.js`)**:
   - Sends the video URL to the Flask backend for summarization.
   - Receives the summary and sends it back to the popup script.

3. **Flask Backend**:
   - Fetches the transcript using `youtube-transcript-api`.
   - Summarizes the transcript using the Gemini model.
   - Returns the summary to the extension.

4. **Popup**:
   - Displays the summary in a styled popup.
---

## Customizing the Popup

The popup's appearance is controlled by `popup.css`. You can customize the styles by editing this file. For example:

```css
/* Example: Change the background color of the popup */
#custom-popup {
  background-color: #f9f9f9;
}
```

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- [LangChain](https://langchain.com/) for the summarization chain.
- [YouTube Transcript API](https://pypi.org/project/youtube-transcript-api/) for fetching transcripts.
- [Flask](https://flask.palletsprojects.com/) for the backend server.

---

Enjoy summarizing YouTube videos effortlessly! 🚀

---
