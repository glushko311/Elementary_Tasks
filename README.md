Python Elementary tasks from Soft Serve course

use Python version 3.6 or higher



                    UNITTESTS
To use unittests you need install parameterized
pip install parameterized

to start all unittests use:
python -m  unittest tests/test_start.py

to start single use one of:
python -m  unittest tests/chess_board_tests.py
python -m  unittest tests/envelope_test.py
python -m  unittest tests/fibonachi_tests.py
python -m  unittest tests/sequence_tests.py
python -m  unittest tests/test_file_handler.py
python -m  unittest tests/triangular_tests.py
python -m  unittest tests/ticket_handler_tests.py



                    APPLICATIONS START


CHESS_BOARD - there is a console application.
It can draw chess board n x m with symbols " " and "*"

for start use:
python chess_board.py 9 8
-------------------------------------------------------------
ENVELOPE - there is a console application.
It is check can envelope 1 contain envelope 2 or opposite.

for start use:
python envelope.py
-------------------------------------------------------------
TRIANGULAR - there is console application.
It can get data from user convert them into triangle objects
put them into list, sort list an print

for start use:
python triangular.py
-------------------------------------------------------------
FILE HANDLER - there is console application.
Count how many substrings in txt file or
replace one substring to another

for start use:
python file_handler.py test/test.txt kad
python file_handler.py test/test.txt kad mab
-------------------------------------------------------------
NUMBER_TRANSLATOR - there is console application.
It convert number into text appearance
Need to use parameter - a number.
Max number it can process (10**102)-1

for start use:
python number_translator.py 3232002
-------------------------------------------------------------
TICKET_HANDLER - There is console application.
It calculate number of happy tickets
You should input file path with mark of
algorithm("Moskow" or "Piter")for test use
data/mosk.txt and data/piter.txt
You can input tickets manually or load them from file or input
max and min value of ticket and tickets will be generated
for test use file data/tickets.txt

for start use:
python ticket_handler.py
-------------------------------------------------------------
SQUARE_SEQUENCE - There is console application.
Display sequence from 1 to number if number**2 less then parameter

for start use:
python square_sequence.py 54
-------------------------------------------------------------
FIBONACHI - There is console application.
It should be started with two parameters min and max
It calculate fibonachi numbers between min and max
and print they.

for start use:
python fibonachi.py 134 555
