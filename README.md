# Seek Sphere

## Overview
**Seek Sphere** is a **Mini Search Engine** built using **Django**, designed to allow users to efficiently search through **Wikipedia's technology-related articles**. The application leverages **Redis** for storing the search index and is deployed on **Heroku** for easy accessibility.

---

[**Live Demo**](https://seek-sphere-37a11b29c017.herokuapp.com/)  
Check out the live version of the application!

---

## Features
- **Fast Search Capabilities**: Users can quickly search through pre-indexed technology-related Wikipedia articles.
- **Efficient Indexing**: Articles are already **indexed, tokenized, and processed** for optimal search performance.
- **Redis-powered Indexing**: The search index is stored in **Redis**, ensuring fast query responses.
- **User-friendly Interface**: Simple and intuitive UI for seamless search experience.
- **Scalable Deployment**: Hosted on **Heroku**, allowing for easy scalability and availability.

## Tech Stack
- **Backend**: Django (Python)
- **Search Indexing**: Redis
- **Deployment**: Heroku

## Setup & Installation
### Prerequisites
Ensure you have the following installed:
- Python (>= 3.8)
- Redis

### Installation Steps
1. Clone the repository:
   ```sh
   git clone https://github.com/DharamveerSinghGrewal/SeekSphere.git
   cd SeekSphere
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Set up Redis:
   ```sh
   redis-server
   ```
6. Start the development server:
   ```sh
   python manage.py runserver
   ```
7. Access the application at `http://127.0.0.1:8000/`

## Usage
1. Enter a search query related to technology.
2. Browse through the retrieved Wikipedia articles.
3. Click on an article for further reading.

## Future Enhancements
- Implement **autocomplete suggestions** for better user experience.
- Improve **ranking algorithms** for more accurate search results.
- Introduce **caching mechanisms** for enhanced performance.

---
### Made with ❤️ using Django & Redis

