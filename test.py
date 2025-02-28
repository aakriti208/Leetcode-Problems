def dfa_accepts(string):
    states = {'q0', 'q1', 'q2'}
    alphabet = {'a', 'b', '0', '1'}
    
    initial_state = 'q0'
    accept_state = {'q2'}

    transitions = {
        ('q0', '0'): 'q0',
        ('q0', '1'): 'q0',
        ('q0', 'a'): 'q0',
        ('q0', 'b'): 'q1',
        ('q1', '0'): 'q2',
        ('q1', '1'): 'q0',
        ('q1', 'a'): 'q0',
        ('q1', 'b'): 'q1',
        ('q2', '0'): 'q2',
        ('q2', '1'): 'q2',
        ('q2', 'a'): 'q2',
        ('q2', 'b'): 'q2',
    }

    current_state = initial_state

    for symbol in string:
        if (current_state, symbol) in transitions:
            current_state = transitions[(current_state, symbol)]
        else:
            return "Rejected"

    if current_state in accept_state:
        return "Accepted"
    else:
        return "Rejected"

input_string = input("Enter a string: ")
print(dfa_accepts(input_string))
