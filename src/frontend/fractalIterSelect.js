const fractalList = [];

function createFractalList() {
  let sierpinski = new optionValue("Sierpinski Triangle", "Sierpinski", 8);
  fractalList.push(sierpinski);
  let dragon = new optionValue("Dragon Curve", "Dragon", 11);
  fractalList.push(dragon);
  let gosper = new optionValue("Gosper Curve", "Gosper", 5);
  fractalList.push(gosper);
  let koch = new optionValue("Square Koch Snowflake", "Koch", 5);
  fractalList.push(koch);
  let hilbert = new optionValue("Hilbert Curve", "Hilbert", 8);
  fractalList.push(hilbert);
}

function selected() {
  //om man valt en viss fraktal ska den med lägst iterationer visas i dropdownmenyn
  let option2 = getOption("selectFractal2");
  let option1 = getOption("selectFractal1");
  let option3 = getOption("selectIter1");
  let opt1iter = 0;
  let opt2iter = 0;
  let selectID = "";

  for (i in fractalList) {
    if (fractalList[i].text === option1.value) {
      opt1iter = fractalList[i].maxIter;
    }
    if (fractalList[i].text === option2.value) {
      opt2iter = fractalList[i].maxIter;
    }
  }
  if (opt1iter > opt2iter) {
    selectID = option2.value;
  } else if (opt1iter < opt2iter) {
    selectID = option1.value;
  } else {
    selectID = option1.value;
  }
  addIterOptions(selectID, "selectIter1");
}

function selectedIter(id) {
  select = document.getElementById(id);
  addMaxIterOptions(select.value, "selectTranslationIteration");
}

function addMaxIterOptions(selectiterID, iterID) {
  //adding the iteration options corresponding to the fractal
  let max = selectiterID;
  let select = document.getElementById(iterID);
  select.options.length = 0;

  for (i = 1; i < max; i++) {
    select.options[select.options.length] = new Option(i);
  }
}

function optionValue(text, jsonFractal, maxIter) {
  //create optionvalue objects for dropwodn menu
  //type = text (det som syns), maxIter = maximum of iterations, jsonFractal (det som skickas till server)
  this.text = text;
  this.jsonFractal = jsonFractal;
  this.maxIter = maxIter;
}

function addFractalOptions(selectID) {
  //add the objects to the <select>
  //add the fractals to the select dropdown
  let select = document.getElementById(selectID);
  for (let index in fractalList) {
    select.options[select.options.length] = new Option(fractalList[index].text);
  }
}

function findFractalInSelect(fractoption) {
  let value = "";
  for (let index in fractalList) {
    if (fractalList[index].text === fractoption.value) {
      value = fractalList[index].jsonFractal;
      break;
    }
  }

  return value;
}

function addIterOptions(textFractal, selectID) {
  //adding the iteration options corresponding to the fractal
  let max = 0;
  let select = document.getElementById(selectID);
  //console.log(select.options);
  select.options.length = 0;

  for (let index in fractalList) {
    if (fractalList[index].text === textFractal) {
      max = fractalList[index].maxIter;
      for (let i = 1; i < max + 1; i++) {
        select.options[select.options.length] = new Option(i);
        //console.log(fractalList[index].text);
      }
      break;
    }
  }
}

function getOption(dropdown) {
  //get the option from one of the select
  let e = document.getElementById(dropdown);
  //console.log(selected);

  return e.options[e.selectedIndex];
}
