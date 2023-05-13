from time import sleep

#essa função retorna o valor "=" o numero de vezes de "tam",nesse caso 42.
def linha(tam=42):
    return '=' * tam

#essa função retorna o texto mandado como parâmetro a ela centralizado com 42 espaços a cada lado.
def menu(text):
    print(linha())
    print(text.center(42))
    print(linha())

#essa função recebe uma lista/array,que contem opções.
def opc(lista):
    c = 1
    #para cada op(que vale por cada valor em lista) em lista, eu irei repetir o looping,assim,no primeiro looping retornarei "1 - 'algum valor da lista'".
    for op in lista:
        print(f'{c} - {op}')
        c+=1

#essa função funciona como um input,resumidamente recebe um texto para mostrar ao usuario e ele vai nos mandar um valor,a ideia é ter certeza que esse valor é o que queremos,nesse caso,um valor inteiro menor ou igual a 3.
def leiaint(text):
    valor = 0
    try:
        valor = int(input(text))
        if valor > 3:
            #se for maior que 3 retornamos um erro e chamamos essa mesma função,gerando um looping.
            print('Erro:Por favor,digite uma opção valida.')
            return leiaint(text)
    except ValueError:#erro se não for um valor inteiro.
        print('Erro:Por favor,digite um valor valido.')
        return leiaint(text)
    except KeyboardInterrupt:
        print('Você saiu do sistema.')
        return leiaint(text)
    else:
            return valor
    
#essa função abre o nosso arquivo txt e retorna os valores inseridos nele.
def vercad():
    print(menu('Opção 1'))
    cad = open('tarefas.txt','r')
    print(cad.read())
    sleep(1)
    
#essa é a função que cadastra as tarefas
def cad():
    print(menu('Opção 2'))
    dados = {}#dicionario/array
    op = 0
    cad = open('tarefas.txt','a')#abri o arquivo txt
    while True:
        dados['nome'] = str(input('Nome: ')).strip()
        dados['dataini'] = str(input('Data inicial: ')).strip()
        dados['dataf'] = str(input('Data final: ')).strip()
        dados['tarefa'] = str(input('Descrição da tarefa: '))#até aqui são só os inputs dos valores que irei colocar no txt
        cad.write(f'nome:{dados["nome"]}    de:{dados["dataini"]} até {dados["dataf"]} \nDescrição: {dados["tarefa"]}.')#formatação de como esses arquivos serão inseridos no txt
        print(f'{dados["nome"]},foi adcionado(a)!')#informe ao usuario
        dados.clear()#limpei os dados inseridos no dicionario
        while True:
            #looping para saber se o usuario gostaria de inserir mais uma tarefa na lista
            op = str(input('Quer cadastrar mais alguma tarefa[S/N]? ')).upper()[0]#uooer() coloca os valores inseridos em letras maiusculas e o [0] recebe somente a primeira letra da frase.
            if op in 'SN':
                #se o valor de op estiver entre a string "SN",então o usuario respondeu corretamente a pergunta.
                break
        if op == 'N':
            #se op for exatamente "N",então ele não quer adcionar outro valor,saimos dos todos os loopings
            break
    cad.close()#fechamos o arquivo txt
    sleep(1)

#função para criar um encerramento de programa estilizado
def fim():
    print(menu('Saindo do programa...'))
    sleep(1)

#essa função não foi usada no programa
def criarq(nome):
    try:
        arq = open(f'{nome}','w')
        arq.close()
    except FileExistsError:
        print('Esse arquivo já existe,por favor crie um arquivo novo.')
        return criarq(nome)
    else:
        return arq