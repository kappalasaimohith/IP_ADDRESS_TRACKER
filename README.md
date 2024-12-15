
# IP Address Tracker

This is a simple web application built with Django that allows users to track their public IP address and retrieve geographical information associated with it.

## Features

- Fetches the user's public IP address using the [ipify API](https://www.ipify.org/).
- Retrieves geographical information about the IP address using the [ipinfo API](https://ipinfo.io/).
- Displays the information in a user-friendly format.

## Technologies Used

- Python
- Django
- Requests library for API calls
- HTML, CSS, JavaScript

## Getting Started

### Prerequisites

Make sure you have the following installed:

- Python (3.x)
- pip (Python package installer)

### Installation

1. **Clone the repository** (or create the project from scratch):
   ```bash
   git clone https://github.com/kappalasaimohith/IP_ADDRESS_TRACKER.git
   cd IP_ADDRESS_TRACKER/ip_tracker
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install the required packages**:
   ```bash
   pip install requirements.txt
   ```

5. **Run the Django migrations**:
   ```bash
   python manage.py migrate
   ```

6. **Start the Django development server**:
   ```bash
   python manage.py runserver
   ```

7. **Open your web browser** and go to `http://127.0.0.1:8000/`.

### Usage

- Click the "Track My IP" button to fetch and display your public IP address and its geographical information.

## Contributing

Contributions are welcome! If you have suggestions or improvements, feel free to create an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [ipify API](https://www.ipify.org/) for IP address retrieval.
- [ipinfo API](https://ipinfo.io/) for geographical information.
