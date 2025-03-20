let numero1, numero2, resultado;

function somar(n1, n2)
{
    let soma = Number(n1) + Number(n2)
    document.getElementById("mensagem").innerHTML = "A soma dos números é: " + soma;
}

function solicitarEntradasDados()
{
    numero1 = Number(prompt("digite o numero 1:"));
    numero2 = Number(prompt("digite o numero 2:"));

    somar(numero1, numero2);
}

function processar()
{
    numero1 = document.getElementById("numero1").value;
    numero2 = document.getElementById("numero2").value;

    somar(numero1, numero2);
}