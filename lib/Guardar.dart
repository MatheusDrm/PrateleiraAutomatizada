import 'package:flutter/material.dart';

class Guardar extends StatelessWidget {
  const Guardar({Key? key}) : super(key: key);

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
                    ElevatedButton(onPressed: (){}, child: const Text('1', style: TextStyle(color: Colors.white),), style: ElevatedButton.styleFrom(primary: Colors.amber),),
                    ElevatedButton(onPressed: (){}, child: const Text('2', style: TextStyle(color: Colors.white)), style: ElevatedButton.styleFrom(primary: Colors.amber)),
                    ElevatedButton(onPressed: (){}, child: const Text('3', style: TextStyle(color: Colors.white)), style: ElevatedButton.styleFrom(primary: Colors.amber)),
                    ElevatedButton(onPressed: (){}, child: const Text('4', style: TextStyle(color: Colors.white)), style: ElevatedButton.styleFrom(primary: Colors.amber)),
                    ElevatedButton(onPressed: (){}, child: const Text('5', style: TextStyle(color: Colors.white)), style: ElevatedButton.styleFrom(primary: Colors.amber)),
                    ElevatedButton(onPressed: (){}, child: const Text('6', style: TextStyle(color: Colors.white)), style: ElevatedButton.styleFrom(primary: Colors.amber)),
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
