# -*- coding: utf-8 -*-
"""Case Study: Hacker Statistics

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RalwIvyctjOBg7R14p4AqTcPncECTJwm
"""

# Import numpy as np
import numpy as np

# Set the seed
number =  np.random.seed(123)

# Generate and print random float
print(number)
None
# Import numpy as np
import numpy as np

# Set the seed
np.random.seed(123)


# Generate and print random float
print(np.random.rand())
0.6964691855978616

<script.py> output:
    0.6964691855978616
# Import numpy as np
import numpy as np

# Set the seed
np.random.seed(123)


# Generate and print random float
print(np.random.rand())
# Import numpy and set seed
import numpy as np
np.random.seed(123)

# Use randint() to simulate a dice
dice = np.random.randint(1, 7)
print(dice)


# Use randint() again
dice = np.random.randint(1, 7)
print(dice)
6
3

<script.py> output:
    6
    3
# Import numpy and set seed
import numpy as np
np.random.seed(123)

# Use randint() to simulate a dice
dice = np.random.randint(1, 7)
print(dice)


# Use randint() again
dice = np.random.randint(1, 7)
print(dice)
# NumPy is imported, seed is set

# Starting step
step = 50

# Roll the dice
dice = np.random.randint(1,7)


# Finish the control construct
if dice <= 2 :
    step = step - 1
elif <=5 :
    step = step + 1
else :
    step = step + np.random.randint(1,7)

# Print out dice and step
print(dice)
print(step)
Traceback (most recent call last):
  File "/var/lib/python/site-packages/python3.9/IPython/core/interactiveshell.py", line 2944, in _run_cell
    return runner(coro)
  File "/var/lib/python/site-packages/python3.9/IPython/core/async_helpers.py", line 68, in _pseudo_sync_runner
    coro.send(None)
  File "/var/lib/python/site-packages/python3.9/IPython/core/interactiveshell.py", line 3150, in run_cell_async
    self.showsyntaxerror()
  File "/var/lib/python/site-packages/python3.9/IPython/core/interactiveshell.py", line 2114, in showsyntaxerror
    self._showtraceback(etype, value, stb)
  File "/var/lib/python/site-packages/python3.9/pythonbackend/shell_utils.py", line 72, in exceptionCatcher
    raise exception
  File "/var/lib/python/site-packages/python3.9/IPython/core/interactiveshell.py", line 3140, in run_cell_async
    code_ast = compiler.ast_parse(cell, filename=cell_name)
  File "/var/lib/python/site-packages/python3.9/IPython/core/compilerop.py", line 101, in ast_parse
    return compile(source, filename, symbol, self.flags | PyCF_ONLY_AST, 1)
  File "<stdin>", line 13
    elif <=5 :
         ^
SyntaxError: invalid syntax
# NumPy is imported, seed is set

# Starting step
step = 50

# Roll the dice
dice = np.random.randint(1,7)


# Finish the control construct
if dice <= 2 :
    step = step - 1
elif dice <=5 :
    step = step + 1
else :
    step = step + np.random.randint(1,7)

# Print out dice and step
print(dice)
print(step)
6
53

<script.py> output:
    6
    53
# NumPy is imported, seed is set

# Starting step
step = 50

# Roll the dice
dice = np.random.randint(1,7)


# Finish the control construct
if dice <= 2 :
    step = step - 1
elif dice <=5 :
    step = step + 1
else :
    step = step + np.random.randint(1,7)

# Print out dice and step
print(dice)
print(step)
# NumPy is imported, seed is set

# Initialize random_walk
random_walk = [0]


# Complete the ___
for x in range(100) :
    # Set step: last element in random_walk
    step = random_walk[-1]

    # Roll the dice
    dice = np.random.randint(1,7)

    # Determine next step
    if dice <= 2:
        step = step - 1
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1,7)

    # append next_step to random_walk
    random_walk.append(step)

# Print random_walk
print(random_walk)
[0, 3, 4, 5, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1, 0, -1, 0, 5, 4, 3, 4, 3, 4, 5, 6, 7, 8, 7, 8, 7, 8, 9, 10, 11, 10, 14, 15, 14, 15, 14, 15, 16, 17, 18, 19, 20, 21, 24, 25, 26, 27, 32, 33, 37, 38, 37, 38, 39, 38, 39, 40, 42, 43, 44, 43, 42, 43, 44, 43, 42, 43, 44, 46, 45, 44, 45, 44, 45, 46, 47, 49, 48, 49, 50, 51, 52, 53, 52, 51, 52, 51, 52, 53, 52, 55, 56, 57, 58, 57, 58, 59]

<script.py> output:
    [0, 3, 4, 5, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1, 0, -1, 0, 5, 4, 3, 4, 3, 4, 5, 6, 7, 8, 7, 8, 7, 8, 9, 10, 11, 10, 14, 15, 14, 15, 14, 15, 16, 17, 18, 19, 20, 21, 24, 25, 26, 27, 32, 33, 37, 38, 37, 38, 39, 38, 39, 40, 42, 43, 44, 43, 42, 43, 44, 43, 42, 43, 44, 46, 45, 44, 45, 44, 45, 46, 47, 49, 48, 49, 50, 51, 52, 53, 52, 51, 52, 51, 52, 53, 52, 55, 56, 57, 58, 57, 58, 59]
# NumPy is imported, seed is set

# Initialize random_walk
random_walk = [0]


# Complete the ___
for x in range(100) :
    # Set step: last element in random_walk
    step = random_walk[-1]

    # Roll the dice
    dice = np.random.randint(1,7)

    # Determine next step
    if dice <= 2:
        step = step - 1
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1,7)

    # append next_step to random_walk
    random_walk.append(step)

# Print random_walk
print(random_walk)
# NumPy is imported, seed is set

# Initialize random_walk
random_walk = [0]

for x in range(100) :
    step = random_walk[-1]
    dice = np.random.randint(1,7)

    if dice <= 2:
        # Replace below: use max to make sure step can't go below 0
        step =max (0, step - 1)
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1,7)

    random_walk.append(step)

print(random_walk)
[0, 3, 4, 5, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1, 0, 0, 1, 6, 5, 4, 5, 4, 5, 6, 7, 8, 9, 8, 9, 8, 9, 10, 11, 12, 11, 15, 16, 15, 16, 15, 16, 17, 18, 19, 20, 21, 22, 25, 26, 27, 28, 33, 34, 38, 39, 38, 39, 40, 39, 40, 41, 43, 44, 45, 44, 43, 44, 45, 44, 43, 44, 45, 47, 46, 45, 46, 45, 46, 47, 48, 50, 49, 50, 51, 52, 53, 54, 53, 52, 53, 52, 53, 54, 53, 56, 57, 58, 59, 58, 59, 60]
# NumPy is imported, seed is set

# Initialize random_walk
random_walk = [0]

for x in range(100) :
    step = random_walk[-1]
    dice = np.random.randint(1,7)

    if dice <= 2:
        # Replace below: use max to make sure step can't go below 0
        step =max (0, step - 1)
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1,7)

    random_walk.append(step)

print(random_walk)
[0, 4, 3, 2, 4, 3, 4, 6, 7, 8, 13, 12, 13, 14, 15, 16, 17, 16, 21, 22, 23, 24, 23, 22, 21, 20, 19, 20, 21, 22, 28, 27, 26, 25, 26, 27, 28, 27, 28, 29, 28, 33, 34, 33, 32, 31, 30, 31, 30, 29, 31, 32, 35, 36, 38, 39, 40, 41, 40, 39, 40, 41, 42, 43, 42, 43, 44, 45, 48, 49, 50, 49, 50, 49, 50, 51, 52, 56, 55, 54, 55, 56, 57, 56, 57, 56, 57, 59, 64, 63, 64, 65, 66, 67, 68, 69, 68, 69, 70, 71, 73]

<script.py> output:
    [0, 3, 4, 5, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1, 0, 0, 1, 6, 5, 4, 5, 4, 5, 6, 7, 8, 9, 8, 9, 8, 9, 10, 11, 12, 11, 15, 16, 15, 16, 15, 16, 17, 18, 19, 20, 21, 22, 25, 26, 27, 28, 33, 34, 38, 39, 38, 39, 40, 39, 40, 41, 43, 44, 45, 44, 43, 44, 45, 44, 43, 44, 45, 47, 46, 45, 46, 45, 46, 47, 48, 50, 49, 50, 51, 52, 53, 54, 53, 52, 53, 52, 53, 54, 53, 56, 57, 58, 59, 58, 59, 60]
# NumPy is imported, seed is set

# Initialize random_walk
random_walk = [0]

for x in range(100) :
    step = random_walk[-1]
    dice = np.random.randint(1,7)

    if dice <= 2:
        # Replace below: use max to make sure step can't go below 0
        step =max (0, step - 1)
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1,7)

    random_walk.append(step)

print(random_walk)
# NumPy is imported, seed is set

# Initialization
random_walk = [0]

for x in range(100) :
    step = random_walk[-1]
    dice = np.random.randint(1,7)

    if dice <= 2:
        step = max(0, step - 1)
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1,7)

    random_walk.append(step)

# Import matplotlib.pyplot as plt
matplotlib.pyplot as plt


# Plot random_walk
plt.plot(random_walk)


# Show the plot
plt.show()
Traceback (most recent call last):
  File "/var/lib/python/site-packages/python3.9/IPython/core/interactiveshell.py", line 2944, in _run_cell
    return runner(coro)
  File "/var/lib/python/site-packages/python3.9/IPython/core/async_helpers.py", line 68, in _pseudo_sync_runner
    coro.send(None)
  File "/var/lib/python/site-packages/python3.9/IPython/core/interactiveshell.py", line 3150, in run_cell_async
    self.showsyntaxerror()
  File "/var/lib/python/site-packages/python3.9/IPython/core/interactiveshell.py", line 2114, in showsyntaxerror
    self._showtraceback(etype, value, stb)
  File "/var/lib/python/site-packages/python3.9/pythonbackend/shell_utils.py", line 72, in exceptionCatcher
    raise exception
  File "/var/lib/python/site-packages/python3.9/IPython/core/interactiveshell.py", line 3140, in run_cell_async
    code_ast = compiler.ast_parse(cell, filename=cell_name)
  File "/var/lib/python/site-packages/python3.9/IPython/core/compilerop.py", line 101, in ast_parse
    return compile(source, filename, symbol, self.flags | PyCF_ONLY_AST, 1)
  File "<stdin>", line 20
    matplotlib.pyplot as plt
                      ^
SyntaxError: invalid syntax
# NumPy is imported, seed is set

# Initialization
random_walk = [0]

for x in range(100) :
    step = random_walk[-1]
    dice = np.random.randint(1,7)

    if dice <= 2:
        step = max(0, step - 1)
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1,7)

    random_walk.append(step)

# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt


# Plot random_walk
plt.plot(random_walk)


# Show the plot
plt.show()
# NumPy is imported, seed is set

# Initialization
random_walk = [0]

for x in range(100) :
    step = random_walk[-1]
    dice = np.random.randint(1,7)

    if dice <= 2:
        step = max(0, step - 1)
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1,7)

    random_walk.append(step)

# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt


# Plot random_walk
plt.plot(random_walk)


# Show the plot
plt.show()
# NumPy is imported; seed is set

# Initialize all_walks (don't change this line)
all_walks = []

# Simulate random walk 10 times
for i in range(10) :

    # Code from before
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)

        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        random_walk.append(step)

    # Append random_walk to all_walks
    random_walk.append(step)
    

# Print all_walks
all_walks.append(random_walk)
# NumPy is imported; seed is set

# Initialize all_walks (don't change this line)
all_walks = []

# Simulate random walk 10 times
for i in range(10) :

    # Code from before
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)

        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        random_walk.append(step)

    # Append random_walk to all_walks
    all_walks.append(random_walk)
    

# Print all_walks
print(all_walks)
[[0, 1, 2, 3, 2, 5, 4, 6, 7, 13, 12, 13, 14, 13, 12, 13, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 25, 26, 27, 28, 27, 26, 25, 26, 25, 29, 28, 27, 28, 30, 31, 36, 35, 36, 37, 41, 40, 41, 42, 41, 40, 41, 42, 43, 42, 41, 40, 41, 40, 39, 40, 39, 38, 37, 38, 39, 38, 37, 36, 37, 38, 39, 38, 37, 38, 39, 40, 41, 40, 41, 40, 41, 42, 43, 44, 45, 50, 55, 54, 55, 56, 55, 56, 62, 61, 62], [0, 0, 1, 0, 1, 2, 3, 2, 1, 2, 3, 4, 3, 2, 1, 3, 4, 5, 4, 3, 2, 3, 4, 5, 4, 3, 4, 7, 12, 15, 16, 17, 23, 24, 25, 26, 25, 27, 32, 33, 34, 35, 36, 37, 38, 37, 38, 39, 40, 41, 42, 44, 48, 49, 50, 51, 52, 56, 61, 60, 59, 58, 57, 60, 61, 62, 63, 62, 61, 64, 65, 64, 63, 62, 63, 64, 65, 66, 65, 66, 65, 66, 67, 66, 67, 68, 69, 70, 71, 72, 73, 72, 71, 72, 73, 76, 77, 76, 75, 76, 77], [0, 1, 6, 5, 4, 3, 2, 1, 0, 1, 0, 0, 1, 4, 3, 2, 3, 4, 5, 4, 5, 6, 7, 8, 9, 10, 11, 12, 15, 21, 22, 23, 24, 25, 26, 25, 24, 23, 24, 25, 26, 27, 29, 30, 31, 32, 34, 38, 37, 36, 35, 34, 35, 36, 37, 36, 35, 34, 33, 32, 31, 32, 36, 40, 41, 42, 41, 40, 41, 42, 43, 49, 50, 49, 48, 49, 48, 49, 48, 49, 50, 49, 50, 49, 48, 49, 50, 49, 50, 49, 50, 53, 54, 55, 56, 57, 56, 57, 58, 63, 62], [0, 1, 2, 3, 7, 6, 5, 6, 7, 9, 8, 7, 8, 11, 10, 11, 10, 16, 17, 18, 19, 20, 19, 18, 19, 22, 21, 22, 23, 24, 25, 26, 30, 29, 30, 29, 30, 31, 32, 33, 34, 35, 36, 35, 36, 37, 38, 39, 40, 39, 42, 43, 44, 43, 44, 43, 44, 43, 44, 43, 42, 43, 44, 45, 46, 47, 46, 45, 44, 45, 46, 45, 46, 45, 46, 47, 46, 47, 46, 45, 46, 47, 52, 51, 52, 53, 52, 53, 54, 60, 61, 60, 59, 60, 64, 63, 62, 61, 60, 59, 58], [0, 1, 2, 7, 9, 13, 12, 17, 18, 19, 18, 17, 18, 19, 20, 19, 18, 19, 20, 21, 22, 21, 20, 21, 22, 23, 24, 30, 32, 33, 38, 39, 38, 37, 38, 39, 44, 43, 44, 45, 47, 48, 47, 48, 49, 50, 49, 50, 49, 48, 47, 48, 47, 46, 47, 46, 47, 52, 53, 54, 55, 56, 55, 56, 55, 57, 58, 57, 58, 57, 56, 57, 56, 62, 63, 62, 63, 64, 65, 64, 66, 67, 71, 72, 73, 72, 71, 72, 73, 74, 75, 78, 77, 76, 77, 78, 77, 78, 79, 78, 83], [0, 1, 2, 8, 9, 10, 9, 8, 9, 10, 11, 12, 13, 14, 15, 20, 19, 18, 17, 18, 19, 20, 19, 23, 29, 30, 35, 36, 35, 36, 42, 41, 42, 41, 42, 41, 42, 41, 42, 47, 48, 47, 48, 49, 50, 51, 50, 51, 52, 53, 52, 53, 56, 55, 56, 57, 58, 59, 62, 61, 60, 66, 67, 69, 72, 73, 76, 77, 78, 79, 80, 81, 82, 81, 82, 83, 82, 83, 82, 81, 82, 85, 84, 83, 84, 85, 84, 85, 91, 90, 91, 90, 91, 92, 91, 90, 89, 91, 90, 95, 96], [0, 3, 4, 5, 6, 11, 17, 20, 23, 22, 23, 24, 23, 26, 25, 26, 27, 28, 29, 28, 29, 30, 36, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 50, 56, 58, 57, 60, 63, 64, 63, 62, 68, 69, 72, 73, 74, 75, 76, 77, 78, 79, 78, 77, 78, 77, 78, 77, 78, 77, 76, 77, 78, 79, 78, 79, 78, 83, 82, 81, 82, 86, 87, 88, 87, 88, 87, 88, 87, 86, 85, 86, 87, 88, 89, 88, 89, 88, 89, 90, 89, 90, 89, 90, 89, 88, 89, 90, 91, 92, 91], [0, 2, 4, 5, 6, 5, 6, 7, 8, 7, 12, 11, 12, 13, 12, 16, 20, 26, 27, 26, 27, 28, 29, 28, 32, 33, 37, 36, 37, 38, 39, 40, 41, 42, 43, 42, 41, 42, 41, 42, 41, 42, 43, 48, 53, 52, 51, 52, 53, 54, 55, 54, 55, 54, 53, 54, 53, 54, 53, 54, 57, 58, 57, 58, 63, 64, 65, 71, 77, 76, 77, 78, 77, 76, 77, 78, 77, 83, 84, 85, 86, 85, 88, 87, 86, 87, 88, 87, 93, 98, 97, 98, 97, 98, 99, 100, 101, 102, 103, 102, 104], [0, 0, 1, 2, 3, 4, 5, 4, 3, 2, 3, 2, 3, 2, 1, 5, 7, 12, 11, 17, 18, 17, 18, 19, 20, 21, 24, 25, 26, 27, 30, 29, 30, 29, 28, 32, 31, 32, 33, 39, 38, 39, 40, 41, 42, 41, 42, 44, 45, 46, 45, 46, 47, 46, 47, 48, 49, 50, 56, 57, 58, 59, 60, 61, 60, 59, 60, 59, 60, 61, 62, 61, 62, 61, 67, 68, 67, 66, 67, 66, 67, 68, 69, 70, 69, 68, 69, 68, 67, 68, 69, 68, 67, 68, 67, 66, 67, 68, 69, 68, 69], [0, 4, 3, 4, 5, 6, 7, 8, 9, 8, 7, 12, 13, 12, 13, 14, 15, 16, 18, 17, 18, 19, 23, 24, 25, 24, 23, 22, 23, 22, 21, 22, 26, 27, 26, 27, 28, 32, 33, 34, 35, 36, 35, 36, 37, 38, 39, 38, 37, 39, 40, 39, 40, 41, 43, 44, 43, 44, 43, 44, 43, 44, 45, 49, 50, 49, 48, 47, 48, 47, 46, 45, 46, 45, 46, 45, 46, 49, 50, 51, 52, 53, 52, 53, 54, 57, 56, 55, 59, 63, 64, 65, 70, 71, 70, 69, 70, 71, 70, 73, 74]]

<script.py> output:
    [[0, 3, 4, 5, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1, 0, 0, 1, 6, 5, 4, 5, 4, 5, 6, 7, 8, 9, 8, 9, 8, 9, 10, 11, 12, 11, 15, 16, 15, 16, 15, 16, 17, 18, 19, 20, 21, 22, 25, 26, 27, 28, 33, 34, 38, 39, 38, 39, 40, 39, 40, 41, 43, 44, 45, 44, 43, 44, 45, 44, 43, 44, 45, 47, 46, 45, 46, 45, 46, 47, 48, 50, 49, 50, 51, 52, 53, 54, 53, 52, 53, 52, 53, 54, 53, 56, 57, 58, 59, 58, 59, 60], [0, 4, 3, 2, 4, 3, 4, 6, 7, 8, 13, 12, 13, 14, 15, 16, 17, 16, 21, 22, 23, 24, 23, 22, 21, 20, 19, 20, 21, 22, 28, 27, 26, 25, 26, 27, 28, 27, 28, 29, 28, 33, 34, 33, 32, 31, 30, 31, 30, 29, 31, 32, 35, 36, 38, 39, 40, 41, 40, 39, 40, 41, 42, 43, 42, 43, 44, 45, 48, 49, 50, 49, 50, 49, 50, 51, 52, 56, 55, 54, 55, 56, 57, 56, 57, 56, 57, 59, 64, 63, 64, 65, 66, 67, 68, 69, 68, 69, 70, 71, 73], [0, 2, 1, 2, 3, 6, 5, 6, 5, 6, 7, 8, 7, 8, 7, 8, 9, 11, 10, 9, 10, 11, 10, 12, 13, 14, 15, 16, 17, 18, 17, 18, 19, 24, 25, 24, 23, 22, 21, 22, 23, 24, 29, 30, 29, 30, 31, 32, 33, 34, 35, 34, 33, 34, 33, 39, 38, 39, 38, 39, 38, 39, 43, 47, 49, 51, 50, 51, 53, 52, 58, 59, 61, 62, 61, 62, 63, 64, 63, 64, 65, 66, 68, 67, 66, 67, 73, 78, 77, 76, 80, 81, 82, 83, 85, 84, 85, 84, 85, 84, 83], [0, 6, 5, 6, 7, 8, 9, 10, 11, 12, 13, 12, 13, 12, 11, 12, 11, 12, 11, 12, 13, 17, 18, 17, 23, 22, 21, 22, 21, 20, 21, 20, 24, 23, 24, 23, 24, 23, 24, 26, 25, 24, 23, 24, 23, 28, 29, 30, 29, 28, 29, 28, 29, 28, 33, 34, 33, 32, 31, 30, 31, 32, 36, 42, 43, 44, 45, 46, 45, 46, 48, 49, 50, 51, 50, 49, 50, 49, 50, 51, 52, 51, 52, 53, 54, 53, 52, 53, 54, 59, 60, 61, 66, 65, 66, 65, 66, 67, 68, 69, 68], [0, 6, 5, 6, 5, 4, 5, 9, 10, 11, 12, 13, 12, 11, 10, 9, 8, 9, 10, 11, 12, 13, 14, 13, 14, 15, 14, 15, 16, 19, 18, 19, 18, 19, 22, 23, 24, 25, 24, 23, 26, 27, 28, 29, 28, 27, 28, 31, 32, 37, 38, 37, 38, 37, 38, 37, 43, 42, 41, 42, 44, 43, 42, 41, 42, 43, 44, 45, 49, 54, 55, 56, 57, 60, 61, 62, 63, 64, 65, 66, 65, 64, 65, 66, 65, 71, 70, 71, 72, 71, 70, 71, 70, 69, 75, 74, 73, 74, 75, 74, 73], [0, 0, 0, 1, 7, 8, 11, 12, 18, 19, 20, 26, 25, 31, 30, 31, 32, 33, 32, 38, 39, 38, 39, 38, 39, 38, 39, 38, 39, 43, 44, 46, 45, 46, 45, 44, 45, 44, 45, 44, 48, 52, 51, 50, 49, 50, 51, 55, 56, 57, 61, 60, 59, 58, 59, 60, 62, 61, 60, 61, 62, 64, 67, 72, 73, 72, 73, 74, 75, 76, 77, 76, 77, 78, 84, 83, 88, 87, 91, 90, 94, 93, 96, 97, 96, 97, 103, 102, 101, 100, 104, 103, 102, 103, 104, 103, 104, 105, 106, 107, 106], [0, 0, 0, 1, 0, 0, 4, 5, 7, 11, 17, 16, 15, 16, 17, 18, 17, 18, 17, 18, 19, 18, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 33, 32, 35, 36, 35, 34, 35, 36, 37, 36, 35, 34, 33, 34, 35, 36, 37, 38, 39, 40, 39, 40, 41, 43, 42, 43, 44, 47, 49, 50, 49, 48, 47, 46, 45, 46, 45, 46, 48, 49, 50, 49, 50, 49, 48, 49, 48, 47, 46, 47, 46, 45, 46, 47, 48, 50, 51, 52, 51, 50, 51, 57, 56, 57, 58, 63, 62, 63], [0, 0, 1, 2, 1, 2, 3, 9, 10, 11, 12, 11, 13, 14, 15, 16, 15, 16, 17, 18, 19, 18, 19, 18, 19, 20, 19, 20, 24, 25, 28, 29, 33, 34, 33, 34, 35, 34, 33, 38, 39, 40, 39, 38, 39, 40, 41, 40, 44, 43, 44, 45, 46, 47, 48, 49, 50, 49, 48, 47, 48, 49, 53, 54, 53, 54, 55, 54, 60, 61, 62, 63, 62, 63, 64, 67, 66, 67, 66, 65, 64, 65, 66, 68, 69, 70, 74, 75, 74, 73, 74, 75, 74, 73, 74, 75, 76, 75, 74, 75, 76], [0, 1, 0, 1, 2, 1, 0, 0, 1, 2, 3, 4, 5, 10, 14, 13, 14, 13, 12, 11, 12, 11, 12, 13, 12, 16, 17, 16, 17, 16, 15, 16, 15, 19, 20, 21, 22, 23, 24, 23, 24, 25, 26, 27, 28, 27, 32, 33, 34, 33, 34, 33, 34, 35, 34, 35, 40, 41, 42, 41, 42, 43, 44, 43, 44, 43, 44, 45, 44, 43, 42, 43, 44, 43, 42, 41, 42, 46, 47, 48, 49, 50, 51, 50, 51, 52, 51, 52, 57, 58, 57, 56, 57, 56, 55, 54, 58, 59, 60, 61, 60], [0, 1, 2, 3, 4, 5, 4, 3, 6, 5, 4, 3, 2, 3, 9, 10, 9, 10, 11, 10, 9, 10, 11, 12, 11, 15, 16, 15, 17, 18, 17, 18, 19, 20, 21, 22, 23, 22, 21, 22, 23, 22, 23, 24, 23, 22, 21, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 33, 34, 35, 36, 37, 38, 37, 36, 42, 43, 44, 43, 42, 41, 45, 46, 50, 49, 55, 56, 57, 61, 62, 61, 60, 61, 62, 63, 64, 63, 69, 70, 69, 73, 74, 73, 74, 73, 79, 85, 86, 85, 86, 87]]
# NumPy is imported; seed is set

# Initialize all_walks (don't change this line)
all_walks = []

# Simulate random walk 10 times
for i in range(10) :

    # Code from before
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)

        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        random_walk.append(step)

    # Append random_walk to all_walks
    all_walks.append(random_walk)
    

# Print all_walks
print(all_walks)
# numpy and matplotlib imported, seed set.

# initialize and populate all_walks
all_walks = []
for i in range(10) :
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        random_walk.append(step)
    all_walks.append(random_walk)

# Convert all_walks to NumPy array: np_aw
np_aw = np.array(all_walks)


# Plot np_aw and show
plt.plot(np_aw)
plt.show()


# Clear the figure
plt.clf()

# Transpose np_aw: np_aw_t
np_aw_t = np.transpose(np_aw)


# Plot np_aw_t and show
plt.plot(np_aw_t)
plt.show()
# numpy and matplotlib imported, seed set.

# initialize and populate all_walks
all_walks = []
for i in range(10) :
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        random_walk.append(step)
    all_walks.append(random_walk)

# Convert all_walks to NumPy array: np_aw
np_aw = np.array(all_walks)


# Plot np_aw and show
plt.plot(np_aw)
plt.show()


# Clear the figure
plt.clf()

# Transpose np_aw: np_aw_t
np_aw_t = np.transpose(np_aw)


# Plot np_aw_t and show
plt.plot(np_aw_t)
plt.show()
# numpy and matplotlib imported, seed set

# Simulate random walk 250 times
all_walks = []
for i in range(250) :
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)

        # Implement clumsiness
        if np.random.rand() <= 0.001:
            step = 0

        random_walk.append(step)
    all_walks.append(random_walk)

# Create and plot np_aw_t
np_aw_t = np.transpose(np.array(all_walks))
plt.plot(np_aw_t)
plt.show()
# numpy and matplotlib imported, seed set

# Simulate random walk 250 times
all_walks = []
for i in range(250) :
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)

        # Implement clumsiness
        if np.random.rand() <= 0.001:
            step = 0

        random_walk.append(step)
    all_walks.append(random_walk)

# Create and plot np_aw_t
np_aw_t = np.transpose(np.array(all_walks))
plt.plot(np_aw_t)
plt.show()
# numpy and matplotlib imported, seed set

# Simulate random walk 500 times
all_walks = []
for i in range(500) :
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        if np.random.rand() <= 0.001 :
            step = 0
        random_walk.append(step)
    all_walks.append(random_walk)

# Create and plot np_aw_t
np_aw_t = np.transpose(np.array(all_walks))

# Select last row from np_aw_t: ends
ends = np_aw_t[-1,:]

# Plot histogram of ends, display plot
plt.hist(ends)
plt.show()
____
Traceback (most recent call last):
  File "<stdin>", line 72, in exceptionCatcher
    raise exception
  File "<stdin>", line 3361, in run_ast_nodes
    if (await self.run_code(code, result,  async_=asy)):
  File "<stdin>", line 3458, in run_code
    self.showtraceback(running_compiled_code=True)
  File "<stdin>", line 2066, in showtraceback
    self._showtraceback(etype, value, stb)
  File "<stdin>", line 72, in exceptionCatcher
    raise exception
  File "<stdin>", line 3441, in run_code
    exec(code_obj, self.user_global_ns, self.user_ns)
  File "<stdin>", line 30, in <module>
    ____
NameError: name '____' is not defined
Traceback (most recent call last):
  File "script.py", line 72, in exceptionCatcher
    raise exception
  File "script.py", line 3361, in run_ast_nodes
    if (await self.run_code(code, result,  async_=asy)):
  File "script.py", line 3458, in run_code
    self.showtraceback(running_compiled_code=True)
  File "script.py", line 2066, in showtraceback
    self._showtraceback(etype, value, stb)
  File "script.py", line 72, in exceptionCatcher
    raise exception
  File "script.py", line 3441, in run_code
    exec(code_obj, self.user_global_ns, self.user_ns)
  File "script.py", line 30, in <module>
    ____
NameError: name '____' is not defined
# numpy and matplotlib imported, seed set

# Simulate random walk 500 times
all_walks = []
for i in range(500) :
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        if np.random.rand() <= 0.001 :
            step = 0
        random_walk.append(step)
    all_walks.append(random_walk)

# Create and plot np_aw_t
np_aw_t = np.transpose(np.array(all_walks))

# Select last row from np_aw_t: ends
ends = np_aw_t[-1,:]

# Plot histogram of ends, display plot
plt.hist(ends)
plt.show()
# numpy and matplotlib imported, seed set

# Simulate random walk 500 times
all_walks = []
for i in range(500) :
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        if np.random.rand() <= 0.001 :
            step = 0
        random_walk.append(step)
    all_walks.append(random_walk)

# Create and plot np_aw_t
np_aw_t = np.transpose(np.array(all_walks))

# Select last row from np_aw_t: ends
ends = np_aw_t[-1,:]

# Plot histogram of ends, display plot
plt.hist(ends)
plt.show()