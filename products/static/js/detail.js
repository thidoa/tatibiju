var number = document.getElementById('number');

var index = parseInt(number.value)

function next() {
    index += 1
    number.value = index
}

function back() {
    index -= 1
    number.value = index
}