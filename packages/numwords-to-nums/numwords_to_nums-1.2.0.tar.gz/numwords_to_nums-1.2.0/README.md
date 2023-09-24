# numwords_to_nums: 
  - numwords_to_nums not only handles a wide range of numeric conversions, including large numbers and Indian numbering systems but also ensures that it maintains the integrity of your input string.
  - It won't alter punctuation marks like full stops, capitalization of characters, word order in sentences, or sentence arrangement.
  - You can trust that it will provide you with your exact input string while making only the necessary conversions.
    - <b>Exception</b> : evaluate() method or evaluation mode as they return evaluation of mathematical expression found in your text.
  - Large number support till quadrillion and Indian scale support till arab so no need to worry about large numbers.
  - I find this useful when I've transcribed audio into text and need to seamlessly transform that textual data into numerical digits, mathematical operators, and ultimately, evaluate complex numerical expressions.

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#installation">Installation</a>
    </li>
    <li><a href="#prerequisites">Prerequisites</a></li>
    <li>
      <a href="#usage">Usage</a>
      <ul>
        <li><a href="#method-overview">Method overview</a></li>
         <ul>
          <li><a href="#numerical_words_to_numbers">numerical_words_to_numbers()</a></li>
          <li><a href="#evaluate">evaluate()</a></li>
         </ul>
      </ul>
    </li>
   <li><a href="#examples">Examples</a>
      <ul>
        <li><a href="#sentence-without-any-conversion">Sentence without any conversion</a></li>
        <li><a href="#convert-digits-from-a-random-sentence">Convert digits from a random sentence</a></li>
        <li><a href="#large-numbers">Large numbers</a></li>
        <li><a href="#indian-numbering-system">Indian numbering system</a></li>
        <li><a href="#convert-ordinals">Convert ordinals</a></li>
        <li><a href="#dates-and-years">Dates and Years</a></li>
        <li><a href="#operator-conversion">Operator Conversion</a></li>
        <li><a href="#operator-not-with-digits">Operator not with digits?</a></li>
        <li><a href="#decimal-numbers">Decimal numbers</a></li>
        <li><a href="#have-your-own-evaluate-function">Have your own evaluate function?</a></li>
        <li><a href="#expression-evaluation">Expression Evaluation</a></li>
        <li><a href="#numeric-calculation-in-text">Numeric Calculation in Text</a></li>
        <li><a href="#handle-all-patterns-at-same-time">Handle all patterns at same time</a></li>
      </ul>
   </li>
    <li><a href="#improvements-or-issues">Improvements or Issues</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>


## Installation
```
pip3 install numwords_to_nums
```

## Prerequisites
- Python 3 or later

## Usage
1) Import the NumWordsToNum class
   ```
   from numwords_to_nums.numwords_to_nums import NumWordsToNum
    ```
2) Initialize the NumWordsToNum object
    ```
    num = NumWordsToNum()
    ```
3) Select one of the below method based on your requirement
   - numerical_words_to_numbers()
   - evaluate()

4) Here's a <b>basic example</b>
   ```
   from numwords_to_nums.numwords_to_nums import NumWordsToNum
   num = NumWordsToNum()
      
   result = num.numerical_words_to_numbers("twenty ten and twenty one")
   print(result)  # Output: 2010 and 21
      
   eval_result = num.evaluate('Hey calculate 2+5')
   print(eval_result) # Output: 7
    ```

### Method overview

- #### numerical_words_to_numbers()

   ```
   numerical_words_to_numbers(text, convert_operator=False, calculate_mode=False, evaluate=False)
   ```
   
   - Converts numerical words in the input text to their corresponding numeric digits. Optionally, it can also handle mathematical operator words and perform calculations.

   - <b>Parameters: </b>
     - <b>text (str)</b>: The input text containing numerical words to be converted.
     - <b>convert_operator (bool, optional)</b>: If True, converts operator words like "plus," "minus," etc., to their corresponding mathematical symbols (+, -, etc.). Use to display operators on UI or for user. Default is False.
     - <b>calculate_mode (bool, optional)</b>: If True, activates the calculation mode, allowing mathematical operations to be performed later on if required, using converted numerical words and operators. Default is False
     - <b>evaluate (bool, optional)</b>: If True, evaluates the mathematical expression in the text when in calculate_mode. Raises an exception if calculate_mode is not enabled. Default is False.

   - <b>Returns: </b>
     - <b>str</b>: The input text with numerical words and optionally operators converted to their numeric equivalents. If calculate_mode is enabled and evaluate is True, it returns the result of the mathematical expression. 

   - <b>Raises:</b>
     -  <b>Exception</b>: If convert_operator is set to False when calculate_mode is True, as operator conversion is required
                  for calculation.
     - <b>Exception</b>: If evaluate is True but calculate_mode is not enabled, as calculation mode is necessary for evaluation.

- #### evaluate()

   ```
   evaluate()
   ```
   - Evaluates a mathematical expression represented as a string.
   - This method takes an input string containing a mathematical expression, cleans it by removing non-numeric and non-mathematical characters,
             and then attempts to evaluate the expression.
   - If the evaluation is successful, it returns the result as a string.
   - If an evaluation error occurs, it returns an error message indicating that the answer is undefined along with the
             specific evaluation error.

   - <b>Args</b>:
     - <b>str</b>:  The input string containing a mathematical expression to be evaluated.

   - <b>Returns</b>:
     - <b>str</b>: The result of the mathematical expression as a string if evaluation is successful. If an error occurs
                          during evaluation, it returns an error message with details of the error.

   - <b>Example</b>:
     - Input : '2 + 3 * 4' --> Output: '14'
     - Input : '10 / 0' --> Output: ' The answer is undefined. Evaluation error: division by zero'.


## Examples

- #### Sentence without any conversion
  <b>What happens if you feed a string which has no digits, ordinals or operators to be converted?</b> Well we don't touch it
  - 'This is just a random sentence.' --> 'This is just a random sentence.'
  - <b>How to use? </b>
    - ```
      from numwords_to_nums.numwords_to_nums import NumWordsToNum
      scenario = 'This is just a random sentence.'
      num = NumWordsToNum()
      result = num.numerical_words_to_numbers(scenario)
      print(result)
      ```

- #### Convert digits from a random sentence
  <b>Want to convert just the digits from your sentence?</b> It's possible now. Here are a few <b>examples</b>
  - 'I am twenty five years old and my dad is fifty years old. I would like to get my father two cars!' --> 'I am 25 years old and my dad is 50 years old. I would like to get my father 2 cars!'
  - 'Joe Biden became the oldest person to assume the presidency at the age of seventy eight.' --> 'Joe Biden became the oldest person to assume the presidency at the age of 78.'
  - 'The event was held at the U.S. Capitol in Washington, D.C., and was attended by a limited number of people due to the COVID-nineteen pandemic.' --> 'The event was held at the U.S. Capitol in Washington, D.C., and was attended by a limited number of people due to the COVID-19 pandemic.'
  - <b>How to use? </b>
    - ```
      from numwords_to_nums.numwords_to_nums import NumWordsToNum
      scenario = 'Joe Biden became the oldest person to assume the presidency at the age of seventy eight.'
      num = NumWordsToNum()
      result = num.numerical_words_to_numbers(scenario)
      print(result)
      ```

- ####   Large numbers
  <b>Want support for large numbers?</b> Sure, we will support you. <b>We support till quadrillion</b>
  - 'three hundred and forty five' --> '345'
  - 'five thousand three hundred and forty five' --> '5345'
  - 'sixty five thousand and twenty two' --> '65022'
  - 'one hundred thousand and sixty --> '100060'
  - 'ten million seventy thousand' --> '10070000'
  - 'one billion' --> '1000000000'
  - 'ten billion' --> '10000000000'
  - 'hundred billion' --> '100000000000'
  - 'thousand billion' --> '1000000000000'
  - 'one trillion' --> '1000000000000'
  - 'ten trillion' --> '10000000000000'
  - 'hundred trillion' --> '100000000000000'
  - 'thousand trillion' --> '1000000000000000'
  - 'one quadrillion' --> '1000000000000000'
  - 'ten quadrillion' --> '10000000000000000'
  - 'hundred quadrillion' --> '100000000000000000'
  - 'thousand quadrillion' --> '1000000000000000000'
  - 'That will be thousand Rs sir.' --> 'That will be 1000 Rs sir'
  - <b>How to use? </b>
    - ```
      from numwords_to_nums.numwords_to_nums import NumWordsToNum
      scenario = 'five thousand three hundred and forty five'
      num = NumWordsToNum()
      result = num.numerical_words_to_numbers(scenario)
      print(result)
      ```

- ####   Indian numbering system
  <b>Want support for large numbers in Indian scale?</b> Sure, you have it. <b>We support till arab</b>
  - 'one lakh sixty thousand three hundred and twelve' --> '160312'
  - 'ten lakh thirty thousand' --> '1030000'
  - 'hundred lakh five thousand' --> '10005000'
  - 'thousand lakh' --> '100000000'
  - 'one crore two lakh thirty thousand' --> '10230000'
  - 'ten crore' --> '100000000'
  - 'hundred crore' --> '1000000000'
  - 'thousand crore' --> '10000000000'
  - 'one arab' --> '1000000000'
  - 'ten arab' --> '10000000000' 
  - <b>How to use? </b>
    - ```
      from numwords_to_nums.numwords_to_nums import NumWordsToNum
      scenario = 'one crore two lakh thirty thousand'
      num = NumWordsToNum()
      result = num.numerical_words_to_numbers(scenario)
      print(result)
      ```

- ####   Convert ordinals
  <b>Looking for a way to convert ordinal numbers?</b> Sure, you have it.
  - 'His inauguration took place on January twentieth, which marked the fifty ninth quadrennial presidential inauguration.' --> 'His inauguration took place on January 20th, which marked the 59th quadrennial presidential inauguration.'
  - 'Despite the challenges, the fifty ninth presidential inauguration was a historic moment for the country.' --> 'Despite the challenges, the 59th presidential inauguration was a historic moment for the country.'
  - <b>How to use? </b>
    - ```
      from numwords_to_nums.numwords_to_nums import NumWordsToNum
      scenario = 'Despite the challenges, the fifty ninth presidential inauguration was a historic moment for the country.'
      num = NumWordsToNum()
      result = num.numerical_words_to_numbers(scenario)
      print(result)
      ```

- ####   Dates and Years
  <b>Looking to manipulate dates and years?</b> You're in the right place!
  - 'He was elected in November twenty twenty after defeating other contenders' --> 'He was elected in November 2020 after defeating other contenders'
  - 'I was born on first September nineteen ninety five' --> 'I was born on 1st September 1995'
  - 'I was born in two thousand and five and I an twenty five years old' --> 'I was born in 2005 and I an 25 years old'
  - <b>How to use? </b>
    - ```
      from numwords_to_nums.numwords_to_nums import NumWordsToNum
      scenario = 'I was born in two thousand and five and I an twenty five years old'
      num = NumWordsToNum()
      result = num.numerical_words_to_numbers(scenario)
      print(result)
      ```

- ####   Operator Conversion
  <b>Interested in converting operators for your programming needs? Want to display them on UI?</b> Let's dive in!
  - <b>plus</b>
    - 'three plus five' --> '3+5'
  - <b>minus</b>
    - 'three minus five' --> '3-5'
  - <b>multiply</b>
    - 'multiply five by six' --> '5*6'
    - 'five multiplied by six' --> '5*6'
  - <b>divide</b>
    - 'five divided by six' --> '5/6'
    - 'divide five by six' --> '5/6'
  - <b>equals</b>
    - 'five is equal to five' --> '5=5'
    - 'five equals to five' --> '5=5'
    - 'five equal to five' --> '5=5'
    - 'five equal five' --> '5=5'
    - 'five equals five' --> '5=5'
  - <b>not equal</b>
    - 'four is not equal to five' --> '4≠5'
    - 'four is not equal five' --> '4≠5'
    - 'four is not equals five' --> '4≠5'
    - 'four not equal to five' --> '4≠5'
  - <b>less than</b>
    - 'three is less than seven' --> '3<7'
    - 'three less than seven' --> '3<7'
  - <b>greater than</b>
    - 'seven is greater than six' --> '7>6'
    - 'seven greater than six' --> '7>6'
  - <b>less than equal to</b>
    - 'three is less than or equals to three' --> '3≤3'
    - 'three is less than or equal to three' --> '3≤3'
    - 'three is less than equals to three' --> '3≤3'
    - 'three is less than equal to three' --> '3≤3'
    - 'three less than equals to three' --> '3≤3'
    - 'three less than equal to three' --> '3≤3'
  - <b>greater than equal to</b>
    - 'three is greater than or equals to three' --> '3≥3'
    - 'three is greater than or equal to three' --> '3≥3'
    - 'three is greater than equals to three' --> '3≥3'
    - 'three is greater than equal to three' --> '3≥3'
    - 'three greater than equals to three' --> '3≥3'
    - 'three greater than equal to three' --> '3≥3'
  - <b>square root of</b>
    - 'square root of seven' --> '√7'
  - <b>square of</b>
    - 'square of seven' --> '7 ²'
  - <b>percent</b>
    - 'ninety five percent' --> '95%'
  - <b>How to use? </b>
    - ```
      from numwords_to_nums.numwords_to_nums import NumWordsToNum
      scenario = 'ninety five percent'
      num = NumWordsToNum()
      result = num.numerical_words_to_numbers(scenario, convert_operator=True)
      print(result)
      ```

- ####   Operators not with digits?
  <b>Worried what will happen to operators if they are not with digits?</b> Sure, we will take care of your input
  - 'Oxygen plus Hydrogen equals water' --> 'Oxygen plus Hydrogen equals water'
  - <b>Note:</b> We make sure to convert operators when you have digits with them

 

- ####   Decimal numbers
  <b>Want to convert decimal numbers?</b> Sure, why not we support it
    - 'two point five equals two point five' --> '2.5=2.5'
    - 'two point five' --> '2.5'
    - 'The temperature outside is twenty five point five degrees Celsius.' --> 'The temperature outside is 25.5 degrees Celsius.'
  - <b>How to use? </b>
    - ```
      from numwords_to_nums.numwords_to_nums import NumWordsToNum
      scenario = 'The temperature outside is twenty five point five degrees Celsius.'
      num = NumWordsToNum()
      result = num.numerical_words_to_numbers(scenario, convert_operator=True)
      print(result)
      ```
      
- ####   Have your own evaluate function?
  <b>Want to convert operators so that you can pass it to your own evaluate function?</b> Sure, we support it
  - 'four is not equal to five' --> '4!=5'
  - <b>How to use? </b>
    - ```
      from numwords_to_nums.numwords_to_nums import NumWordsToNum
      scenario = 'four is not equal to five'
      num = NumWordsToNum()
      result = num.numerical_words_to_numbers(scenario, convert_operator=True, calculate_mode=True)
      print(result)
      ```
- ####   Expression Evaluation
  <b>Need to evaluate expressions?</b> We'll show you the way.
  - 'one point five plus zero point five' --> '2.0'
  - 'fifty percent of thousand' --> '500.0'
  - 'twenty-five percent of two hundred equals fifty' --> 'True'
  - 'three plus square of five' --> '28'
  - 'square root of four multiplied by square root of one plus six is equal to square root of twenty-five multiplied by three' --> 'False'
  - <b>How to use? </b>
    - ```
      from numwords_to_nums.numwords_to_nums import NumWordsToNum
      scenario = 'three plus square of five'
      num = NumWordsToNum()
      result = num.numerical_words_to_numbers(scenario, convert_operator=True, calculate_mode=True, evaluate=True)
      print(result)
      ```

- ####   Numeric Calculation in Text
  <b>Expressions along with different text?</b> We'll show you the way.
    - 'Hey calculate three plus five' --> '8'
    - 'Hey calculate 3+5' --> '8'
  - <b>How to use? </b>
    - ```
      from numwords_to_nums.numwords_to_nums import NumWordsToNum
      scenario = 'Hey calculate three plus five'
      num = NumWordsToNum()
      result = num.numerical_words_to_numbers(scenario, convert_operator=True, calculate_mode=True, evaluate=True)
      print(result)
      ```
- ####  Handle all patterns at same time
  <b>Sure you can do that.</b> Just go through above examples and you will get the idea


## Improvements or Issues
- Complex arithmetic operations.
- Please email us if you find any issues.

## License
- MIT License

## Contact
- Please mail us if you have any issues.
- Make sure to put subject as --> <b>Improvements for python library</b>

## Acknowledgements
I have heavily used code from the SO answers from here: https://stackoverflow.com/questions/493174/is-there-a-way-to-convert-number-words-to-integers
and improved upon them