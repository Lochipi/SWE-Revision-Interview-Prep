Will cover the basic foundation concept by questions and explanations.

we'll begin, with the first question:

### Q1. What is JavaScript?

You'd prolly wonder, what is JavaScript? Well, JavaScript is a high-level, interpreted programming language that conforms to the **ECMAScript specification**. It is a programming language that is characterized as dynamic, weakly typed, prototype-based, and multi-paradigm.

by _\_dynamic_, it means that JavaScript code can be executed on the client side, which means that it can be used to create interactive effects within web pages.

_\_a weakly typed language_, which means that variables do not have to be declared with a specific data type. JavaScript is a prototype-based language, which means that objects are created by cloning existing objects.

_\_JavaScript is a multi-paradigm language_, which means that it supports a wide range of programming styles, including **object-oriented**, **functional**, and **imperative programming**.

### Q2. What are the different data types in JavaScript?

JavaScript data types are divided into two categories: **primitive** and **non-primitive** data types.

**Primitive data types** include:

1. **String**: represents a sequence of characters.
   example:

```javascript
let name = "John Doe" | "John Doe";
```

you can use template literals for string interpolation and multi-line strings.

2. **Number**: represents numeric values, both integer and floating point numbers.
   example:

```javascript
let integerExample = 42;
let floatExample = 3.14;
```

you can use `Number.isInteger()` to check if a value is an integer.

3. **Boolean**: represents a logical value, either `true` or `false`.
   example:

```javascript
let isJavaScriptFun = true;
```

you should remember that JavaScript is case-sensitive and that Booleans are often used in conditional statements for decision-making.

4. **Undefined**: represents an undefined value, a variable has not been assigned a value.
   example:

```javascript
let x; // x is undefined
let y = undefined; // It is also possible to explicitly assign undefined as a variable value this way.
```

Tip: Initializing variables can prevent undefined errors.

5. **Null**: represents a 'no value', an 'empty value'.
   example:

```javascript
let z = null;
//indicates that z variable is set to have no value.
```

Tip: Use null to clear an object reference.

6. **Symbol**: represents a unique value that is not equal to any other value. This data type was introduced in **ES6**.
   When you create a Symbol, JavaScript guarantees that it is distinct from all other symbols, even if they have the same descriptions.
   example:

```javascript
const symbol1 = Symbol("symbol");
const symbol2 = Symbol("symbol");
console.log(symbol1 === symbol2); // false
```

Tip: Symbols are often used as unique keys for object properties.Asymbol is a **unique** and **immutable** primitive value.

7. **BigInt**: represents integers with arbitrary precision. A type of number that can represent very large or very small integers beyond the range of the regular number data type.

**Note**: The regular number data type can handle values less than `(2^53 - 1)` and greater than `-(2^53 - 1)`.

It is created by appending `n` to the end of an integer literal or by calling the BigInt() function.
example:

```javascript
const bigInt = 1234567890123456789012345678901234567890n;
```

**Note**: BigInt was introduced in a newer version of JavaScript (ES11) and is not supported by many browsers, including Safari.

**Non-primitive data types**
The data types that are derived from primitive data types. These include:

**Object**: represents a collection of key-value pairs. Objects are used to store multiple values in a single variable.

The most common way to create an object is by using an object literal, which is a comma-separated list of key-value pairs enclosed in curly braces `{}`.
Objects form the backbone of JavaScript, and almost everything in JavaScript is an object.

example:

```javascript
const person = {
  name: "John Doe",
  age: null,
  isStudent: false,
};
```

### 3. How do you declare variables in JavaScript?

In JavaScript, variables are declared using the `var`, `let`, or `const` keywords.

**var**:
Variables declared with `var` are **function-scoped**, which means that they are only available within the function in which they are declared.

    ```javascript
    let name = "John Doe";
    ```

**Tip**: var has function scope and can be re-declared and updated.

**let**:
Variables declared with `let` are **block-scoped**, which means that they are only available within the block in which they are declared.

    ```javascript
    let name = "John Doe";
    ```

**Tip**: let is block-scoped and cannot be re-declared in the same scope.

**const**:
Declares a block-scoped, read-only named constant.

```javascript
const PI = 3.142;
```

**Tip**: const cannot be updated or re-declared and must be initialized at declaration.

The choice of which keyword to use depends on the scope and mutability of the variable.

### 4. What is the difference between `==` and `===` in JavaScript?

`==` (equality) operator compares two values for equality after converting both variables to a common type.

```javascript
if (1 == "1") {
  console.log('1 is equal to "1"');
}
// Output: 1 is equal to "1", because the '==' operator converts the string '1' to a number before comparing the values.
```

On the other hand,
`===` (strict equality) operator compares two values for equality without converting their types.

```javascript
if (1 === "1") {
  console.log('1 is equal to "1"');
}
// Output: No output, because the '===' operator does not convert the string '1' to a number before comparing the values.
```

**Tip**: Use === to ensure that the comparison is both value-wise and type-wise accurate.

In essence, `==` might seem more lenient as it allows the comparison of different data types by converting them, while `===` is stricter, requiring both value and type to match. As a best practice, I recommend using `===` to avoid confusion and ensure your code behaves as expected.

### 5. How do you define a function in JavaScript?

In JavaScript, functions can be defined using function declarations, function expressions, arrow functions, and class expressions.

**Function Declaration**:
A function declaration defines a named function using the `function` keyword followed by the function name, a list of parameters enclosed in parentheses, and the function body enclosed in curly braces.

```javascript
function greet(name) {
  return `Hello, ${name}!`;
}
```

**Function Expression**:
A function expression defines an unnamed function using the `function` keyword followed by a list of parameters enclosed in parentheses and the function body enclosed in curly braces. The function is assigned to a variable.

```javascript
const greet = function (name) {
  return `Hello, ${name}!`;
};
```

**Arrow Function**:
An arrow function is a concise way to define a function using the `=>` syntax. It does not have its own `this` value and is best suited for non-method functions.

```javascript
const greet = (name) => `Hello, ${name}!`;
```

**Class Expression**:

A class expression defines a class using the `class` keyword followed by the class name, a class body enclosed in curly braces, and the class assigned to
a variable.

```javascript
const Person = class {
  constructor(name) {
    this.name = name;
  }
};
```

**Tip**: Choose the appropriate function definition based on your use case and coding style. Function declarations are hoisted, while function expressions are not.

### 6. Explain the concept of hoisting in JavaScript.

Hoisting is a JavaScript mechanism where variables and function declarations are moved to the top of their containing scope(to the top of the current script or the current function) during the compilation phase. This means that you can use a variable or function before it has been declared.

Let’s break it down with an example:

```javascript
console.log(myVar); // Outputs 'undefined', not a ReferenceError
var myVar = 5;
```

In the example above, myVar is hoisted to the top of its scope. So, the JavaScript engine interprets it as:

```javascript
var myVar;
console.log(myVar); // Outputs 'undefined'
myVar = 5;
```

**Tip**: You should remember that even though var declarations are _hoisted_, _initializations_ are **not**. That’s why myVar outputs undefined rather than 5.

However, it’s important to note that hoisting behaves differently with let and const:

Variables declared with let and const are also hoisted, but they are not initialized. Accessing them before the declaration results in a ReferenceError.
This is due to the **“temporal dead zone,”** a time from the block start until the declaration is processed, during which the variables cannot be accessed.
Here’s an example demonstrating this:

```javascript
console.log(myLetVar); // ReferenceError: myLetVar is not defined
let myLetVar = 10;

console.log(myConstVar); // ReferenceError: myConstVar is not defined
```

_Tip:_ Always declare your variables at the beginning of the scope to avoid confusion caused by hoisting and make your code cleaner and more predictable.

### 7. What is the difference between `null` and `undefined`?

`null` and `undefined` are both primitive values in JavaScript, but they have different meanings and use cases.

**\_undefined** is a type that has one value, undefined. It is the default value of a variable that has been declared but not yet assigned a value. If a function does not explicitly return a value, it implicitly returns undefined.

```javascript
let uninitializedVariable;
console.log(uninitializedVariable); // Outputs 'undefined'
```

`undefined` is a sign that a variable has been declared but not defined.

**\_null** intentional absence of any object value. It is often used to represent an empty value or a non-existent object. It is explicitly assigned by the programmer.

```javascript
let emptyObject = null;
console.log(emptyObject); // Outputs 'null'
```

use `null` to intentionally denote that a variable is currently empty or unknown.

The key difference is that undefined means a variable has been declared but has not yet been assigned a value, while null is an assignment value that can be assigned to a variable as a representation of no value. Also, undefined is a type itself, whereas null is an object.

## Wrap

We've come to the end of part one, you can check out the next part for more questions and explanations.

Note that the questions and explanations are not exhaustive, but they provide a good starting point for understanding the basic concepts of JavaScript.
