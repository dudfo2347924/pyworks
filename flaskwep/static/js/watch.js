
var watch = setInterval(myWatch, 100)

function myWatch(){
    var date = new Date();
    var now = date.toLocaleTimeString();
    document.getElementById("demo").innerHTML = now;

}