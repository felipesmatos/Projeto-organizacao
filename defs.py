from time import sleep


def linha(tam=42):
    return '=' * tam


def menu(text):
    print(linha())
    print(text.center(42))
    print(linha())


def opc(lista):
    c = 1
    for op in lista:
        print(f'{c} - {op}')
        c+=1


def leiaint(text):
    valor = 0
    try:
        valor = int(input(text))
        if valor > 3:
            print('Erro:Por favor,digite uma opção valida.')
            return leiaint(text)
    except ValueError:
        print('Erro:Por favor,digite um valor valido.')
        return leiaint(text)
    except KeyboardInterrupt:
        print('Você saiu do sistema.')
        return leiaint(text)
    else:
            return valor
    

def vercad():
    print(menu('Opção 1'))
    cad = open('tarefas.txt','r')
    print(cad.read())
    sleep(1)
    

def cad():
    print(menu('Opção 2'))
    dados = {}
    op = 0
    cad = open('tarefas.txt','a')
    while True:
        dados['nome'] = str(input('Nome: ')).strip()
        dados['dataini'] = str(input('Data inicial: ')).strip()
        dados['dataf'] = str(input('Data final: ')).strip()
        dados['tarefa'] = str(input('Descrição da tarefa: '))
        cad.write(f'nome:{dados["nome"]}    de:{dados["dataini"]} até {dados["dataf"]} \nDescrição: {dados["tarefa"]}.')
        print(f'{dados["nome"]},foi adcionado(a)!')
        dados.clear()
        while True:
            op = str(input('Quer cadastrar mais alguma tarefa[S/N]? ')).upper()[0]
            if op in 'SN':
                break
        if op == 'N':
            break
    cad.close()
    sleep(1)


def fim():
    print(menu('Saindo do programa...'))
    sleep(1)


def criarq(nome):
    try:
        arq = open(f'{nome}','w')
        arq.close()
    except FileExistsError:
        print('Esse arquivo já existe,por favor crie um arquivo novo.')
        return criarq(nome)
    else:
        return arq