"""

Setup

Most of us learn how to do math with operators in between numbers. For example:

`(((4 * 3) + 1) - 2) = 11`

You have an operator like `+ - * /`, and numbers (“operands”) on each side of the operator, and you apply the operator to those operands. If you have multiple expressions, you resolve them according to some order of operations (or forcing the order using parenthesis). This way of doing math uses infix notation — the operators are in between the operands.

There’s another way of doing math that uses postfix notation — the operators come after the operands. This is a cool way of doing math — you don’t need parenthesis or rules to describe the order of operations, so it’s easier to parse a math expression, and you can use a stack to manage the calculation (using the stack data structure in the real world!).

Let’s build a basic postfix notation calculator.

What to implement

Write a function that takes as an argument a string containing a mathematical expression in postfix notation, using as available operators `+ - * /`. The function should return the result of evaluating that expression.

Example algorithm

The postfix notation version of `(((4 * 3) + 1) - 2)` is:

`1 3 4 * + 2 -`

Here’s how the stack evolves while evaluating this expression:

| Token                        | Stack                                                                                                         |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------- |
| Before processing any tokens | [] // initially empty                                                                                         |
| 1                            | [1] // Push the operand onto the stack                                                                        |
| 3                            | [1, 3] // Push the operand onto the stack                                                                     |
| 4                            | [1, 3, 4]  // Push the operand onto the stack                                                                 |
| *                            | [1, 12] // Pop the last 2 operands off the stack, apply the operator, and push the result back onto the stack |
| +                            | [13] // Pop the last 2 operands off the stack, apply the operator, and push the result back onto the stack    |
| 2                            | [13, 2] // Push the operand onto the stack                                                                    |
| -                            | [11] // Pop the last 2 operands off the stack, apply the operator, and push the result back onto the stack    |

Example inputs and outputs

| Input           | Output                                           |
| --------------- | ------------------------------------------------ |
| “1 3 4 * + 2 -" | 11                                               |
| “3 2 1 + + 2 /” | 3                                                |
| “2 +”           | <raise an error, this is a malformed expression> |

Once you have a working implementation:

- What edge cases would you need to handle to have a robust calculator?


pseudocode:

create a stack
split the string input so each item is in a list
loop through list
if element in list is a number
	 add/push it to the stack
if element is not a number (an operand)
	pop from the end of the stack- put that number on the right side of the operator
	pop from the end of the stack again- put that number on the left side of the operator
	push the result of that expression to the stack
when the list is empty
return the one remaining number in the stack
"""

def evaluate_postfix(s):

    num_stack = []
    s = s.split()

    for element in s:
        try:
        # if element.isdigit():
            num_stack.append(float(element))
        except ValueError:
            b = num_stack.pop()
            a = num_stack.pop()

            if element == '+':
                num_stack.append(a + b)
            elif element == '-':
                num_stack.append(a - b)
            elif element == '*':
                num_stack.append(a * b)
            elif element == '/':
                num_stack.append(a / b)
            else:
                print('Error, please check input')
                raise f'bad input + {element}'
    return num_stack.pop()
print(evaluate_postfix('1 3 4 * + 2 -'))