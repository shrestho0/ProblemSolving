



# # def neat_breacket(brackets):
# #     if brackets[0] == ')' or brackets[-1] == '(': return "No"
# #     return "Yes" if brackets.count('(') == brackets.count(')') else "No"
# # print(neat_breacket(input()))
# # print(neat_breacket("((()("))
# # print(neat_breacket("((()()))"))



# def neat_breacket(brackets):
#     brackets = [x for x in brackets if x in '()']
#     if brackets[0] == ')' or brackets[-1] == '(': return "No"
#     remaining_brackets = []
#     for bracket in brackets:
#         if bracket == '(':
#             remaining_brackets.append('(')
#         elif bracket == ')':
#             remaining_brackets.pop()

#     return "No" if remaining_brackets else "Yes"
 
# print(neat_breacket(input()))
# print(neat_breacket("((()("))
# print(neat_breacket("((()()))"))




class Stack:
    def __init__(self) -> None:
        self.elems = []

    def push(self, elem):
        self.elems.append(elem)

    def pop(self):
        self.elems.pop()

    def is_empty(self):
        return self.elems == []
        
    def peek(self):
        if not self.is_empty():
            return self.elems[-1]

    def get_stack(self):
        return self.elems
        
    def __str__(self):
        return str(self.elems)


def is_match(opening, closing) -> bool:
    if opening == '(' and closing == ')': return True
    if opening == '{' and closing == '}': return True
    if opening == '[' and closing == ']': return True
    return False
    
def is_bracket_balanced(brackets: str) -> bool:
    if brackets == '': return "No"
    balanced_brackets = Stack()
    
    for bracket in brackets:
        if bracket in ('(', '{', '['): 
            balanced_brackets.push(bracket)
        else:
            if bracket in (')', '}', ']'):
                if balanced_brackets.is_empty(): return "No"
                else:
                    if is_match(balanced_brackets.peek(), bracket): balanced_brackets.pop()

    return "Yes" if balanced_brackets.is_empty() else "No"



print(is_bracket_balanced(input()))