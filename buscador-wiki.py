""" Cria um programa onde você digita um termo e ele pesquisa na wikipedia,
resume o texto e devolve em um arquivo.txt """

import wikipedia

buscador = input('Digite algo para pesquisar: ')

wikipedia.set_lang('pt')   # Mudei a linguagem da busca para português
wikic = wikipedia.page(buscador)

wikit = wikic.title    # Retorna o título
wikic = wikic.content  # Retorna o conteúdo

with open(f'{buscador}.txt', 'w', encoding='utf-8') as wf1:
    wf1.write(wikit + '\n\n')
    wf1.write(str(wikic))

with open(f'{buscador}.txt', 'r', encoding='utf-8') as wf2:
    print(wf2.read())

# Caso o prompt da sua IDE retorne o texto sem formatação, verifique o arquivo criado na pasta
