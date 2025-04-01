# Chatbot

A modern web-based chatbot application with a Python FastAPI backend and JavaScript frontend. Features a clean, responsive UI with real-time AI responses and multilingual support.

## Features

### User Interface
- 🎨 Modern, clean design with smooth animations
- 🌓 Dark/light theme toggle with persistent preferences
- 📱 Fully responsive design for mobile and desktop
- ⚡ Real-time connection status indicator
- 💬 Message history with localStorage persistence
- 🗑️ Clear chat history functionality
- ⌨️ Enter key support for sending messages
- 🌐 Multi-language support with 12 languages:
  - English
  - Spanish (Español)
  - French (Français)
  - German (Deutsch)
  - Italian (Italiano)
  - Portuguese (Português)
  - Russian (Русский)
  - Chinese (中文)
  - Japanese (日本語)
  - Korean (한국어)
  - Arabic (العربية)
  - Hindi (हिन्दी)
- 🎤 Voice input with language-specific recognition
- 📎 File attachments:
  - Image upload with preview
  - Document upload support
  - File size display
- 📍 Location sharing with coordinates
- 💭 Message bubbles with distinct styling:
  - User messages in blue
  - Bot messages in light gray
  - Proper spacing and alignment
  - Rounded corners
- 🎯 Bottom toolbar with:
  - Microphone button for voice input
  - Attachment button for files
  - Send button with animations
- 🎨 Theme features:
  - Light/Dark mode toggle
  - High contrast colors
  - Persistent theme preference
  - Smooth theme transitions
- 🔄 Status indicators:
  - Connection status
  - Voice recording status
  - Upload progress
  - Language selection status
  
  ![Screenshot 2025-04-01 041931](https://github.com/user-attachments/assets/7af0d8d4-0206-48c4-9f18-d6147e326aa1)
  ![Screenshot 2025-04-01 041940](https://github.com/user-attachments/assets/dbd9ee68-106b-491a-a947-a6280f1b1afb)
  ![Screenshot 2025-04-01 042000](https://github.com/user-attachments/assets/8f308c07-047e-4022-9ff6-9e1d74da01b0)




### Backend Capabilities
- 🤖 OpenAI GPT-3.5-turbo integration
- ⚡ FastAPI for high-performance backend
- 🔒 Rate limiting (60 requests per minute)
- 📊 Usage tracking and statistics
  - Total requests and tokens used
  - Per-IP request tracking
  - Daily usage statistics
- 🛡️ CORS support for security
- 💾 Automatic usage logs persistence

### Error Handling
- 🔄 Automatic reconnection attempts
- 🚦 Visual connection status updates
- ⚠️ Clear error messages for API issues
- 🛑 Rate limit warnings
- 🔑 API key validation

## Prerequisites

- Python 3.13 or higher
- OpenAI API key
- Modern web browser

## Installation

1. Clone this repository
2. Configure the OpenAI API key:
```bash
# In backend/.env
OPENAI_API_KEY=your-api-key-here
```

## Running the Application

1. Double-click `run_chatbot.bat`
2. The backend server will start automatically on http://localhost:8000
3. Your default browser will open with the chatbot interface
4. Wait for the "Connected" status indicator

## Project Structure

```
project/
├── .github/                    # GitHub configuration
├── backend/
│   ├── app/
│   │   ├── __pycache__/
│   │   ├── auth.py            # Authentication handling
│   │   ├── database.py        # Database configuration
│   │   ├── db_service.py      # Database service layer
│   │   ├── firebase_config.py # Firebase configuration
│   │   ├── llm.py            # LLM integration logic
│   │   ├── logger.py         # Logging configuration
│   │   ├── main.py           # FastAPI server with OpenAI integration
│   │   ├── models.py         # Data models
│   │   └── security.py       # Security utilities
│   ├── tests/                 # Backend tests
│   ├── .env                   # Environment variables
│   ├── requirements.txt       # Python dependencies
│   └── run.py                 # Backend startup script
├── docs/                      # Documentation files
├── frontend/
│   ├── src/
│   │   ├── components/        # React components
│   │   ├── store/            # State management
│   │   ├── types/            # TypeScript types
│   │   ├── App.tsx           # Main React component
│   │   ├── embed.tsx         # Embedding configuration
│   │   └── index.css         # Global styles
│   ├── chatbot.html          # Standalone chat interface
│   ├── index.html            # Main application entry
│   ├── package.json          # Node.js dependencies
│   ├── server.py             # Development server
│   ├── tailwind.config.js    # Tailwind CSS configuration
│   └── vite.config.ts        # Vite configuration
├── .gitignore                # Git ignore rules
├── README.md                 # Project documentation
└── run_chatbot.bat           # Windows startup script
```

## API Endpoints

- `GET /` - Health check endpoint
- `GET /stats` - Usage statistics
- `POST /chat` - Chat endpoint for message processing

## Usage Statistics

The application tracks:
- Total number of requests
- Total tokens used
- Requests per IP address
- Daily usage statistics

## Rate Limiting

- 60 requests per minute per IP
- Visual feedback when limit is reached
- Automatic tracking and enforcement

## Browser Support

- Chrome/Edge (recommended for full speech recognition support)
- Firefox
- Safari
- Any modern browser with JavaScript enabled
- Note: Voice input works best in Chrome and Edge

## Security Features

- CORS protection
- Rate limiting
- No API key exposure to frontend
- Input sanitization

## Future Improvements

- [ ] Message streaming for faster responses
- [ ] Multiple LLM provider support
- [ ] User authentication
- [ ] Conversation context memory
- [ ] Export chat history
- [ ] Custom chatbot personality settings
- [ ] Enhanced file preview support
- [ ] Improved accessibility features
- [ ] Additional language support
- [ ] Voice output for messages
- [ ] Rich text formatting
- [ ] Custom theme creation
- [ ] Message search functionality
- [ ] Chat organization features

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Author
Developed by Jeremy Martinez-Quinones.
