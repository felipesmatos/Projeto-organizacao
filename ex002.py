import defs
#Trabalho por Felipe,Rudney e Guilherme

while True:
    defs.menu('Menu Principal')
    defs.opc(['Ver tarefas cadastradas.', 'Cadastrar tarefas.', 'Encerrar programa.'])
    print(defs.linha())
    op = defs.leiaint('Sua opção: ')
    if op == 1:
        defs.vercad()
    elif op == 2:
        defs.cad()
    elif  op == 3:
        defs.fim()
        break