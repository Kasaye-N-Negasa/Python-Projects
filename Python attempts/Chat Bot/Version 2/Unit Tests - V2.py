import unittest
from unittest.mock import patch, mock_open
from Main_Script import view_faqs, enter_error_code, create_ticket, read_file_content
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


class TestCustomerSupport(unittest.TestCase):

    @patch("builtins.open", new_callable=mock_open, read_data="FAQ content")
    @patch("os.path.exists", return_value=True)
    def test_view_faqs(self, mock_exists, mock_open):
        with patch("builtins.print") as mock_print:
            view_faqs()
            mock_print.assert_any_call("\n--- Frequently Asked Questions ---\n")
            mock_print.assert_any_call("FAQ content")

    @patch("builtins.input", side_effect=["404"])
    def test_enter_error_code(self, mock_input):
        with patch("builtins.print") as mock_print:
            enter_error_code()
            mock_print.assert_any_call("\nError Code: 404")
            mock_print.assert_any_call("Description: Not Found")

    @patch("builtins.open", new_callable=mock_open, read_data="")
    @patch("os.path.exists", return_value=True)
    def test_read_file_content(self, mock_exists, mock_open):
        content = read_file_content("some_file.txt")
        self.assertEqual(content, "")

    @patch("builtins.input", side_effect=["John Doe", "System crash"])
    @patch("builtins.open", new_callable=mock_open)
    def test_create_ticket(self, mock_open, mock_input):
        with patch("builtins.print") as mock_print:
            create_ticket()
            mock_print.assert_any_call("Ticket created successfully.")
            mock_open().write.assert_called_once_with("Name: John Doe, Issue: System crash\n")


if __name__ == "__main__":
    unittest.main()
