const users = [
  { name: "Affan", age: 19, gender: "male" },
  { name: "Arshu", age: 20, gender: "female" },
  { name: "Naina", age: 19, gender: "female" },
  { name: "Temu", age: 25, gender: "male" },
  { name: "Shamu", age: 17, gender: "male" },
];

// Step 1: Filter users who are male and age > 18
const filteredUsers = users.filter(user => user.age > 18 && user.gender === "male");

// Step 2: Map the filtered users to their names
const userNames = filteredUsers.map(user => user.name);

// Step 3: Reduce the names into a single string
const result = userNames.reduce((acc, name) => acc + ", " + name,);

console.log("Filtered Users:", filteredUsers);
console.log("User Names:", userNames);
console.log("Result:", result);