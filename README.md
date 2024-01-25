# Django Weather App

This project is a simple weather application built with Django, a high-level Python web framework. It allows users to get real-time weather information for different locations.

## Getting Started

These instructions will help you set up a copy of the Weather App project on your local machine for development and testing purposes.

### Prerequisites

Before you begin, ensure you have the following installed:

- Python (3.11.6 or latest)
- Django (5.0.1 or latest)
- pip (Python package manager)
- Virtualenv (optional, but recommended for Python package management)

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/vishnukkrishna/Weather-App-Python-Django.git
   cd Weather-App-Python-Django
   ```

2. **Set Up a Virtual Environment (Optional)**

   It's recommended to use a virtual environment to manage dependencies.

   ```bash
   virtualenv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**

   Create a `.env` file in the project root and add the necessary environment variables, such as API keys for the weather service.

   ```
   WEATHER_API_KEY='your_api_key_here'
   ```

5. **Run Database Migrations**

   ```bash
   python manage.py migrate
   ```

6. **Start the Development Server**

   ```bash
   python manage.py runserver
   ```

   After running this command, the app should be available at `http://127.0.0.1:8000/`.

## Running Tests

To run the automated tests for this system:

```bash
python manage.py test
```
