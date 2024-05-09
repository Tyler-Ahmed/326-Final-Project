import pytest
from Take_A_Quiz import Quiz, sample_quizzes

# Test the Quiz class methods
@pytest.fixture
def sample_quiz():
    return sample_quizzes()[0]  




def test_add_question(sample_quiz):
    sample_quiz.add_question("Test Question", "Test Answer")
    assert len(sample_quiz.questions) == 1
    assert sample_quiz.questions[0] == ("Test Question", "Test Answer")




def test_save_score(tmp_path, sample_quiz):
    score_file = tmp_path / "test_scores.txt"
    name = "Test User"
    score = 80
    sample_quiz.save_score(name, score)
    assert score_file.exists()
    with open(score_file, "r") as f:
        content = f.read()
        assert f"Name: {name}, Score: {score}%" in content




def test_add_new_question(sample_quiz):
    num_questions_before = len(sample_quiz.questions)
    sample_quiz.add_new_question([], 0)  # Passing empty list and index 0 for simplicity
    num_questions_after = len(sample_quiz.questions)
    assert num_questions_after == num_questions_before + 1



def test_run_quiz(sample_quiz, capsys, monkeypatch):
    # Mock user inputs
    mock_inputs = iter(["correct", "wrong", "yes"])  # Assuming first two answers are correct and last is to exit
    monkeypatch.setattr('builtins.input', lambda _: next(mock_inputs))

    sample_quiz.run_quiz(sample_quiz)
    captured = capsys.readouterr()
    assert "Correct!" in captured.out
    assert "Wrong!" in captured.out
    assert "You got 1 out of" in captured.out  # Assuming there are 2 questions





def test_retake_quiz(sample_quiz, monkeypatch):
    # Mock user input for "yes"
    monkeypatch.setattr('builtins.input', lambda _: 'yes')
    with pytest.raises(SystemExit):
        sample_quiz.retake_quiz()

    # Mock user input for "no"
    monkeypatch.setattr('builtins.input', lambda _: 'no')
    with pytest.raises(SystemExit):
        sample_quiz.retake_quiz()




def test_display_scores(tmp_path, sample_quiz, capsys, monkeypatch):
    # Create a temporary score file\\

    score_file = tmp_path / "test_scores.txt"
    with open(score_file, "w") as f:
        f.write("Name: Test User, Score: 80%\n")

    # Mock user input for choice
    monkeypatch.setattr('builtins.input', lambda _: '1')
    sample_quiz.display_scores()
    captured = capsys.readouterr()
    assert "Test User" in captured.out
    assert "80%" in captured.out
    # Mock user input for invalid choice
    monkeypatch.setattr('builtins.input', lambda _: 'invalid')
    sample_quiz.display_scores()
    captured = capsys.readouterr()
    assert "Invalid choice" in captured.out



def test_reset_scores(tmp_path, sample_quiz):
    # Create a temporary score file
    score_file = tmp_path / "test_scores.txt"
    with open(score_file, "w") as f:
        f.write("Name: Test User, Score: 80%\n")
    sample_quiz.reset_scores()
    assert score_file.exists()
    assert score_file.stat().st_size == 0
