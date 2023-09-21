# parspy
A tool to parse text into a list where it can be interpreted and executed.
## Install
Install using `pip install parspy`.
## Usage
First, import and initiate the class:
```python
import re
import parspy
parsertool = parspy.Parser()
```
Then, add elements to the alphabet:
```python
parsertool.addelems("ad", "bc", " ")
```
If you have things more complicated than static elements, use the `setregelems` method by feeding it compiled regex objects:
```python
parsertool.setregelems(number = re.compile("Number: \d+"), string = re.compile("String: '.*'"))
```
But what use is this without using it to parse something? None. Here is how you parse a string with this:
```python
parsertool.parse("adbcbcbcad  Number: 123      String: 'banana!'")
```
The output should be:
```python
['ad', 'bc', 'bc', 'bc', 'ad', ' ', ' ', {'number':'Number: 123'}, ' ', ' ', ' ', ' ', ' ', ' ', {'string':"String: 'banana!'"}]
```
Now you can pass this into a program where it can be processed more easily.

If something goes wrong during parsing, a `ParseError` will be thrown.
## Notes
It seems to have an issue when executing in a REPL environment (`name 're' is not defined`).
