# pybottrain

pybotlearn is a Python library that provides functions for conditional code execution based on random numbers. It can be used to create bots with various levels of intelligence.

## Functions

### `learn(num1, num2, num3, code)`

This function generates a random integer between `num1` and `num2` (inclusive) and compares it to `num3`. If the generated random number is equal to `num3`, it executes the provided `code` using the `eval()` function and returns `True`. Otherwise, it returns `False`.

#### install using:
```bash
pip install pybottrain
```

##### Example:

```python
from pybottrain import bot

while True:
    bot.learn_else(0,1,1,"print('the bot is learning')","print('the bot is not learning')")
    bot.learn(0,1,1,"print('the bot is learning')")
```