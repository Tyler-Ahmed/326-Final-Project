import pytest
from io import StringIO
from contextlib import redirect_stdout
from Take_A_Quiz import main

# Test that the quiz options display when running the program
def test_display_quiz_options(capsys):
    # Capture standard output
    with redirect_stdout(StringIO()) as stdout:
        # Run the main function
        main()
    
    # Get the captured output
    output = stdout.getvalue()
    
    # Assert that the quiz options are displayed
    assert "Choose an option:" in output
    assert "1. Take a Quiz" in output

# Test that something displays for the scores
def test_display_scores(capsys):
    # Capture standard output
    with redirect_stdout(StringIO()) as stdout:
        # Run the main function
        main()
    
    # Get the captured output
    output = stdout.getvalue()
    
    # Assert that something related to scores is displayed
    assert "Scores" in output  # Assuming there's some text related to scores displayed

if __name__ == "__main__":
    pytest.main()
