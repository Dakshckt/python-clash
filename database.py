LESSON_STAGE_1 = [
    "Variables store data values that can be used or changed later.",
    "They hold different types of data like numbers, text, or lists.",
    "Multiple variables can be declared in a single line",
    "Must start with a letter or underscore (_) ",
    "Ex: player_name = `Hero1` score = 100  ",
]

LESSON_STAGE_2 = [
    "Functions group reusable code into a single unit.",
    "They can accept parameters and return values.",
    "Use 'def' keyword to declare a function.",
    "Functions improve code readability and reduce repetition.",
    "Ex: def greet(name): return 'Hello ' + name"
]

LESSON_STAGE_3 = [
    "Loops repeat a block of code multiple times.",
    "For loops iterate over a sequence of items.",
    "While loops repeat until a condition is False.",
    "Break and continue control the loop flow.",
    "Ex: for i in range(5): print(i)"
]

MCQ_STAGE_1 = [
    {
        "question": "What is the primary purpose of variables in Python?",
        "options": ["(A) Perform mathematical operations", 
                    "(B) Store and manage data values", 
                    "(C) Display text on the screen", 
                    "(D) Create loops"],
        "answer": "(B)"
    },
    {
        "question": "Which of the following is a valid variable name?",
        "options": ["(A) 1player", 
                    "(B) player_name", 
                    "(C) player-name", 
                    "(D) player name"],
        "answer": "(B)"
    },
    {
        "question": "What type of data can variables hold?",
        "options": ["(A) Numbers", 
                    "(B) Text", 
                    "(C) Lists", 
                    "(D) All of the above"],
        "answer": "(D)"
    },
    {
        "question": "How do you declare multiple variables in a single line?",
        "options": ["(A) var1 = 10; var2 = 20", 
                    "(B) var1, var2 = 10, 20", 
                    "(C) var1 = 10, var2 = 20", 
                    "(D) var1 = 10 var2 = 20"],
        "answer": "(B)"
    },
    {
        "question": "Which symbol is used to start a variable name, other than a letter?",
        "options": ["(A) #", 
                    "(B) _ (underscore)", 
                    "(C) - (hyphen)", 
                    "(D) @"],
        "answer": "(B)"
    },
    {
        "question": "Which of the following is a correct variable declaration?",
        "options": ["(A) player-score = 100", 
                    "(B) player name = 'Hero1'", 
                    "(C) player_name = 'Hero1'", 
                    "(D) 1player = 'Hero1'"],
        "answer": "(C)"
    },
    {
        "question": "What is the value of `score` in the following declaration?\nplayer_name = 'Hero1'  score = 100",
        "options": ["(A) 'Hero1'", 
                    "(B) 100", 
                    "(C) player_name", 
                    "(D) None"],
        "answer": "(B)"
    },
    {
        "question": "What is an invalid variable name?",
        "options": ["(A) _player", 
                    "(B) score100", 
                    "(C) 100score", 
                    "(D) player_score"],
        "answer": "(C)"
    },
    {
        "question": "What type of data is stored in the following variable?\nplayer_name = 'Hero1'",
        "options": ["(A) Integer", 
                    "(B) String", 
                    "(C) List", 
                    "(D) Float"],
        "answer": "(B)"
    },
    {
        "question": "Which statement about variables is true?",
        "options": ["(A) Variables must start with a number", 
                    "(B) Variables can only hold text values", 
                    "(C) Variables store data values that can be used or changed later", 
                    "(D) Variables cannot be declared in a single line"],
        "answer": "(C)"
    }
]

MCQ_STAGE_2 = [
    {
        "question": "What is the main purpose of functions in Python?",
        "options": ["(A) Store values permanently", 
                    "(B) Group reusable code into a single unit", 
                    "(C) Execute code only once", 
                    "(D) Display variables"],
        "answer": "(B)"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["(A) def", 
                    "(B) func", 
                    "(C) define", 
                    "(D) fn"],
        "answer": "(A)"
    },
    {
        "question": "What is the term for the values passed to a function?",
        "options": ["(A) Variables", 
                    "(B) Parameters", 
                    "(C) Constants", 
                    "(D) Arguments"],
        "answer": "(B)"
    },
    {
        "question": "What is the purpose of the 'return' statement in a function?",
        "options": ["(A) End the function execution", 
                    "(B) Return a value from the function", 
                    "(C) Print a message", 
                    "(D) Repeat the function call"],
        "answer": "(B)"
    },
    {
        "question": "Which of the following is a valid function declaration?",
        "options": ["(A) function greet(name):", 
                    "(B) def greet(name):", 
                    "(C) func greet(name):", 
                    "(D) declare greet(name):"],
        "answer": "(B)"
    },
    {
        "question": "What will be the output of the following function?\n\ndef add(x, y):\n    return x + y\n\nprint(add(5, 3))",
        "options": ["(A) 8", 
                    "(B) 53", 
                    "(C) 15", 
                    "(D) Error"],
        "answer": "(A)"
    },
    {
        "question": "What happens if a function doesn't have a return statement?",
        "options": ["(A) It returns `None`", 
                    "(B) It throws an error", 
                    "(C) It returns 0", 
                    "(D) It automatically prints the output"],
        "answer": "(A)"
    },
    {
        "question": "Which of the following is NOT a valid function name?",
        "options": ["(A) my_function", 
                    "(B) func1", 
                    "(C) 1function", 
                    "(D) myFunction"],
        "answer": "(C)"
    },
    {
        "question": "What is the output of the following function?\n\ndef greet():\n    print('Hello')\n\nprint(greet())",
        "options": ["(A) Hello", 
                    "(B) None", 
                    "(C) Hello followed by `None`", 
                    "(D) Error"],
        "answer": "(C)"
    },
    {
        "question": "Which statement is true about functions?",
        "options": ["(A) Functions can only return strings", 
                    "(B) Functions cannot have multiple parameters", 
                    "(C) Functions allow code reuse and modularity", 
                    "(D) Functions are only used in large programs"],
        "answer": "(C)"
    }
]

MCQ_STAGE_3 = [
    {
        "question": "What is the primary purpose of loops in Python?",
        "options": ["(A) Store multiple values", 
                    "(B) Repeat a block of code multiple times", 
                    "(C) Print output", 
                    "(D) Perform mathematical calculations"],
        "answer": "(B)"
    },
    {
        "question": "Which loop is used to iterate over a sequence?",
        "options": ["(A) while", 
                    "(B) for", 
                    "(C) do-while", 
                    "(D) repeat"],
        "answer": "(B)"
    },
    {
        "question": "What is the purpose of the `break` statement in a loop?",
        "options": ["(A) Continue to the next iteration", 
                    "(B) Exit the loop immediately", 
                    "(C) Skip the current iteration", 
                    "(D) Repeat the current iteration"],
        "answer": "(B)"
    },
    {
        "question": "Which of the following loops will run at least once?",
        "options": ["(A) for loop", 
                    "(B) while loop", 
                    "(C) do-while loop", 
                    "(D) infinite loop"],
        "answer": "(C)"
    },
    {
        "question": "What will be the output of the following loop?\n\nfor i in range(3):\n    print(i)",
        "options": ["(A) 0 1 2", 
                    "(B) 1 2 3", 
                    "(C) 0 1 2 3", 
                    "(D) 1 2"],
        "answer": "(A)"
    },
    {
        "question": "What is the difference between `while` and `for` loops?",
        "options": ["(A) `while` is used for known iterations, `for` for unknown iterations", 
                    "(B) `for` is used for known iterations, `while` for unknown iterations", 
                    "(C) Both loops are identical", 
                    "(D) `while` loops do not accept conditions"],
        "answer": "(B)"
    },
    {
        "question": "Which keyword is used to skip the current iteration of a loop?",
        "options": ["(A) break", 
                    "(B) continue", 
                    "(C) skip", 
                    "(D) exit"],
        "answer": "(B)"
    },
    {
        "question": "What will be the output of the following loop?\n\nx = 0\nwhile x < 5:\n    print(x)\n    x += 2",
        "options": ["(A) 0 1 2 3 4", 
                    "(B) 0 2 4", 
                    "(C) 0 1 3", 
                    "(D) 1 3 5"],
        "answer": "(B)"
    },
    {
        "question": "How many times will the following loop run?\n\nfor i in range(0, 10, 2):\n    print(i)",
        "options": ["(A) 5 times", 
                    "(B) 4 times", 
                    "(C) 3 times", 
                    "(D) 6 times"],
        "answer": "(A)"
    },
    {
        "question": "What is an infinite loop?",
        "options": ["(A) A loop that runs indefinitely", 
                    "(B) A loop that terminates after a single iteration", 
                    "(C) A loop with no break condition", 
                    "(D) A loop that only runs once"],
        "answer": "(A)"
    }
]


def split_into_chunks(text, chunk_size=4):
    words = text.split()
    chunks = []

    for i in range(0, len(words), chunk_size):
        chunk = ""
        for j in range(i, min(i + chunk_size, len(words))):
            chunk += words[j] + " "
        chunks.append(chunk.strip())

    return chunks



def split_into_chunks_10(text, chunk_size=10):
    words = text.split()
    chunks = []

    for i in range(0, len(words), chunk_size):
        chunk = ""
        for j in range(i, min(i + chunk_size, len(words))):
            chunk += words[j] + " "
        chunks.append(chunk.strip())

    return chunks