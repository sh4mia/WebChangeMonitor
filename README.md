# Website Change Monitoring

A Python script for monitoring changes on a website at specified intervals. The script compares the previous and current content of the website and displays and records the differences if any.

## Requirements

- Python 3.x
- Python libraries: requests, difflib

## Instructions

1. Clone the repository to your local machine:
git clone https://github.com/sh4mia/WebChangeMonitor

2. Navigate to the project directory:

3. Install the required Python libraries.

4. Run the script.


5. Follow the instructions displayed on the screen:

- Enter the URL of the website you want to monitor.
- Choose the interval for checking website changes.

The script will regularly check the website at the specified interval and display any differences found.

6. The script will also log the changes in a `log.txt` file located in the same directory as the script.

## Notes

- Ensure that you have a stable internet connection to access the websites you want to monitor.
- The `log.txt` file will be created in the same directory as the script if it doesn't exist already.
- Customize the interval by providing the number of seconds. For example, to check every 10 minutes, enter an interval of 600 seconds.
