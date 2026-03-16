"""
Mock up testing examples.
"""

import unittest
from unittest.mock import Mock, mock_open, patch

import requests

from white_box.mockup_exercises import (
    execute_command,
    fetch_data_from_api,
    perform_action_based_on_time,
    read_data_from_file,
)


class TestReadDataFromFile(unittest.TestCase):
    """
    Read data from file unittest class.
    """

    @patch("white_box.mockup_exercises.open")
    def test_read_file_success(self, mock_file):
        """
        Test that read_data_from_file returns the correct file content
        when the file is found and can be read successfully.
        """

        # Values for the test
        filename = "test.txt"
        file_content = "hola mundo"

        # Set up the mock to return the desired file content using the side_effect attribute
        # mock_file.side_effect = mock_open(read_data=file_content)

        # Set up the mock to return the desired file content using the return_value attribute
        mock_file.return_value = mock_open(read_data=file_content).return_value

        # Call the function being tested
        result = read_data_from_file(filename)

        # Assert that the result is as expected and that
        # the open function was called with the correct parameters
        self.assertEqual(result, file_content)
        mock_file.assert_called_once_with(filename, encoding="utf-8")

    @patch("white_box.mockup_exercises.open")
    def test_read_file_not_found(self, mock_file):
        """
        Test that read_data_from_file raises a FileNotFoundError
        when the specified file does not exist."""

        # Values for the test
        filename = "missing.txt"

        # Set up the mock to raise a FileNotFoundError when called
        mock_file.side_effect = FileNotFoundError

        # Call the function being tested and assert that it raises a FileNotFoundError
        with self.assertRaises(FileNotFoundError):
            read_data_from_file(filename)


class TestExecuteCommand(unittest.TestCase):
    """
    Execute command unittest class.
    """

    @patch("white_box.mockup_exercises.subprocess.run")
    def test_execute_command_success(self, mock_run):
        """
        Success case.
        """
        command = "echo Hello, World!"
        expected_output = "Hello, World!\n"

        # Configura el mock para retornar un objeto con stdout
        mock_run.return_value.stdout = expected_output

        # Call the function under test
        result = execute_command(command)

        # Assert que el resultado es el esperado
        self.assertEqual(result, expected_output)

        # Assert que subprocess.run fue llamado con el comando correcto
        mock_run.assert_called_once_with(
            command, capture_output=True, check=False, text=True
        )

    @patch("white_box.mockup_exercises.subprocess.run")
    def test_execute_command_failure(self, mock_run):
        """
        Failure case.
        """
        command = "invalid_command"
        expected_output = ""

        # Configura el mock para retornar un objeto con stdout
        mock_run.return_value.stdout = expected_output

        # Call the function under test
        result = execute_command(command)

        # Assert que el resultado es el esperado
        self.assertEqual(result, expected_output)

        # Assert que subprocess.run fue llamado con el comando correcto
        mock_run.assert_called_once_with(
            command, capture_output=True, check=False, text=True
        )


class TestPerformActionBasedOnTime(unittest.TestCase):
    """
    Perform Action Based On Time unittest class.
    """

    @patch("white_box.mockup_exercises.time.time")
    def test_perform_action_based_on_time_action_a(self, mock_time):
        """
        Action A.
        """

        # Configuramos el mock para retornar un valor específico
        mock_time.return_value = 5

        # Llamamos a la función de prueba
        result = perform_action_based_on_time()

        # Assert para que la función devuelve el resultado esperado
        self.assertEqual(result, "Action A")

    @patch("white_box.mockup_exercises.time.time")
    def test_perform_action_based_on_time_action_b(self, mock_time):
        """
        Action B.
        """
        # Configuramos el mock para retornar un valor específico
        mock_time.return_value = 15

        # Llamamos a la función de prueba
        result = perform_action_based_on_time()

        # Assert para que la función devuelve el resultado esperado
        self.assertEqual(result, "Action B")


class TestExample(unittest.TestCase):
    """
    Unit tests for the fetch_data_from_api function.
    """

    @patch("white_box.mockup_exercises.requests.get")
    def test_fetch_data_success(self, mock_get):
        """
        Test that fetch_data_from_api returns the correct JSON data when the API call is successful.
        """

        # Create a mock response object with the desired JSON data
        mock_response = Mock()
        json_data = {"status": "ok"}
        mock_response.json.return_value = json_data
        mock_get.return_value = mock_response

        # Call the function being tested
        url = "https://api.test.com"
        result = fetch_data_from_api(url)

        # Assert that the result is as expected and that
        # the requests.get method was called with the correct parameters
        self.assertEqual(result, json_data)
        mock_get.assert_called_once_with(url, timeout=10)

    @patch("white_box.mockup_exercises.requests.get")
    def test_fetch_data_timeout(self, mock_get):
        """
        Test that fetch_data_from_api handles timeout correctly.
        """
        # Create a mock response object with the desired JSON data
        mock_get.side_effect = requests.exceptions.Timeout

        # Call the function being tested
        url = "https://api.test.com"

        # Assert that the result is as expected and that
        # the requests.get method was called with the correct parameters
        with self.assertRaises(requests.exceptions.Timeout):
            fetch_data_from_api(url)

        mock_get.assert_called_once_with(url, timeout=10)
