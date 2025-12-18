# SafeShort – Secure Backend URL Management Service

SafeShort is an API-first backend service for creating, managing, and tracking shortened URLs.
The project focuses on clean REST API design, backend lifecycle management, and secure input
handling without relying on frontend templates.

This project is intended to demonstrate backend engineering fundamentals such as API development,
database integration, validation, and usage analytics.

## Features

- REST APIs for creating short URLs
- URL redirection with lifecycle and expiry checks
- Click tracking and access analytics
- Active and inactive URL state management
- Secure input validation and error handling

## Tech Stack

- Python
- Flask
- SQLite
- SQLAlchemy

## API Endpoints

### Create Short URL

**POST** '/api/shorten'

Request Body:
json
{
  "url": "https://example.com",
  "expiry_days": 7
}


Response:
json
{
  "short_code": "AbC123"
}


### Redirect to Original URL

**GET** '/api/<short_code>'

Redirects to the original URL if the short link is active and not expired.

### View URL Analytics

**GET** '/api/stats/<short_code>'

Response:
json
{
  "original_url": "https://example.com",
  "click_count": 3,
  "created_at": "2025-09-18T10:12:44",
  "last_accessed_at": "2025-09-18T11:02:10",
  "is_active": true
}


## How to Run Locally

1. Clone the repository
2. Create and activate a virtual environment
3. Install dependencies:
   'bash'
   pip install -r requirements.txt
   
4. Run the application:
   'bash'
   python app.py
   

The API will be available at:

http://127.0.0.1:5000


## Project Design Notes

- The project is designed as an API-first backend service.
- Frontend templates are intentionally excluded to focus on backend logic.
- Clear separation of routing, business logic, and data models is maintained.
- Emphasis is placed on correctness, validation, and maintainable backend code.

## License

This project is created for learning and demonstration purposes.
