def execute_user_input(user_input):
    # Warning: Dangerous! This will execute arbitrary Python code.
    eval(user_input)

# Simulating user input
user_input = "import os; os.system('ls')"
execute_user_input(user_input)
