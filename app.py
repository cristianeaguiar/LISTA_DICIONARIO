# tupla
atributos = ("Nome", " E-mail", "Profissão")


# lista de dicionarios
usuarios = [
    {
        atributos[0]:"Cris Aguiar" ,
        atributos[1]:"cris@gmail.com",
        atributos[2]:"programador"
    }, 
    {
        atributos[0]:"Sofia Aguiar",
        atributos[1]:"sofia@gmail.com",
        atributos[2]:"programador"
    },
    {
        atributos[0]:"Théo Aguiar",
        atributos[1]:"theo@gmail.com",
        atributos[2]:"Analista"
    }
]

# cadastrar um novo usuário
usuario = {}

for atributo in atributos:
    usuario[atributo] = input(f"Informe o valor do campo {atributo}: ")
usuarios.append(usuario)

# exibir os dados de cada usuário
for usuario in usuarios:
    print(" ")
    for atributo in atributos:
        print(f"{atributo}: {usuario.get("atributo")}.")
       
print(" ")