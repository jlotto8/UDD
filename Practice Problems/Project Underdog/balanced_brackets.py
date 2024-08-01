
"""
Given a string of different bracket types (parentheses, square brackets, and curly braces), write a function that returns whether or not the string is balanced.

The string is balanced if each opening bracket is followed by a corresponding close bracket, and all brackets between those open and close brackets are also balanced.

Examples of balanced strings

- `{[()]}`
- `{}[]()`
- `[(){()}]`

Examples of unbalanced strings

- `{[(])}` // Has a `]` before the `(` was closed with a `)`
- `{}][()` // Has a `]` without a preceding `[`
- `[(){()}` // Missing a closing `]`

Example function calls

- `checkBrackets("{[()]}") → True`
- `checkBrackets("{}][()") → False`

"""
def checkBrackets(s):
    # Dictionary to keep track of matching brackets
    bracket_pairs = {')': '(', ']': '[', '}': '{'}
    
    # Initialize an empty stack
    stack = []
    
    # Iterate through each character in the string
    for char in s:
        if char in bracket_pairs.values():
            # If the character is an opening bracket, push it onto the stack
            stack.append(char)
        elif char in bracket_pairs.keys():
            # If the character is a closing bracket
            if stack == [] or bracket_pairs[char] != stack.pop():
                # Check if the stack is empty or the top of the stack does not match
                return False
        else:
            # Ignore any non-bracket characters (optional based on problem constraints)
            continue
    
    # If the stack is empty, all brackets were matched; otherwise, they were not
    return stack == []

# Example function calls
assert (checkBrackets("{[()]}"))  # Should return True
assert not (checkBrackets("{}][()"))  # Should return False
assert (checkBrackets("[(){()}]"))  # Should return True
assert not (checkBrackets("{[(])}"))  # Should return False
assert not (checkBrackets("[(){()}"))  # Should return False

