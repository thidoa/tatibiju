
function get_id(id) {
    pk = "number-" + id
    number = document.getElementById(pk)
    return number
}

function next(id) {
    number = get_id(id)
    var index = parseInt(number.value)
    index += 1
    number.value = index
}

function back(id) {
    number = get_id(id)
    var index = parseInt(number.value)
    if(index > 1) {
        index -= 1
    }
    
    number.value = index
}


function copiarTexto() {
    var textos = document.getElementsByName("texto")
    var total = document.getElementById("total")

    var texto = ""
    for (var i = 0; i < textos.length; i++) {
        console.log(textos[i].value)
        texto += textos[i].value + ";\n"
    }
    texto += "\nTotal: R$" + total.value + "."
    navigator.clipboard.writeText(texto);

    var botao = document.getElementById('copied')
    var img = document.getElementById('copied_img')

    botao.innerHTML = "COPIADO "
    img.style.display = "block"

    setTimeout(function(){
        botao.innerHTML = "copiar"
        img.style.display = "none"
    },1800);
}   