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
def calc(value1, value2, operation ="multiply"):
    result = None
    try:
        num1 = float(value1)
        num2 = float(value2)
        int_num1 = int(value1)
        int_num2 = int(value2)
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
            result = int_num1 // int_num2
        elif operation == "power":
            result = num1 ** num2
    except ZeroDivisionError:
        return ("You can't divide by 0!")
    except ValueError:
        return ("You can't multiply those values!")
    else:
        return result

print("\nOutput of task 3")            
print(calc(2,0, "divide"))
print(calc(2,4, "add"))
print(calc(2,"test", "multiply"))
print(calc(8,0, "int_divide"))

# Task 4
def data_type_conversion(value, datatype):
    try:
        result = None
        if datatype == "int":
            result = int(value)
        elif datatype == "float":
            result = float(value)
        elif datatype == "str":
            result = str(value)
        
    except Exception as e:
        return (f"You can't convert {value} into a {datatype}.")
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
        elif result >= 80:
           grade_letter = "B"
        elif result >= 70:
            grade_letter = "C"
        elif result >= 60:
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
    num_values = [v for v in kwargs.values()]
    avg_val = sum(num_values) / len(num_values)

    if position == "best":
        return max_key
    elif position == "mean":
        return avg_val
    else:
        return ("Invalid position!, Enter 'best' or 'mean'")

print("\nOutput of task 7")
print(student_scores("best",Roopa=80, Jeniffer=78, Nancy=85))
print(student_scores("mean",Roopa=80, Jeniffer=79, Nancy=85))

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

def pig_latin(word):
    vowels = "aeiou"
    word = word.lower()

    # Rule 1: Starts with a vowel
    if word[0] in vowels:
        return word + "ay"

    # Rule 3: Special case for 'qu'
    if word.startswith("qu"):
        return word[2:] + "quay"

    # Rule 2: Starts with consonant(s)
    for i, letter in enumerate(word):
        # Handle 'qu' inside consonant cluster
        if letter in vowels:
            if word[i-1:i+1] == "qu":
                return word[i+1:] + word[:i+1] + "ay"
            return word[i:] + word[:i] + "ay"

    return word

print("\nOutput of task 10")
print(pig_latin("apple"))
print(pig_latin("square"))
print(pig_latin("queen"))
print(pig_latin("student"))