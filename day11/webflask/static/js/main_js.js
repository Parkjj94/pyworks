setInterval(myWatch, 1000)

function myWatch(){
    var date = new Date();
    var now = date.toLocaleTimeString();
    document.getElementById('display').innerHTML = now
    }
