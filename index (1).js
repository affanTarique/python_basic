//create a function that takes an array of object as input and returns the users whose age > 18 are male

function check(arr) {
  return arr.filter(user => user.age > 18 && user.gender === "male");
}



const users =[ {
  
  name: "Affan",
  age: 20,
  gender: "male",
},{
  
  name: "Arshu",
  age: 20,
  gender: "female",
}, {
  
  name: "Naina",
  age: 19,
  gender: "female",
}


];

console.log(check(users));