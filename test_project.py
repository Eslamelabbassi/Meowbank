import pytest
from project import Account, check_balance, deposit, withdraw, transfer
from unittest.mock import patch

# Define fixtures for creating sample accounts
@pytest.fixture
def sample_accounts():
    return {
        1: Account(1,"Hamasa","Abosha5a",100,123),
        2: Account(2,"Besla", "Hanem",200,456),
        3: Account(3,"Lotion", "Sarena",75,789)
    }

# Mocking the get_positive_integer_input function
@patch('project.get_positive_integer_input')
def test_deposit(mock_input, sample_accounts):
    mock_input.return_value = 50  # Simulate user input
    account = sample_accounts[1]
    assert deposit(account) == "\nSuccessful deposit. Your new balance is: 150 Treat."

# Mocking the get_positive_integer_input function
@patch('project.get_positive_integer_input')
def test_withdraw(mock_input, sample_accounts):
    mock_input.return_value = 100  # Simulate user input
    account = sample_accounts[1]
    assert withdraw(account) == "\nSuccessful withdrawal. Your new balance is: 0 Treat."

# Mocking the get_positive_integer_input function
@patch('project.get_positive_integer_input')
def test_transfer(mock_input, sample_accounts):
    mock_input.return_value = 50  # Simulate user input
    sender_account = sample_accounts[1]
    receiver_account = sample_accounts[2]
    assert transfer(sender_account, receiver_account) == "\nSuccessful transfer. Your new balance is: 50 Treat."

@patch('project.get_positive_integer_input')
def test_check_balance(mock_input, sample_accounts):
    mock_input.return_value = 1
    account = sample_accounts[1]
    assert check_balance(account)=="\nYour current balance is: 100 Treat."

