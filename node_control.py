var mysql = require("mysql")

var con = mysql.createConnection({
    host: "localhost",
    user: "root",
    password: "jjbalvpo",
    database : "DB"
  });

const io = require("socket.io")(require("http").createServer(function(){}).listen(80)); 

io.on("connection", io =>{
    console.log("Conexão estabelecida")
    con.connect();
    dados = con.query("Select * FROM armazen", function(err, result){
        if (err) throw err
    })
    io.emit("enviando",dados)
    console.log("Conectado")
})

io.on("salvar", (dono, objeto, compartimento) =>{
    values = [[dono, objeto, compartimento]]
    con.query("Insert INTO armazen (dono, objeto, compartimento) VALUES ?", [values], function(err, result){
        if (err) throw err
    })
    console.log("Dados Salvos")
    dados = con.query("Select * FROM armazen", function(err, result){
        if (err) throw err
    })
    io.emit("enviando",dados)
    console.log("Dados atualizados")


    io.emit("procedimentoArmazenar", { compartimento: compartimento });
})
