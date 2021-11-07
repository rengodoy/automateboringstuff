"""
Regular expressions are mini-language for specifying text patterns. Writing code to do pattern matching without regular expressions is a huge pain.
Regex strings often use backslashes (like \d), so they are often written using raw strings: r'\d'
\d is the regex for a numeric digit character.
Import the re module first.
Call the re.compile() function to create a regex object.
Call the regex object's search() method to create a match object.
Call the match object's group() method to get the matched string.

Groups are created in regex strings with parentheses.
The first set of parentheses is group 1, the second is 2, and so on.
Calling group() or group(0) returns the full matching string, group(1) returns group 1's matching string, and so on.
Use \( and \) to match literal parentheses in the regex string. >>> batRegex = re.compile(r'Bat(man|mobile|copter)')
The | pipe can match one of many possible groups.


The ? says the group matches zero or one times.
The * says the group matches zero or more times.
The + says the group matches one or more times.
The curly braces can match a specific number of times.
The curly braces with two numbers matches a minimum and maximum number of times.
Leaving out the first or second number in the curly braces says there is no minimum or maximum.
"Greedy matching" matches the longest string possible, "nongreedy matching" (or "lazy matching") matches the shortest string possible.
Putting a question mark (?) after the curly braces makes it do a nongreedy/lazy match.

The regex method findall() is passed a string, and returns all matches in it, not just the first match.
If the regex has 0 or 1 group, findall() returns a list of strings.
If the regex has 2 or more groups, findall() returns a list of tuples of strings.
\d is a shorthand character class that matches digits. \w matches "word characters" (letters, numbers, and the underscore). \s matches whitespace characters (space, tab, newline).
The uppercase shorthand character classes \D, \W, and \S match charaters that are not digits, word characters, and whitespace.
You can make your own character classes with square brackets: [aeiou]
A ^ caret makes it a negative character class, matching anything not in the brackets: [^aeiou]

\d Any numeric digit from 0 to 9
\D Any character that is not a numeric digit from 0 to 9
\w Any letter, numeric digit, or the underscore character. (Think of this as matching "word" characters.)
\W Any character that is not a letter, numeric digit, or the underscore character.
\s Any space, tab, os new line character. (Think of this as matching "space" characters)
\S Any character that is not a space, tab or new line.

^ means the string must start with pattern, $ means the string must end with the pattern. Both means the entire string must match the entire pattern.
The . dot is a wildcard; it matches any character except newlines.
Pass re.DOTALL as the second argument to re.compile() to make the . dot match newlines as well.
Pass re.I as the second argument to re.compile() to make the matching case-insensitive.

Using '.*' exemple:
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
nameRegex.findall('First Name: Al Last Name: Sweigart')
[('Al', 'Sweigart')]

The sub() regex method will substitute matches with some other text.
Using \1, \2 and so will substitute group 1, 2, etc in the regex pattern.
Passing re.VERBOSE lets you add whitespace and comments to the regex string passed to re.compile().
If you want to pass multiple arguments (re.DOTALL , re.IGNORECASE, re.VERBOSE), combine them with the | bitwise operator.

Practice Projects

For practice, write programs to do the following tasks.
Date Detection

Write a regular expression that can detect dates in the DD/MM/YYYY format. Assume that the days range from 01 to 31, the months range from 01 to 12, and the years range from 1000 to 2999. Note that if the day or month is a single digit, it’ll have a leading zero.

The regular expression doesn’t have to detect correct days for each month or for leap years; it will accept nonexistent dates like 31/02/2020 or 31/04/2021. Then store these strings into variables named month, day, and year, and write additional code that can detect if it is a valid date. April, June, September, and November have 30 days, February has 28 days, and the rest of the months have 31 days. February has 29 days in leap years. Leap years are every year evenly divisible by 4, except for years evenly divisible by 100, unless the year is also evenly divisible by 400. Note how this calculation makes it impossible to make a reasonably sized regular expression that can detect a valid date.
Strong Password Detection

Write a function that uses regular expressions to make sure the password string it is passed is strong. A strong password is defined as one that is at least eight characters long, contains both uppercase and lowercase characters, and has at least one digit. You may need to test the string against multiple regex patterns to validate its strength.
Regex Version of the strip() Method

Write a function that takes a string and does the same thing as the strip() string method. If no other arguments are passed other than the string to strip, then whitespace characters will be removed from the beginning and end of the string. Otherwise, the characters specified in the second argument to the function will be removed from the string.

"""
