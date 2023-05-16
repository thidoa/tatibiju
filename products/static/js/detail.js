
function get_id(id) {
    pk = "number-" + id
    number = document.getElementById(pk)
    return number
}

function next(id, type) {
    number = get_id(id)
    // console.log(number)
    var index = parseInt(number.value)
    // console.log(index)
    index += 1
    var reservados_cliente = parseInt(document.getElementById(`reservei-${id}`).value)
    if(type == 'detail') {
        
        var estoque = parseInt(document.getElementById('estoque').value)
        if(index <= estoque) {
            number.style.opacity = "1"
        } else {
            number.style.opacity = "0.5"
        }
    } else {
        var estoque = parseInt(document.getElementById(`estoque-${id}`).value)
        console.log(index + estoque + reservados_cliente)
        if(index <= (estoque + reservados_cliente)) {
            number.style.opacity = "1"
        } else {
            number.style.opacity = "0.5"
        }
    }
    number.value = index
}

function back(id, type) {
    number = get_id(id)
    console.log(number)
    var index = parseInt(number.value)
    if(index > 1) {
        index -= 1
    }
    
    var reservados_cliente = parseInt(document.getElementById(`reservei-${id}`).value)
    if(type == 'detail') {
        var estoque = parseInt(document.getElementById('estoque').value)
        if(index <= estoque) {
            number.style.opacity = "1"
        } else {
            number.style.opacity = "0.5"
        }
    } else {
        var estoque = parseInt(document.getElementById(`estoque-${id}`).value)
        if(index <= (estoque + reservados_cliente)) {
            number.style.opacity = "1"
        } else {
            number.style.opacity = "0.5"
        }
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