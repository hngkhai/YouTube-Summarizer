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
