# Task 1
def hello():
    return "Hello!"

print("Output of task 1")    
print(hello())

# Task 2
def greet(name):
    return f"Hello, {name}!"
    
print("\nOutput of task 2")
print(greet("Roopa"))

# Task 3
def calc(num1, num2, operation ="multiply"):
    result = None
    try:
        if operation == "add":
            result = num1 + num2 #adding the numbers
        elif operation == "subtract":
            result = num1 - num2 #subtracting numbers
        elif operation == "multiply":
            result = num1 * num2 
        elif operation == "divide":
            result = num1 / num2
        elif operation == "modulo":
            result = num1 % num2
        elif operation == "int_divide":
            result = num1 // num2
        elif operation == "power":
            result = num1 ** num2
    except ZeroDivisionError:
        return ("You can't divide by 0!")
    except Exception as e:
        return ("You can't multiply those values!")
    else:
        return result

print("\nOutput of task 3")            
print(calc(2,4, "divide"))

# Task 4
def data_type_conversion(value, type):
    try:
        result = None
        if type == "int":
            result = int(value)
        elif type == "float":
            result = float(value)
        elif type == "str":
            result = str(value)
        
    except Exception as e:
        return (f"You can't convert {value} into a {type}.")
    else:
        return result

print("\nOutput of task 4")
print(data_type_conversion(55.88, "int"))

#Task 5
def grade(*args):
    grade_letter = ""
    try:
        result = sum(args)/len(args)
        if result >= 90:
            grade_letter = "A"
        elif result >= 80 and result <= 89:
           grade_letter = "B"
        elif result >= 70 and result <= 79:
            grade_letter = "C"
        elif result >= 60 and result <= 69:
            grade_letter = "D"
        elif result < 60:
            grade_letter = "F"
    except Exception as e:
        return ("Invalid data was provided.")
    
    return grade_letter

print("\nOutput of task 5")
print(grade(90,92,88,95))

# Task 6
def repeat(string, count):
    repeat_string = ""
    for i in range(count):
        repeat_string += string
    return repeat_string

print("\nOutput of task 6")        
print(repeat("Python",4))

# Task 7
def student_scores(position, **kwargs):
    max_key = max(kwargs, key=kwargs.get)
    num_values = [v for v in kwargs.values() if isinstance(v, (int,float))]
    avg_val = sum(num_values) / len(num_values)
    
    if position == "best":
        return max_key
    elif position == "mean":
        return avg_val
    else:
        return ("Invalid position!, Enter 'best' or 'mean'")

print("\nOutput of task 7")
print(student_scores("best",Roopa=80, Jeniffer=78, Nancy=85))

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
    words = sentence.lower().split()
    result = []
    #word = word.lower()

    for word in words:
        if word in vowels:
            result.append(word +"ay")
            
        if word.startswith("qu"):
            result.append(word[2:] + "quay")

        for i, letter in enumerate(word):
            if letter in vowels:
                if word[i-1:i+1] == "qu":
                    result.append(word[i+1:] + word[:i+1] + "ay")
        result.append(word[i:] + word[:i] + "ay")

    return " ".join(result)

print("\nOutput of task 10")
print(pig_latin("testing the pig latin game in the square"))