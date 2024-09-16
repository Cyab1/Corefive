# Corefive Django Project

This is a Django-based web application for [Corefive], band management system.

## Prerequisites

- Python 3.x
- Docker (optional, for containerized deployment)

## Usage Examples

### Managing Bands

1. Create a new band:
   - Navigate to the "Bands" section
   - Click on "Add New Band"
   - Fill in the band details (name, genre, formation date)
   - Click "Save"

2. View band details:
   - Go to the "Bands" list
   - Click on a band name to view its full profile

3. Update band information:
   - From the band's profile page
   - Click "Edit"
   - Update the necessary fields
   - Click "Save Changes"

### User Authentication

1. Register a new user:
   - Click on "Sign Up" in the navigation bar
   - Fill in the required information (username, email, password)
   - Click "Register"

2. Log in:
   - Click "Log In" in the navigation bar
   - Enter your username and password
   - Click "Login"

3. Reset password:
   - On the login page, click "Forgot Password?"
   - Enter your email address
   - Follow the instructions sent to your email

### API Usage (if applicable)

To retrieve a list of all bands:
GET /api/bands/

 
To get details of a specific band:
GET /api/bands/{band_id}/


To create a new band via API:
POST /api/bands/
{
"name": "The Rockers",
"genre": "Rock",
"formation_date": "2023-01-15"
}

## Setup and Installation

### Using venv

1. Clone the repository:```
   git clone https://github.com/Cyab1/Corefive.git
   cd Corefive

## Create a virtual environment:
   python -m venv venv

## Activate the virtual environment:
On Windows:
 venv\Scripts\activate

On macOS and Linux:
 source venv/bin/activate

## Install the required packages:
pip install -r requirements.txt

## Apply database migrations:
python manage.py migrate

## Run the development server:
Access the application at http://localhost:8000

## Using Docker
Build the Docker image:
docker build -t corefive .

Run the Docker container:
docker run -p 8000:8000 corefive
Access the application at http://localhost:8000
