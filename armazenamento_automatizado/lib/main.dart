import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:socket_io_client/socket_io_client.dart' as IO;


void main(){
  SystemChrome.setPreferredOrientations([DeviceOrientation.portraitUp]);
  runApp(MyApp());
}

class MyApp extends StatefulWidget{

  @override
  MyAppState createState() => MyAppState();
}

class MyAppState extends State{

  late IO.Socket socket;

  @override
  void initState() {
    initSocket();
    super.initState();
  }
  initSocket() {
    socket = IO.io('http://192.168.0.8:80', <String, dynamic>{
      'autoConnect': false,
      'transports': ['websocket'],
    });
    socket.connect();
    socket.onConnect((_) {
      print('Connection established');
    });
    socket.onDisconnect((_) => print('Connection Disconnection'));
    socket.onConnectError((err) => print(err));
    socket.onError((err) => print(err));
  }

  retirar(int comp){
    socket.emit("retirar", comp);
  }

  salvar(var cliente, var objeto, var compartimento){
    socket.emit('salvar', [cliente, objeto, compartimento]);
  }


 GlobalKey<FormState> _formKey = new GlobalKey<FormState>();
  String? _selectedProduct;
  var cliente = new TextEditingController();
  var objeto = new TextEditingController();
  var compartimento = new TextEditingController();
  List<String> _products = [
    "1",
    "2",
    "3",
    "4",
    "5"
  ];

  @override
  Widget build(BuildContext context){
    return MaterialApp(
      title: 'armazenamento_automatizado',
      home:Scaffold(
        body: Container(
          width: double.infinity,
          decoration: BoxDecoration(
            gradient: LinearGradient(
              begin: Alignment.topCenter,
              colors: [
                Colors.purple[900]!,
                Colors.purple[800]!,
                Colors.purple[400]!
              ],
            ),
          ),
          child: SingleChildScrollView(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: <Widget>[
                SizedBox(height:  40,),
                Padding(
                  padding: EdgeInsets.all(20),
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: <Widget>[
                      Text("Armazem automático", style: TextStyle(color: Colors.white, fontSize: 35)),
                      SizedBox(height: 10,),
                      Text("Escolha uma operação:", style: TextStyle(color: Colors.white, fontSize: 18))
                    ],
                  ),
                ),
                SizedBox(height: 15,),
                Container(
                  decoration: BoxDecoration(borderRadius: BorderRadius.all(Radius.circular(15)), color: Colors.black54),
                  margin: EdgeInsets.symmetric(horizontal: 20),
                    height: 300,
                    width: 400,
                  child: Column(
                    children: [
                      SizedBox(height: 20),
                      Text('Retirar', style: TextStyle(fontSize: 20, color: Colors.white),),
                      SizedBox(height: 15,),
                      SizedBox(
                        width: 370,
                        height: 240,
                        child: GridView.count(
                          crossAxisCount: 3,
                          padding: EdgeInsets.symmetric(horizontal: 20),
                          crossAxisSpacing: 10,
                          mainAxisSpacing: 10,
                          children: [
                            ElevatedButton(onPressed: (){retirar(1);}, child: Text('1'), style: ButtonStyle(backgroundColor: MaterialStateProperty.all<Color>(Colors.orange[900]!)),),
                            ElevatedButton(onPressed: (){retirar(2);}, child: Text('2'), style: ButtonStyle(backgroundColor: MaterialStateProperty.all<Color>(Colors.orange[900]!)),),
                            ElevatedButton(onPressed: (){retirar(3);}, child: Text('3'), style: ButtonStyle(backgroundColor: MaterialStateProperty.all<Color>(Colors.orange[900]!)),),
                            ElevatedButton(onPressed: (){retirar(4);}, child: Text('4'), style: ButtonStyle(backgroundColor: MaterialStateProperty.all<Color>(Colors.orange[900]!)),),
                            ElevatedButton(onPressed: (){retirar(5);}, child: Text('5'), style: ButtonStyle(backgroundColor: MaterialStateProperty.all<Color>(Colors.orange[900]!)),),
                            ElevatedButton(onPressed: (){retirar(6);}, child: Text('6'), style: ButtonStyle(backgroundColor: MaterialStateProperty.all<Color>(Colors.orange[900]!),),),

                          ],
                        ),
                      )
                    ],
                  ),
                  ),
                SizedBox(height: 15,),
              Container(
                  decoration: BoxDecoration(borderRadius: BorderRadius.all(Radius.circular(15)), color: Colors.black54),
                  margin: EdgeInsets.symmetric(horizontal: 20),
                  height: 300,
                  width: 400,
                  child: Column(
                      children: [
                        SizedBox(height: 20),
                        Text('Guardar', style: TextStyle(fontSize: 20, color: Colors.white),),
                        SizedBox(height: 15,),
                        SizedBox(
                          width: 370,
                          height: 240,
                          child: Form(
                            key: this._formKey,
                            child: Column(
                              children: [
                              Padding(
                                padding: const EdgeInsets.symmetric(horizontal: 15.0),
                                child: TextFormField(
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
                                  controller: cliente,
                            ),
                              ),
                                Padding(
                                  padding: const EdgeInsets.symmetric(horizontal: 15.0),
                                  child: TextFormField(
                                    style: TextStyle(color: Colors.white),
                                    decoration: InputDecoration(
                                      labelText: "Nome do objeto",
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
                                        return "Por favor, insira o nome do objeto";
                                      }
                                      return null;
                                    },
                                    controller: objeto,
                                  ),
                                ),
                                Padding(
                                  padding: const EdgeInsets.symmetric(horizontal: 15.0),
                                  child: DropdownButtonFormField<String>(
                                    value: _selectedProduct,
                                    style: TextStyle(color: Colors.white),
                                    decoration: InputDecoration(
                                      labelText: "Compartimento",
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
                                      return null;}
                                  ),
                                ),
                                SizedBox(height: 10),
                                ElevatedButton(onPressed: (){print(this.cliente);salvar(cliente.text, objeto.text, 2);}, child: Text('Enviar'), style: ButtonStyle(backgroundColor: MaterialStateProperty.all<Color>(Colors.orange[900]!)),),
                              ],
                            ),
                          ),
                  )]
                  )
              )
              ],
            ),
          ),
        )
        ),
      );
  }
}
