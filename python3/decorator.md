### Python Decorator
A decorator is simply a function that takes another function as an argument and adding to its behavior by wrapping it. Here is a simple example:

```python
def my_decorator(func):
    def inner():
        print('Before func!')
        func()
        print('After func!')
    return inner


@my_decorator
def some_func():
    print("Hey, you are in some_func!")

some_func()
```

If you run the above code, you will see:
```bash
Before func!
Hey, you are in some_func!
After func!
```

As you can see, the my_decorator() function dynamically creates a new function to return using the input function, adding code to be executed before and after the original function runs.