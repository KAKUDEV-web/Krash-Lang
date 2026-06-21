# Krash Standard Libraries

Official standard libraries for the **Krash Programming Language**. These libraries provide essential functionality for common programming tasks including mathematics, string operations, HTTP requests, file I/O, JSON parsing, date/time operations, and random generation.

Libraries are built with Python and seamlessly integrate with the Krash interpreter.

---

## 📦 Installation

All libraries are installed globally using the Krash package manager. Once installed, they are available to all your Krash projects.

### Install Individual Libraries

```bash
krsh --install --mathBasic
krsh --install --ArraysAndStrings
krsh --install --HTTPClient
krsh --install --FileUtils
krsh --install --JSONParser
krsh --install --DateUtils
krsh --install --Random
```

### Install All Libraries

```bash
krsh --install --all
```

### List Installed Libraries

```bash
krsh --list
```

### Remove a Library

```bash
krsh --remove --LibraryName
```

---

## 📚 Available Libraries

### 1. **mathBasic** – Basic Arithmetic Operations

Provides safe arithmetic operations with error handling.

**Functions:**
- `add(int a, int b)` → Returns a + b
- `subtract(int a, int b)` → Returns a - b
- `multiply(int a, int b)` → Returns a * b
- `divide(int a, int b)` → Returns a / b (throws ValueError if b == 0)

**Usage Example:**

```krash
#mathBasic

int x = 10
int y = 5

int sum = mathBasic.add(x, y)           // sum = 15
int diff = mathBasic.subtract(x, y)     // diff = 5
int prod = mathBasic.multiply(x, y)     // prod = 50

try>:
    int quotient = mathBasic.divide(x, y)   // quotient = 2
<: catch>: ValueError:
    show "Cannot divide by zero"
<:

showf "Sum: {sum}, Difference: {diff}, Product: {prod}, Quotient: {quotient}"
```

---

### 2. **ArraysAndStrings** – Array & String Utilities

Extended utilities for working with arrays and strings beyond built-in methods.

**Functions:**
- `capitalize(str word)` → Capitalizes first letter
- `reverse(str text)` → Reverses string
- `reverse(int[] arr)` → Reverses array
- `removeDuplicates(int[] arr)` → Removes duplicate values
- `removeDuplicates(str[] arr)` → Removes duplicate strings
- `join(str[] arr, str delimiter)` → Joins array into string
- `shuffle(int[] arr)` → Randomly shuffles array
- `shuffle(str[] arr)` → Randomly shuffles array

**Usage Example:**

```krash
#ArraysAndStrings

str name = "alice"
str capitalized = ArraysAndStrings.capitalize(name)
showf "{capitalized}"                   // Alice

str text = "hello"
str reversed = ArraysAndStrings.reverse(text)
showf "{reversed}"                      // olleh

str[] words = ["hello", "world", "hello"]
str[] unique = ArraysAndStrings.removeDuplicates(words)
showf "{unique}"                        // ["hello", "world"]

str[] items = ["apple", "banana", "cherry"]
str joined = ArraysAndStrings.join(items, ", ")
showf "{joined}"                        // apple, banana, cherry

int[] numbers = [1, 5, 3, 8, 2]
int[] shuffled = ArraysAndStrings.shuffle(numbers)
showf "{shuffled}"                      // [random order]
```

---

### 3. **HTTPClient** – HTTP Requests

Make HTTP GET, POST, PUT, DELETE, and PATCH requests with optional headers and timeouts.

**Functions:**
- `get(str url)` → GET request
- `get(str url, int timeout_ms)` → GET with timeout
- `post(str url, str data)` → POST request
- `post(str url, str data, str[] headers)` → POST with headers
- `put(str url, str data)` → PUT request
- `delete(str url)` → DELETE request
- `patch(str url, str data)` → PATCH request

**Usage Example:**

```krash
#HTTPClient

// Simple GET request
try>:
    str response = HTTPClient.get("https://api.example.com/users")
    showf "Response: {response}"
<: catch>: NetworkError:
    show "Failed to fetch data"
<:

// POST request with data
str payload = "{"name": "Alice", "age": 31}"
try>:
    str result = HTTPClient.post("https://api.example.com/users", payload)
    showf "Created: {result}"
<: catch>: NetworkError:
    show "Failed to create user"
<:

// POST with custom headers
str[] headers = ["Authorization: Bearer token123",
                 "Content-Type: application/json"]
str data = "{"message": "Hello from Krash"}"
try>:
    str response = HTTPClient.post("https://api.example.com/message", data, headers)
    showf "{response}"
<: catch>: NetworkError:
    show "Request failed"
<:

// GET with timeout (5 seconds)
try>:
    str data = HTTPClient.get("https://api.example.com/data", 5000)
    showf "{data}"
<: catch>: NetworkError:
    show "Request timed out"
<:
```

---

### 4. **FileUtils** – Advanced File Operations

Extended file operations beyond basic read/write.

**Functions:**
- `fileExists(str filename)` → Returns True/False
- `fileSize(str filename)` → Returns file size in bytes
- `deleteFile(str filename)` → Deletes file
- `copyFile(str source, str destination)` → Copies file
- `renameFile(str oldName, str newName)` → Renames file
- `appendToFile(str filename, str text)` → Appends text to file
- `clearFile(str filename)` → Clears file contents
- `listFiles(str directory)` → Lists all files in directory

**Usage Example:**

```krash
#FileUtils

// Check if file exists
if>: FileUtils.fileExists("data.txt"):
    showf "File exists"
<: else>:
    showf "File not found"
<:

// Get file size
int size = FileUtils.fileSize("data.txt")
showf "File size: {size} bytes"

// Copy file
FileUtils.copyFile("original.txt", "backup.txt")

// Rename file
FileUtils.renameFile("oldname.txt", "newname.txt")

// Append to file
FileUtils.appendToFile("log.txt", "New log entry\n")

// Clear file
FileUtils.clearFile("temp.txt")

// List files in directory
str[] files = FileUtils.listFiles("./documents")
for>: int i = 0, i < files.length(), i++:
    showf "File: {files[i]}"
<:
```

---

### 5. **JSONParser** – JSON Parsing & Generation

Parse JSON strings and generate JSON from data structures.

**Functions:**
- `parse(str json)` → Parses JSON string to object
- `stringify(oth object)` → Converts object to JSON string
- `getString(oth json, str key)` → Gets string value
- `getInt(oth json, str key)` → Gets integer value
- `getArray(oth json, str key)` → Gets array value

**Usage Example:**

```krash
#JSONParser

// Parse JSON
str jsonStr = "{"name": "Alice", "age": 31, "city": "NYC"}"
oth user = JSONParser.parse(jsonStr)

str name = JSONParser.getString(user, "name")
int age = JSONParser.getInt(user, "age")
showf "Name: {name}, Age: {age}"

// Stringify object
showf "{JSONParser.stringify(user)}"

// Work with JSON arrays
str jsonArray = "[{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]"
oth users = JSONParser.parse(jsonArray)
showf "Users: {users}"
```

---

### 6. **DateUtils** – Date & Time Operations

Work with dates, times, and timestamps.

**Functions:**
- `now()` → Returns current timestamp
- `today()` → Returns today's date as string (YYYY-MM-DD)
- `time()` → Returns current time as string (HH:MM:SS)
- `formatDate(str date, str format)` → Formats date string
- `daysUntil(str endDate)` → Days until target date
- `daysSince(str startDate)` → Days since target date
- `isLeapYear(int year)` → Returns True/False
- `addDays(str date, int days)` → Adds days to date

**Usage Example:**

```krash
#DateUtils

// Get current date and time
str currentDate = DateUtils.today()
str currentTime = DateUtils.time()
showf "Date: {currentDate}, Time: {currentTime}"

// Calculate days until event
int daysLeft = DateUtils.daysUntil("2025-12-31")
showf "Days until year end: {daysLeft}"

// Check if leap year
bool isLeap = DateUtils.isLeapYear(2024)
showf "2024 is leap year: {isLeap}"

// Add days to date
str futureDate = DateUtils.addDays("2025-01-01", 30)
showf "30 days from Jan 1: {futureDate}"

// Days since event
int daysPassed = DateUtils.daysSince("2025-01-01")
showf "Days since Jan 1: {daysPassed}"
```

---

### 7. **Random** – Random Number & Item Generation

Generate random numbers and pick random items from collections.

**Functions:**
- `integer(int min, int max)` → Random int between min and max (inclusive)
- `float(float min, float max)` → Random float between min and max
- `boolean()` → Random True or False
- `item(str[] arr)` → Random item from string array
- `item(int[] arr)` → Random item from int array
- `shuffle(str[] arr)` → Shuffles string array
- `shuffle(int[] arr)` → Shuffles int array

**Usage Example:**

```krash
#Random

// Random integers
int dice = Random.integer(1, 6)
showf "Dice roll: {dice}"

int randomNum = Random.integer(1, 100)
showf "Random number 1-100: {randomNum}"

// Random float
float randomFloat = Random.float(0.0, 1.0)
showf "Random float: {randomFloat}"

// Random boolean
bool coin = Random.boolean()
showf "Coin flip: {coin}"

// Random item from array
str[] colors = ["red", "green", "blue", "yellow"]
str randomColor = Random.item(colors)
showf "Random color: {randomColor}"

// Shuffle array
int[] numbers = [1, 2, 3, 4, 5]
int[] shuffled = Random.shuffle(numbers)
showf "Shuffled: {shuffled}"

// Simple lottery simulator
showf "Lottery numbers:"
int[] lottery = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
int[] winning = Random.shuffle(lottery)
for>: int i = 0, i < 6, i++:
    showf "{winning[i]}"
<:
```

---

## 🚀 Complete Example Program

Here's a complete program using multiple libraries:

```krash
#mathBasic
#ArraysAndStrings
#HTTPClient
#DateUtils
#Random
#JSONParser

fxn>: calculateStats(int[] scores):
    int sum = 0
    for>: int i = 0, i < scores.length(), i++:
        sum = sum + scores[i]
    <:
    int count = scores.length()
    int average = mathBasic.divide(sum, count)
    givef "{average}"
<:

// Main program
showf "Welcome to Krash Library Demo!"
showf "Today is: {DateUtils.today()}"

// Work with arrays
int[] testScores = [85, 92, 78, 95, 88]
int avg = calculateStats(testScores)
showf "Average score: {avg}"

// Generate random data
str[] names = ["Alice", "Bob", "Charlie", "Diana"]
str randomName = Random.item(names)
showf "Random winner: {randomName}"

// Make HTTP request
try>:
    str data = HTTPClient.get("https://jsonplaceholder.typicode.com/users/1")
    showf "API Response: {data}"
<: catch>: NetworkError:
    show "Could not fetch data"
<:

// Work with strings
str greeting = "krash programming"
str capitalized = ArraysAndStrings.capitalize(greeting)
showf "Capitalized: {capitalized}"

showf "Demo complete!"
```

---

## 📖 How Libraries Work

### Installation Process

1. Run `krsh --install --LibraryName`
2. Package manager downloads from GitHub
3. Library installed globally (not in project folder)
4. Available to all Krash programs

### Using in Your Code

```krash
#LibraryName

// Use library functions
int result = LibraryName.functionName(params)
```

### Variable Scope

Libraries maintain their own scope. Variables in library functions don't affect your program's variables:

```krash
#mathBasic

int result = mathBasic.add(5, 10)  // Uses library's internal logic
// result = 15
```

---

## 🔧 Creating Your Own Libraries

You can create custom libraries in **Krash (.ksh)** or **Python**:

### Option 1: Krash Library (.ksh)

**myMath.ksh:**
```krash
fxn>: square(int x):
    givef "{x * x}"
<:

fxn>: cube(int x):
    givef "{x * x * x}"
<:
```

**Use in your program:**
```krash
#myMath

int sq = myMath.square(5)    // sq = 25
int cb = myMath.cube(5)      // cb = 125
showf "Square: {sq}, Cube: {cb}"
```

### Option 2: Python Library

**myMath.py:**
```python
def square(x):
    return x * x

def cube(x):
    return x * x * x

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)
```

**Use in your program:**
```krash
#myMath  // Automatically loads myMath.py if myMath.ksh doesn't exist

int sq = myMath.square(5)      // sq = 25
int cb = myMath.cube(5)        // cb = 125
int fact = myMath.factorial(5) // fact = 120
showf "Square: {sq}, Cube: {cb}, Factorial: {fact}"
```

**Note:** Python libraries integrate seamlessly with Krash. The interpreter automatically converts types and handles function calls.

---

## 📝 Library Documentation

- **mathBasic**: [mathBasic-docs.md](./docs/mathBasic-docs.md)
- **ArraysAndStrings**: [ArraysAndStrings-docs.md](./docs/ArraysAndStrings-docs.md)
- **HTTPClient**: [HTTPClient-docs.md](./docs/HTTPClient-docs.md)
- **FileUtils**: [FileUtils-docs.md](./docs/FileUtils-docs.md)
- **JSONParser**: [JSONParser-docs.md](./docs/JSONParser-docs.md)
- **DateUtils**: [DateUtils-docs.md](./docs/DateUtils-docs.md)
- **Random**: [Random-docs.md](./docs/Random-docs.md)

---

## 🐛 Error Handling

Most library functions can throw errors. Always use try/catch:

```krash
try>:
    str response = HTTPClient.get("https://api.example.com/data")
<: catch>: NetworkError:
    show "Network request failed"
<: catch>: ValueError:
    show "Invalid data received"
<:
```

**Common Error Types:**
- `NetworkError` → HTTP/network failures
- `ValueError` → Type or value errors
- `FileError` → File operation failures
- `KeyError` → Missing dictionary key
- `IndexError` → Array index out of bounds

---

## 📄 License

All Krash Standard Libraries are released under the **MIT License**. See LICENSE file for details.

---

## 🤝 Contributing

Want to contribute a library or improvement? Great! 

**Libraries can be written in:**
- **Krash (.ksh)** - For pure Krash implementations
- **Python (.py)** - For advanced functionality and performance

Process:
1. Fork this repository
2. Create a feature branch
3. Add your library (`.ksh` or `.py` format)
4. Submit a pull request

---

## 📞 Support

For issues or questions:
- Check the [Krash Language Specification](https://github.com/KAKUDEV-web/Krash)
- Open an issue on GitHub
- Visit the Krash community forum

---

**Happy coding with Krash! 🚀**
