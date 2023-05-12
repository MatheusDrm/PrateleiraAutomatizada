import 'package:flutter/material.dart';

class Guardar extends  StatefulWidget {
  const Guardar({Key? key}) : super(key: key);

  @override
  _MyPageState createState() => _MyPageState();
}

class _MyPageState extends State<Guardar> {
  final TextEditingController _nameController = TextEditingController();
  final TextEditingController _productController = TextEditingController();

  void _showFormDialog(BuildContext context, int compartment) {
    showDialog(
      context: context,
      builder: (BuildContext context) {
        return AlertDialog(
          backgroundColor: Colors.white,
          shape: RoundedRectangleBorder(
            borderRadius: BorderRadius.circular(10.0),
          ),
          title: Center(
            child: Text(
              'Dados de armazenamento',
              style: TextStyle(
                fontSize: 18.0,
                fontWeight: FontWeight.bold,
                color: Colors.blueGrey[800],
              ),
            ),
          ),
          content: Container(
            width: double.maxFinite,
            child: SingleChildScrollView(
              child: Column(
                mainAxisSize: MainAxisSize.min,
                children: [
                  TextField(
                    controller: _nameController,
                    decoration: InputDecoration(
                      hintText: 'Nome do usuário',
                      border: OutlineInputBorder(),
                      focusedBorder: OutlineInputBorder(
                        borderSide: BorderSide(
                          color: Colors.blueGrey[800]!,
                        ),
                      ),
                      enabledBorder: OutlineInputBorder(
                        borderSide: BorderSide(
                          color: Colors.blueGrey[800]!,
                        ),
                      ),
                      labelStyle: TextStyle(
                        color: Colors.blueGrey[800],
                      ),
                    ),
                  ),
                  const SizedBox(height: 16.0),
                  TextField(
                    controller: _productController,
                    decoration: InputDecoration(
                      hintText: 'Nome do produto',
                      border: OutlineInputBorder(),
                      focusedBorder: OutlineInputBorder(
                        borderSide: BorderSide(
                          color: Colors.blueGrey[800]!,
                        ),
                      ),
                      enabledBorder: OutlineInputBorder(
                        borderSide: BorderSide(
                          color: Colors.blueGrey[800]!,
                        ),
                      ),
                      labelStyle: TextStyle(
                        color: Colors.blueGrey[800],
                      ),
                    ),
                  ),
                ],
              ),
            ),
          ),
          actions: [
            ElevatedButton(
              onPressed: () {
                // Faz algo com os dados do formulário aqui
                // ...
                // Fecha o pop-up
                Navigator.pop(context);
              },
              style: ButtonStyle(
                backgroundColor: MaterialStateProperty.all(
                  Colors.purple[800],
                ),
                foregroundColor: MaterialStateProperty.all(
                  Colors.white,
                ),
                shape: MaterialStateProperty.all(
                  RoundedRectangleBorder(
                    borderRadius: BorderRadius.circular(10.0),
                  ),
                ),
              ),
              child: Text('Salvar'),
            ),
          ],
        );
      },
    );
  }



  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.white30,
      appBar: AppBar(
      title: Text("Guardar produto"),
      ),
      body: Center(
        child: SizedBox(
          width: 400,
          child: Column(
            children: [
              SizedBox(height: 30,),
              const Text('Escolha o compartimento para o armazenamento:', style: TextStyle(fontSize: 20, color: Colors.white), textAlign: TextAlign.center,),
              SizedBox(height: 50,),
              SizedBox(
                width: 300,
                height: 400,
                child: GridView.count(
                  crossAxisCount: 3,
                  mainAxisSpacing: 10,
                  crossAxisSpacing: 10,
                  children: [
                    ElevatedButton(onPressed: (){
                      _showFormDialog(context, 1);
                    }, child: const Text('1', style: TextStyle(color: Colors.white),), style: ElevatedButton.styleFrom(primary: Colors.amber),),
                    ElevatedButton(onPressed: (){
                      _showFormDialog(context, 2);
                    }, child: const Text('2', style: TextStyle(color: Colors.white)), style: ElevatedButton.styleFrom(primary: Colors.amber)),
                    ElevatedButton(onPressed: (){
                      _showFormDialog(context, 3);
                    }, child: const Text('3', style: TextStyle(color: Colors.white)), style: ElevatedButton.styleFrom(primary: Colors.amber)),
                    ElevatedButton(onPressed: (){
                      _showFormDialog(context, 4);
                    }, child: const Text('4', style: TextStyle(color: Colors.white)), style: ElevatedButton.styleFrom(primary: Colors.amber)),
                    ElevatedButton(onPressed: (){
                      _showFormDialog(context, 5);
                    }, child: const Text('5', style: TextStyle(color: Colors.white)), style: ElevatedButton.styleFrom(primary: Colors.amber)),
                    ElevatedButton(onPressed: (){
                      _showFormDialog(context, 6);
                    }, child: const Text('6', style: TextStyle(color: Colors.white)), style: ElevatedButton.styleFrom(primary: Colors.amber)),
                  ],
                ),
              )
            ],
          ),
        ),
      ),
    );
  }
}
