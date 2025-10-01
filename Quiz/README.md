# Pop Quiz Application

A static quiz application perfect for GitHub Pages hosting.

## Features

- Static file-based quiz system
- Easy to add new quizzes
- Works with GitHub Pages
- Simple, clean interface

## Setup

1. Simply open `index.html` in your browser or deploy to GitHub Pages
2. No server setup required!

## Adding New Quizzes

1. Create a new quiz file (e.g., `quiz3.json`) following the format below
2. Add an entry to `quizzes.json` with the quiz name and filename:

```json
[
  {
    "name": "General Knowledge",
    "file": "quiz1.json"
  },
  {
    "name": "Science Trivia", 
    "file": "quiz2.json",
    "url": "https://www.youtube.com/watch?v=example",
    "sourceUrl": "https://github.com/username/repo/blob/main/path/to/source.md"
  },
  {
    "name": "Your New Quiz",
    "file": "quiz3.json"
  }
]
```

Note: `url` and `sourceUrl` fields are optional and can be used to link to source material.

## Quiz File Format

Each quiz file should be a JSON array of question objects:

```json
[
  {
    "question": "Your question here?",
    "options": ["Option 1", "Option 2", "Option 3", "Option 4"],
    "answer": "Correct Answer"
  }
]
```

## GitHub Pages Deployment

1. Push your files to a GitHub repository
2. Enable GitHub Pages in repository settings
3. Your quiz will be available at `https://yourusername.github.io/repository-name`
