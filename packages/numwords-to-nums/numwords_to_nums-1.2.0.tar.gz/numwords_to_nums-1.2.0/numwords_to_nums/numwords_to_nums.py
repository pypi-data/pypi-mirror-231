import re
from typing import List

from numwords_to_nums.tokens_basic import Token, WordType
from numwords_to_nums.rules import FusionRule, LinkingRule
from numwords_to_nums.text_processing_helpers import split_glues, find_similar_word
from numwords_to_nums.constants import OPERATORS


class NumWordsToNum(object):
    def __init__(self, convert_ordinals=True, add_ordinal_ending=False):
        """
        This class can be used to convert text representations of numbers to digits. That is, it replaces all occurrences of numbers (e.g. forty-two) to the digit representation (e.g. 42).

        :param convert_ordinals: Whether to convert ordinal numbers (e.g. third --> 3).
        :param add_ordinal_ending: Whether to add the ordinal ending to the converted ordinal number (e.g. twentieth --> 20th). Implies convert_ordinals=True.
        """

        # Used for spelling correction. It specifies the minimal similarity in the range [0, 1] of a word to one of
        # the number words. 0 indicates that every other word is similar and 1 requires a perfect match,
        # i.e. no spelling correction is performed with a value of 1.
        self.__similarity_threshold = 1.0

        if self.__similarity_threshold < 0 or self.__similarity_threshold > 1:
            raise ValueError('The similarity_threshold must be in the range [0, 1]')

        self._convert_ordinals = convert_ordinals
        self._add_ordinal_ending = add_ordinal_ending

        # Keeping the ordinal ending implies that we convert ordinal numbers
        if self._add_ordinal_ending:
            self._convert_ordinals = True

    def numerical_words_to_numbers(self, text, convert_operator=False, calculate_mode=False, evaluate=False):
        """
        Converts all number representations to digits.
        Can convert expression such that you can pass it for mathematical operations
        Can evaluate expressions for you

        Args:
            text (str): The input text containing numerical words to be converted.

            convert_operator (bool, optional): If True, converts operator words like "plus," "minus," etc. to their
            corresponding mathematical symbols (+, -, etc.). Use to display operators on UI or for user.
            Default is False.

            calculate_mode (bool, optional): If True, activates the calculation mode, allowing mathematical operations to
            be performed later on if required, using converted numerical words and operators. Default is False.

            evaluate (bool, optional): If True, evaluates the mathematical expression in the text when in calculate_mode.
            Raises an exception if calculate_mode is not enabled. Default is False.

        Returns:
            str: The input text with numerical words, ordinal numbers and optionally operators converted to their numeric equivalents.
                If calculate_mode is enabled and evaluate is True, it returns the result of the mathematical expression.

        Raises:
            Exception: If convert_operator is set to False when calculate_mode is True, as operator conversion is required
                for calculation.
            Exception: If evaluate is True but calculate_mode is not enabled, as calculation mode is necessary for evaluation.
        """
        # Check parameter logically
        if calculate_mode and convert_operator == False:
            raise Exception("ParameterException: Convert Operator must be True if Calculation mode is activated")

        # Tokenize the input string by assigning a type to each word (e.g. representing the number type like units (
        # e.g. one) or teens (twelve)) This makes it easier for the subsequent steps to decide which parts of the
        # sentence need to be combined e.g. I like forty-two apples --> I [WordType.Other] like [WordType.Other]
        # forty [WordType.TENS] two [WordType.UNITS] apples [WordType.Other]
        tokens = self._aspect(text)

        # Apply a set of rules to the tokens to combine the numeric tokens and replace them with the corresponding
        # digit e.g. I [WordType.Other] like [WordType.Other] 42 [ConcatenatedToken] apples [WordType.Other] (it
        # merged the TENS and UNITS tokens)
        converted_text = self._portray(tokens).replace('_', '')

        if convert_operator and calculate_mode:
            converted_text = self.__convert_operators(converted_text, True)
        elif convert_operator:
            converted_text = self.__convert_operators(converted_text)
        if evaluate and calculate_mode != True:
            raise Exception("ParameterException: Calculate mode needs to be True if Evaluation is activated")
        elif evaluate and calculate_mode:
            converted_text = self.evaluate(converted_text)

        return converted_text

    def __convert_operators(self, expression_text, calculate_mode=False):
        expression_text = re.sub(' +', ' ', expression_text)

        for operator_word in OPERATORS:
            if operator_word in expression_text.lower():
                # mode selection
                if calculate_mode:
                    operator_symbol = OPERATORS[operator_word][1]
                else:
                    operator_symbol = OPERATORS[operator_word][0]

        for operator_word in OPERATORS:
            if operator_word in expression_text.lower():
                # for scenario's like  multiply 3 by 3
                if expression_text.lower().startswith(operator_word) and 'square' not in expression_text.lower():
                    if 'by' in expression_text.lower():
                        expression_text = expression_text.replace(operator_word, '').replace('by', operator_word)
                        # expression_text = expression_text.replace('by', operator_word)
                    if 'with' in expression_text:
                        expression_text = expression_text.replace(operator_word, '').replace('with', operator_word)
                        # expression_text = expression_text.replace('with', operator_word)

                valid_pattern = f'\d+ {operator_word} \d+'
                rare_case = f'{operator_word}\s+square|√'
                if calculate_mode:
                    operator_symbol = OPERATORS[operator_word][1]
                else:
                    operator_symbol = OPERATORS[operator_word][0]

                if re.findall('(percent)', expression_text.lower()) and 'per' in operator_word:
                    pattern = f' {operator_word}'
                    expression_text = expression_text.replace(pattern, operator_symbol)

                if re.findall(rf'\bsquare\b', expression_text.lower()) and 'square' in operator_word:
                    if calculate_mode is False:
                        if operator_symbol == '√':
                            pattern = re.compile(f'{operator_word} ', re.IGNORECASE)
                            expression_text = pattern.sub("√", expression_text)
                        elif operator_symbol == '²':
                            pattern = re.compile(f'{operator_word}', re.IGNORECASE)
                            expression_list = pattern.sub("²", expression_text).split()
                            index = 0
                            while index < len(expression_list):
                                if expression_list[index] == "²":
                                    if index + 1 < len(expression_list):
                                        expression_list[index + 1], expression_list[index] = operator_symbol, \
                                            expression_list[
                                                index + 1]
                                    index += 1  # Skip the next element
                                index += 1

                            expression_list = [item for item in expression_list if item != ""]
                            expression_text = " ".join(expression_list)

                    else:
                        pattern = re.compile(f'{operator_word}', re.IGNORECASE)
                        expression_list = pattern.sub("√", expression_text).split()
                        index = 0
                        while index < len(expression_list):
                            if expression_list[index] == "√":
                                if index + 1 < len(expression_list):
                                    expression_list[index + 1], expression_list[index] = operator_symbol, \
                                        expression_list[
                                            index + 1]
                                index += 1  # Skip the next element
                            index += 1

                        expression_list = [item for item in expression_list if item != ""]
                        expression_text = " ".join(expression_list)

                if re.findall(valid_pattern, expression_text.lower()) or \
                        re.match(operator_word, expression_text.lower()) or \
                        re.search(rare_case, expression_text.lower()):
                    expression_text = expression_text.replace(f' {operator_word} ', operator_symbol)

        return expression_text

    def _aspect(self, text: str) -> List[Token]:
        """
        This function takes an arbitrary input string, splits it into tokens (words) and assigns each token a type corresponding to the role in the sentence.

        :param text: The input string.
        :return: The tokenized input string.
        """
        tokens = []

        conjunctions = []
        for i, (word, glue) in enumerate(split_glues(text)):
            # Address spelling corrections
            if self.__similarity_threshold != 1:
                matched_num = find_similar_word(word, Token.numwords.keys(), self.__similarity_threshold)
                if matched_num is not None:
                    word = matched_num
            token = Token(word, glue)
            tokens.append(token)

            # Conjunctions need special treatment since they can be used for both, to combine numbers or to combine other parts in the sentence
            if token.type == WordType.CONJUNCTION:
                conjunctions.append(i)

        # A word should only have the type WordType.CONJUNCTION when it actually combines two digits and not some other words in the sentence
        for i in conjunctions:
            if i >= len(tokens) - 1 or tokens[i + 1].type in [WordType.CONJUNCTION, WordType.OTHER]:
                tokens[i].type = WordType.OTHER

        return tokens

    def _portray(self, tokens: List[Token]) -> str:
        """
        Parses the tokenized input based on predefined rules which combine certain tokens to find the correct digit representation of the textual number description.

        :param tokens: The tokenized input string.
        :return: The transformed input string.
        """
        rules = [FusionRule(), LinkingRule()]

        # Apply each rule to process the tokens
        for rule in rules:
            new_tokens = []
            i = 0
            while i < len(tokens):
                if tokens[i].is_ordinal() and not self._convert_ordinals:
                    # When keeping ordinal numbers, treat the whole number (which may consists of multiple parts, e.g. ninety-seventh) as a normal word
                    tokens[i].type = WordType.OTHER

                if tokens[i].type != WordType.OTHER:

                    # Check how many tokens this rule wants to process...
                    n_match = rule.match(tokens[i:])
                    if n_match > 0:
                        # ... and then merge these tokens into a new one (e.g. a token representing the digit)
                        token = rule.action(tokens[i:i + n_match])
                        new_tokens.append(token)
                        i += n_match
                    else:
                        new_tokens.append(tokens[i])
                        i += 1
                else:
                    new_tokens.append(tokens[i])
                    i += 1

            tokens = new_tokens

        # Combine the tokens back to a string (with special handling of ordinal numbers)
        text = ''
        for token in tokens:
            if token.is_ordinal() and not self._convert_ordinals:
                text += token.word_raw
            else:
                text += token.text()
                if token.is_ordinal() and self._add_ordinal_ending:
                    text += token.ordinal_ending

            text += token.glue

        return text

    @staticmethod
    def evaluate(et):
        """
        Evaluates a mathematical expression represented as a string.

        This method takes an input string containing a mathematical expression, cleans it by removing non-numeric and non-mathematical characters,
        and then attempts to evaluate the expression. If the evaluation is successful, it returns the result as a string.
        If an evaluation error occurs, it returns an error message indicating that the answer is undefined along with the
        specific evaluation error.

        Args:
            et (str): The input string containing a mathematical expression to be evaluated.

        Returns:
            str: The result of the mathematical expression as a string if evaluation is successful. If an error occurs
                 during evaluation, it returns an error message with details of the error.

        Example:
            If et is "2 + 3 * 4", the method returns "14".
            If et is "10 / 0", the method returns " The answer is undefined. Evaluation error: division by zero".
        """
        # Clean character other than numeric and math characters
        expr_text = ''.join(re.findall("[\d\W]", et))
        # Clean new line, tab and space characters
        expr_text = ''.join(re.findall("[\S]", expr_text))
        # clean extra special character at the end
        expr_text = re.sub(r'[^\w\s]+$', '', expr_text)

        result = None

        try:
            result = eval(expr_text)
        except Exception as e:
            result = f" The answer is undefined. Evaluation error: {e}"
        return str(result)
