class Stack:
    def __init__(self, size, data_type):
        self.size = size
        self.stack = []
        self.data_type = data_type
        self.top_in = -1

    def push(self, element):
        if self.top_in + 2 > self.size:
            print("Stack is full")
        elif self.data_type(element) == element:
            if self.top_in + 1 == len(self.stack):
                self.stack += [self.data_type(element)]
                self.top_in += 1
            else:
                self.top_in += 1
                self.stack[self.top_in] = self.data_type(element)
        else:
            print("Incorrect data type")

    def pop(self):
        if self.top_in == -1:
            return None
        else:
            self.top_in -= 1
            return self.stack[self.top_in+1]

    def is_empty(self):
        if self.top_in == -1:
            return True
        return False

    def top(self):
        if self.top_in == -1:
            return None
        else:
            return self.stack[self.top_in]

    def print_stack(self):
        print(self.stack[0:self.top_in+1])


operators = ('+', '-', '*', '/', '(', ')', ',')
operators_value = {'+': 2, '-': 2, '/': 1, '*': 1}


def isNumber(ch):
    is_digit = False
    is_dot = False
    if ch[-1] == '.':
        return False
    for i in range(len(ch)):
        if ch[i].isdigit():
            is_digit = True
        if ch[i] == '-' and i != 0:
            return False
        if ch[i] == '.' and not is_digit:
            return False
        if ch[i] == '.' and is_dot:
            return False
        if ch[i] != '-' and not ch[i].isdigit() and ch[i] != '.':
            return False
        if ch[i] == '.':
            is_dot = True
    if not is_digit:
        return False
    return True


def get_input(string_f, user_input):
    global operators
    is_last_space = True
    j = 0
    open_paran = 0
    closed_paran = 0
    for i in range(len(user_input)):
        if ord(user_input[i]) != 32:
            if user_input[i] == '(':
                open_paran += 1
            if user_input[i] == ')':
                closed_paran += 1
            if user_input[i] in operators or isNumber(user_input[i]) or user_input[i] == '.':
                if is_last_space:
                    if user_input[i] == '.':
                        return 'error'
                    string_f.push(user_input[i])
                    is_last_space = False
                else:
                    if string_f.top_in >= j:
                        string_f.stack[j] += user_input[i]
                    else:
                        string_f.push(user_input[i])
        else:
            is_last_space = True
            j += 1
    if closed_paran != open_paran:
        return 'error'


def toPostfix(stack):
    global operators, operators_value
    operators_temp = Stack(100, str)
    result = Stack(100, str)
    operators_temp.push('(')
    j = 0

    while j < len(stack.stack):
        popped = stack.stack[j]

        if isNumber(popped):
            result.push(popped)
        elif popped == '(':
            operators_temp.push('(')
        elif popped == ')':
            temp = operators_temp.pop()
            while temp != '(':
                result.push(temp)
                temp = operators_temp.pop()
        elif popped in operators:
            if operators_temp.top() != '(' and operators_temp.top != ')':
                if operators_value[popped] <= operators_value[operators_temp.top()]:
                    result.push(operators_temp.pop())
                    operators_temp.push(popped)
                else:
                    operators_temp.push(popped)
            else:
                operators_temp.push(popped)
        j += 1

    popped = operators_temp.pop()
    while len(operators_temp.stack) != 0 and popped != '(':
        result.push(popped)
        popped = operators_temp.pop()

    return result


def postfix_calc(stack, type_of_data):
    temp_stack = Stack(100, type_of_data)
    for i in range(len(stack.stack)):
        if isNumber(stack.stack[i]):
            temp_stack.push(type_of_data(stack.stack[i]))
        else:
            if temp_stack.is_empty():
                return 'error'
            a = temp_stack.pop()
            if temp_stack.is_empty():
                return 'error'
            b = temp_stack.pop()
            match stack.stack[i]:
                case '+':
                    temp_stack.push(a + b)
                case '-':
                    temp_stack.push(b - a)
                case '*':
                    temp_stack.push(a * b)
                case '/':
                    temp_stack.push(b / a)
    if temp_stack.top_in == 0:
        return temp_stack.top()
    else:
        return 'error'


s = Stack(30, str)
input = input()
print(str(input))
is_error = get_input(s, str(input))

if not is_error:
    print(s.stack)

    s = toPostfix(s)

    print(s.stack)

    value = postfix_calc(s, float)
    if value != 'error':
        print(f"The result: {value}")
