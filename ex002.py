import defs
#Trabalho por Felipe,Rudney e Guilherme

while True:#enquanto for verdade.
    defs.menu('Menu Principal')#chamando a função menu()
    defs.opc(['Ver tarefas cadastradas.', 'Cadastrar tarefas.', 'Encerrar programa.'])#chamando a função opc() e passando seu parâmetro
    print(defs.linha())
    op = defs.leiaint('Sua opção: ')#chamando função leiaint()
     #dependendo do valor da variavel op eu chamarei uma das seguintes funções.
    if op == 1:
        defs.vercad()
    elif op == 2:
        defs.cad()
    elif  op == 3:
        defs.fim()
        break