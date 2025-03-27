function ex1(n1,n2)
{
    n1 = document.getElementById("n1").value;
    n2 = document.getElementById("n2").value;
    if (n1 == n2){
        document.getElementById("mensagem1").innerHTML = "Os numeros digitados são iguais ";
    } else{
        document.getElementById("mensagem1").innerHTML = "Os numeros digitados não são iguais ";
    }
}

function ex2(n1,n2,n3){
    n1 = document.getElementById("n1").value;
    n2 = document.getElementById("n2").value;
    n3 = document.getElementById("n3").value;
    if ( (Number(n1) + Number(n2)) < Number(n3)){
        document.getElementById("mensagem2").innerHTML = n1 + " + " + n2 + " é menor que " + n3;
    } else if ( (Number(n1) + Number(n2)) > Number(n3)){
        document.getElementById("mensagem2").innerHTML = n1 + " + " + n2 + " é maior que " + n3;
    } else{
        document.getElementById("mensagem2").innerHTML = n1 + " + " + n2 + " é igual " + n3;
    }
}

function ex3(salario){
    salario = document.getElementById("salario").value;
    if (Number(salario) < 500){
        document.getElementById("mensagem3").innerHTML = "Você tem direito ao aumento de salario"
    } else{
        document.getElementById("mensagem3").innerHTML = "Você não tem direito ao aumento de salario"
    }
}

function ex4(salario){
    salario = document.getElementById("salario").value;
    let reajuste = Number(salario) + (Number(salario) * 0.3) ;
    if (Number(salario) <= 500){
        document.getElementById("mensagem4").innerHTML = "O valor foi reajustado para R$" + reajuste;
    } else {
        document.getElementById("mensagem4").innerHTML = "Você não tem direito ao aumento de salario";
    }
}