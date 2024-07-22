// Javascript
console.log("hello world");
console.log("without semicolon")

console.log(2+2)
console.log(2-2)
console.log(2*2)
console.log(2/2)

// this is comment
var age =75
console.log(age)
console.log(age*2)
age =age +1
console.log(age)

var name = "sandhya" ; 
var age = 23;
var is_married = false;




var xObject = {};
xObject = {
  name : "pramod",
  agr : 23
  
}

console.log(xObject.name)
// console.log(xObject[age])


var a=12
var b=9
c = a+b
console.log(c)


p=30
if(p>=0){
  console.log("p>=0")
}
else{
  console.log("p<0")
}



var x=10
switch(x){
    case 1:
    console.log("MON")
    case 2:
    console.log("TUE")
    case 3:
    console.log("WED")
    case 4:
    console.log("THURS")
    case 5:
    console.log("FRI")
    case 6:
    console.log("SAT")
    case 7:
    console.log("MON")
    default :
    console.log("invalid")
}



for (var i=1;i <= 5;i++){
  console.log(i);
}


// function
// a logic which can perform task

function greet(){
  console.log("hi,hello")
  
}
greet()


function dosomething(m){
  console.log(m*2)
}

dosomething(2)


function add(s,d){
  return s+d
}
var result = add(2,3)
console.log(result)


// converting JSON to JS Object


var res = '{"name" :"pramod","age": 23,"cars":["audi","bmw"]}'
var parseresjson = JSON.parse(res)
console.log(parseresjson)
console.log(parseresjson["name"])

console.log(parseresjson["name"])
console.log(parseresjson["cars"][0])


// JS object to JSON

var jsObject = {
  age: 23,
  cars: ["audi", "bmw"],
  name: "pramod"
}
var jsobjecttojson = JSON.stringify(jsObject)

console.log(jsobjecttojson)






