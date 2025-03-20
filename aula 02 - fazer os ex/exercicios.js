function ex1(n1)
{
    n1 = document.getElementById("n1").value;
    let quadrado = Number(n1) * Number(n1);
    let cubo = Number(n1) * Number(n1) * Number(n1);
    
    document.getElementById("mensagem1").innerHTML = "O numero digitado é: " + n1 + "<br> O quadrado do número é: " + quadrado + "<br> O cudo do numero é: " + cubo;
}

function ex2(F)
{
    F = document.getElementById("F").value;
    let C = (Number(F)-32)*5/9;

    document.getElementById("mensagem2").innerHTML = "A temperatura em graus Fahrenheit foi " + F + "<br> A temperatura em graus Celsius é : " + C;
}

function ex3(valor,tempo,taxa)
{
    valor = document.getElementById("valor").value;
    taxa = document.getElementById("taxa").value;
    tempo = document.getElementById("tempo").value;

    let valorParcela = Number(valor) + (Number(valor) * (Number(taxa) * Number(taxa)/100) * Number(tempo));

    document.getElementById("mensagem3").innerHTML = "<u>Valores informados</u>" + "<br>Valor = " + valor + "<br>Taxa = " + taxa + "<br>Tempo = " + tempo + "<br><br><b>O valor atualizado é: " + valorParcela + "</b>";

}

function ex4(base,altura)
{
    base = document.getElementById("base").value;
    altura = document.getElementById("altura").value;

    let areaTriangulo = Number(base)*Number(altura)/2;

    document.getElementById("mensagem4").innerHTML = "Base = " + base + "<br>Altura = " + altura + "<br><br><b>A ârea do triâgulo é : " + areaTriangulo + "</b>";
}

function ex5(lado)
{
    lado = document.getElementById("lado").value;

    let areaQuadrado = Number(lado) * Number(lado);

    document.getElementById("mensagem5").innerHTML = "O lado do quadrado é " + lado + "<br><br><b>A area do quadrado é : " + areaQuadrado + "</b>";
}

function ex6(produto,preco)
{
    produto = document.getElementById("produto").value;
    preco = document.getElementById("preco").value;

    let subtotal = Number(produto) * Number(preco);
    let desconto = Number(subtotal) * 0.10;
    let valorFinal = (Number(subtotal) - Number(desconto));

    document.getElementById("mensagem6").innerHTML = "Subtotal: " + subtotal + "<br>Desconto em 10%: " + desconto + "<br>Valor final: " + valorFinal;
}