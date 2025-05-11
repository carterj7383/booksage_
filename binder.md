# BookSage Project Binder

## Table of Contents

### Section 1: Overview
1. [Executive Summary](#executive-summary)
2. [Project Description](#project-description)
3. [Team Information](#team-information)

### Section 2: Technical Documentation
4. [System Architecture](#system-architecture)
5. [Database Structure](#database-structure)
6. [Technology Stack](#technology-stack)

### Section 3: Features & Functionality
7. [Current Features](#current-features)
8. [User Interface](#user-interface)
9. [Screenshots](#screenshots)

### Section 4: Implementation Details
10. [Code Structure](#code-structure)
11. [Deployment Process](#deployment-process)
12. [Security Measures](#security-measures)

### Section 5: Project Management
13. [Development Timeline](#development-timeline)
14. [Technical Challenges](#technical-challenges)
15. [Error Handling](#error-handling)
16. [Testing Strategy](#testing-strategy)
17. [CI/CD Pipeline](#cicd-pipeline)
18. [Future Roadmap](#future-roadmap)

### Section 6: User Documentation
16. [User Guide](#user-guide)
17. [Installation Instructions](#installation-instructions)
18. [System Requirements](#system-requirements)

---

# Section 1: Overview

## Executive Summary

BookSage is a book recommendation platform designed to help readers discover their next favorite read. Built with Flask, the application provides personalized book suggestions, reading progress tracking, and a community-driven approach to book discovery.

**Key Accomplishments:**
- Developed working recommendation system
- Implemented secure user authentication
- Created responsive web interface
- Deployed automated CI/CD pipeline

**Technical Highlights:**
- Python Flask framework
- SQLite database
- REST API integration
- Cross-platform deployment

## Project Description

### Purpose
BookSage addresses the challenge of book discovery by creating a centralized platform where readers can find books that match their interests and reading preferences.

### Scope
The application includes:
- User authentication system
- Book recommendation engine
- Reading progress tracker
- Personal library management
- Community features (planned)

### Target Audience
- Book enthusiasts
- Casual readers
- Reading groups
- Library patrons

## Team Information

### Development Team
- **Alya** - Backend Engineering & Database Management
- **Laura** - Backend Engineering & Database Management
- **Josh** - DevOps & Frontend Developer & UI/UX Design 

### Project Timeline
- Start Date: March 2025
- Current Status: MVP Complete
- Next Milestone: Beta Testing

---

# Section 2: Technical Documentation

## System Architecture

### Architecture Overview
BookSage employs a three-tier architecture:

1. **Presentation Layer**
   - HTML templates with Jinja2
   - CSS styling (dark theme)
   - JavaScript interactions

2. **Application Layer**
   - Flask web framework
   - Python business logic
   - Session management

3. **Data Layer**
   - SQLite database
   - External API integration
   - File storage

### System Diagram
```
Browser → Flask App → SQLite DB
               ↓
        External APIs
```

## Database Structure

### Current Schema

```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    is_new_user BOOLEAN DEFAULT 1
);
```

### Planned Tables
- books
- reading_progress
- user_ratings
- book_categories

## Technology Stack

### Backend Components
- Python 3.9+
- Flask 2.2.3
- SQLite
- Werkzeug
- Requests

### Frontend Components
- HTML5
- CSS3
- JavaScript ES6+
- Jinja2 Templates
- Animate.css

### Development Tools
- Git/GitHub
- PyInstaller
- GitHub Actions
- VS Code

---

# Section 3: Features & Functionality

## Current Features

### User Management
- Account registration
- Secure login
- Password hashing
- Profile customization
- Reading preferences

### Book Discovery
- Personalized recommendations
- Category browsing (fiction, non-fiction, technical, etc.)
- Search functionality
- Book details page
- Cover image display

### Reading Tracking
- Current reading list
- Progress percentage
- Reading goals
- Completion tracking
- Reading statistics

### Interface Features
- Dark theme design
- Mobile responsiveness
- 3D book animations
- Smooth transitions
- Loading states

## User Interface

### Design Principles
- Clean, minimal layout
- Consistent color scheme
- Intuitive navigation
- Accessible design
- Performance optimized

### Color Scheme
- Primary: #c5db94 (Green)
- Backgrounds: #121212 (Dark)
- Cards: #222222
- Text: #e5e5e5 (Light Gray)


# Section 4: Implementation Details

## Code Structure

```
booksage_/
├── app.py              # Main application
├── models.py           # Database models
├── requirements.txt    # Dependencies
├── templates/          # HTML templates
├── static/            # CSS, JavaScript, images
├── .github/           # CI/CD workflows
└── dist/              # Production builds
```

### Key Files

#### app.py
- Flask application setup
- Route definitions
- Authentication logic
- Book cover fetching
- Session management

#### templates/
- base.html - Layout template
- mainPage.html - Home page
- browse.html - Book catalog
- dashboard.html - User dashboard
- profile.html - User settings
- login.html / register.html - Auth forms

## Deployment Process

### Development Environment
```bash
# Setup steps
git clone https://github.com/carterj7383/booksage_.git
cd booksage_
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

### Production Deployment
1. GitHub Actions builds executable
2. PyInstaller packages application
3. Releases distributed via GitHub
4. Users download and run standalone app

## Security Measures

### Authentication
- Werkzeug password hashing (not encryption)
- Flask session management
- Email uniqueness validation
- Password strength requirements

### Data Protection
- SQL injection prevention
- XSS protection via escaping
- CSRF protection
- Secure cookie handling

### Best Practices
- Input validation
- Error handling
- Secure file paths
- API rate limiting

---

# Section 5: Project Management

## Development Timeline

### Phase 1: Foundation (March 2025)
- Project planning and team formation
- Technology stack selection
- Database schema design
- Basic Flask application setup

### Phase 2: Core Features (April 2025)
- User authentication implementation
- Book data integration with external APIs
- Basic recommendation algorithm
- Frontend template development

### Phase 3: Enhancement (April-May 2025)
- UI/UX improvements and dark theme
- Mobile responsiveness
- Performance optimization
- 3D book flip animations

### Phase 4: Testing & Deployment (May 2025)
- CI/CD pipeline setup
- Cross-platform executable creation
- Documentation completion
- User testing and feedback

## Technical Challenges

### Challenge 1: API Integration
**Problem:** Integrating with multiple book APIs (Open Library, Google Books) with different response formats and reliability.

**Solution:** 
- Implemented fallback mechanism (try Open Library first, then Google Books)
- Added caching to reduce API calls
- Created abstraction layer to normalize responses

### Challenge 2: Book Cover Reliability
**Problem:** External API cover images not always available or consistent.

**Solution:**
- Added default cover image fallback
- Implemented intelligent cover fetching based on ISBN/title/author
- Used SVG placeholder for missing covers

### Challenge 3: Database Performance
**Problem:** SQLite limitations for concurrent users and query performance.

**Solution:**
- Optimized queries with proper indexing
- Limited to appropriate use case (small-medium scale)
- Planned migration path to PostgreSQL for scaling

### Challenge 4: Cross-platform Deployment
**Problem:** Creating executable that works on Windows, Mac, and Linux.

**Solution:**
- Used PyInstaller with specific configurations
- Handled resource paths properly for packaged app
- Separated development and production configurations

## Error Handling

### Input Validation
```python
# Form validation
if not email or not password:
    flash('All fields are required')
    return redirect(url_for('login'))

# Email format checking
if '@' not in email:
    flash('Invalid email format')
```

### API Error Handling
```python
try:
    response = requests.get(api_url, timeout=5)
    if response.status_code != 200:
        return url_for('static', filename='images/default-book-cover.svg')
except Exception as e:
    print(f"API error: {e}")
    return default_cover_url
```

### Database Error Management
```python
try:
    conn = get_db_connection()
    # database operations
except sqlite3.Error as e:
    print(f"Database error: {e}")
    flash('Database connection error')
    return redirect(url_for('index'))
finally:
    conn.close()
```

### Session Management
```python
# Login requirement check
if 'user_id' not in session:
    return redirect(url_for('login'))

# Invalid session handling
try:
    user = get_user_by_id(session['user_id'])
except:
    session.clear()
    return redirect(url_for('login'))
```

## Testing Strategy

### Manual Testing
**User Flow Testing:**
- Registration → Login → Browse → Add to List → Track Progress
- Edge cases: invalid inputs, missing data, API failures
- Cross-browser testing (Chrome, Firefox, Safari)
- Mobile responsiveness testing

### Component Testing
**Template Rendering:**
- Verify all pages load correctly
- Check dynamic content population
- Test conditional logic (logged in/out states)

**Database Operations:**
- User creation and authentication
- Data persistence across sessions
- Query performance with sample data

### Integration Testing
**API Integration:**
- Mock API responses for reliable testing
- Test fallback mechanisms
- Verify error handling with timeout scenarios

**Authentication Flow:**
- User registration validation
- Password hashing verification
- Session management testing

### Future Testing Improvements
- Implement unit tests with pytest
- Add automated UI testing with Selenium
- Set up continuous testing in CI pipeline
- Create test database for isolated testing

## CI/CD Pipeline

### GitHub Actions Workflow

```yaml
jobs:
  validate:
    - Lint Python code
    - Validate HTML templates
    - Check JavaScript syntax
  
  build:
    - Install dependencies
    - Create executable
    - Run tests
  
  deploy:
    - Generate release
    - Upload artifacts
    - Update documentation
```

### Pipeline Features
- Automated testing
- Cross-platform builds
- Version management
- Release automation

## Future Roadmap

### Short-term Goals
- Complete user rating system
- Implement email notifications
- Add social features
- Enhance recommendations

### Medium-term Goals
- Mobile application
- API for integrations
- Advanced analytics
- Community features

### Long-term Vision
- Machine learning integration
- Academic database connections
- Enterprise features
- Open source community

---

# Section 6: User Documentation

## User Guide

### Getting Started

#### 1. Create Account
1. Go to BookSage website
2. Click "Register"
3. Enter details
4. Verify email
5. Set preferences

#### 2. Find Books
1. Browse recommendations
2. Use search bar
3. Filter by category
4. Read descriptions
5. Add to reading list

#### 3. Track Reading
1. Mark as "Reading"
2. Update progress
3. Rate completed books
4. View statistics
5. Set reading goals

## Installation Instructions

### For Regular Users
1. Visit GitHub releases page
2. Download latest version
3. Extract ZIP file
4. Run BookSage executable
5. Create account

### For Developers
```bash
# Clone repository
git clone https://github.com/carterj7383/booksage_.git

# Install dependencies
pip install -r requirements.txt

# Initialize database
python models.py

# Run application
python app.py
```

## System Requirements

### Minimum Requirements
- Operating System: Windows 10, macOS 10.15+, Linux
- RAM: 4GB
- Storage: 100MB
- Internet: Broadband connection
- Browser: Chrome 90+, Firefox 88+, Safari 14+

### Recommended Specifications
- RAM: 8GB
- SSD storage
- Modern processor
- High-speed internet

---

## Project Metadata

**Repository:** https://github.com/carterj7383/booksage_  
**Version:** 1.0.0  
**License:** MIT  
**Last Updated:** May 2025  

© 2025 BookSage Project. All rights reserved.