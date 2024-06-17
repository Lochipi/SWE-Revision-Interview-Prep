# More questions on basic concepts of JavaScript

1. What are falsy values in JavaScript?

These are the values that are considered false when encountered in a `boolean context`. There are 6 falsy values in JavaScript:

- `false`: The keyword `false`.
- `0`: The number zero.
- `''`: An empty string.
- `null`: Absence of any value.
- `undefined`: When a declared variable has no value.
- `NaN`: Not a Number.

You should at any point avoid using these values in your code as they can lead to unexpected behavior. Be more explicit in your checks to avoid these values.

2. What do the spread and rest operatoes do?

The `spread` and `rest` operators are denoted by `...` and are used in different contexts.

- `Spread`: The spread operator is used to split up array elements or object properties. It is used to make copies of arrays and objects. For example, `[...array]` will create a copy of the array `array`.

```javascript
const arr = [1, 2, 3];

const copy = [5, ...arr];
console.log(copy); // output => [5, 1, 2, 3]

// Copying object properties
const obj = { name: "David", age: 25 };

const copy = { ...obj };
console.log(copy); // output => { name: 'David', age: 25 }
```

- `Rest`: The rest operator is used to merge a list of function arguments into an array. It is used to collect all the remaining elements into an array. For example, `function(a, b, ...args)` will collect all the remaining arguments into an array called `args`.

```javascript
function sum(...args) {
  return args.reduce((acc, val) => acc + val, 0);
}

sum(1, 2, 3, 4); // output => 10
// acc = accumulator(The previously returned value (or the initial value if provided)), val = value, 0 = initial value
// acc = 0, val = 1 => 0 + 1 = 1
```

The `reduce()` method executes a reducer function for `each element` above. It returns a single accumulated value, which is the result of the custom operation(`sum`) above.

3. What is and why might you destructure an object or an array?

`Destructuring` is a convenient way of extracting multiple values from data stored in objects and arrays. It can be used in locations that receive data (such as the left-hand side of an assignment). `Destructuring` can also be used to provide default values for objects that might be `undefined`.

- Destructuring an object:

```javascript
const person = { name: "David", age: 25 };

const { name, age } = person;

console.log(name); // output => David
console.log(age); // output => 25
```

- Destructuring an array:

```javascript
const numbers = [1, 2, 3, 4, 5];

const [first, second] = numbers;

console.log(first); // output => 1
console.log(second); // output => 2
```
