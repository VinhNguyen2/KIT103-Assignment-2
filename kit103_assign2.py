'''
KIT103/KMA155 Programming Assignment 2: Logic
Submission script

Name: Vinh Nguyen
ID: 470821

Enter your answers to each question below by completing each function
or, in the case of Question 4a, filling in the Karnaugh map.
After answering a question run this script and test your implementation.
'''

# Question 1: Bolt Quality Assurance

PASS, REJECT, IKEA = 'Pass', 'Reject', 'Send to IKEA'

def q1_bolt_check(strength, diameter_error, ikea_near):
    '''Returns one of three string messages depending on whether a
    bolt is of acceptable quality or not.
    Parameters:
    strength - the bolt's tensile strength in MPa
    diameter_error - the bolt's diameter variation in micrometres
    ikea_near - True iff there is an IKEA near the factory
    '''
    if strength >= 310 and diameter_error <= 100 :
        
        return PASS
    if not (strength >= 310 and diameter_error <= 100) and \
            (diameter_error < 200) and (ikea_near != False) :
                
        return IKEA
    else:
        
        return REJECT


# Question 2: Implementing predicates as functions

def q2_a(a, b, c, d):
    return (not a and not b and not c) or d

def q2_b(a, b):
    return (a or b) and (not a or not b)

def q2_c(a):
    return a or not a

def q2_d(a, b, c):
    return (a and b) or (b and c)


# Question 3: Simplifying predicates

def q3_a(a, b, c, d):
    return not(a or b or c) or d

def q3_b(a, b):
    return (not a and b) or (a and not b)

def q3_c(a):
    return True

def q3_d(a, b, c):
    return b and (a or c)


# Question 4: Simplifying a predicate using a Karnaugh map

#Part a: Digit Detector Karnaugh Map --- replace the appropriate 0 entries with 1 (representing True)
q4_kmap = [
#cd\ab
    [0, 0, 0, 0],
    [0, 1, 1, 1],
    [0, 0, 1, 1],
    [0, 1, 0, 0]
]

#Part b: The detector function
def q4_acme_digit_detector(a, b, c, d):
    '''Returns True iff the curves present resemble a digit, False otherwise.'''
    #Your task is to replace this with an equivalent but simpler expression.
    # If you wish to split your expression over multiple lines then use a
    # slash \ at the end of each line, as below.
    return (a and d) or ( b and not c and d) or \
            (not a and b and c and not d)

#End of answers
