const objetos = {};
var mysql = require("mysql");

dados = null

var con = mysql.createConnection({
    host: "localhost",
    user: "root",
    password: "jjbalvpo",
    database : "DB"
  });

const io = require("socket.io")(
    require("http").createServer(
        function(){}
    ).listen(80)
);

io.on("connection", (client) =>{
        con.query("Select * FROM armazen",async function (err, resultado, fields){dados  =  resultado})
        if (dados){
            console.log("Conectado")
            console.log(dados)}  
            io.emit("iniciando",dados)
        client.on("retirar", (compartimento)=>{
            console.log(compartimento)
            con.query("Delete FROM armazen where Compartimento = ?", [compartimento], (err, result)=>{
                if (err){
                    console.log(err)
                }
                console.log(result)})
        })
        client.on("salvar", (dono, objeto, compartimento) =>{
            con.query("Insert into armazen (nome, objeto, compartimento) Values ?", [[[dono, objeto, compartimento]]],(err, result)=>{
                if(err){
                    console.log(err)
                }
                console.log(result)
            })
            console.log(dono+objeto+compartimento)
        })
})
