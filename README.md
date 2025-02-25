# Tea Website

A web platform dedicated to showcasing traditional Chinese tea, its history, tea gardens, and the cultural significance of tea. This platform is designed to educate users about different types of tea, the tea-making process, and the history behind tea cultivation in China. The website also offers a community feature for users to interact.

## Features

- **Tea Categories**: Learn about different types of tea, their descriptions, and images.
- **Tea Gardens**: Explore tea gardens, their locations, and rich histories.
- **Tea History**: A detailed view of the history of Chinese tea and its cultural importance.
- **Theme Toggle**: A dynamic day/night mode for the user interface.
- **Comment Section**: Users can comment on tea-related content (tea gardens, history, etc.).

## Technologies Used

- **Django**: Backend framework used for server-side logic and database management.
- **Bootstrap**: Frontend framework for responsive design.
- **SQLite**: Database used for storing tea data (gardens, categories, history).
  
## Installation

### Prerequisites

Make sure you have the following installed:
- Python 3.11 or higher
- pip (Python package installer)
- Git (for version control)

### Setup Instructions

1. **Clone the repository**:
    ```bash
    git clone git@github.com:YourGitHubUsername/Tea-Website.git
    cd Tea-Website
    ```

2. **Create a virtual environment**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On MacOS/Linux
    venv\Scripts\activate     # On Windows
    ```

3. **Install required dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run migrations** to set up the database:
    ```bash
    python manage.py migrate
    ```

5. **Create a superuser** to access the Django admin panel:
    ```bash
    python manage.py createsuperuser
    ```

6. **Run the development server**:
    ```bash
    python manage.py runserver
    ```

7. Open your browser and go to `http://127.0.0.1:8000` to view the site.

### Admin Panel
- To access the admin panel, go to `http://127.0.0.1:8000/admin/`.
- Use the **superuser credentials** you created in step 5 to log in and manage content (Tea Categories, Tea Gardens, Tea History, etc.).

## Features & Usage

- **Tea Category Page**: Displays various types of tea, each with a description and image.
- **Tea Garden Page**: Learn about various tea gardens in China, their locations, history, and image.
- **Tea History Page**: A page dedicated to explaining the rich history of Chinese tea.
- **User Interaction**: Allows users to log in and post comments on tea-related content.
- **Dynamic Theme**: Users can toggle between a day and night theme.
- **Font Size Adjustment**: Available on the **Tea History** page for a better reading experience.
