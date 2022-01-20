from masters_project.main import get_data

def test_add():
    assert get_data() == {1: 2}