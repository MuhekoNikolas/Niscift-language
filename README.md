# Niscift

Niscift is a Python-like programming language created to support the ecosystem of Python modules. It is currently under development and includes its own parser, lexer, and interpreter. The initial version is being developed in Python, with plans to eventually translate it into a lower-level language like C++.

A VSCode extension is also available to provide code highlighting, formatting, and an overall better development environment for Niscift. This project is tested to run with Python v3.11.9. 

## Getting Started

To try out Niscift in its current stage, follow these steps:

1. Navigate to the `Implementations\PyImpl\TestCases` directory.
2. Read through the existing files in this directory to understand the syntax.
3. Create a new file with a `.nis` extension.
4. Write your Niscift code in this new file.
5. Copy the file name and open the `runPy.sh` file.
6. Set the `niscift_filename` variable in `runPy.sh` to your new file's name.
7. Run the `runPy.sh` script. The output will be JSON data representing the interpretation of your Niscift code.

Please note that the project is still under development, and some features may output error objects.

VSCode extension: [Niscift VSCode Extension](https://marketplace.visualstudio.com/items?itemName=MuhekoNikolas.nis)

## Example

### Define Variables

Niscift supports both JavaScript and Python variable definitions. You can use JavaScript constants like `var`, `let`, and `const`, or use none of these.

```js
test = true
var foo = "bar"
let bar = foo
const primes = {1: "2", 2: "3", 3: [5, 7, 11, 13, 17, 19]}
```

### Import Modules (Under Development)

You can import Python modules with the `include` keyword, as well as native Niscift modules. This feature is still under development.

```python 
include json
from os.path include os as imported_python_os
from os include sys
include os as operating_system

python_path_join_function = imported_python_os.path.join
y = imported_python_os.path.join

operating_system.x = {}
operating_system.x.y = {2000000000: {x: "fijfiohfohfoi"}}

parent_key = "2000000000"
child_key = "x"

const zol = operating_system.x.y[parent_key][child_key]
zo = operating_system["x"]
```

### Comments

```js
# Python single-line comments
// JavaScript-like single-line comments

/*
    JavaScript multi-line comments
*/

/* 
    Python-like multi-line strings will be supported in the near future. 
    Currently, they only function as strings. 
*/

var multi_line_string = """
Hello, this is a multiline
string
"""
```