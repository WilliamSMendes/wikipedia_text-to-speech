""" Cria um programa no qual você digita um termo e ele pesquisa na wikipedia,
resume o texto e devolve em um arquivo.txt """

import wikipedia
import playsound
from gtts import gTTS
from deep_translator import GoogleTranslator
"""
GoogleTranslator(source = 'Linguagem de origem' , target = 'Linguagem da Tradução').translate('texto a ser traduzido')

    *Linguagem de origem : Linguagem do texto original , caso use o valor "auto" ele detecta automaticamente a lingua original ;

    *Linguagem da Tradução : Linguagem que queremos ter o texto ;

    *texto a ser traduzido : O texto que queremos fazer a tradução;
"""

buscador = input('Digite algo para pesquisar: ')

wikipedia.set_lang('pt')  # Idioma alterado para Português
wikic = wikipedia.page(buscador)

wikit = wikic.title    # Retorna o título
wikic = wikic.content  # Retorna o conteúdo

with open(f'{buscador}.txt', 'w', encoding='utf-8') as wf1:
    wf1.write(wikit + '\n\n')
    wf1.write(str(wikic))

with open(f'{buscador}.txt', 'r', encoding='utf-8') as wf2:
    print(wf2.read())

print('\n\nAguarde um momento enquanto o audio carrega...\n\n')

fala = gTTS(text=wikic, lang='pt')
audio = "audio.mp3"
fala.save(audio)
playsound.playsound(audio)
