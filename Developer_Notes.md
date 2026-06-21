# Krash Programming Language – Developer Notes

**Complete Reference Guide with Expected Outputs**

---

## TABLE OF CONTENTS

1. [Overview & Philosophy](#overview--philosophy)
2. [Language Design](#language-design)
3. [Interpreter & Execution](#interpreter--execution)
4. [Strict Behavior (Like Python)](#strict-behavior-like-python)
5. [Data Types](#data-types)
6. [Variables & Scope](#variables--scope)
7. [Operators](#operators)
8. [Control Flow](#control-flow)
9. [Functions](#functions)
10. [Arrays & Strings](#arrays--strings)
11. [Dictionaries](#dictionaries)
12. [Error Handling](#error-handling)
13. [File I/O](#file-io)
14. [HTTP Requests](#http-requests)
15. [Imports & Libraries](#imports--libraries)
16. [Indentation Rules](#indentation-rules)
17. [Type System](#type-system)
18. [Best Practices](#best-practices)
19. [Common Mistakes](#common-mistakes)

---

## COMPREHENSIVE EXAMPLES WITH OUTPUTS

This section shows **complete, working examples** with all outputs displayed.

### Example 1: String Manipulation & Nested Format Strings

```krash
str name = "alice"

// Simple operations
showf "{name}"
// Output: alice

// Uppercase
showf "{name.toUpperCase()}"
// Output: ALICE

// Capitalize first letter
showf "{name.charAt(0).toUpperCase()}{name.RmCharAt(0)}"
// Output: Alice

// Store in variable
str capitalized = "{name.charAt(0).toUpperCase()}{name.RmCharAt(0)}"
showf "{capitalized}"
// Output: Alice

// Use in sentences
showf "Hello, {capitalized}! Welcome back!"
// Output: Hello, Alice! Welcome back!

// Multiple operations
str email = "alice.smith@example.com"
str username = email.split("@")[0]
str domain = email.split("@")[1]
showf "User: {username.toUpperCase()} | Domain: {domain.toUpperCase()}"
// Output: User: ALICE.SMITH | Domain: EXAMPLE.COM
```

### Example 2: Mathematical Operations with Format Strings

```krash
int x = 15
int y = 8

// Basic math
showf "{x} + {y} = {x + y}"
// Output: 15 + 8 = 23

showf "{x} - {y} = {x - y}"
// Output: 15 - 8 = 7

showf "{x} * {y} = {x * y}"
// Output: 15 * 8 = 120

// Using library
int division = mathBasic.divide(x, y)
showf "{x} / {y} = {division}"
// Output: 15 / 8 = 1

// Multiple operations
int sum = x + y
int product = x * y
int average = mathBasic.divide(x + y, 2)
showf "Sum: {sum} | Product: {product} | Average: {average}"
// Output: Sum: 23 | Product: 120 | Average: 11
```

### Example 3: Array Processing

```krash
int[] scores = [85, 92, 78, 95, 88]

// Access elements
showf "First score: {scores[0]}"
// Output: First score: 85

showf "Last score: {scores[4]}"
// Output: Last score: 95

showf "Total scores: {scores.length()}"
// Output: Total scores: 5

// Calculate sum and average
int total = 0
for>: int i = 0, i < scores.length(), i++:
    total = total + scores[i]
<:
int average = mathBasic.divide(total, scores.length())
showf "Total: {total} | Average: {average}"
// Output: Total: 438 | Average: 87

// Display all with formatting
showf "Scores: {scores[0]}, {scores[1]}, {scores[2]}, {scores[3]}, {scores[4]}"
// Output: Scores: 85, 92, 78, 95, 88
```

### Example 4: String Array and Methods

```krash
str[] fruits = ["apple", "banana", "cherry", "date"]

// Access and display
showf "Fruit 1: {fruits[0]}"
// Output: Fruit 1: apple

showf "Fruit 2: {fruits[1].toUpperCase()}"
// Output: Fruit 2: BANANA

// Find in array
bool hasCherry = fruits.contains("cherry")
showf "Has cherry: {hasCherry}"
// Output: Has cherry: True

// Join array
str fruitList = fruits.join(", ")
showf "All fruits: {fruitList}"
// Output: All fruits: apple, banana, cherry, date

// Array length
showf "Total fruits: {fruits.length()}"
// Output: Total fruits: 4

// Pick random
str randomFruit = fruits.pickRandom()
showf "Today's special: {randomFruit}"
// Output: Today's special: cherry
```

### Example 5: Dictionary Operations

```krash
mydict{} = {
    "firstName": "Alice",
    "lastName": "Smith",
    "age": 28,
    "city": "NYC"
}

// Access values
showf "{mydict{"firstName"}}"
// Output: Alice

showf "{mydict{"age"}}"
// Output: 28

// Combine values
showf "Name: {mydict{"firstName"}} {mydict{"lastName"}}"
// Output: Name: Alice Smith

// With transformations
showf "Welcome, {mydict{"firstName"}.toUpperCase()}!"
// Output: Welcome, ALICE!

// Check key exists
bool hasEmail = mydict{}.has("email")
showf "Has email: {hasEmail}"
// Output: Has email: False

// Add new key
mydict{}.Add{"email": "alice@example.com"}
showf "Email: {mydict{"email"}}"
// Output: Email: alice@example.com
```

### Example 6: Control Flow with Formatting

```krash
int score = 87

// If/else with output
if>: score >= 90:
    showf "Grade: A (Excellent!)"
<: elif>: score >= 80:
    showf "Grade: B (Good work!)"
<: elif>: score >= 70:
    showf "Grade: C (Passing)"
<: else>:
    showf "Grade: F (Need improvement)"
<:
// Output: Grade: B (Good work!)

// Loop with formatted output
showf "Score breakdown:"
for>: int i = 1, i <= 5, i++:
    showf "Test {i}: {60 + (i * 5)} points"
<:
// Output:
// Score breakdown:
// Test 1: 65 points
// Test 2: 70 points
// Test 3: 75 points
// Test 4: 80 points
// Test 5: 85 points
```

### Example 7: Functions Returning Values

```krash
fxn>: calculateTax(float amount):
    float tax = amount * 0.1
    givef "{tax}"
<:

fxn>: formatCurrency(float amount):
    givef "${amount}"
<:

float purchase = 100.0
float tax = calculateTax(purchase)
float total = purchase + tax

showf "Purchase: {formatCurrency(purchase)}"
// Output: Purchase: $100

showf "Tax (10%): {formatCurrency(tax)}"
// Output: Tax (10%): $10

showf "Total: {formatCurrency(total)}"
// Output: Total: $110
```

### Example 8: Complex Real-World Example

```krash
#mathBasic
#ArraysAndStrings

// Define data
str[] employees = ["Alice", "Bob", "Charlie"]
int[] salaries = [50000, 60000, 55000]

// Calculate statistics
int totalSalary = 0
for>: int i = 0, i < salaries.length(), i++:
    totalSalary = totalSalary + salaries[i]
<:
int avgSalary = mathBasic.divide(totalSalary, salaries.length())

// Display results
showf "=== PAYROLL REPORT ==="
showf "Total Employees: {employees.length()}"
// Output: Total Employees: 3

showf "Total Payroll: ${totalSalary}"
// Output: Total Payroll: $165000

showf "Average Salary: ${avgSalary}"
// Output: Average Salary: $55000

showf "\nEmployee List:"
for>: int i = 0, i < employees.length(), i++:
    showf "- {ArraysAndStrings.capitalize(employees[i])}: ${salaries[i]}"
<:
// Output:
// Employee List:
// - Alice: $50000
// - Bob: $60000
// - Charlie: $55000
```

### Example 9: String Processing & Transformation

```krash
str fullText = "hello world from krash"

// Split into words
str[] words = fullText.split(" ")

showf "Original: {fullText}"
// Output: Original: hello world from krash

showf "Word count: {words.length()}"
// Output: Word count: 4

showf "First word: {words[0].toUpperCase()}"
// Output: First word: HELLO

showf "Last word: {words[3].toUpperCase()}"
// Output: Last word: KRASH

// Reconstruct with modifications
showf "Modified: {words[0].toUpperCase()} {words[1]} {words[2]} {words[3].toUpperCase()}"
// Output: Modified: HELLO world from KRASH

// Character operations
showf "Length: {fullText.length()}"
// Output: Length: 22

showf "First char: {fullText.charAt(0).toUpperCase()}"
// Output: First char: H
```

### Example 10: Error Handling with Formatted Output

```krash
try>:
    int age = input>: "Enter your age:"
    if>: age < 0:
        // (throw might not be in simple version)
        show "Invalid age!"
    <: else>:
        showf "You entered: {age}"
        showf "Next year you'll be: {age + 1}"
    <:
<: catch>: ValueError:
    show "Please enter a valid number!"
<:

// Sample run 1 (valid):
// Enter your age: 25
// You entered: 25
// Next year you'll be: 26

// Sample run 2 (invalid):
// Enter your age: hello
// Please enter a valid number!
```

### Example 11: Multiple Format String Operations

```krash
str firstName = "alice"
str lastName = "johnson"
int age = 30
str occupation = "engineer"

// Full profile with nested operations
showf "Name: {firstName.charAt(0).toUpperCase()}{firstName.RmCharAt(0)} {lastName.toUpperCase()}"
// Output: Name: Alice JOHNSON

showf "Age: {age} (Born: {2025 - age})"
// Output: Age: 30 (Born: 1995)

showf "Occupation: {occupation.toUpperCase()}"
// Output: Occupation: ENGINEER

// Combined display
showf "{firstName.charAt(0).toUpperCase()}{firstName.RmCharAt(0)} {lastName}, {age}, {occupation}"
// Output: Alice johnson, 30, engineer
```

### Example 12: Using Libraries in Format Strings

```krash
#mathBasic
#Random
#DateUtils

int a = 10
int b = 20

// Library function in format string
showf "{a} + {b} = {mathBasic.add(a, b)}"
// Output: 10 + 20 = 30

// Random data
int diceRoll = Random.integer(1, 6)
showf "You rolled: {diceRoll}"
// Output: You rolled: 4

// Date operations
str today = DateUtils.today()
showf "Today is: {today}"
// Output: Today is: 2025-06-20

// All combined
int random = Random.integer(1000, 9999)
showf "Ticket #{random} purchased on {today}"
// Output: Ticket #5432 purchased on 2025-06-20
```

---

## NESTED FORMAT STRINGS - THE POWER

**Nested format strings can do ANYTHING.** Here's why they're so powerful:

### You Can Put Any Expression Inside `{}`

```krash
// Variables
showf "{x}"

// Arithmetic
showf "{x + y}"
showf "{x * y}"
showf "{mathBasic.divide(x, y)}"

// String methods
showf "{text.toUpperCase()}"
showf "{text.charAt(0)}"
showf "{text.split(" ")[0]}"

// Array access
showf "{arr[0]}"
showf "{arr[arr.length() - 1]}"

// Dictionary access
showf "{dict{"key"}}"

// Function calls
showf "{myFunction(x, y)}"

// Chained operations
showf "{text.toUpperCase().split(" ")[0]}"

// Conditionals (if supported)
showf "{age >= 18 ? "Adult" : "Minor"}"

// ANY COMBINATION
showf "Name: {name.charAt(0).toUpperCase()}{name.RmCharAt(0)}, Age: {age + 1}, Status: {isActive ? "Active" : "Inactive"}"
```

### Real-World Use Cases

```krash
// Building URLs
str baseUrl = "https://api.example.com"
str endpoint = "users"
int id = 123
showf "{baseUrl}/{endpoint}/{id}"
// Output: https://api.example.com/users/123

// Formatting reports
str name = "Alice"
int score = 85
showf "Student: {name.toUpperCase()} | Score: {score}% | Grade: {score >= 90 ? "A" : "B"}"
// Output: Student: ALICE | Score: 85% | Grade: B

// Building JSON
showf "{"name": "{name}", "score": {score}}"
// Output: {"name": "Alice", "score": 85}

// Data tables
showf "{item.padEnd(20)} | {price.toString().padStart(8)} | {quantity.toString().padStart(5)}"

// Error messages with context
showf "Error at line {lineNum}: {error.toUpperCase()}"

// Progress indicators
int progress = 75
showf "Progress: [{progress}%] {'='*progress}{'_'*(100-progress)}"
```

---

**Krash** is an interpreted programming language written in Python that emphasizes:

- **Readability** – Clear, intuitive syntax similar to Python
- **Simplicity** – Minimal boilerplate, maximum clarity
- **Strictness** – Like Python, enforces good practices
- **Extensibility** – Libraries in both Krash (.ksh) and Python (.py)
- **Developer Experience** – Fast iteration, instant feedback

### Key Characteristics

```
Interpreted:      No compilation step, run directly
Python-Based:     Built on Python interpreter
Strict:           Type checking, scope enforcement, indentation required
Dynamic Typing:   Types inferred automatically but checked strictly
Block Syntax:     Uses >: and <: for code blocks (unique syntax)
4-Space Indent:   Mandatory 4-space indentation (like Python)
```

---

## LANGUAGE DESIGN

### Design Philosophy

Krash is designed to be **"Python-like but with distinct syntax"**. The language borrows Python's strictness and clarity while introducing a unique block syntax using `>:` and `<:` to differentiate from other C-like languages.

### Design Decisions

| Decision | Reason |
|----------|--------|
| **Interpreted** | Faster development, instant feedback, no compilation overhead |
| **Python Base** | Leverage mature runtime, excellent libraries, proven stability |
| **Strict Typing** | Prevent subtle bugs, make code intentions clear |
| **4-Space Indent** | Enforce readable, consistent code structure |
| **>: <: Blocks** | Visually distinct from C, clearer intent, harder to nest incorrectly |
| **givef/give** | Explicit return mechanism, automatic type inference from formatting |

---

## INTERPRETER & EXECUTION

### How Krash Programs Run

```
┌──────────────────────────────────────────────────────────┐
│ Your Krash Program (program.ksh)                         │
│ ┌────────────────────────────────────────────────────┐  │
│ │ #mathBasic                                         │  │
│ │ int x = input>: "Enter number:"                    │  │
│ │ showf "Result: {mathBasic.add(x, 10)}"             │  │
│ └────────────────────────────────────────────────────┘  │
└──────────────────────────────────────────────────────────┘
                         ↓
┌──────────────────────────────────────────────────────────┐
│ Krash Interpreter (written in Python)                    │
│ ┌────────────────────────────────────────────────────┐  │
│ │ 1. Lexical Analysis   (tokenize input)             │  │
│ │ 2. Parsing           (build AST)                    │  │
│ │ 3. Semantic Check    (type checking, scope)        │  │
│ │ 4. Interpretation    (execute instructions)        │  │
│ │ 5. Library Loading   (.ksh or .py files)          │  │
│ └────────────────────────────────────────────────────┘  │
└──────────────────────────────────────────────────────────┘
                         ↓
┌──────────────────────────────────────────────────────────┐
│ Output                                                    │
└──────────────────────────────────────────────────────────┘
```

### Running Programs

```bash
krsh program.ksh                    # Run Krash program directly
krsh run program.ksh                # Alternative syntax
krsh --version                      # Check interpreter version
krsh --help                         # Show help information
```

**No compilation step** – The interpreter processes and executes in one pass.

---

## STRICT BEHAVIOR (Like Python)

### What "Strict" Means in Krash

Krash enforces correctness like Python:

#### 1. **Indentation is Mandatory**

```krash
// ✅ CORRECT - 4-space indentation
if>: x > 5:
    show "x is greater than 5"
<:

// ❌ WRONG - Missing indentation
if>: x > 5:
show "x is greater than 5"
<:

// Output: IndentationError: expected indented block
```

#### 2. **Type Checking**

```krash
// ✅ CORRECT - Types match
int x = 10
int y = 20
int sum = x + y  // Both ints, result is int

// ❌ WRONG - Type mismatch
int x = 10
str y = "hello"
int result = x + y  // Can't add int and str
// Output: TypeError: cannot add 'int' and 'str'
```

#### 3. **Variable Must Be Declared Before Use**

```krash
// ✅ CORRECT
int x = 5
showf "{x}"

// ❌ WRONG - Variable not declared
showf "{y}"
// Output: NameError: variable 'y' is not defined
```

#### 4. **Function Must Be Defined Before Call**

```krash
// ✅ CORRECT
fxn>: greet(str name):
    givef "Hello, {name}"
<:

str msg = greet("Alice")
showf "{msg}"  // Output: Hello, Alice

// ❌ WRONG - Calling before definition
str msg = greet("Alice")  // greet not defined yet!

fxn>: greet(str name):
    givef "Hello, {name}"
<:
// Output: NameError: 'greet' is not defined at line 1
```

#### 5. **Array Index Must Be Valid**

```krash
str[] names = ["Alice", "Bob"]

// ✅ CORRECT
showf "{names[0]}"  // Output: Alice
showf "{names[1]}"  // Output: Bob

// ❌ WRONG - Index out of bounds
showf "{names[5]}"
// Output: IndexError: list index out of range
```

#### 6. **Dictionary Key Must Exist (or check first)**

```krash
mydict{} = {"name": "Alice", "age": 31}

// ✅ CORRECT - Key exists
showf "{mydict{"name"}}"  // Output: Alice

// ✅ CORRECT - Check before access
if>: mydict{}.has("email"):
    showf "{mydict{"email"}}"
<:

// ❌ WRONG - Key doesn't exist
showf "{mydict{"email"}}"
// Output: KeyError: 'email' not found in dictionary
```

#### 7. **Type Casting is Automatic But Careful**

```krash
int x = 10
float y = 3.5
float result = x + y  // int auto-casts to float
showf "{result}"      // Output: 13.5

// ⚠️ CAREFUL - Auto-casting can lose precision
int a = 10
int b = 3
int division = mathBasic.divide(a, b)  // Result is 3 (integer division)
```

#### 8. **No Undefined or Null (Like Python's None)**

```krash
// ❌ WRONG - Can't use undefined variables
showf "{undefined_var}"
// Output: NameError: 'undefined_var' is not defined

// ✅ Krash doesn't have null/undefined
// All variables must be initialized
```

### Strict Error Messages

Like Python, Krash provides **descriptive error messages**:

```krash
int x = "hello"     // TypeError: expected int, got str
for>: int i = 0, i < 5    // SyntaxError: for loop condition incomplete
if>: x = 5:               // SyntaxError: assignment not allowed in condition
```

---

## DATA TYPES

Krash has **4 core data types** (simplified, like Python):

### 1. **int** – Integer Numbers

```krash
int x = 42
int y = -100
int z = 0

showf "{x}"      // Output: 42
showf "{y}"      // Output: -100
showf "{z}"      // Output: 0

// Operations
int sum = 10 + 20        // sum = 30
int diff = 50 - 15       // diff = 35
int prod = 5 * 6         // prod = 30
int div = mathBasic.divide(20, 4)   // div = 5
```

**Valid Operations:**
- Arithmetic: `+`, `-`, `*`, `/`, `%`
- Comparison: `==`, `!=`, `<`, `>`, `<=`, `>=`
- Logical: `&&`, `||`

### 2. **float** – Decimal Numbers

```krash
float pi = 3.14159
float temp = -40.5
float zero = 0.0

showf "{pi}"     // Output: 3.14159
showf "{temp}"   // Output: -40.5

// Mix with int (auto-casting)
float result = 10 + 3.5    // result = 13.5
showf "{result}"           // Output: 13.5
```

**Important:** Integer division loses decimal:
```krash
int div = mathBasic.divide(10, 3)    // div = 3 (not 3.33)
float fdiv = 10 + 0.0 / 3            // fdiv = 3.33... (float division)
```

### 3. **str** – Text Strings

```krash
str name = "Alice"
str empty = ""
str multiline = "Line 1\nLine 2"

showf "{name}"        // Output: Alice
showf "{empty}"       // Output: (empty)
showf "{multiline}"   // Output: 
                      //         Line 1
                      //         Line 2

// Escape sequences
str escaped = "Quote: \" and Backslash: \\"
showf "{escaped}"     // Output: Quote: " and Backslash: \

// String concatenation (implicit in format strings)
str greeting = "Hello, " + "World!"
showf "{greeting}"    // Output: Hello, World!
```

**Valid Operations:**
- Concatenation: `+`
- Comparison: `==`, `!=`
- Methods: `.length()`, `.charAt()`, `.toUpperCase()`, etc.

### 4. **bool** – Boolean (True/False)

```krash
bool success = True
bool failure = False

if>: success:
    show "It worked!"
<:

showf "{success}"     // Output: True
showf "{failure}"     // Output: False

// From comparisons
bool isGreater = 10 > 5   // isGreater = True
bool isEqual = 10 == 10   // isEqual = True
bool isLess = 3 < 2       // isLess = False
```

**Valid Operations:**
- Logical: `&&`, `||`, `!`
- Comparison: All comparison operators return bool

### Type Conversion

```krash
// String to int
int num = int("42")         // num = 42
int bad = int("hello")      // ValueError: invalid literal for int()

// Int to string (automatic in showf)
int age = 25
showf "Age: {age}"          // Output: Age: 25

// Float to int (truncates)
int x = int(3.99)           // x = 3 (not 4)
```

---

## VARIABLES & SCOPE

### Variable Declaration

```krash
int x = 10          // Type required
str name = "Alice"
float pi = 3.14
bool flag = True
```

**Rules:**
- ❌ `x = 10` – Type declaration required
- ✅ `int x = 10` – Correct syntax

### Variable Naming

```krash
// ✅ Valid names
int count = 0
str user_name = "Alice"
float PI_VALUE = 3.14
bool isValid = True

// ❌ Invalid names
int 2count = 0          // Can't start with number
str user-name = ""      // Hyphens not allowed
int class = 5           // 'class' might be reserved
int x y = 10            // Space not allowed
```

### Scope Rules (Function Scope)

```krash
int global_x = 100     // Global scope

fxn>: testScope():
    int local_x = 50   // Local scope (only in function)
    showf "{global_x}"    // Can access global: 100
    showf "{local_x}"     // Can access local: 50
<:

testScope()
showf "{local_x}"       // ❌ Error: local_x not defined globally
// Output: NameError: 'local_x' is not defined
```

### Parameter Shadowing

```krash
int x = 100     // Global x

fxn>: modify(int x):
    x = 200     // This is local x, not global
    showf "Inside: {x}"    // Output: Inside: 200
<:

modify(50)
showf "Outside: {x}"   // Output: Outside: 100 (unchanged)
```

---

## OPERATORS

### Arithmetic Operators

```krash
int a = 10
int b = 3

int add = a + b         // add = 13
int sub = a - b         // sub = 7
int mul = a * b         // mul = 30
int div = mathBasic.divide(a, b)   // div = 3 (integer division)
int mod = a % b         // mod = 1 (remainder)

showf "Add: {add}"      // Output: Add: 13
showf "Sub: {sub}"      // Output: Sub: 7
showf "Mul: {mul}"      // Output: Mul: 30
showf "Div: {div}"      // Output: Div: 3
showf "Mod: {mod}"      // Output: Mod: 1
```

### Comparison Operators

```krash
int x = 10
int y = 20

bool eq = (x == y)      // eq = False
bool neq = (x != y)     // neq = True
bool lt = (x < y)       // lt = True
bool gt = (x > y)       // gt = False
bool lte = (x <= y)     // lte = True
bool gte = (x >= y)     // gte = False

showf "{eq}"            // Output: False
showf "{lt}"            // Output: True
```

### Logical Operators

```krash
bool a = True
bool b = False

bool and_result = a && b        // and_result = False
bool or_result = a || b         // or_result = True
bool not_result = !a            // not_result = False

showf "{and_result}"            // Output: False
showf "{or_result}"             // Output: True
showf "{not_result}"            // Output: False

// Short-circuit evaluation (like Python)
bool result = False && undefined_var   // ✅ Doesn't error (short-circuits)
```

### String Operators

```krash
str a = "Hello"
str b = "World"

str concat = a + " " + b
showf "{concat}"                // Output: Hello World

// Repetition
str repeat = "abc" + "abc"
showf "{repeat}"                // Output: abcabc
```

### Operator Precedence

```
Precedence (highest to lowest):
1. () [] {} .              (parentheses, brackets, member access)
2. * / %                   (multiplication, division, modulo)
3. + -                     (addition, subtraction)
4. < > <= >= == !=        (comparison)
5. &&                      (logical AND)
6. ||                      (logical OR)
```

**Example:**
```krash
int result = 2 + 3 * 4         // result = 14 (not 20)
                                // Multiplication first

int result2 = (2 + 3) * 4      // result2 = 20 (parentheses first)
```

---

## CONTROL FLOW

### If / Elif / Else

```krash
int score = 85

if>: score >= 90:
    show "Grade: A"
<: elif>: score >= 80:
    show "Grade: B"
<: elif>: score >= 70:
    show "Grade: C"
<: else>:
    show "Grade: F"
<:

// Output: Grade: B
```

**Key Points:**
- Condition must evaluate to bool
- ❌ `if>: x:` – Ambiguous, not allowed
- ✅ `if>: x > 0:` – Clear comparison
- All branches closed with `<:`

### For Loop

```krash
// Basic for loop
for>: int i = 0, i < 5, i++:
    showf "Count: {i}"
<:

// Output:
// Count: 0
// Count: 1
// Count: 2
// Count: 3
// Count: 4

// Loop through array
str[] fruits = ["apple", "banana", "cherry"]
for>: int i = 0, i < fruits.length(), i++:
    showf "Fruit: {fruits[i]}"
<:

// Output:
// Fruit: apple
// Fruit: banana
// Fruit: cherry
```

**Syntax:** `for>: init, condition, increment:`

### While Loop

```krash
int count = 0
while>: count < 3:
    showf "Count: {count}"
    count = count + 1
<:

// Output:
// Count: 0
// Count: 1
// Count: 2

// ⚠️ Infinite loop (be careful)
bool running = True
while>: running:
    show "Looping..."
    // Must set running = False somewhere or will loop forever
<:
```

### Break & Continue (If Supported)

```krash
// Break - exit loop early
for>: int i = 0, i < 10, i++:
    if>: i == 5:
        break   // Exit loop
    <:
    showf "{i}"
<:

// Output: 0 1 2 3 4

// Continue - skip to next iteration
for>: int i = 0, i < 5, i++:
    if>: i == 2:
        continue  // Skip this iteration
    <:
    showf "{i}"
<:

// Output: 0 1 3 4
```

---

## FUNCTIONS

### Function Definition

```krash
fxn>: greet(str name):
    givef "Hello, {name}!"
<:

str result = greet("Alice")
showf "{result}"            // Output: Hello, Alice!
```

### Multiple Parameters

```krash
fxn>: add(int a, int b):
    givef "{a + b}"
<:

int sum = add(10, 20)
showf "{sum}"               // Output: 30
```

### No Return Type Specification

```krash
// Type automatically inferred from givef content
fxn>: getInt():
    givef "{42}"            // Returns int
<:

fxn>: getText():
    givef "{"text"}"        // Returns string
<:

fxn>: getFloat():
    givef "{3.14}"          // Returns float
<:
```

### Conditional Returns

```krash
fxn>: classify(int num):
    if>: num > 0:
        givef "Positive"
    <: elif>: num < 0:
        givef "Negative"
    <: else>:
        givef "Zero"
    <:
<:

showf "{classify(5)}"       // Output: Positive
showf "{classify(-3)}"      // Output: Negative
showf "{classify(0)}"       // Output: Zero
```

### Variable Scope in Functions

```krash
int global_var = 100

fxn>: testScope():
    int local_var = 50
    givef "{global_var + local_var}"  // Can access both
<:

int result = testScope()
showf "{result}"            // Output: 150
showf "{local_var}"         // ❌ Error: not defined globally
```

### Function Calling Before Definition

```krash
// ❌ WRONG - greet not defined yet
str msg = greet("Alice")

fxn>: greet(str name):
    givef "Hello, {name}"
<:

// ❌ Output: NameError: 'greet' is not defined

// ✅ CORRECT - define first, then call
fxn>: greet(str name):
    givef "Hello, {name}"
<:

str msg = greet("Alice")
showf "{msg}"               // Output: Hello, Alice
```

---

## ARRAYS & STRINGS

### Array Declaration

```krash
int[] numbers = [10, 20, 30, 40, 50]
str[] names = ["Alice", "Bob", "Charlie"]
bool[] flags = [True, False, True]

showf "{numbers[0]}"        // Output: 10
showf "{names[1]}"          // Output: Bob
showf "{flags[2]}"          // Output: True
```

### String Operations with Nested Format Strings

Nested format strings allow **complex operations directly in output**. Anything that can be done in code can be done in a format string:

```krash
str name = "alice"

// Simple uppercase
showf "{name.toUpperCase()}"
// Output: ALICE

// Capitalize (first letter uppercase)
str capitalized = "{.toUpperCase(name.charAt(0))}{name.RmCharAt(0)}"
showf "{capitalized}"
// Output: Alice

// Combine operations
showf "Hello, {name.toUpperCase()}! Welcome!"
// Output: Hello, ALICE! Welcome!

// Multiple operations chained
str text = "hello world"
showf "Original: {text} | Upper: {text.toUpperCase()} | Length: {text.length()}"
// Output: Original: hello world | Upper: HELLO WORLD | Length: 11
```

### What You Can Do with Nested Format Strings

**ANYTHING** - You can put any valid expression inside `{}`:

#### 1. **Math Operations**

```krash
int x = 10
int y = 20

showf "{x} + {y} = {x + y}"
// Output: 10 + 20 = 30

showf "{x} * {y} = {x * y}"
// Output: 10 * 20 = 200

showf "Average: {(x + y) / 2}"
// Output: Average: 15

showf "Difference: {y - x}"
// Output: Difference: 10
```

#### 2. **String Manipulations**

```krash
str name = "alice"
str greeting = "hello"

// Combine strings
showf "{name.toUpperCase()} says {greeting.toUpperCase()}"
// Output: ALICE says HELLO

// Multiple string methods
str text = "  hello world  "
showf "Original: '{text}' | Cleaned: '{text.RmSpaces()}'"
// Output: Original: '  hello world  ' | Cleaned: 'helloworld'

// Create patterns
showf "{name.charAt(0)}{name.charAt(1)}{name.charAt(2)}"
// Output: alh

// Reverse string
str original = "racecar"
str reversed = ArraysAndStrings.reverse(original)
showf "Original: {original} | Reversed: {reversed}"
// Output: Original: racecar | Reversed: racecar
```

#### 3. **Array Operations**

```krash
int[] nums = [1, 2, 3, 4, 5]

// Array access
showf "First: {nums[0]}, Last: {nums[4]}, Length: {nums.length()}"
// Output: First: 1, Last: 5, Length: 5

// Array calculations
int total = 0
for>: int i = 0, i < nums.length(), i++:
    total = total + nums[i]
<:
showf "Sum: {total}, Average: {mathBasic.divide(total, nums.length())}"
// Output: Sum: 15, Average: 3

// Find specific items
str[] fruits = ["apple", "banana", "cherry"]
showf "First fruit: {fruits[0]}, Random: {fruits.pickRandom()}"
// Output: First fruit: apple, Random: (random fruit)
```

#### 4. **Conditional Logic in Format Strings**

```krash
int age = 25

// Using ternary or conditional (if supported)
// If not supported directly, use variable assignment first
bool isAdult = age >= 18
showf "Age: {age} | Adult: {isAdult}"
// Output: Age: 25 | Adult: True

// Multiple conditions
int score = 85
if>: score >= 90:
    showf "Grade: A (Score: {score})"
<: elif>: score >= 80:
    showf "Grade: B (Score: {score})"
<: else>:
    showf "Grade: C (Score: {score})"
<:
// Output: Grade: B (Score: 85)
```

#### 5. **Complex String Transformations**

```krash
str email = "alice.smith@example.com"

// Extract username
str username = email.split("@")[0]
showf "Username: {username}"
// Output: Username: alice.smith

// Extract domain
str domain = email.split("@")[1]
showf "Domain: {domain}"
// Output: Domain: example.com

// Mask email
str masked = "{username.charAt(0)}***@{domain}"
showf "Masked: {masked}"
// Output: Masked: a***@example.com
```

#### 6. **Dictionary Operations**

```krash
mydict{} = {
    "first": "Alice",
    "last": "Smith",
    "age": 28
}

// Access and combine
showf "Name: {mydict{"first"}} {mydict{"last"}}"
// Output: Name: Alice Smith

// With transformations
showf "User: {mydict{"first"}.toUpperCase()} ({mydict{"age"}} years old)"
// Output: User: ALICE (28 years old)

// Build sentences dynamically
str status = mydict{"age"} >= 18 ? "Adult" : "Minor"
// (If ternary supported, else use if/else)
```

#### 7. **Data Formatting**

```krash
float price = 19.99
int quantity = 5

// Calculate total
float total = price * quantity
showf "Price: ${price} x {quantity} = ${total}"
// Output: Price: $19.99 x 5 = $99.95

// Format numbers
int hours = 2
int minutes = 30
showf "Duration: {hours}h {minutes}m"
// Output: Duration: 2h 30m

// String padding
str item = "Apple"
int stock = 42
showf "{item}...{stock} in stock"
// Output: Apple...42 in stock
```

#### 8. **Creating Tables**

```krash
// Create a simple table
showf "Name      | Age | City"
showf "-"*20
showf "Alice     | 28  | NYC"
showf "Bob       | 35  | LA"
showf "Charlie   | 22  | SF"
// Output:
// Name      | Age | City
// --------------------
// Alice     | 28  | NYC
// Bob       | 35  | LA
// Charlie   | 22  | SF
```

#### 9. **URL/API Building**

```krash
str base = "https://api.example.com"
str endpoint = "users"
int userId = 42

// Build URL
showf "{base}/{endpoint}/{userId}"
// Output: https://api.example.com/users/42

// With query parameters
str name = "alice"
str filter = "active"
showf "{base}/{endpoint}?name={name}&filter={filter}"
// Output: https://api.example.com/users?name=alice&filter=active
```

#### 10. **Text Processing**

```krash
str sentence = "the quick brown fox"

// Title case each word
str[] words = sentence.split(" ")
showf "{words[0].charAt(0).toUpperCase()}{words[0].RmCharAt(0)} {words[1].charAt(0).toUpperCase()}{words[1].RmCharAt(0)} ..."
// Output: The Quick ...

// Word count
showf "Words: {words.length()}"
// Output: Words: 4

// Character count
showf "Characters: {sentence.length()}"
// Output: Characters: 19
```

#### 11. **Date/Time Operations**

```krash
#DateUtils

str today = DateUtils.today()
str time = DateUtils.time()

// Display formatted
showf "Current date and time: {today} at {time}"
// Output: Current date and time: 2025-06-20 at 14:35:45

// Calculate future date
str futureDate = DateUtils.addDays(today, 30)
showf "30 days from now: {futureDate}"
// Output: 30 days from now: 2025-07-20

// Days remaining
int daysLeft = DateUtils.daysUntil("2025-12-31")
showf "Days until year end: {daysLeft}"
// Output: Days until year end: 194
```

#### 12. **Random Data Generation**

```krash
#Random

str[] names = ["Alice", "Bob", "Charlie"]
int[] scores = [Random.integer(0, 100), Random.integer(0, 100), Random.integer(0, 100)]

showf "Winner: {names.pickRandom()} with score {scores[0]}"
// Output: Winner: Bob with score 87

// Generate fake data
showf "ID: {Random.integer(1000, 9999)}, Active: {Random.boolean()}"
// Output: ID: 5432, Active: True
```

#### 13. **HTTP Response Processing**

```krash
#HTTPClient
#JSONParser

try>:
    str response = HTTPClient.get("https://jsonplaceholder.typicode.com/users/1")
    oth user = JSONParser.parse(response)
    
    showf "User: {JSONParser.getString(user, "name")} ({JSONParser.getString(user, "email")})"
    // Output: User: Leanne Graham (Bret@example.com)
<: catch>: NetworkError:
    show "Failed to fetch user"
<:
```

#### 14. **Error Messages with Context**

```krash
int x = -5
str operation = "square"

if>: x < 0:
    showf "ERROR: Cannot {operation} negative number {x}"
<:
// Output: ERROR: Cannot square negative number -5

// With variable context
int line = 42
str error = "TypeError"
showf "At line {line}: {error} - expected int, got str"
// Output: At line 42: TypeError - expected int, got str
```

#### 15. **JSON-like Output**

```krash
str name = "Alice"
int age = 28
str city = "NYC"

// Simulate JSON
showf "{"name": "{name}", "age": {age}, "city": "{city}"}"
// Output: {"name": "Alice", "age": 28, "city": "NYC"}
```

### Complete Real-World Example: User Profile

```krash
str firstName = "alice"
str lastName = "smith"
int userAge = 28
float balance = 1234.56
str[] tags = ["admin", "user", "verified"]

// Build user profile display
showf "=== USER PROFILE ==="
showf "Name: {firstName.charAt(0).toUpperCase()}{firstName.RmCharAt(0)} {lastName.toUpperCase()}"
showf "Age: {userAge} years old"
showf "Account Balance: ${balance}"
showf "Tags: {tags.join(", ")}"
showf "Status: {userAge >= 18 && tags.contains("verified") ? "Verified Member" : "Unverified"}"
showf "ID: {Random.integer(100000, 999999)}"

// Output:
// === USER PROFILE ===
// Name: Alice Smith
// Age: 28 years old
// Account Balance: $1234.56
// Tags: admin, user, verified
// Status: Verified Member
// ID: 543287
```

### Key Insight: Nested Format Strings Are Powerful

**You can do ANYTHING in `{}`:**
- ✅ Math: `{x + y * 2}`
- ✅ String methods: `{name.toUpperCase()}`
- ✅ Array access: `{arr[0]}`
- ✅ Function calls: `{mathBasic.add(x, y)}`
- ✅ Dictionary access: `{dict{"key"}}`
- ✅ Method chaining: `{text.toUpperCase().split(" ")[0]}`
- ✅ Complex expressions: `{scores[0] > 90 ? "Excellent" : "Good"}`

**Format strings are NOT just for display** – they're a complete expression evaluation system that puts code directly in your output.

### Array Length

```krash
int[] nums = [1, 2, 3, 4, 5]

int len = nums.length()
showf "{len}"               // Output: 5

for>: int i = 0, i < nums.length(), i++:
    showf "{nums[i]}"
<:

// Output: 1 2 3 4 5
```

### Array Methods

```krash
str[] words = ["hello", "world", "hello"]

// Check containment
bool has = words.contains("world")
showf "{has}"               // Output: True

// Check empty
bool empty = words.isEmpty()
showf "{empty}"             // Output: False

// Get random item
str random = words.pickRandom()
showf "{random}"            // Output: (random word)

// Remove duplicates
str[] unique = ArraysAndStrings.removeDuplicates(words)
showf "{unique}"            // Output: ["hello", "world"]
```

### String Methods

```krash
str text = "hello world"

// Length
int len = text.length()
showf "{len}"               // Output: 11

// Character at position
str char = text.charAt(0)
showf "{char}"              // Output: h

// Uppercase
str upper = text.toUpperCase()
showf "{upper}"             // Output: HELLO WORLD

// Lowercase
str lower = text.toLowerCase()
showf "{lower}"             // Output: hello world

// Contains
bool has = text.contains("world")
showf "{has}"               // Output: True

// Split
str[] parts = text.split(" ")
showf "{parts[0]}"          // Output: hello
showf "{parts[1]}"          // Output: world
```

### String Manipulation

```krash
str original = "  hello world  "

// Remove spaces
str trimmed = original.RmSpaces()
showf "{trimmed}"           // Output: helloworld

// First character uppercase
str capitalized = ArraysAndStrings.capitalize("hello")
showf "{capitalized}"       // Output: Hello

// Reverse
str reversed = ArraysAndStrings.reverse("hello")
showf "{reversed}"          // Output: olleh
```

---

## DICTIONARIES

### Dictionary Declaration

```krash
mydict{} = {
    "name": "Alice",
    "age": 31,
    "city": "NYC"
}

showf "{mydict{"name"}}"    // Output: Alice
showf "{mydict{"age"}}"     // Output: 31
```

### Dictionary Operations

```krash
mydict{} = {"name": "Alice", "age": 31}

// Check key exists
bool has = mydict{}.has("name")
showf "{has}"               // Output: True

bool no = mydict{}.has("email")
showf "{no}"                // Output: False

// Add key-value
mydict{}.Add{"email": "alice@example.com"}
showf "{mydict{"email"}}"   // Output: alice@example.com

// Remove key-value
mydict{}.Rm{"age"}
// Age is now gone

// Get all keys
str[] keys = mydict{}.keys()
showf "{keys}"              // Output: ["name", "email"]

// Get all values
str[] values = mydict{}.values()
showf "{values}"            // Output: ["Alice", "alice@example.com"]
```

### Dictionary with Type Mixing

```krash
mydict{} = {
    "name": "Alice",
    "age": 31,
    "active": True,
    "scores": [90, 85, 88]
}

showf "{mydict{"name"}}"        // Output: Alice
showf "{mydict{"age"}}"         // Output: 31
showf "{mydict{"active"}}"      // Output: True

// ⚠️ Arrays in dicts are tricky - implementation dependent
```

---

## ERROR HANDLING

### Try/Catch Blocks

```krash
try>:
    int age = input>: "Enter your age:"
    if>: age < 0:
        throw ValueError("Age can't be negative")
    <:
    showf "You are {age} years old"
<: catch>: ValueError:
    show "Please enter a valid age!"
<:
```

### Multiple Error Types

```krash
try>:
    str response = HTTPClient.get("https://api.example.com/users/123")
    int id = int(response)
<: catch>: NetworkError:
    show "Network error occurred"
<: catch>: ValueError:
    show "Could not parse response"
<:
```

### Error Types

| Error | Cause | Example |
|-------|-------|---------|
| `ValueError` | Invalid value | `int("hello")`, division by zero |
| `TypeError` | Wrong type | `"text" + 5` |
| `NameError` | Variable undefined | Using undefined variable |
| `IndexError` | Array index out of bounds | `arr[100]` for 5-element array |
| `KeyError` | Dictionary key missing | `dict{"nonexistent"}` |
| `FileError` | File operation failed | Reading non-existent file |
| `NetworkError` | HTTP request failed | Server unreachable |
| `IndentationError` | Wrong indentation | Inconsistent spacing |
| `SyntaxError` | Invalid syntax | Malformed statement |

---

## FILE I/O

### Writing to Files

```krash
// Create new file
write>: "Hello, World!":
    .new("hello.txt")
<:

// File now contains:
// Hello, World!

// Append to file
write>: "Another line":
    .append("hello.txt")
<:

// File now contains:
// Hello, World!Another line

// Multi-line write
write>: "Line 1\nLine 2\nLine 3":
    .new("multiline.txt")
<:

// File now contains:
// Line 1
// Line 2
// Line 3
```

### Reading from Files

```krash
read>: ("hello.txt"):
    str first = read.getFirstLine()
    showf "{first}"                 // Output: Hello, World!
    
    str all = read.getAllLines()
    showf "{all}"                   // Output: (all lines as array)
<:

// Get specific line
read>: ("multiline.txt"):
    str line2 = read.getLine(2)
    showf "{line2}"                 // Output: Line 2
<:
```

### File Utilities

```krash
#FileUtils

// Check if file exists
bool exists = FileUtils.fileExists("data.txt")
if>: exists:
    show "File exists"
<: else>:
    show "File not found"
<:

// Get file size
int size = FileUtils.fileSize("data.txt")
showf "File size: {size} bytes"     // Output: File size: 42 bytes

// Copy file
FileUtils.copyFile("original.txt", "backup.txt")

// Rename file
FileUtils.renameFile("old.txt", "new.txt")

// Clear file
FileUtils.clearFile("log.txt")

// List files
str[] files = FileUtils.listFiles("./documents")
for>: int i = 0, i < files.length(), i++:
    showf "{files[i]}"
<:
```

---

## HTTP REQUESTS

### GET Request

```krash
#HTTPClient

try>:
    str response = HTTPClient.get("https://jsonplaceholder.typicode.com/users/1")
    showf "{response}"
<: catch>: NetworkError:
    show "Failed to fetch data"
<:

// Output:
// {"id":1,"name":"Leanne Graham","username":"Bret",...}
```

### POST Request

```krash
#HTTPClient

str payload = "{"name": "John", "email": "john@example.com"}"
try>:
    str response = HTTPClient.post("https://api.example.com/users", payload)
    showf "{response}"
<: catch>: NetworkError:
    show "Failed to create user"
<:
```

### Request with Headers

```krash
#HTTPClient

str[] headers = [
    "Authorization: Bearer token123",
    "Content-Type: application/json"
]

str data = "{"message": "Hello"}"
try>:
    str response = HTTPClient.post(
        "https://api.example.com/message",
        data,
        headers
    )
    showf "{response}"
<: catch>: NetworkError:
    show "Request failed"
<:
```

### All HTTP Methods

```krash
#HTTPClient

// GET
str get_resp = HTTPClient.get("https://api.example.com/users/1")

// POST
str post_resp = HTTPClient.post("https://api.example.com/users", data)

// PUT
str put_resp = HTTPClient.put("https://api.example.com/users/1", data)

// DELETE
str del_resp = HTTPClient.delete("https://api.example.com/users/1")

// PATCH
str patch_resp = HTTPClient.patch("https://api.example.com/users/1", data)
```

---

## IMPORTS & LIBRARIES

### Standard Libraries

```krash
#mathBasic          // Basic arithmetic
#ArraysAndStrings   // Array/string utilities
#HTTPClient         // HTTP requests
#FileUtils          // File operations
#JSONParser         // JSON parsing
#DateUtils          // Date/time operations
#Random             // Random generation
```

### Using Libraries

```krash
#mathBasic

int sum = mathBasic.add(10, 20)
showf "{sum}"           // Output: 30

#Random

int roll = Random.integer(1, 6)
showf "Dice: {roll}"    // Output: Dice: 4
```

### Multiple Imports

```krash
#mathBasic
#ArraysAndStrings
#HTTPClient

int math_result = mathBasic.add(5, 5)
str str_result = ArraysAndStrings.capitalize("hello")
str http_result = HTTPClient.get("https://api.example.com/data")

showf "{math_result}"       // Output: 10
showf "{str_result}"        // Output: Hello
showf "{http_result}"       // Output: (API response)
```

### Custom Libraries

**myLib.ksh:**
```krash
fxn>: square(int x):
    givef "{x * x}"
<:

fxn>: cube(int x):
    givef "{x * x * x}"
<:
```

**Usage:**
```krash
#myLib

int sq = myLib.square(5)
int cb = myLib.cube(5)
showf "{sq}"            // Output: 25
showf "{cb}"            // Output: 125
```

### Python Libraries

**myPyLib.py:**
```python
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
```

**Usage:**
```krash
#myPyLib

int fact = myPyLib.factorial(5)
int fib = myPyLib.fibonacci(10)
showf "{fact}"          // Output: 120
showf "{fib}"           // Output: 55
```

---

## INDENTATION RULES

### 4-Space Indentation (Mandatory)

```krash
// ✅ CORRECT - Exactly 4 spaces per level
if>: x > 5:
    show "Greater"
<:

// ❌ WRONG - Only 2 spaces
if>: x > 5:
  show "Greater"
<:
// Output: IndentationError: expected 4 spaces, got 2

// ❌ WRONG - Tab character
if>: x > 5:
	show "Greater"      // Tab, not 4 spaces
<:
// Output: IndentationError
```

### Nested Indentation

```krash
for>: int i = 0, i < 3, i++:
    if>: i > 0:
        show "Greater than 0"       // 8 spaces (2 levels)
    <:
<:

// Output:
// Greater than 0
// Greater than 0
```

### Closing Block Syntax

```krash
// ✅ CORRECT - Both valid
// Style 1: Closing on next line
if>: x > 5:
    show "text"
<:

// Style 2: Closing on same line
if>: x > 5:
    show "text"<:

// ❌ WRONG - Extra spaces before <:
if>: x > 5:
    show "text" <:
    // Error: unexpected token
```

---

## TYPE SYSTEM

### Type Inference

```krash
// ✅ Type automatically inferred
int x = 42              // int inferred
str name = "Alice"      // str inferred
float pi = 3.14         // float inferred
bool flag = True        // bool inferred

// ❌ Type required in declaration
x = 42                  // SyntaxError: type required
```

### Type Coercion Rules

```krash
// Int to float (automatic, safe)
int a = 10
float b = a + 3.5       // b = 13.5 (int 10 coerced to float)

// Float to int (truncates, might lose data)
float c = 3.99
int d = int(c)          // d = 3 (decimal lost)

// String to int
int e = int("42")       // e = 42
int f = int("hello")    // ValueError: invalid literal
```

### Type Checking

```krash
// Type checking is done at runtime (like Python)
int x = 10
x = "hello"             // TypeError: cannot assign str to int

// Mixed types in operations
int result = 10 + "20"  // TypeError: unsupported operand types
```

---

## BEST PRACTICES

### 1. Always Declare Types

```krash
// ✅ GOOD
int count = 0
str name = "Alice"
bool active = True

// ❌ BAD
count = 0           // Type not specified
```

### 2. Use Meaningful Variable Names

```krash
// ✅ GOOD
int user_age = 25
str first_name = "Alice"
bool is_active = True

// ❌ BAD
int ua = 25
str fn = "Alice"
bool ia = True
```

### 3. Initialize Variables Before Use

```krash
// ✅ GOOD
int count = 0
for>: int i = 0, i < 5, i++:
    count = count + 1
<:

// ❌ BAD
for>: int i = 0, i < 5, i++:
    count = count + 1   // count not initialized
<:
```

### 4. Check Dictionary Keys Before Access

```krash
// ✅ GOOD
if>: mydict{}.has("key"):
    showf "{mydict{"key"}}"
<:

// ❌ BAD
showf "{mydict{"key"}}"  // KeyError if key doesn't exist
```

### 5. Use Try/Catch for Risky Operations

```krash
// ✅ GOOD
try>:
    int num = input>: "Enter number:"
    showf "You entered: {num}"
<: catch>: ValueError:
    show "Please enter a valid number"
<:

// ❌ BAD
int num = input>: "Enter number:"  // No error handling
showf "{num}"
```

### 6. Use Libraries for Common Tasks

```krash
// ✅ GOOD
#mathBasic
int sum = mathBasic.add(10, 20)

// ❌ BAD (reinventing the wheel)
fxn>: add(int a, int b):
    givef "{a + b}"
<:
int sum = add(10, 20)
```

### 7. Keep Functions Small and Focused

```krash
// ✅ GOOD
fxn>: calculateTax(float amount):
    givef "{amount * 0.1}"
<:

fxn>: calculateTotal(float amount):
    float tax = calculateTax(amount)
    givef "{amount + tax}"
<:

// ❌ BAD (doing too much)
fxn>: processPayment(float amount, str name, str address):
    // 50 lines of mixed logic
<:
```

### 8. Use Consistent Indentation

```krash
// ✅ GOOD - Consistent 4 spaces
if>: x > 5:
    show "text"
<:
for>: int i = 0, i < 5, i++:
    show "i"
<:

// ❌ BAD - Inconsistent spacing
if>: x > 5:
  show "text"
<:
for>: int i = 0, i < 5, i++:
    show "i"
<:
```

---

## COMMON MISTAKES

### 1. Forgetting Type Declaration

```krash
// ❌ WRONG
name = "Alice"

// ✅ CORRECT
str name = "Alice"

// Error: SyntaxError: expected type declaration
```

### 2. Wrong Indentation

```krash
// ❌ WRONG - Only 2 spaces
if>: x > 5:
  show "text"
<:

// ✅ CORRECT - 4 spaces
if>: x > 5:
    show "text"
<:

// Error: IndentationError: expected 4 spaces, got 2
```

### 3. Using Variable Before Definition

```krash
// ❌ WRONG
showf "{name}"
str name = "Alice"

// ✅ CORRECT
str name = "Alice"
showf "{name}"

// Error: NameError: 'name' is not defined
```

### 4. Type Mismatch in Assignment

```krash
// ❌ WRONG
int x = "hello"

// ✅ CORRECT
str x = "hello"

// Error: TypeError: expected int, got str
```

### 5. Array Index Out of Bounds

```krash
str[] arr = ["a", "b", "c"]

// ❌ WRONG
showf "{arr[10]}"

// ✅ CORRECT - Check bounds first
if>: 10 < arr.length():
    showf "{arr[10]}"
<: else>:
    show "Index out of bounds"
<:

// Error: IndexError: list index out of range
```

### 6. Dictionary Key Not Found

```krash
mydict{} = {"name": "Alice"}

// ❌ WRONG
showf "{mydict{"age"}}"

// ✅ CORRECT
if>: mydict{}.has("age"):
    showf "{mydict{"age"}}"
<: else>:
    show "Key not found"
<:

// Error: KeyError: 'age' not found
```

### 7. Missing Closing Block

```krash
// ❌ WRONG
if>: x > 5:
    show "text"

// ✅ CORRECT
if>: x > 5:
    show "text"
<:

// Error: SyntaxError: expected <:
```

### 8. Function Call Before Definition

```krash
// ❌ WRONG
int result = add(5, 5)

fxn>: add(int a, int b):
    givef "{a + b}"
<:

// ✅ CORRECT
fxn>: add(int a, int b):
    givef "{a + b}"
<:

int result = add(5, 5)

// Error: NameError: 'add' is not defined
```

### 9. Using Comparison as Condition (Ambiguous)

```krash
int x = 10

// ❌ WRONG - Ambiguous
if>: x:
    show "x is truthy"
<:

// ✅ CORRECT - Explicit
if>: x > 0:
    show "x is positive"
<:

// Error: TypeError: expected bool, got int
```

### 10. Integer Division Losing Decimals

```krash
int a = 10
int b = 3

// ❌ WRONG - Expects float result
int result = a / b      // SyntaxError or wrong result

// ✅ CORRECT - Use mathBasic.divide
int result = mathBasic.divide(a, b)     // result = 3
float fresult = a + 0.0 / b             // fresult = 3.33...
```

---

## ADVANCED TOPICS

### Nested Blocks

```krash
for>: int i = 0, i < 3, i++:
    for>: int j = 0, j < 3, j++:
        showf "({i}, {j})"
    <:
<:

// Output:
// (0, 0)
// (0, 1)
// (0, 2)
// (1, 0)
// (1, 1)
// (1, 2)
// (2, 0)
// (2, 1)
// (2, 2)
```

### Nested Functions (If Supported)

```krash
fxn>: outer(int x):
    fxn>: inner(int y):
        givef "{x + y}"
    <:
    // May or may not be supported
<:
```

### Closures (If Supported)

```krash
fxn>: makeAdder(int x):
    fxn>: adder(int y):
        givef "{x + y}"
    <:
    // Implementation dependent
<:
```

---

## PERFORMANCE NOTES

### Execution Speed

- **Interpreted:** Slower than compiled languages (like Python)
- **Good For:** Scripts, automation, prototyping
- **Not Ideal For:** Real-time systems, games, heavy computation

### Memory Usage

- **Dynamic Allocation:** Lists/dicts grow as needed
- **No Manual Management:** GC handles cleanup (like Python)
- **Efficient:** Leverages Python's optimized memory management

### Optimization Tips

```krash
// ✅ Good - Pre-allocate if possible
for>: int i = 0, i < 1000, i++:
    // do something
<:

// ❌ Avoid - Redundant operations in loop
for>: int i = 0, i < list.length(), i++:  // length() called each iteration
    show list[i]
<:

// ✅ Better - Cache length
int len = list.length()
for>: int i = 0, i < len, i++:
    show list[i]
<:
```

---

## GETTING HELP

### Resources

- **Official Spec:** KRASH_LANGUAGE_SPEC.md
- **Libraries:** KRASH_LIBRARIES_README.md
- **GitHub:** https://github.com/KAKUDEV-web/Krash
- **Issues:** Report bugs on GitHub

### Debugging Tips

1. **Read Error Messages** – They're descriptive (like Python)
2. **Check Indentation** – Must be exactly 4 spaces
3. **Check Variable Scope** – Variables must be declared first
4. **Use showf** – Add debugging output
5. **Use Try/Catch** – Catch and handle errors explicitly

### Example Debugging

```krash
// Add output to track execution
showf "Start of program"

int x = input>: "Enter number:"
showf "Received: {x}"

int result = mathBasic.add(x, 10)
showf "Result: {result}"

// Output:
// Start of program
// Enter number: (user input)
// Received: 42
// Result: 52
```

---

## CONCLUSION

**Krash** is a **strict, interpreted programming language** that emphasizes clarity, correctness, and ease of use. By following the principles outlined in this document and adhering to Python-like strictness, you can write reliable, maintainable Krash programs.

**Key Takeaways:**
- ✅ Strict about types, scope, indentation
- ✅ Interpreted (no compilation overhead)
- ✅ Python-based (leverage ecosystem)
- ✅ Clear error messages
- ✅ Fast development and prototyping
- ✅ Extensible with libraries

Happy coding with Krash! 🚀

---

**Document Version:** 1.0  
**Krash Version:** 1.0  
**Last Updated:** 2025  
**Author:** Krash Community
