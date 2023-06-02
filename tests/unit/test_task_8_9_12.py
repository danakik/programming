from task_8_9.task_8_9_12 import get_player_choice, play_game


def test_get_player_choice_negative(monkeypatch, capsys):
    input_values = ['water', 'Rock']
    monkeypatch.setattr('builtins.input', lambda _: input_values.pop(0))
    get_player_choice()
    captured = capsys.readouterr()
    assert captured.out == 'Invalid choice. Please try again.\n'


def test_get_player_choice(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'Rock')
    actual = get_player_choice()
    assert actual == 'Rock'


def test_play_game_draw(monkeypatch, capsys):
    monkeypatch.setattr('random.choice', lambda _: 'Rock')
    player_choice = 'Rock'
    play_game(player_choice)
    captured = capsys.readouterr()
    assert "It's a draw!\n" in captured.out


def test_play_game_computer_wins(monkeypatch, capsys):
    monkeypatch.setattr('random.choice', lambda _: 'paper')
    player_choice = 'Rock'
    play_game(player_choice)
    captured = capsys.readouterr()
    assert 'Computer wins!\n' in captured.out


def test_play_game_wins(monkeypatch, capsys):
    monkeypatch.setattr('random.choice', lambda _: 'scissors')
    player_choice = 'Rock'
    play_game(player_choice)
    captured = capsys.readouterr()
    assert 'You win!\n' in captured.out
