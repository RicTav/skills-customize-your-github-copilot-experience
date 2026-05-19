# 📘 Assignment: Python Decorator Patterns

## 🎯 Objective

Master the decorator pattern in Python by creating and using decorators to enhance function and method behavior. Learn how to apply common patterns like timing, logging, caching, and authentication validation. By the end of this assignment, you'll understand how decorators work and be able to implement them in real-world scenarios.

## 📝 Tasks

### 🛠️ Create a Basic Function Decorator

#### Description
Write your first decorator that modifies the behavior of a function without changing its original code.

#### Requirements
Completed program should:

- Create a decorator called `@timer` that measures how long a function takes to execute
- The decorator should print the function name and execution time in seconds
- Apply the decorator to a sample function and verify it works
- Example output:
  ```
  Function 'slow_task' took 2.05 seconds to execute
  ```
- The original function's return value should remain unchanged

### 🛠️ Build a Logging Decorator with Arguments

#### Description
Create a more sophisticated decorator that logs function calls and can be customized.

#### Requirements
Completed program should:

- Create a decorator called `@log_calls` that logs every time a function is called
- The decorator should record: function name, arguments passed, and the return value
- Make the decorator configurable with a `level` parameter (e.g., "INFO", "DEBUG")
- Support stacking multiple decorators on the same function
- Example:
  ```python
  @log_calls(level="INFO")
  def add(a, b):
      return a + b
  
  result = add(5, 3)
  # Output: [INFO] Calling add with args=(5, 3)
  # Output: [INFO] add returned: 8
  ```

### 🛠️ Implement a Caching Decorator

#### Description
Create a decorator that caches function results to improve performance.

#### Requirements
Completed program should:

- Create a decorator called `@cache` that stores function results based on arguments
- Return cached results for repeated calls with the same arguments
- Include a method to clear the cache
- Demonstrate performance improvement with a slow function
- Example:
  ```python
  @cache
  def fibonacci(n):
      if n <= 1:
          return n
      return fibonacci(n-1) + fibonacci(n-2)
  
  result = fibonacci(10)  # Takes time on first call
  result = fibonacci(10)  # Returns instantly from cache
  ```

### 🛠️ ⭐ Stretch Goal: Authentication Decorator

#### Description
Create a practical decorator that validates user permissions before executing a function.

#### Requirements
Completed program should:

- Create a decorator called `@require_auth` that checks if a user has the required role
- Store a current user context (e.g., username and role)
- Raise a `PermissionError` if the user doesn't have the required role
- Support multiple role requirements
- Example:
  ```python
  @require_auth(roles=['admin', 'moderator'])
  def delete_user(user_id):
      return f"User {user_id} deleted"
  
  # Should work for admin users
  # Should raise PermissionError for regular users
  ```
