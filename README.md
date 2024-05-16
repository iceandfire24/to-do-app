# Todo app
This is a simple Todo app that contains user authentication, user sign-up, search feature, and a dedicated todo view. 
The app allows you to create and delete todos along with the ability to mark them as completed.

## Prerequisites

Make sure you have the following installed on your local machine:

- Python
- Pipenv

## Getting Started

Follow these steps to clone and set up the project on your device:

1. Clone the repository:
`git clone https://github.com/iceandfire24/to-do-app.git`

2. Navigate to the project directory:
`cd project-name`

3. Install project dependencies using Pipenv:
`pipenv install`

4. Activate the virtual environment:
`pipenv shell`

5. Run database migrations:
`python manage.py migrate`

6. (Optional) Load initial data (if applicable):
`python manage.py loaddata initial_data`

7. Start the development server:
`python manage.py runserver`

8. Access the project in your web browser at `http://127.0.0.1:8000/`.

## Additional Notes

- Make sure to update settings such as database configuration (`DATABASES` in `settings.py`) and secret key (`SECRET_KEY` in `settings.py`) according to your environment and security needs.
- Customize the project-specific settings in `config/settings.py`.
- You may need to install additional dependencies depending on your project requirements. Add them to `Pipfile` and run `pipenv install` again.
- Remember to deactivate the virtual environment when you're done working on the project by running `exit` in the terminal or command prompt.

## Contributing

If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Make your changes and commit them (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Create a new Pull Request.

## License

This project is licensed under the [MIT License](LICENSE).
