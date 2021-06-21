// // Assign the data from `data.js` to a descriptive variable
// var sleep = data;

// // Select the button
// var button = d3.select("#button");

// // Select the form
// var form = d3.select("#form");

// // Create event handlers 
// button.on("click", runEnter);
// form.on("submit",runEnter);

// // Complete the event handler function for the form
// function runEnter() {

//   // Prevent the page from refreshing
//   d3.event.preventDefault();
  
//   // Select the input element and get the raw HTML node
//   var inputElement = d3.select("#person-form-input");

//   // Get the value property of the input element
//   var inputValue = inputElement.property("value");

//   console.log(inputValue);
//   console.log(sleep);

//   var filteredData = sleep.filter(person => person.rate === inputValue);

//   console.log(filteredData);

// };


// var inputValue = [9, 8, 7, 6, 5, 4, 3, 2, 1];

//     if (inputValue > 7) {
//         console.log("good sleep");
//       }
//       else if (inputValue <= 7 && inputValue > 5) {
//         console.log("ok sleep");
//       }
//       else {
//         console.log("bad sleep");
//       }

//       // Print results
//       console.log("---------");


