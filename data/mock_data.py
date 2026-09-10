USER_PROFILE = {
    "name": "Sandya",
    "email": "alex.morgan@example.com",
    "avatar": "https://api.dicebear.com/7.x/avataaars/svg?seed=Alex",
    "plan": "Pro",
    "joined": "September 2026"
}

SUGGESTED_PROMPTS = [
    {"title": "Plan my day", "desc": "Create a structured timetable for peak focus", "icon": "📅"},
    {"title": "Explain complex topic", "desc": "Break down Quantum Computing in simple terms", "icon": "🧠"},
    {"title": "Draft an email", "desc": "Write a professional project update to stakeholders", "icon": "✉️"},
    {"title": "Learn Python UI", "desc": "Teach me Streamlit session state architecture", "icon": "🐍"}
]

FEATURE_CARDS = [
    {
        "title": "Contextual Intelligence",
        "description": "Remembers preferences and conversation nuance across all workspace sessions."
    },
    {
        "title": "Privacy First Design",
        "description": "Your conversation logic and data controls stay strictly isolated and user-managed."
    },
    {
        "title": "Adaptive Workflows",
        "description": "Instantly switch between creative brainstorming, coding, and analysis tasks."
    }
]

MOCK_CONVERSATION_HISTORY = {
    "Today": [
        {"id": "c1", "title": "Streamlit Layout Optimization", "time": "10:42 AM", "favorite": True},
        {"id": "c2", "title": "Weekly Planning & Goals", "time": "08:15 AM", "favorite": False}
    ],
    "Yesterday": [
        {"id": "c3", "title": "Python Async Execution Notes", "time": "Yesterday", "favorite": False},
        {"id": "c4", "title": "System Architecture Draft", "time": "Yesterday", "favorite": True}
    ],
    "Previous 7 Days": [
        {"id": "c5", "title": "CSS Glassmorphism Palette", "time": "3 days ago", "favorite": False},
        {"id": "c6", "title": "API Gateway Design Pattern", "time": "5 days ago", "favorite": False}
    ],
    "Older": [
        {"id": "c7", "title": "Initial Setup Specifications", "time": "Jan 12, 2026", "favorite": False}
    ]
}

INITIAL_CHAT_MESSAGES = [
    {
        "role": "assistant",
        "content": "Hello Alex! I am your personal AI companion. How can I assist you with your projects today?",
        "timestamp": "10:42 AM"
    }
]