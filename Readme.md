# ChatBot using Django and OpenAI's API

This project is a chatbot built with Django and OpenAI's API. The chatbot is capable of interacting with users, providing responses based on the OpenAI GPT model.

## Features

- Interactive chat interface
- Uses OpenAI's API for generating responses
- Built with Django framework
- Simple and easy to use

## Prerequisites

Before you begin, ensure you have the following installed on your system:

- Python 3.6+
- Django 3.0+
- An OpenAI API key

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/pavan98765/ChatBot.git
   cd ChatBot/django_chatbot
   ```

2. **Install Django:**

   ```bash
   pip install django
   ```

3. **Add your OpenAI API key:**
   Open [views.py](./django_chatbot/chatbot/views.py) in the chat app and add your OpenAI API key:

   ```bash
   OPENAI_API_KEY = 'your_openai_api_key_here'
   ```

4. **Run database migrations:**

   ```bash
   python manage.py migrate
   ```

5. **Start the development server:**

   ```bash
   python manage.py runserver
   ```

   The application will be available at `http://127.0.0.1:8000`.

## Usage

- Open your web browser and navigate to `http://127.0.0.1:8000`.
- You will see a chat interface where you can start interacting with the chatbot.
- Type your messages and receive responses powered by OpenAI's API.

## Project Structure

- `chatbot/`: Contains the main Django project settings and configuration.
- `chat/`: Contains the Django app for the chatbot functionality.
- `templates/`: HTML templates for the chat interface.
- `static/`: Static files (CSS, JavaScript) for the project.
- `requirements.txt`: List of Python dependencies.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request if you have any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgements

- [Django](https://www.djangoproject.com/) - The web framework used
- [OpenAI](https://www.openai.com/) - For providing the API that powers the chatbot
