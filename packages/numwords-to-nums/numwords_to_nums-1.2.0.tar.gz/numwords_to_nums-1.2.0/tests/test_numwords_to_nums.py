import pytest

from numwords_to_nums.numwords_to_nums import NumWordsToNum


@pytest.mark.parametrize("input_text,expected", [
    ("I was born in twenty ten", "I was born in 2010"),
    ("I was born in nineteen sixty four", "I was born in 1964"),
    ("thirty twenty one", "3021"),
    ("sixteen sixty six", "1666"),
    ("twenty nineteen", "2019"),
    ("twenty twenty", "2020"),
    ("fifty one thirty three", "5133"),
    ("fifty five twelve", "5512"),
    ("thirty eleven", "3011"),
    ("sixty six ten", "6610"),
    ('In the year twenty twenty one, the forty sixth President of the United States was inaugurated.',
     'In the year 2021, the 46th President of the United States was inaugurated.'
     )
])
def test_positive_integers(input_text, expected):
    num = NumWordsToNum()
    result = num.numerical_words_to_numbers(input_text)
    assert result == expected
