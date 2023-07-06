import 'package:flutter/material.dart';

class Retirar extends StatefulWidget {
  const Retirar({Key? key}) : super(key: key);

  @override
  _RetirarState createState() => _RetirarState();
}

class _RetirarState extends State<Retirar> {
  String? _selectedProduct;

  final _formKey = GlobalKey<FormState>();
  final _scaffoldKey = GlobalKey<ScaffoldState>();

  final _nomeController = TextEditingController();

  final List<String> _products = [
    "Produto A",
    "Produto B",
    "Produto C",
    "Produto D",
    "Produto E"
  ];

  void _submitForm() {
    final form = _formKey.currentState;
    if (form!.validate()) {
      form.save();

      // Substitua este código com o código para enviar o pedido de retirada ao banco de dados
      _showSnackBar("Pedido de retirada enviado com sucesso!");
    }
  }

  void _showSnackBar(String message) {
    final snackBar = SnackBar(content: Text(message));
    ScaffoldMessenger.of(context).showSnackBar(snackBar);
  }


  @override
  Widget build(BuildContext context) {
    return Scaffold(
      key: _scaffoldKey,
      appBar: AppBar(
        title: Text("Retirar produto"),
      ),
      backgroundColor: Colors.white30,
      body: Padding(
        padding: EdgeInsets.all(16.0),
        child: Form(
          key: _formKey,
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.stretch,
            children: [
              TextFormField(
                controller: _nomeController,
                style: TextStyle(color: Colors.white),
                decoration: InputDecoration(
                  labelText: "Nome do cliente",
                  labelStyle: TextStyle(color: Colors.white),
                  enabledBorder: UnderlineInputBorder(
                    borderSide: BorderSide(color: Colors.white),
                  ),
                  focusedBorder: UnderlineInputBorder(
                    borderSide: BorderSide(color: Colors.white),
                  ),
                ),
                validator: (value) {
                  if (value!.isEmpty) {
                    return "Por favor, insira seu nome";
                  }
                  return null;
                },
              ),
              SizedBox(height: 16.0),
              DropdownButtonFormField<String>(
                value: _selectedProduct,
                style: TextStyle(color: Colors.white),
                decoration: InputDecoration(
                  labelText: "Produto a ser retirado",
                  labelStyle: TextStyle(color: Colors.white),
                  enabledBorder: UnderlineInputBorder(
                    borderSide: BorderSide(color: Colors.white),
                  ),
                  focusedBorder: UnderlineInputBorder(
                    borderSide: BorderSide(color: Colors.white),
                  ),
                ),
                items: _products.map((String product) {
                  return DropdownMenuItem<String>(
                    value: product,
                    child: Text(product, style: TextStyle(color: Colors.white)),
                  );
                }).toList(),
                onChanged: (String? value) {
                  setState(() {
                    _selectedProduct = value;
                  });
                },
                validator: (value) {
                  if (value == null) {
                    return "Por favor, selecione um produto";
                  }
                  return null;
                },
              ),
              SizedBox(height: 16.0),
              ElevatedButton(
                onPressed: _submitForm,
                child: Text("Enviar pedido de retirada", style: TextStyle(color: Colors.white,)),
                style: ElevatedButton.styleFrom(
                  primary: Colors.indigo,
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}