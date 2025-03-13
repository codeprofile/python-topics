"""
## `__new__` vs `__init__` in Python

Both `__new__` and `__init__` are special methods used in Python classes, but they serve **different purposes** in object creation.

### **1️⃣ `__new__` Method**
- **Responsible for creating a new instance of a class.**
- It is a **static method** and returns a new instance of the class.
- Used when **subclassing immutable types** like `int`, `str`, `tuple`, etc.

🔹 **Syntax:**
```python
class MyClass:
    def __new__(cls, *args, **kwargs):
        print("Creating instance")
        instance = super().__new__(cls)
        return instance
```

🔹 **Example with `__new__`:**
```python
class Singleton:
    _instance = None  # Class-level variable to store a single instance

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)  # Create instance only once
        return cls._instance  # Return existing instance

obj1 = Singleton()
obj2 = Singleton()
print(obj1 is obj2)  # ✅ True (Same instance)
```

---

### **2️⃣ `__init__` Method**
- **Responsible for initializing an already created instance.**
- It is called **after `__new__`** and is used to set attributes.

🔹 **Example with `__init__`:**
```python
class MyClass:
    def __init__(self, value):
        print("Initializing instance")
        self.value = value

obj = MyClass(10)
print(obj.value)  # ✅ 10
```

---

### **3️⃣ `__new__` vs `__init__` Summary**

| Feature | `__new__` | `__init__` |
|---------|----------|-----------|
| **Purpose** | Creates a new instance | Initializes an existing instance |
| **Type** | Static method | Instance method |
| **Return Value** | Must return an instance | Returns `None` |
| **When to Use?** | Subclassing immutable types, Singleton pattern | Normal object initialization |

✅ **Use `__new__` only when object creation needs control.**
✅ **Use `__init__` for setting attributes after an object is created.**
"""