import enum
import re
from decimal import Decimal


class WordType(enum.Enum):
    OTHER = 0
    LITERAL_INT = 1
    LITERAL_FLOAT = 2
    UNITS = 3
    TEENS = 4
    TENS = 5
    SCALES = 6
    CONJUNCTION = 7
    REPLACED = 8


class Token(object):
    # Static init code (only executed once and not for each token instance)
    UNITS = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    TEENS = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen',
             'nineteen']
    TENS = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    SCALES = ['hundred', 'thousand', 'million', 'billion', 'trillion', 'quadrillion']
    SCALE_VALUES = [100, 1_000, 10_000, 1_000_000, 10_000_000, 1_000_000_000, 100_000_000_000,
                    1_000_000_000_000, 1_000_000_000_000_000]  # used for has_large_scale
    INDIAN_SCALES = ['lakh', 'crore', 'arab']
    CONJUNCTION = ['and']
    ORDINAL_WORDS = {'oh': 'zero', 'first': 'one', 'second': 'two', 'third': 'three', 'fifth': 'five',
                     'eighth': 'eight', 'ninth': 'nine', 'twelfth': 'twelve'}
    ORDINAL_ENDINGS = [('ieth', 'y'), ('th', '')]
    ORDINAL_SUFFIXES = ['_st', '_nd', '_rd', '_th', '_ieth']

    numwords = {
        'and': (1, 0)  # (scale, value)
    }
    for idx, word in enumerate(UNITS):
        numwords[word] = (1, idx)
        numwords[f'{word}{ORDINAL_SUFFIXES[0]}'] = (1, f'{idx}{ORDINAL_SUFFIXES[0]}')
        numwords[f'{word}{ORDINAL_SUFFIXES[1]}'] = (1, f'{idx}{ORDINAL_SUFFIXES[1]}')
        numwords[f'{word}{ORDINAL_SUFFIXES[2]}'] = (1, f'{idx}{ORDINAL_SUFFIXES[2]}')
        numwords[f'{word}{ORDINAL_SUFFIXES[3]}'] = (1, f'{idx}{ORDINAL_SUFFIXES[3]}')
        numwords[f'{word}{ORDINAL_SUFFIXES[4]}'] = (1, f'{idx}{ORDINAL_SUFFIXES[4]}')
    for idx, word in enumerate(TEENS):
        numwords[word] = (1, idx + 10)
        numwords[f'{word}{ORDINAL_SUFFIXES[0]}'] = (1, f'{idx + 10}{ORDINAL_SUFFIXES[0]}')
        numwords[f'{word}{ORDINAL_SUFFIXES[1]}'] = (1, f'{idx + 10}{ORDINAL_SUFFIXES[1]}')
        numwords[f'{word}{ORDINAL_SUFFIXES[2]}'] = (1, f'{idx + 10}{ORDINAL_SUFFIXES[2]}')
        numwords[f'{word}{ORDINAL_SUFFIXES[3]}'] = (1, f'{idx + 10}{ORDINAL_SUFFIXES[3]}')
        numwords[f'{word}{ORDINAL_SUFFIXES[4]}'] = (1, f'{idx + 10}{ORDINAL_SUFFIXES[4]}')
    for idx, word in enumerate(TENS):
        numwords[word] = (1, (idx + 2) * 10)
        numwords[f'{word}{ORDINAL_SUFFIXES[0]}'] = (1, f'{(idx + 2) * 10}{ORDINAL_SUFFIXES[0]}')
        numwords[f'{word}{ORDINAL_SUFFIXES[1]}'] = (1, f'{(idx + 2) * 10}{ORDINAL_SUFFIXES[1]}')
        numwords[f'{word}{ORDINAL_SUFFIXES[2]}'] = (1, f'{(idx + 2) * 10}{ORDINAL_SUFFIXES[2]}')
        numwords[f'{word}{ORDINAL_SUFFIXES[3]}'] = (1, f'{(idx + 2) * 10}{ORDINAL_SUFFIXES[3]}')
        numwords[f'{word}{ORDINAL_SUFFIXES[4]}'] = (1, f'{(idx + 2) * 10}{ORDINAL_SUFFIXES[4]}')
    for idx, word in enumerate(SCALES):
        numwords[word] = (10 ** (idx * 3 or 2), 0)
        numwords[f'{word}{ORDINAL_SUFFIXES[0]}'] = (1, f'{10 ** (idx * 3 or 2), 0}{ORDINAL_SUFFIXES[0]}')
        numwords[f'{word}{ORDINAL_SUFFIXES[1]}'] = (1, f'{10 ** (idx * 3 or 2), 0}{ORDINAL_SUFFIXES[1]}')
        numwords[f'{word}{ORDINAL_SUFFIXES[2]}'] = (1, f'{10 ** (idx * 3 or 2), 0}{ORDINAL_SUFFIXES[2]}')
        numwords[f'{word}{ORDINAL_SUFFIXES[3]}'] = (1, f'{10 ** (idx * 3 or 2), 0}{ORDINAL_SUFFIXES[3]}')
        numwords[f'{word}{ORDINAL_SUFFIXES[4]}'] = (1, f'{10 ** (idx * 3 or 2), 0}{ORDINAL_SUFFIXES[4]}')
    for idx, word in enumerate(INDIAN_SCALES):
        numwords[word] = (10 ** (5 + idx * 2), 0)
        numwords[f'{word}{ORDINAL_SUFFIXES[0]}'] = (1, f'{10 ** (5 + idx * 2), 0}{ORDINAL_SUFFIXES[0]}')
        numwords[f'{word}{ORDINAL_SUFFIXES[1]}'] = (1, f'{10 ** (5 + idx * 2), 0}{ORDINAL_SUFFIXES[1]}')
        numwords[f'{word}{ORDINAL_SUFFIXES[2]}'] = (1, f'{10 ** (5 + idx * 2), 0}{ORDINAL_SUFFIXES[2]}')
        numwords[f'{word}{ORDINAL_SUFFIXES[3]}'] = (1, f'{10 ** (5 + idx * 2), 0}{ORDINAL_SUFFIXES[3]}')
        numwords[f'{word}{ORDINAL_SUFFIXES[4]}'] = (1, f'{10 ** (5 + idx * 2), 0}{ORDINAL_SUFFIXES[4]}')

    def __init__(self, word: str, glue: str):
        """
        Represents a word in the text with some additional knowledge about the word (e.g. information about its type).

        :param word: The string representation in the text.
        :param glue: The glue (e.g. whitespace) which follows the word.
        """

        self.word_raw = word
        self.glue = glue

        # Basic preprocessing of the word to find the type
        self._word = word.lower().replace(',', '')
        if re.match(r'^[^\w]+|\w+[^\w]+$', self._word):
            # If there are special characters adjacent to the word
            self._word = re.sub(r'[^\w\s]', '', self._word)

        # Try to match ordinal numbers and then treat them as cardinal ones
        self.ordinal_ending = None  # We need to keep a reference to the original ending in case the user wants to preserve it
        if self._word in Token.ORDINAL_WORDS:
            self.ordinal_ending = self._word[-2:]
            self._word = f'{Token.ORDINAL_WORDS[self._word]}_{self.ordinal_ending}'

        for ending, replacement in Token.ORDINAL_ENDINGS:
            if self._word.endswith(ending):
                replaced = self._word[:-len(ending)] + replacement
                if replaced in Token.numwords:
                    self.ordinal_ending = self._word[-2:]
                    self._word = f'{replaced}_{self.ordinal_ending}'

        # Assign a type to each token (from specific to general)
        self.temp_word = self._word.split('_')[0] if '_' in self._word else self._word
        if self.temp_word in Token.UNITS:
            self.type = WordType.UNITS
        elif self.temp_word in Token.TEENS:
            self.type = WordType.TEENS
        elif self.temp_word in Token.TENS:
            self.type = WordType.TENS
        elif self.temp_word in Token.SCALES or self.temp_word in Token.INDIAN_SCALES:
            self.type = WordType.SCALES
        elif self.temp_word in Token.CONJUNCTION:
            self.type = WordType.CONJUNCTION
        elif re.search(r'^\d+\.\d*|\d*\.\d+$', self.temp_word):
            self.type = WordType.LITERAL_FLOAT
        elif re.search(r'^\d+$', self.temp_word):
            self.type = WordType.LITERAL_INT
        else:
            self.type = WordType.OTHER

    def __repr__(self) -> str:
        return f'{self._word} ({self.type})'

    def is_ordinal(self) -> bool:
        return self.ordinal_ending is not None

    def has_large_scale(self) -> bool:
        """
        Returns True when the token has a scale >= 100.
        """
        if self.type == WordType.SCALES:
            return True
        elif self.type in [WordType.LITERAL_INT, WordType.LITERAL_FLOAT]:
            return Decimal(self._word) in self.SCALE_VALUES
        else:
            return False

    def value(self) -> Decimal:
        """
        Returns the value of a token (e.g. twelve -> 12). SCALES have a value of 0 since they are defined by their scale and not by their value, e.g. for two hundred we calculate 2 * 100 + 0.
        """
        if self.type in [WordType.LITERAL_INT, WordType.LITERAL_FLOAT]:
            if self.has_large_scale():
                return Decimal(0)
            else:
                return Decimal(self._word)
        elif self.type != WordType.OTHER:
            value = Token.numwords[self._word][1]
            return value

    def scale(self) -> Decimal:
        """
        Returns the scale of a token (e.g. hundred -> 100).
        """
        if self.type in [WordType.LITERAL_INT, WordType.LITERAL_FLOAT]:
            if self.has_large_scale():
                return Decimal(self._word)
            else:
                return Decimal(1)
        elif self.type != WordType.OTHER:
            value = Token.numwords[self._word][0]
            return Decimal(value)

    def text(self) -> str:
        """
        Returns the textual (digit) representation of the token (e.g. twelve -> 12).
        """
        if self.type in [WordType.LITERAL_INT, WordType.LITERAL_FLOAT, WordType.CONJUNCTION, WordType.OTHER]:
            # Keep the original representation of the literal in case there were e.g. some thousand separators
            return self.word_raw
        elif self.type == WordType.SCALES:
            return str(self.scale())
        else:
            return str(self.value())


class NoneToken(object):
    """
    Special token type which serves as a mock-up for a word which does not exist in the input.
    """

    def __init__(self):
        self.type = None

    def is_ordinal(self) -> bool:
        return False

    def has_large_scale(self) -> bool:
        return False
