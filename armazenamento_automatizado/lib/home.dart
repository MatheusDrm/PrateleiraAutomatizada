import 'package:flutter/material.dart';

class Home extends StatelessWidget {
  const Home({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.white12,
      appBar: AppBar(
        backgroundColor: Colors.blueAccent,
        title: Text("Home"),
      ),
      body: Center(
        child: SizedBox(
          width: 350,
          height: 700,
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children:  [
              Text('''Bem-vindo ao nosso sistema de armazenagem automatizado! Este aplicativo tem como objetivo permitir que você consiga armazenar e retirar produtos de forma fácil e intuitiva desta prateleira automatizada.Para armazenar um produto, basta acessar a página "Armazenagem" e seguir as instruções. Você poderá inserir informações detalhadas sobre o produto, como seu nome, categoria e local de armazenamento.Para retirar um produto, acesse a página "Retirada" e localize o produto que deseja retirar. Você poderá selecionar o produto e confirmar sua retirada, garantindo que seu estoque seja sempre preciso e atualizado.Agradeçemos o voto de confiança utilizando nosso aplicativo!''',
                style: TextStyle(color: Colors.white,),),
              Image(image: NetworkImage('https://media2.giphy.com/media/vfC1yHKDGrNE7ooJOE/giphy.gif?cid=6c09b9527jdxpj1a5cd37d3p8hepphubusgpz2wwury6nu34&rid=giphy.gif&ct=s'))
            ],
          ),
        ),
      ),
    );
  }
}


