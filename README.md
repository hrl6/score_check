# Simple Score API

A simple Django REST API that calculates and logs user scores with PostgreSQL database integration.

## Features

- Simple score calculation endpoint (input + 1)
- PostgreSQL database for data persistence
- User score logging with timestamps

## Prerequisites

- Python 3.8+
- PostgreSQL
- pip

## Installation

1. Clone the repository

```bash
git clone https://github.com/hrl6/score_check.git
cd score-check
```

2. Create and activate virtual environment

```bash
python -m venv venv
source venv/bin/activate
# On Windows use: venv\Scripts\activate
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Configure PostgreSQL database settings in settings.py:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'score_db',
        'USER': 'your_username', # change to your username
        'PASSWORD': 'your_password', # change to your password
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

5. Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

## Testing

1. Run test:
```bash
python manage.py test
```

## Usage

1. Start the server:

```bash
python manage.py runserver
```

2. Make POST request to API endpoint:

```powershell
$body = @{
    user_id = "test_user"
    input_value = 5.0
} | ConvertTo-Json

Invoke-WebRequest -Uri "http://localhost:8000/get_score/" `
    -Method Post `
    -ContentType "application/json" `
    -Body $body
```