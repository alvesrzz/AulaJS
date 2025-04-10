function ex1(quantidade,preco){
    quantidade = Number(document.getElementById("quantidade").value);
    preco = Number(document.getElementById("preco").value);
    Subtotal = quantidade * preco;
    switch(true){
        case(quantidade >=1 || quantidade<=5):
        desconto = 0  ;
        break;
        
        case(quantidade >=6 || quantidade<=10):
        desconto = 0.05;
        break;

        case(quantidade >=11 || quantidade <=20):
        desconto = 0.10;
        break;

        case(quantidade > 20):
        desconto = 0.15;
        break;

        default:
            document.getElementById("mensagem1").innerHTML = "numero invalido";
    }
    ValorDesconto = Subtotal * desconto;
    ValorTotal = preco - ValorDesconto;
    document.getElementById("mensagem1").innerHTML = "Quantidade: " + quantidade +"<br>Preço do produto: " + preco + "<br>Valor Total com desconto: " + ValorTotal;
}