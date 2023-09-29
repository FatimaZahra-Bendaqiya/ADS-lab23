# ADS-lab23 in Politechnika Łódzka

Exercise 1 (Stack and RPN)
1. Implement a stack using an array. Your program should implement the following functions: push(), pop() (returning the popped element), isempty() and top(). You should construct your stack, declaring the data type (int or float) and maximum stack size.

2. You are given an expression in infix (standard) notation. The possible tokens (separated by spaces) are:
Operators: +, -, *, /
Parentheses: (, )
Numbers: Positive or negative integers or floats.
The problem with these expressions is that someone reversed the priority of mathematical operations as we know it, so they thought that addition and subtraction is executed before multiplication and division. Using your stack, convert it to postfix notation correcting this mistake. For example:
3 + 6 * 2 -> 3 6 + 2 *

3. Having converted the expressions to postfix notation, write a part of the program that evaluates them. Your program should take erroneous expressions as input and print the value.
Then, evaluate the following expressions:
( 3 * 6 + 2 ) + ( 14 / 3 + 4 ) = 26
17 * ( 2 + 3 ) + 4 + ( 8 * 5 ) = 833
   
Exercise 2 (Palindromes)
Implement a singly linked list. You should be able to insert a given string of characters into your list, where each character is a separate list element. Then, using previously implemented stack, check if this string is a palindrome.
Evaluate your program on the following expression:
12203022, 3120213
