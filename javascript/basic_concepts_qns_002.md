# Control flow and functions

### 8. How do you loop through an array in Js?

Looping through an array in JavaScript can be done using several methods.

a. For loop

```javascript
let fruits = ["Apple", "Banana", "Cherry"];
for (let i = 0; i < fruits.length; i++) {
  console.log(fruits[i]);
}
```

It starts at the index of zero, continue as `i` is less than the array's length, and increase `i` by 1 after each iteration.

b. For...of Loop

```javascript
let fruits = ["Apple", "Banana", "Cherry"];
for (let fruit of fruits) {
  console.log(fruit);
}
```

This is a modern method that retrieves the value from the array without dealing with the index.

c. forEach() method

```javascript
let fruits = ["Apple", "Banana", "Cherry"];
fruits.forEach((fruit, index, arr) => {
  console.log(fruit);
});

// arr - the array that forEach is being applied to or traversed.
```

d. `for...in` loop:
This iterates over indices, better for objects.

```javascript
let fruits = ["Apple", "Banana", "Cherry"];
for (let index in fruits) {
  console.log(fruits[index]);
}
```

e. `while` loop:
This loop continues to execute as long as the specified condition evaluates to true.

```javascript
let array = [1, 2, 3, 4, 5];
let i = 0;

while (i < array.lenght) {
  console.log(array[i]);
  i++;
}
```

f. `do...while` loop
This loop will execute the code block once, before checking if the condition is true, then it will repeat the loop as long as the condition is true.

```javascript
let array = [1, 2, 3, 4, 5];
let i = 0;

do {
  console.log(array[i]);
  i++;
} while (i < array.length);
```

g. `map()` method
This method creates a new array with the results of calling a provided function on every element in the array.

```javascript
let numbers = [1, 2, 3, 4, 5];
let doubled = numbers.map((number) => number * 2);
console.log(doubled); // [2, 4, 6, 8, 10]
```

### 9. Explain the concept of closures in JavaScript.

A closure is a feature in Js where an inner function has access to the outer (enclosing) function's variables. The inner function has access to the outer function's variables even after the outer function has returned.

```javascript
function outerFunction() {
  let outerVariable = "I am outside";

  function innerFunction() {
    console.log(outerVariable); // I am outside
  }

  return innerFunction;
}

const closure = outerFunction();
closure(); // 'I am outside' is returned
```

example 2. Closure with parameters

```javascript
function createAdder(x) {
  return function (y) {
    return x + y;
  };
}

const add5 = createAdder(5);
console.log(add5(2)); // 7
```

Explanation:

- The `createAdder` function returns a function that takes a single argument `y` and returns the sum of `x` and `y`.
  createAdder(5) returns a function that adds 5 to its argument.
  creating `add5`:
  `add5` is a closure because it captures the `x` value from the outer function `createAdder`.
  When `add5(2)` is called, it adds 5 (captured `x` value) to 2 (passed argument) and returns (`5 + 2`) which is `7`.

When you call `add5(2)`, it's doing like this:

````javascript
   function(2){
       return 5 +2;
   }
```

Example 3. Private variables and methods
Closures can be used to create private variables and methods.

```javascript
function Counter(){
   let counter = 0; // private variable

   return {
       incremement: function(){
           counter ++
           return count;
       }
       decrement: function (){
           counter --;
           return count;
       }
       getCount: function() {
           return count;
       }
   }
}
const myCounter = Counter();
console.log(myCounter.increment()); // Outputs: 1
console.log(myCounter.increment()); // Outputs: 2
console.log(myCounter.decrement()); // Outputs: 1
console.log(myCounter.getCount()); // Outputs: 1
````

#### Advantages of closures
- data encapsulation
- mantaining states
- functional programming

The key feature os closures, is to persist access to the outer functions's scope variables after the outer function has returned.