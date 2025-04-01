# 📚 BookSage

<div align="center">
  
<button id="theme-toggle" style="background: #222222; color: #b5e25a; border: none; padding: 8px 16px; border-radius: 4px; cursor: pointer; margin-bottom: 20px; font-weight: bold;">Toggle Dark Mode 🌓</button>

BookSage is a comprehensive platform that provides personalized book recommendations based on users' preferred genres, popular content, and highly rated titles by fellow readers. 

Discover your next favorite book with our intelligent recommendation system!

![Python](https://img.shields.io/badge/Python-3.9+-blue)
![Flask](https://img.shields.io/badge/Flask-2.0+-lightgrey)
![Status](https://img.shields.io/badge/Status-In%20Development-yellow)

</div>

<style>
  :root {
    --bg-color: #ffffff;
    --text-color: #24292e;
    --heading-color: #1b1f23;
    --secondary-color: #b5e25a;
    --accent-color: #9cd43a;
    --link-color: #76a82e;
    --border-color: #e1e4e8;
    --code-bg: #f6f8fa;
    --code-text: #032f62;
    --blockquote-color: #6a737d;
    --feature-bg: #F3F4F6;
    --tag-bg: #f0fadc;
    --tag-text: #5a8622;
    --shadow-color: rgba(0, 0, 0, 0.1);
  }
  
  body.dark-mode {
    --bg-color: #222222;
    --text-color: #e6e6e6;
    --heading-color: #ffffff;
    --secondary-color: #b5e25a;
    --accent-color: #9cd43a;
    --link-color: #c8ff7d;
    --border-color: #444444;
    --code-bg: #333333;
    --code-text: #d1f7a0;
    --blockquote-color: #a0a0a0;
    --feature-bg: #2c2c2c;
    --tag-bg: #4d5d2e;
    --tag-text: #d1f7a0;
    --shadow-color: rgba(0, 0, 0, 0.3);
  }
  
  body {
    background-color: var(--bg-color);
    color: var(--text-color);
    transition: all 0.3s ease;
  }
  
  h1, h2, h3, h4, h5, h6 {
    color: var(--heading-color);
  }
  
  a {
    color: var(--link-color);
    text-decoration: none;
  }
  
  a:hover {
    text-decoration: underline;
  }
  
  code {
    background-color: var(--code-bg);
    color: var(--code-text);
    padding: 0.2em 0.4em;
    border-radius: 3px;
  }
  
  pre {
    background-color: var(--code-bg);
    border: 1px solid var(--border-color);
    border-radius: 6px;
    padding: 16px;
  }
  
  blockquote {
    color: var(--blockquote-color);
    border-left: 4px solid var(--border-color);
    padding: 0 16px;
  }
  
  hr {
    background-color: var(--border-color);
    border: none;
    height: 1px;
  }
  
  table {
    border-collapse: collapse;
    width: 100%;
    margin: 16px 0;
    border: 1px solid var(--border-color);
  }
  
  th, td {
    padding: 8px 12px;
    border: 1px solid var(--border-color);
  }
  
  th {
    background-color: var(--feature-bg);
  }
  
  img {
    max-width: 100%;
  }
  
  ul li strong {
    color: var(--secondary-color);
  }
  
  .badge {
    display: inline-block;
    padding: 4px 8px;
    background-color: var(--tag-bg);
    color: var(--tag-text);
    border-radius: 4px;
    font-size: 0.8em;
    margin-right: 8px;
  }
</style>

## ✨ Features

### Current Features
- **🔮 Personalized Recommendations** 
  - Home page with tailored suggestions based on user preferences
  - Smart algorithm that learns from your reading habits

- **📖 Book Search & Details** 
  - Search for books by title, author, or genre
  - Detailed book pages with comprehensive information
  - View book details including synopsis, author info, and community ratings

- **👤 User Accounts** 
  - Secure user registration and authentication
  - Personalized user profiles with reading history
  - Email verification for account security

- **⭐ Ratings & Reviews** 
  - Rate books on a five-star scale
  - Write and share detailed reviews
  - Discover highly-rated books from the community

### Coming Soon
- **📊 Trending Content** - Discover the most liked books within the community
- **💬 Social Features** - Follow other readers and share recommendations
- **📱 Mobile Application** - Access BookSage on the go with our mobile app
- **✉️ Email Notifications** - Stay updated with personalized book recommendations

## 🛠️ Technologies Used

### Frontend
- HTML5, CSS3 with Tailwind CSS
- JavaScript
- Jinja2 Templates

### Backend
- Python
- Flask Web Framework
- SQLite Database
- Werkzeug Security for Authentication

### Deployment
- GitHub Actions CI/CD Pipeline
- Hosting (TBD)

## 🚀 Getting Started

### Prerequisites
- Python 3.9 or higher
- Pip package manager

### Download

[![Download](https://img.shields.io/badge/Download-Latest%20Release-blue?style=for-the-badge)](https://github.com/carterj7383/booksage_/releases/latest/download/booksage-app.zip)

## 📋 Usage

1. Visit the BookSage website
2. Create an account or log in with your credentials
3. Select your preferred genres to personalize your experience
4. Browse and discover personalized book recommendations
5. Rate books and write reviews to improve future recommendations
6. Click on a book to view details and community feedback

<script>
  const savedTheme = localStorage.getItem('theme') || 'light';
  
  if (savedTheme === 'dark') {
    document.body.classList.add('dark-mode');
  }
  
  document.addEventListener('DOMContentLoaded', () => {
    const themeToggle = document.getElementById('theme-toggle');
    
    themeToggle.addEventListener('click', () => {
      document.body.classList.toggle('dark-mode');
      
      const isDarkMode = document.body.classList.contains('dark-mode');
      localStorage.setItem('theme', isDarkMode ? 'dark' : 'light');
      
      themeToggle.textContent = isDarkMode ? 'Switch to Light Mode 🌞' : 'Switch to Dark Mode 🌓';
    });
    
    if (document.body.classList.contains('dark-mode')) {
      themeToggle.textContent = 'Switch to Light Mode 🌞';
    }
  });
</script>