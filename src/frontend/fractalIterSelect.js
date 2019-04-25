const fractalList = [];

function createFractalList() {
  var sierpinski = new optionValue("Sierpinski Triangle", "Sierpinski", 7);
  fractalList.push(sierpinski);
  var dragon = new optionValue("Dragon Curve", "Dragon", 10);
  fractalList.push(dragon);
  var gosper = new optionValue("Gosper Curve", "Gosper", 3);
  fractalList.push(gosper);
  var koch = new optionValue("Square Koch Snowflake", "Koch", 3);
  fractalList.push(koch);
}

function selected(selectID) {
  var selectIterID = "";

  if (selectID == "selectFractal1") {
    selectIterID = "selectIter1";
  } else if (selectID == "selectFractal3") {
    selectIterID = "selectIter3";
  }
  //om man valt en viss fraktal ska vissa iterationer visas i dropdownmenyn
  var option1 = getOption(selectID);
  addIterOptions(option1.value, selectIterID);
}

function optionValue(text, jsonFractal, maxIter) {
  //create optionvalue objects for dropwodn menu
  //type = text (det som syns), maxIter = maximum of iterations, jsonFractal (det som skickas till server), startpos = middle or bottomleftcorner
  this.text = text;
  this.jsonFractal = jsonFractal;
  this.maxIter = maxIter;
}

function addFractalOptions(selectID) {
  //add the objects to the <select>
  //add the fractals to the select dropdown
  var select = document.getElementById(selectID);
  console.log("kommer vi hit? :) ");
  for (index in fractalList) {
    select.options[select.options.length] = new Option(fractalList[index].text);
  }
}

function findFractalInSelect(fractoption) {
  var value = "";
  for (index in fractalList) {
    if (fractalList[index].text === fractoption.value) {
      value = fractalList[index].jsonFractal;
      console.log("The fractal value: " + value);
      break;
    }
  }

  return value;
}

function addIterOptions(textFractal, selectID) {
  //adding the iteration options corresponding to the fractal
  max = 0;
  var select = document.getElementById(selectID);
  //console.log(select.options);
  select.options.length = 0;

  for (index in fractalList) {
    if (fractalList[index].text == textFractal) {
      max = fractalList[index].maxIter;
      for (i = 1; i < max + 1; i++) {
        select.options[select.options.length] = new Option(i);
        //console.log(fractalList[index].text);
      }
      break;
    }
  }
  maxIter = fractalList[index].text;
}

function getOption(dropdown) {
  //get the option from one of the select
  var e = document.getElementById(dropdown);
  var selected = e.options[e.selectedIndex];
  //console.log(selected);

  return selected;
}
