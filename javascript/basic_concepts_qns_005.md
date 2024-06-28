# 𝗢𝗯𝗷𝗲𝗰𝘁𝘀 𝗮𝗻𝗱 𝗣𝗿𝗼𝘁𝗼𝘁𝘆𝗽𝗲𝘀

Hey, we will get into objects and prototypes.

1. #### What is an object in JavaScript?

   An object in JavaScript is a collection of key-value pairs. Each key-value pair is called a **property**. Properties can reference any data type, including other objects. Objects can also have methods, which are functions that are associated with the object. Here's an example of an object in JavaScript:

```javascript
let person = {
  name: "John Doe",
  age: 30,
  isStudent: false,
  sayHello: function () {
    console.log("Hello!");
  },
};
```

In this example, the `person` object has three properties (`name`, `age`, and `isStudent`) and one **method** (`sayHello`).

2. #### How do you create objects in JavaScript?

   There are several ways to create objects in JavaScript:

   - **Object literals**: You can create an object using object literal syntax, which is the most common way to create objects in JavaScript.

```javascript
let person = {
  name: "John Doe",
  age: 30,
  isStudent: false,
  sayHello: function () {
    console.log("Hello!");
  },
};
```

- **Constructor functions**: You can create objects using constructor functions, which are functions that act as blueprints for creating objects.

```javascript
function Person(name, age, isStudent) {
  this.name = name;
  this.age = age;
  this.isStudent = isStudent;
  this.sayHello = function () {
    console.log("Hello!");
  };
}

let person = new Person("John Doe", 30, false);
```

- **Object.create() method**: You can create objects using the `Object.create()` method, which creates a new object with the specified prototype object.

```javascript
let person = Object.create({
  name: "John Doe",
  age: 30,
  isStudent: false,
  sayHello: function () {
    console.log("Hello!");
  },
});
```

3. #### Explain the concept of prototype inheritance in JavaScript.

   In JavaScript, objects can inherit properties and methods from other objects through a mechanism called **prototype inheritance**. Each object in JavaScript has a prototype object, which acts as a template for the object. When you access a property or method on an object, JavaScript will first look for it on the object itself. If it doesn't find the property or method, it will look for it on the object's prototype, and so on up the prototype chain.

   Here's an example of prototype inheritance in JavaScript:

```javascript
function Person(name, age) {
  this.name = name;
  this.age = age;
}

Person.prototype.sayHello = function () {
  console.log("Hello!");
};

let person = new Person("John Doe", 30);
person.sayHello(); // Output: Hello!
```

In this example, the `Person` function acts as a constructor function for creating `Person` objects. The `sayHello` method is added to the `Person` prototype, so all `Person` objects created using the constructor function will inherit the `sayHello` method.

4. #### What is the purpose of the `this` keyword in JavaScript?

   The `this` keyword in JavaScript refers to the object that is currently executing the function. The value of `this` is determined by how a function is called. There are several ways to call a function in JavaScript, and the value of `this` can change depending on the context in which the function is called.

   Here are some common ways to call a function in JavaScript and how they affect the value of `this`:

   - **Global context**: When a function is called in the global context (i.e., not as a method of an object), `this` refers to the global object (`window` in browsers, `global` in Node.js).

```javascript
function sayHello() {
  console.log(this);
}

sayHello(); // Output: Window {...} (in a browser)
```

- **Method context**: When a function is called as a method of an object, `this` refers to the object that the method is called on.

```javascript
let person = {
  name: "John Doe",
  sayHello: function () {
    console.log(this.name);
  },
};

person.sayHello(); // Output: John Doe
```

- **Constructor context**: When a function is called as a constructor function using the `new` keyword, `this` refers to the newly created object.

```javascript
function Person(name) {
  this.name = name;
}

let person = new Person("John Doe");
console.log(person.name); // Output: John Doe
```

- **Explicit binding**: You can explicitly set the value of `this` using methods like `call()`, `apply()`, and `bind()`.

```javascript
function sayHello() {
  console.log(this.name);
}

let person = { name: "John Doe" };

sayHello.call(person); // Output: John Doe
```

Understanding how `this` works is crucial for writing object-oriented JavaScript code and working with functions in different contexts.

5. #### What is the difference between `prototype` and `__proto__` in JavaScript?

   In JavaScript, every object has a `__proto__` property, which points to its prototype object. The `prototype` property, on the other hand, is used by constructor functions and is not available on instances of objects.

   Here's an example to illustrate the difference:

```javascript
function Person(name) {
  this.name = name;
}

let person = new Person("John Doe");

console.log(person.__proto__ === Person.prototype); // Output: true
console.log(person.prototype); // Output: undefined
```

In this example, `Person.prototype` is the prototype object associated with the `Person` constructor function. When you create a new `Person` object using the `new` keyword, the `__proto__` property of the object points to `Person.prototype`.

6. #### How do you add properties to an object in JavaScript?

You can add properties to an object in JavaScript by simply assigning a value to a new key on the object. Here's an example:

```javascript
let person = {
  name: "John Doe",
  age: 30,
};

person.isStudent = false;
```

In this example, the `isStudent` property is added to the `person` object by assigning the value `false` to the `isStudent` key.

7. #### How do you compare objects in JavaScript?

In JavaScript, objects are compared by reference, not by value. This means that two objects are considered equal only if they reference the same underlying object in memory. Here's an example to illustrate this:

```javascript
let obj1 = { name: "John" };
let obj2 = { name: "John" };

console.log(obj1 === obj2); // Output: false
```

In this example, `obj1` and `obj2` are two separate objects with the same properties, but they are not equal because they reference different objects in memory.
