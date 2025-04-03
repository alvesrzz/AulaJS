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
    cod = document.getElementById("cod").value;
    quantidade = document.getElementById("quantidade").value;
    let descricao;
    let preco;
    let ValorTotal;
    if (cod = 5){
        descricao = "Tênis Nike";
        preco = 500;
        ValorTotal = preco * quantidade;
        document.getElementById("mensagem10").innerHTML = descricao + "<br> Preço: " + preco + "<br>Valor total: " + ValorTotal; 
    }
    if (cod= 10){
        descricao = "Tênis Adidas";
        preco = 300;
        ValorTotal = preco * quantidade;
        document.getElementById("mensagem10").innerHTML = descricao + "<br> Preço: " + preco + "<br>Valor total: " + ValorTotal;
    }
    else {
        document.getElementById("mensagem10").innerHTML = "Código invalido";
    }
}

function ex11(quantidade,preco,cod){
    quantidade = document.getElementById("quantidade").value;
    preco = document.getElementById("preco").value;
    cod = document.getElementById("cod").value;
    
    
}