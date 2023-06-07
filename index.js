const objetos = {};
var mysql = require("mysql")

var con = mysql.createConnection({
    host: "3306",
    user: "root",
    password: "jjbalvpo",
    database : "DB"
  });

const io = require("socket.io")(
    require("http").createServer(
        function(){}
    ).listen(80)
);

io.on("connection", io =>{
    con.connect();
    dados = con.query("Select *")
    io.emit("iniciando",dados)
    console.log("Conectado")
})

io.on("salvar", (dono, objeto, compartimento) =>{
    con.query("Insert into DB (dono, objeto, compartimento))")
    console.log("Dados Salvos")
})

con.end()