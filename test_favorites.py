import pytest
from favorite_things_functions import add_category, update_fav, delete_fav, type_category, display_favs

def test_add_category(monkeypatch):
    favorites = {}
    inputs = iter(["color", "blue"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    add_category(favorites)
    assert favorites == {"color": "blue"}

def test_update_fav(monkeypatch):
    favorites = {"drink": "coffee"}
    inputs = iter(["drink", "tea"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    update_fav(favorites)
    assert favorites["drink"] == "tea"

def test_delete_fav(monkeypatch):
    favorites = {"snack": "chips"}
    monkeypatch.setattr("builtins.input", lambda _: "snack")

    delete_fav(favorites)
    assert "snack" not in favorites

def test_type_category(monkeypatch):
    favorites = {"movie": "Inception"}
    inputs = iter(["invalid", "movie"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    result = type_category(favorites)
    assert result == "My favorite for this is: Inception"

def test_display_favs():
    favorites = {"sport": "basketball"}
    result = display_favs(favorites)
    assert result == "Your favorites:\nsport: basketball"