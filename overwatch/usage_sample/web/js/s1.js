function myFunction() {
   document.getElementById("demo").innerHTML = "Paragraph changed.";
}

function function1() {
  var textFile = null,
    makeTextFile = function (text) {
      var data = new Blob([text], {type: 'text/plain'});

      // If we are replacing a previously generated file we need to
      // manually revoke the object URL to avoid memory leaks.
      if (textFile !== null) {
        window.URL.revokeObjectURL(textFile);
      }

      textFile = window.URL.createObjectURL(data);

      return textFile;
    };


    var create = document.getElementById('create'),
      textbox = document.getElementById('textbox');

    create.addEventListener('click', function () {
      var link = document.getElementById('downloadlink');
      link.href = makeTextFile(textbox.value);
      link.style.display = 'block';
    }, false);
}

// Basic add operator
function basic_add_operator() {
    return 5 + 6;
}
document.getElementById("demo_basic_add").innerHTML = basic_add_operator();

// Temperature
document.getElementById("temp").innerHTML =
"The temperature is " + toCelsius(77) + " Celsius";
function toCelsius(fahrenheit) {
    return (5/9) * (fahrenheit-32);
}

// Formats date to YYMMDD
document.getElementById("getDate").innerHTML = formatDate();
function formatDate() {
    date =  new Date();

    // format day
    var d = date.getDate();
    if (d < 10) dd = '0' + d;
    else        dd = d;

    // format month
    var month = new Array();
    month[0] = "01"; month[1] = "02";
    month[2] = "03"; month[3] = "04";
    month[4] = "05"; month[5] = "06";
    month[6] = "07"; month[7] = "08";
    month[8] = "09"; month[9] = "10";
    month[10] = "11"; month[11] = "12";
    var mm = month[date.getMonth()];

    // format year
    var yy = String(date.getFullYear());
    yy = yy.replace(/^20/i, '');
    
    new_date = yy + mm + dd;
    return new_date;
}



function exportToCsv() {
    var myCsv = "Col1,Col2,Col3\nval1,val2,val3";

    window.open('data:text/csv;charset=utf-8,' + escape(myCsv));
}
var button = document.getElementById('exportcsv');
button.addEventListener('click', exportToCsv);