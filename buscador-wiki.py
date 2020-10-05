""" Cria um programa no qual você digita um termo e ele pesquisa na wikipedia,
resume o texto e devolve em um arquivo.txt """

import wikipedia
import playsound
from gtts import gTTS


buscador = input('Digite algo para pesquisar: ')

wikipedia.set_lang('pt')  # Idioma mudado para Português
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
