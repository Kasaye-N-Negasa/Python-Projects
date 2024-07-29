import os
import curses
from curses import KEY_OPTIONS
import json
import logging
from enum import Enum, auto
from typing import Dict, Callable

# Configuration file path
CONFIG_FILE = "config.json"

# Define global variables for configuration values
FAQ_FILE = "faq.txt"
TICKETS_FILE = "tickets.txt"
ERROR_CODES = {
    "404": ["Page not found", "Check your URL"],
    "500": ["Internal server error", "Contact support"]
}
LOG_FILE = "app.log"
LOG_LEVEL = "DEBUG"


# Function to load configuration from a JSON file
def load_config(config_file: str) -> dict:
    try:
        with open(config_file, "r") as file:
            return json.load(file)
    except FileNotFoundError as e:
        logging.error(f"Config file '{config_file}' not found.")
        raise e
    except json.JSONDecodeError as e:
        logging.error(f"Error decoding JSON in '{config_file}': {e}")
        raise e


# Function to initialize logging based on configuration
def setup_logging(log_file: str, log_level: str) -> None:
    logging.basicConfig(filename=log_file, level=logging.getLevelName(log_level),
                        format='%(asctime)s %(levelname)s %(message)s')

# Utility function to read content from a file
def read_file_content(file_path: str) -> str:
    try:
        if os.path.exists(file_path):
            with open(file_path, "r") as file:
                return file.read().strip()
        return ""
    except Exception as e:
        logging.error(f"Error reading file {file_path}: {e}")
        return ""

# Function to display FAQ content to the user
def view_faqs() -> None:
    faqs = read_file_content(FAQ_FILE)
    if faqs:
        print("\n--- Frequently Asked Questions ---\n")
        print(faqs)
        print("\n--- End of FAQs ---\n")
    else:
        print("FAQ file is empty or not found. Please create one.")
        logging.warning("FAQ file is empty or not found.")


# Function to handle user input for error code and display corresponding information
def enter_error_code() -> None:
    code = input("Enter Error Code: ")
    error_info = ERROR_CODES.get(code)
    if error_info:
        description, details1, details2 = error_info
        print(f"\nError Code: {code}\nDescription: {description}\nDetails: {details1}, {details2}\n")
    else:
        print("That Error Code doesn't exist in the list.")
        logging.warning(f"Error Code {code} not found.")


# Function to handle user search queries and display matching results from FAQ and tickets
def enter_search_query() -> None:
    search = input("Enter your search query: ")
    faqs = read_file_content(FAQ_FILE)
    tickets = read_file_content(TICKETS_FILE)

    search_results = []
    if search:
        for line in faqs.splitlines():
            if search.lower() in line.lower():
                search_results.append(line)
        for line in tickets.splitlines():
            if search.lower() in line.lower():
                search_results.append(line)

    if search_results:
        print("\n--- Search Results ---\n")
        for result in search_results:
            print(result)
        print("\n--- End of Search Results ---\n")
    else:
        print("No results found.")
    logging.info(f"Search query '{search}' executed.")


# Function to create a new ticket with user input
def create_ticket() -> None:
    name = input("Enter your name: ")
    issue = input("Describe your issue: ")
    try:
        with open(TICKETS_FILE, "a") as file:
            file.write(f"Name: {name}, Issue: {issue}\n")
        print("Ticket created successfully.")
        logging.info(f"Ticket created for {name}")
    except IOError as e:
        print(f"Failed to create ticket: {e}")
        logging.error(f"Failed to create ticket: {e}")


# Function to display current tickets to the user
def view_ticket() -> None:
    tickets = read_file_content(TICKETS_FILE)
    if tickets:
        print("\n--- Current Tickets ---\n")
        print(tickets)
        print("\n--- End of Tickets ---\n")
    else:
        print("No tickets found or the tickets file does not exist.")
        logging.warning("No tickets found or the tickets file does not exist.")


# Function to exit the program
def exit_program() -> None:
    print("Goodbye!")
    logging.info("Program exited by user.")
    exit()


# Function to display the menu options to the user
def display_menu() -> None:
    print("\nSelect an option:")
    for idx, option in enumerate(MenuOption, 1):
        print(f"{idx}. {option.name.replace('_', ' ').title()}")
    print()


# Main function to load configuration, set up logging, and handle user interaction
def main() -> None:
    global FAQ_FILE, TICKETS_FILE, ERROR_CODES, LOG_FILE, LOG_LEVEL

    try:
        config = load_config(CONFIG_FILE)
        FAQ_FILE = config["FAQ_FILE"]
        TICKETS_FILE = config["TICKETS_FILE"]
        ERROR_CODES = config["ERROR_CODES"]
        LOG_FILE = config["LOG_FILE"]
        LOG_LEVEL = config["LOG_LEVEL"]

        # Initialize logging based on configuration
        setup_logging(LOG_FILE, LOG_LEVEL)

        # Mapping of menu options to functions
        menu_actions: Dict[str, Callable[[], None]] = {
            "1": view_faqs,
            "2": enter_error_code,
            "3": enter_search_query,
            "4": create_ticket,
            "5": view_ticket,
            "6": exit_program
        }

        name = input("What's your name? ")
        print(f"Hello, {name}, welcome to Customer Support.")
        logging.info(f"User {name} started the program.")

        while True:
            display_menu()
            choice = input("Enter your choice: ")
            action = menu_actions.get(choice)
            if action:
                action()
            else:
                print("I don't understand your selection. Please try again.")
                logging.warning(f"Invalid menu selection: {choice}")

    except FileNotFoundError as e:
        print(f"Error loading configuration: {e}")
        exit(1)
    except (ValueError, KeyError) as e:
        print(f"Error in configuration: {e}")
        exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        exit(1)


# Enum for menu options
class MenuOption(Enum):
    VIEW_FAQS = auto()
    ENTER_ERROR_CODE = auto()
    ENTER_SEARCH_QUERY = auto()
    CREATE_TICKET = auto()
    VIEW_TICKET = auto()
    EXIT = auto()


if __name__ == "__main__":
    main()
