// define variables (const)
// more variables are defined directly inside the function
// tbody element from HTML needs to be accessed

const bodyTable = document.createElement("tbody");
const tableData = document.getElementsByTagName("td");
const chooseColor = "";

// define function to pick the color 
// here I define the variable for color and access the value of the picked color from HTML
// using .bgColor I can access the color and then I assign this color to the color variable 

function addColor(para) {
    const color = document.getElementById("colorPicker").value;
    para.target.bgColor=color;
}

// Then I define a function to create the responsive grid
// using the Element.innerHTML method I can access the HTML information from inside the element (e.g. without the tags)
// then I use tow for loops to create the rows and columns. one loop needs to be nested inside the other
// using the .appedChild method I can add the created element to the higher structure in DOM, so first I append the columns to the rows, then I append the row (and resp. the column) to the taable body, 
// and the I append the body of the table to the HTML pixelCavas element
// Then I need to preven the default event to prevent the submit event listener to refresh the page before a grid is even created 
// Finally I add the event listener the react towards clicks with adding the respective color

function createGrid(height, width) {
    bodyTable.innerHTML = "";
    for (let h = 0; h < height;  h++) {                                 
          var row = document.createElement("tr");
          for (let w = 0; w < width; w++) {
              var column = document.createElement("td");
              row.appendChild(column);                              
          }
      bodyTable.appendChild(row);                                              
    }
    pixelCanvas.appendChild(bodyTable);                                    
    event.preventDefault();
    bodyTable.addEventListener('click', addColor)                     
}

// Now I access the form element from HTML (sizePicker) and add an event listener to it to check for the size of the grid
// first I use an if statement to check if the current table euqals the multiplication of the input for height and width
// when that is true, I reset the grid (the function to reset follows afterwards)
// else, I assign the input for height and width to a let variable (only block scope necessary here)
// and create a grid with this input

sizePicker.addEventListener('submit', function(event) {
    if (tableData.length == (inputHeight.value*inputWidth.value)) {
        resetGrid();
    } else {
      let height = document.getElementById("inputHeight").value;
      let width = document.getElementById("inputWidth").value;
      createGrid(height, width);
    }
})

// Finally, I need to create the function to reset the grid like asked in the project specifiaction
// for that I use a for loop to erase all colors from each cell 
// I use the index as the increment in the for loop and erase the color with "". 
// Again, I need to prevent the default event from happening. 
// 
function resetGrid () {
    for (let x = 0; x < tableData.length; x++) {
        if (tableData[x].bgColor != chooseColor) {
           tableData[x].bgColor = "";
        }
     event.preventDefault();
    }
}






