# KRASH PROGRAMMING LANGUAGE
**Version 1.0 – Complete Specification**

Krash is a new programming language written in Python. It is a general-purpose language with clear, readable syntax and short code lines (once libraries are available). This is an **interpreted language** (not compiled).

**Important:** All blocks require **4-space indentation**. Closing `<:` can be on the next line or same line as the last statement.

---

## PACKAGE MANAGEMENT SYSTEM

Krash uses a built-in package manager similar to Python's `pip`:

```bash
krsh --install --ArraysAndStrings    // Downloads from GitHub (installed globally)
krsh --install --math
krsh --install --HTTPClient
krsh --remove --ArraysAndStrings     // Uninstalls library
krsh --list                          // Lists installed libraries
```

Libraries are downloaded once globally and available to all projects. You do NOT need to include `.ksh` files in your project folder.

---

## BASICS (ULTIMATE)

| Symbol | Description |
|--------|-------------|
| `show "...."` | Prints text |
| `#LibraryName` | Import library (no `.ksh` extension needed) |
| `//` | Single line comment |
| `/ multi line /` | Multi-line comment |
| `input>: "..."` | Take user input |
| `showf "Text is... {val}"` | Format the printed text |

---

## VARIABLE TYPES

```
str → string ("Alice")
int → integer (10)
float → decimal number (3.14)
bool → boolean (True / False)
```

**Note:** Simplified type system. Use built-in string methods for string validation.

---

## EXAMPLES

### 1. Hello, World!
```krash
show "Hello, World!"
// output: Hello, World!
```

---

### 2. Variables & Formatting
```krash
str name = "Alice"
int age = 31
showf "The age of {name} is {age}"
```

---

### 3. Basic Math & Input
```krash
int a = input>: "Type a number."
int b = 10
int add = a + b
showf "{add}"
showf "{a} * {b}"      // Prints result of a*b
showf "{a} / {b}"      // Prints result of a/b
```

---

### 4. If / Elif / Else Statements

```krash
if>: score >= 90:
    show "Great!"
<:
elif>: score >= 50:
    show "Good!"
<:
else>:
    show "Try again"<:
```

**Syntax:**
- `if>: ... :` → if statement (4-space indent, then `<:`)
- `elif>: ... :` → else if statement
- `else>: ... :` → else statement

**Note:** Closing `<:` can be on same line or next line (both valid)

---

### 5. For Loop

```krash
for>: int i = 0, i <= 5, i++:
    showf "Count: {i}"
<:
```

**Note:** Comma-separated conditions. Requires 4-space indentation.

---

### 6. While Loop

```krash
int count = 0
while>: count < 10:
    showf "Count: {count}"
    count = count + 1
<:
```

---

### 7. Functions

```krash
fxn>: add(int a, int b):
    givef "{a + b}"
<:

int x = 10
int y = 20
int res = add(x, y)
showf "{res}"           // prints 30
showf "{add(x, y)}"     // prints 30
```

**Syntax:**
- `fxn>: ... :` → Define function with 4-space indent
- `givef "..."` → Return formatted value (automatically types the return)
- `give value` → Return value (type inferred)
- Closing `<:` on same or next line

---

### 8. Function with Multiple Operations (Conditional Return)

```krash
fxn>: addAndMultiply(int a, int b, str op):
    if>: op.equals("add"):
        givef "{a + b}"         // int result
    <: elif>: op.equals("multiply"):
        givef "{a * b}"         // int result
    <: else>:
        givef "InvalidOperationError"   // str result (error)
    <:
<:

int x = 10
int b = 20
int resultA = addAndMultiply(x, b, "add")       // resultA value = 30
showf "{resultA}"

int resultM = addAndMultiply(x, b, "multiply")  // resultM = 200
showf "{resultM}"
```

**Note:** Functions with multiple conditional returns allow different operations based on parameters.

---

## VARIABLE SCOPE IN FUNCTIONS

Variables defined inside functions are **local to that function** and different from variables in outer scope:

```krash
int a = 5           // Outer scope variable

fxn>: testFunc(int b):
    int a = 10      // Local function variable (different from outer a)
    givef "{a + b}"
<:

int result = testFunc(6)
showf "{result}"    // prints 16 (uses function's a=10, not outer a=5)
showf "{a}"         // prints 5 (outer a unchanged)
```

**Key Points:**
- Function parameters create new local variables
- Variables inside function don't affect outer scope
- `givef` uses function's local variables, NOT outer scope variables
- Each function has its own variable namespace

---

## ARRAYS & STRINGS

### Declaration
```krash
int scores[] = [90, 80, 100, 120]
str names[] = ["Alice", "Leo", "Krash"]
```

### String & Array Methods

```
.length()           → get length of array or string
.charAt(index)      → get character at position
.RmCharAt(index)    → removes character at position
.toUpperCase()      → change to uppercase
.toLowerCase()      → change to lowercase
.contains(val)      → check if array/string contains value (True/False)
.equals(val)        → compare string or array value (True/False)
.highestNum()       → find highest number in int array
.lowestNum()        → find lowest number in int array
.split(delimiter)   → split text to array
.RmSpaces()         → removes spaces in string
.isEmpty()          → check if array or string is empty (True/False)
.pickRandom()       → picks random item from array
.RmDuplicate()      → removes duplicate values from array
.join(delimiter)    → joins array elements into string
.reverse()          → reverses array or string
```

### Array & String Examples

```krash
int scores[] = [90, 20, 40, 50, 100]

// Access and math
showf "{scores[0] + scores[1]}"     // prints 110

// Loop through array
for>: int i = 0, i < scores.length(), i++:
    showf "Score: {scores[i]}"
<:

// String operations
str text = "hello world"
showf "{text.toUpperCase()}"        // HELLO WORLD
showf "{text.contains("world")}"    // True

// Split string
str[] words = text.split(" ")
showf "{words[0]}"                  // hello

// Pick random from array
str[] names = ["Alice", "Bob", "Charlie"]
showf "{names.pickRandom()}"        // Random name
```

---

## DICTIONARIES

```krash
mydict{} = {"name": "Alice",
            "age": 31,
            "school": "Tech Academy"}

// Access
showf "{mydict{"name"}}"            // Alice

// Check key exists
if>: mydict{}.has("school"):
    show "Has school key"
<:

// Add key-value
mydict{}.Add{"class": 12}

// Remove key-value
mydict{}.Rm{"age"}

// Get all keys
str[] keys = mydict{}.keys()

// Get all values
str[] values = mydict{}.values()
```

---

## TRY / CATCH (Error Handling)

```krash
try>:
    int age = input>: "Enter your age:"
    int next_year_age = age + 1
    showf "Next year you'll be {next_year_age}"
<: catch>: ValueError:
    show "Please enter a valid number!"
<:
```

**Syntax:**
- `try>: ... :` → Try block with 4-space indent
- `<: catch>: ErrorType: ... <:` → Catch block (same or next line)

**Supported Error Types:**
- `ValueError` → Wrong type entered
- `FileError` → File operation failed
- `NetworkError` → HTTP/Network request failed
- `IndexError` → Array index out of bounds
- `KeyError` → Dictionary key not found

---

## FILE I/O

### Write to File

```krash
// Create new file
write>: "Hello, World! \n Welcome to Krash": .new("File.txt")<:

// Append to file
write>: "New line added": .append("File.txt")<:
```

### Read from File

```krash
read>: ("File.txt"):
    showf "{read.getFirstLine()}"       // prints 1st line
    showf "{read.getLine(2)}"           // prints 2nd line
    showf "{read.getAllLines()}"        // prints all lines as array
    showf "{read.getWord(1)}"           // prints 1st word of file
<:
```

### File Methods

```
.new(filename)      → creates new file (overwrites if exists)
.append(filename)   → appends to file
.getFirstLine()     → gets first line
.getLine(number)    → gets specific line number
.getAllLines()      → gets all lines as array
.getWord(number)    → gets word at position
.getCharAt(index)   → gets character at position
.removeFile()       → deletes file
```

---

## HTTP REQUESTS (GET / POST)

**Note:** Requires `#HTTPClient` library. Download with: `ksh --install --HTTPClient`

### HTTP GET Request

```krash
#HTTPClient

str response = HTTPClient.get("https://api.example.com/users")

// With error handling
try>:
    str data = HTTPClient.get("https://api.example.com/data")
    showf "{data}"
<: catch>: NetworkError:
    show "Failed to fetch data"
<:
```

### HTTP POST Request

```krash
#HTTPClient

str payload = "{"name": "Alice", "age": 31}"
str response = HTTPClient.post("https://api.example.com/users", payload)
showf "{response}"
```

### HTTP Request with Headers

```krash
#HTTPClient

str[] headers = ["Authorization: Bearer token123",
                 "Content-Type: application/json"]

str payload = "{"message": "Hello"}"
str response = HTTPClient.post("https://api.example.com/message", payload, headers)
showf "{response}"
```

### HTTP Methods & Options

```krash
str getResponse = HTTPClient.get(url)
str postResponse = HTTPClient.post(url, data)
str putResponse = HTTPClient.put(url, data)
str deleteResponse = HTTPClient.delete(url)
str patchResponse = HTTPClient.patch(url, data)

// With timeout (in milliseconds)
str response = HTTPClient.get(url, 5000)

// Parse JSON response
str json_str = HTTPClient.get("https://api.example.com/users")
// Parse using string methods or use #JSONParser library
```

### Complete HTTP Example

```krash
#HTTPClient
#JSONParser

try>:
    str response = HTTPClient.get("https://jsonplaceholder.typicode.com/users/1")
    showf "Response: {response}"

    // Parse JSON (if JSONParser library available)
    oth user = JSONParser.parse(response)
    showf "Name: {user{"name"}}"
    showf "Email: {user{"email"}}"
<: catch>: NetworkError:
    show "Network request failed"
<: catch>: ValueError:
    show "Invalid JSON response"
<:
```

---

## IMPORTS & LIBRARIES

### How Imports Work

Libraries are `.ksh` files downloaded globally via package manager. When importing, use the library name without `.ksh` extension:

```krash
#math
#ArraysAndStrings
#HTTPClient
#FileUtils
```

### Installing Libraries

```bash
ksh --install --math
ksh --install --ArraysAndStrings
ksh --install --HTTPClient
ksh --install --FileUtils
```

Libraries are downloaded once and available to all projects (like `pip install`).

### Using Library Functions

```krash
#ArraysAndStrings

str name = "alice"
str capitalized = ArraysAndStrings.capitalize(name)
showf "{capitalized}"       // Alice
```

### Creating Your Own Library

Create file: `MyLibrary.ksh`

```krash
fxn>: add(int a, int b):
    givef "{a + b}"
<:

fxn>: multiply(int a, int b):
    givef "{a * b}"
<:

fxn>: greet(str name):
    givef "Hello, {name}!"
<:
```

Then in your main file:
```krash
#MyLibrary

int result = MyLibrary.add(5, 10)
showf "{result}"                // 15

str greeting = MyLibrary.greet("Alice")
showf "{greeting}"              // Hello, Alice!
```

### Standard Libraries (Built-in)

These come pre-installed:

- **#math** → Mathematical functions (sqrt, pow, abs, sin, cos, etc.)
- **#mathBasic** → Basic arithmetic with error handling (Add, Subtract, Multiply, Divide)
- **#ArraysAndStrings** → Array/string utilities beyond basic methods
- **#FileUtils** → Advanced file operations
- **#HTTPClient** → HTTP GET/POST requests
- **#JSONParser** → JSON parsing and generation
- **#DateUtils** → Date and time operations
- **#Random** → Random number/item generation

#### mathBasic.ksh Example

The `mathBasic` library provides safe arithmetic operations with error handling:

```krash
#mathBasic

int a = 10
int b = 5

int sum = mathBasic.add(a, b)           // sum = 15
int diff = mathBasic.subtract(a, b)     // diff = 5
int prod = mathBasic.multiply(a, b)     // prod = 50

// Division with error handling
try>:
    int quotient = mathBasic.divide(a, b)   // quotient = 2
<: catch>: ValueError:
    show "Cannot divide by zero"
<:
```

**mathBasic Functions:**
- `add(int a, int b)` → Returns a + b
- `subtract(int a, int b)` → Returns a - b
- `multiply(int a, int b)` → Returns a * b
- `divide(int a, int b)` → Returns a / b (throws ValueError if b == 0)

---

## NESTED FORMAT STRINGS

You can use nested format strings with expressions:

```krash
str name = "alice"
str greeting = showf "Hello {.toUpperCase(name.charAt(0))}{name.RmCharAt(0)}"
// greeting = "Hello Alice"

int[] nums = [1, 2, 3, 4, 5]
showf "Sum of first two: {nums[0] + nums[1]}"

int age = 25
showf "Next year: {age + 1} years old"

// With function calls
showf "Random name: {names.pickRandom()}"
```

---

## COMPLETE EXAMPLE PROGRAM

```krash
#ArraysAndStrings
#HTTPClient

fxn>: calculateGrade(int score):
    if>: score >= 90:
        givef "A"
    <: elif>: score >= 80:
        givef "B"
    <: elif>: score >= 70:
        givef "C"
    <: else>:
        givef "F"
    <:
<:

// Main program
str student_name = input>: "Enter student name:"
int score = input>: "Enter score:"

str grade = calculateGrade(score)
showf "{student_name} scored {score} and got grade {grade}"

// Store results
write>: "{student_name}, {score}, {grade}": .append("results.txt")<:

// Fetch data from API
try>:
    str api_response = HTTPClient.get("https://api.example.com/students")
    showf "API Response: {api_response}"
<: catch>: NetworkError:
    show "Could not fetch from API"
<:
```

---

## INDENTATION & BLOCK SYNTAX

### 4-Space Indentation Rule

All blocks in Krash require **exactly 4 spaces** of indentation, similar to Python:

```krash
if>: x > 5:
    show "x is greater than 5"      // 4 spaces
<:
```

### Flexible Closing Syntax

The closing `<:` can be placed **on the same line** or **next line**:

**Style 1: Closing on next line (cleaner)**
```krash
if>: score >= 90:
    show "Great!"
<:
```

**Style 2: Closing on same line**
```krash
if>: score >= 90:
    show "Great!"<:
```

**Both are valid.** Choose whichever you prefer.

**Important Spacing Note:**
- Spaces between `if>:`, `:`, and `<:` are **meaningful** - do NOT add extra spaces
- Like Python, spaces matter for clarity and error detection
- Example of correct spacing:
  ```krash
  if>: condition:     // correct: no gaps
      code
  <:                  // correct: <: on new line, no space before
  ```
- Example of INCORRECT spacing:
  ```krash
  if >: condition :   // ❌ WRONG: spaces between symbols
  ```

### Nested Blocks Example

```krash
if>: x > 10:
    for>: int i = 0, i < 5, i++:
        if>: i % 2 == 0:
            showf "Even: {i}"
        <:
    <:
<:
```

Each level requires its own 4-space indentation.

---

## SPECIAL CHARACTERS & ESCAPE SEQUENCES

```
\n      → new line
\t      → tab
\"      → double quote
\\      → backslash
\r      → carriage return
```

Example:
```krash
show "Line 1\nLine 2\tTabbed"
// output:
// Line 1
// Line 2	Tabbed
```

---

## OPERATOR PRECEDENCE

```
1. () [] {} .
2. * / %
3. + -
4. < > <= >= == !=
5. && 
6. ||
```

---

## RUNNING KRASH PROGRAMS

```bash
krsh program.ksh                      // Run Krash program
krsh run program.ksh                  // Alternative syntax

krsh --version                        // Check version
krsh --help                           // Show help
```

**Note:** Krash programs are interpreted directly by the Python-based interpreter. No compilation step is needed.

---

## NOTES FOR DEVELOPERS

- Krash is an **interpreted language** built with Python
- All libraries can be written in both Krash (`.ksh`) and Python
- Python libraries integrate seamlessly with the Krash interpreter
- Type inference is automatic when using `givef`
- Error handling is optional but recommended
- All strings support Unicode
- Case-sensitive language
- Tab/space indentation is ignored (use `<:` and `:` for blocks)
- Fast development and prototyping (no compilation needed)

---

**Krash v1.0 – Ready for implementation!** 🚀
