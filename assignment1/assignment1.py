# Task 1
def hello():
    print("Hello!")

print("Output of task 1")    
hello()

# Task 2
def greet(name):
    print(f"Hello, {name}!")
    
print("\nOutput of task 2")
greet("Roopa")

# Task 3
def calc(num1, num2, operation ="multiply"):
    try:
        if operation == "addition":
            result = num1 + num2 #adding the numbers
        elif operation == "subtraction":
            result = num1 - num2 #subtracting numbers
        elif operation == "multiply":
            result = num1 * num2 
        elif operation == "division":
            result = num1 / num2
        elif operation == "modulo":
            result = num1 % num2
        elif operation == "int_dividision":
            result = num1 // num2
        elif operation == "power":
            result = num1 ** num2
    except ZeroDivisionError:
        print("Error: You can't divide by 0")
    except Exception as e:
        print(f"Error: You can't {operation} those values!")
    else:
        print(f"The {operation} of {num1} & {num2} is: {result}")

print("\nOutput of task 3")            
calc(2,"test", "division")

# Task 4
def data_type_conversion(value, datatype):
    try:
        result = datatype(value)
    except Exception as e:
        print(f"You can't convert {value} into a {datatype}")
    else:
        print(f"The {type(value)} {value} converted to {datatype} is: {result}")

print("\nOutput of task 4")
data_type_conversion(67, str)

#Task 5
def grade(*args):
    try:
        result = sum(args)
        if result >= 90:
            print("The grade is: A")
        elif result >= 80 and result <= 89:
            print("The grade is: B")
        elif result >= 70 and result <= 79:
            print("The grade is: C")
        elif result >= 60 and result <= 69:
            print("The grade is: D")
        elif result < 60:
            print("The grade is: F")
    except Exception as e:
        print("Error: Invalid data was provided.")

print("\nOutput of task 5")
grade(10,24,25,18)

# Task 6
def repeat(string, count):
    for i in range(count):
        print(string)

print("\nOutput of task 6")        
repeat("Python",4)

# Task 7
def student_scores(position, **kwargs):
    max_val = max(kwargs, key=kwargs.get)
    min_val = min(kwargs, key=kwargs.get)
    if position == "best":
        print(max_val)
    elif position == "mean":
        print(min_val)

print("\nOutput of task 7")
student_scores("mean",Roopa=80, Dai=78)

# Task 8
def titleize(text):
    words = text.strip().split()
    little_words = {"a", "on", "an", "the", "of", "and", "is", "in"}
    last_index = len(words) -1
    result = []
    
    for i, word in enumerate(words):
        lower_word = word.lower()
        
        if i == 0 or i == last_index:
            result.append(lower_word.capitalize())
        elif lower_word not in little_words:
            result.append(lower_word.capitalize())
        else:
            result.append(lower_word)
    
    return " ".join(result)

print("\nOutput of task 8")
print(titleize("the lord of the rings"))

# Task 9
def hangman(secret, guess):
    result = []
    
    for i in secret:
        if i in guess:
           result.append(i)
        else:
            result.append("_")
    return "".join(result)
            
print("\nOutput of task 9")
print(hangman("alphabet","ab"))

# Task 10
def pig_latin(sentence):
    vowels = "aeiou"
    words = sentence.split()
    result = []

    for word in words:
        if word[0] in vowels:
            result.append(word + "ay")
        elif word.startswith("qu"):
            result.append(word[2:] + "quay")
        else:
            consonants = ""
            rest = word

            while rest[0] not in vowels:
                consonants += rest[0]
                rest = rest[1:]

            result.append(rest + consonants + "ay")

    return " ".join(result)

print("\nOutput of task 10")
print(pig_latin("testing the pig latin game"))