# Website Change Monitoring

`Website Change Monitoring` is a simple Python script dockerized in a Docker container for monitoring changes on websites. The script checks a specified website at regular intervals and logs any changes in the website's content.

## Container Setup

1. Make sure you have Docker installed on your computer.

2. Clone the `WebChangeMonitor` repository to your local machine:
   ```
   git clone https://github.com/sh4mia/WebChangeMonitor.git
   ```
3. Navigate to the `web_check` directory:
   ```
   cd WebChangeMonitor
   ```
4. To build the Docker image, run the following command:
   ```
   docker build -t WebChangeMonitor .
   ```

## Usage

1. Run a Docker container based on the `WebChangeMonitor` image:
   ```
   docker run -it --name WebChangeMonitor_container WebChangeMonitor
   ```
2. Follow the instructions displayed on the screen.

   - Enter the website URL to monitor.
   - Choose the monitoring interval from the available options or enter a custom interval in seconds.

3. The script will start monitoring the website and display information about any changes in the content.

   - If the website content changes, the script will log the changes and display the difference between the previous and current content.
   - Change logs will be saved in the `log.txt` file.

4. To stop the script, use the Ctrl+C key combination.

## Options

- `--interval` - The monitoring interval in seconds. Available options: 30, 60, 300, 1800. Default: 60.
- `--custom-interval` - Custom monitoring interval in seconds.
- `--log-file-path` - Path to the log file. Default: log.txt.

## Recommendations

- It is recommended to run the script inside a Docker container to ensure consistent execution across different environments.
- Ensure that you have the required dependencies installed by building the Docker image.
- Customize the options and arguments as per your specific monitoring needs.

## Update 1.1

In version 1.1 of the "Website Change Monitoring" the following updates have been made:

- Dockerized
- Updated Readme.md

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

This code is provided under the [MIT License](https://opensource.org/licenses/MIT). Feel free to modify and use it in your projects.