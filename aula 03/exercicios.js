function ex6(n1,n2)
{
    n1 = document.getElementById("n1").value;
    n2 = document.getElementById("n2").value;
    if (n1 == n2){
        document.getElementById("mensagem6").innerHTML = "Os numeros digitados são iguais ";
    } else{
        document.getElementById("mensagem6").innerHTML = "Os numeros digitados não são iguais ";
    }
}

function ex7(n1,n2,n3){
    n1 = document.getElementById("n1").value;
    n2 = document.getElementById("n2").value;
    n3 = document.getElementById("n3").value;
    if ( (Number(n1) + Number(n2)) < Number(n3)){
        document.getElementById("mensagem7").innerHTML = n1 + " + " + n2 + " é menor que " + n3;
    } else if ( (Number(n1) + Number(n2)) > Number(n3)){
        document.getElementById("mensagem7").innerHTML = n1 + " + " + n2 + " é maior que " + n3;
    } else{
        document.getElementById("mensagem7").innerHTML = n1 + " + " + n2 + " é igual " + n3;
    }
}

function ex8(salario){
    salario = document.getElementById("salario").value;
    if (Number(salario) < 500){
        document.getElementById("mensagem8").innerHTML = "Você tem direito ao aumento de salario"
    } else{
        document.getElementById("mensagem8").innerHTML = "Você não tem direito ao aumento de salario"
    }
}

function ex9(salario){
    salario = document.getElementById("salario").value;
    let reajuste = Number(salario) + (Number(salario) * 0.3) ;
    if (Number(salario) <= 500){
        document.getElementById("mensagem9").innerHTML = "O valor foi reajustado para R$" + reajuste;
    } else {
        document.getElementById("mensagem9").innerHTML = "Você não tem direito ao aumento de salario";
    }
}

function ex10(cod,quantidade){
    cod = Number(document.getElementById("cod").value);
    quantidade = Number(document.getElementById("quantidade").value);
    switch (cod){
        case 5:
            descricao = "Tênis Nike";
            preco = 500;
        break;
        case 10:
            descricao = "Tênis Adidas";
            preco = 300;
        default:
            document.getElementById("mensagem10").innerHTML = "Código invalido";
        }
        ValorTotal = preco * quantidade;
        document.getElementById("mensagem10").innerHTML = descricao + "<br> Preço: " + preco + "<br>Valor total: " + ValorTotal;

}

function ex11(quantidade,preco,cod){
    quantidade = Number(document.getElementById("quantidade").value);
    preco = Number(document.getElementById("preco").value);
    cod = Number(document.getElementById("cod").value);
    switch(true){
        case (cod ===1):
            procedencia = "Sul";
            frete = 10;
        break;
        case (cod === 2):
            procedencia = "Norte";
            frete = 50;
        break;
        case (cod === 3 || cod === 5):
            procedencia = "Nordeste";
            frete = 30;
        break;
        case (cod >= 6 && cod <=9):
            procedencia = "Sudeste";
            frete = 40;
        break;
        case (cod >= 10 && cod <=15 || cod >=25 && cod<=30):
            procedencia = "Centro Oeste";
            frete = 85;
        default:
            document.getElementById("mensagem11").innerHTML = "código invalido"
    }
    ValorSubTotal = quantidade * preco;
    ValorTotal = ValorSubTotal + frete;
    document.getElementById("mensagem11").innerHTML = "Código de Origem: " + cod +"<br>Quantidade: " + quantidade + "<br>Preço de Venda: R$ " + preco + ",00<br> Valor SubTotal: R$ " + ValorSubTotal + ",00<br>Valor do frete: R$ " + frete + ",00<br>Valor Total a pagar: R$ " + ValorTotal + ",00";
}