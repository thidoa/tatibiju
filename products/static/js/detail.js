
function get_id(id) {
    pk = "number-" + id
    number = document.getElementById(pk)
    return number
}

function next(id) {
    var estoque = document.getElementById('estoque').value
    number = get_id(id)
    console.log(number)
    var index = parseInt(number.value)
    console.log(index)
    index += 1
    if(index <= estoque) {
        number.style.opacity = "1"
    } else {
        number.style.opacity = "0.5"
    }
    number.value = index
}

function back(id) {
    var estoque = document.getElementById('estoque').value
    number = get_id(id)
    console.log(number)
    var index = parseInt(number.value)
    if(index > 1) {
        index -= 1
    }
    if(index <= estoque) {
        number.style.opacity = "1"
    } else {
        number.style.opacity = "0.5"
    }
    
    number.value = index
}

function copiarTexto(pk) {
    var textos = document.getElementsByName("texto-" + pk)
    var total = document.getElementById("total-" + pk)

    var texto = ""
    for (var i = 0; i < textos.length; i++) {
        console.log(textos[i].value)
        texto += textos[i].value + ";\n"
    }
    texto += "\nTotal: R$" + total.value + "."
    navigator.clipboard.writeText(texto);

    var botao = document.getElementById('copied-' + pk)
    var img = document.getElementById('copied_img-' + pk)

    botao.innerHTML = "COPIADO "
    img.style.display = "block"

    setTimeout(function(){
        botao.innerHTML = "copiar"
        img.style.display = "none"
    },1800);
}   