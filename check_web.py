import requests
import datetime
import time
import os
from difflib import ndiff

def check_website(url, interval):
    previous_content = None

    while True:
        try:
            response = requests.get(url)
            response.raise_for_status()
            current_content = response.text

            if previous_content is None:
                previous_content = current_content
                continue

            if current_content != previous_content:
                timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                log_message = f"[{timestamp}] Zmiana na stronie {url}:\n"
                print(log_message)

                diff = ndiff(previous_content.splitlines(keepends=True), current_content.splitlines(keepends=True))
                diff_message = ''.join(line for line in diff if line.startswith('+ ') or line.startswith('- '))
                print(diff_message)

                script_directory = os.path.dirname(os.path.abspath(__file__))
                log_file_path = os.path.join(script_directory, "log.txt")

                with open(log_file_path, "a") as log_file:
                    log_file.write(log_message)
                    log_file.write(diff_message)

            previous_content = current_content

            time.sleep(interval)

        except requests.exceptions.RequestException as e:
            print(f"Nie można pobrać zawartości strony: {e}")
            time.sleep(interval)

def main():
    url = input("Podaj adres strony: ")

    print("Wybierz interwał sprawdzania:")
    print("1. Co 30 sekund")
    print("2. Co 60 sekund")
    print("3. Co 5 minut")
    print("4. Co 30 minut")
    print("5. Inny interwał (w sekundach)")

    choice = input("Wybierz opcję (1-5): ")

    if choice == "1":
        interval = 30
    elif choice == "2":
        interval = 60
    elif choice == "3":
        interval = 300
    elif choice == "4":
        interval = 1800
    elif choice == "5":
        custom_interval = input("Podaj interwał w sekundach: ")
        interval = int(custom_interval)
    else:
        print("Nieprawidłowy wybór.")
        return

    script_directory = os.path.dirname(os.path.abspath(__file__))
    log_file_path = os.path.join(script_directory, "log.txt")

    if not os.path.exists(log_file_path):
        open(log_file_path, "w").close()

    check_website(url, interval)

if __name__ == "__main__":
    main()
