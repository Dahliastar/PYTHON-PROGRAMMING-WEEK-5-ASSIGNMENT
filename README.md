# Object-Oriented Programming in Python

This repository contains two activities demonstrating fundamental Object-Oriented Programming (OOP) concepts in Python, including classes, inheritance, and polymorphism.

## Prerequisites

- Python 3.x installed on your system
- Basic understanding of Python syntax

## Activities Overview

### Activity 1: Classes and Inheritance

This activity demonstrates:
- **Class Definition**: Creating a basic `Student` class with attributes and methods
- **Object Instantiation**: Creating instances of classes
- **String Representation**: Using `__str__` method for readable object output
- **Inheritance**: Creating a `TeachingAssistant` class that inherits from `Student`
- **Method Overriding**: Customizing inherited methods in child classes

#### Classes Included:
- `Student`: Base class with name, age, and student_id attributes
- `TeachingAssistant`: Inherits from Student, adds TA-specific functionality

### Activity 2: Polymorphism

This activity demonstrates:
- **Polymorphism**: Different classes implementing the same method name with different behaviors
- **Method Implementation**: Each vehicle type has its own `move()` method

#### Classes Included:
- `Car`: Implements `move()` as "Driving"
- `Airplane`: Implements `move()` as "Flying"  
- `Boat`: Implements `move()` as "Sailing"

## How to Run

1. Clone or download this repository
2. Navigate to the project directory
3. Run the Python file:
   ```bash
   python main.py
   ```

## Expected Output

When you run the code, you should see:
```
Student(Name: Alice, Age: 20, ID: S12345)
TeachingAssistant(TA ID: TA4523, Name: Alice, Age: 20, Student ID: S12345)
Assigned Classes: ['Web Development', 'Data Science']
```

## Key OOP Concepts Demonstrated

### 1. Encapsulation
- Data (attributes) and methods are bundled together within classes
- Object state is managed through class methods

### 2. Inheritance
- `TeachingAssistant` inherits properties and methods from `Student`
- Demonstrates code reuse and hierarchical relationships

### 3. Polymorphism
- Different classes (`Car`, `Airplane`, `Boat`) implement the same method (`move()`) with different behaviors
- Allows objects of different types to be treated uniformly

### 4. Method Overriding
- `TeachingAssistant` overrides the `__str__` method from `Student` to provide specialized string representation

## Learning Objectives

After studying this code, you should understand:
- How to define classes and create objects
- How inheritance allows code reuse and specialization
- How polymorphism enables flexible and extensible code design
- The importance of the `__str__` method for object representation
- How to call parent class constructors using `super()`

## Extension Ideas

Try modifying the code to:
1. Add more attributes to the classes
2. Create additional vehicle types for the polymorphism example
3. Implement more methods in the `TeachingAssistant` class
4. Create a `Professor` class that also inherits from a base `Person` class
5. Demonstrate polymorphism by creating a list of different vehicles and calling `move()` on each

## Notes

- The code uses `super().__init__()` for calling the parent constructor, which is the modern and preferred approach in Python.
- The `TeachingAssistant` class includes methods for managing class assignments, showing practical inheritance usage.
- `super()` automatically handles the method resolution order (MRO) and is more maintainable than calling parent methods directly.
