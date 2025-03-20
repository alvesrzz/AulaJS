document.write ("<h2>Calcular o valor da parcela </h2>");

var valor = Number( prompt("Digite o valor da prestação em atraso"));
var taxa = Number( prompt("Digite o valor da taxa"));
var tempo = Number( prompt("Digite o tempo de dias de atraso"));

var vparcela = valor +(valor*(taxa**2/100)*tempo);

document.write ("<p>Valor da parcela: " + vparcela + "</p>")