class py_solution:
   def is_valid_parenthese(self, s):

        stack, para = [], {"(": ")", "{": "}", "[": "]"}
        for parenthese in s:
            if parenthese in para:
                stack.append(parenthese)
            elif len(stack) == 0 or para[stack.pop()] != parenthese:
                return False
                
        return len(stack) == 0

print(py_solution().is_valid_parenthese("(){}[]"))
print(py_solution().is_valid_parenthese("()[{)}"))
print(py_solution().is_valid_parenthese("()"))