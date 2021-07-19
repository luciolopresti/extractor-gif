# Autor: Lúcio Lopresti.
# Licença: GNU GPL v2.0

import os, sys
from PIL import Image

# Variáveis globais.
#############################
progname = 'extract-gif.py'

EXIT_SUCCESS = 0
EXIT_FAILURE = 1
#############################
 
# Função para mostrar o uso deste programinha no editor de comandos. (Prompt de Comandos - WIN32 ou bash - Linux)
def usage():
    print('Uso incorreto!\n')
    print(f'Uso: [{progname}] [arquivo.gif] [diretório] - note que [diretório] é opcional.')
    sys.exit(EXIT_FAILURE)
    
# Função para criar um diretório caso o mesmo não exista.
# Argumentos:
#   - directory: Nome do diretório.
def create_dir_if_not_exists(directory):
    if os.path.exists(directory) == False:
        os.mkdir(directory)

# Função para extrair os frames do arquivo GIF.
# Argumentos:
#   - path: Localização (diretório) do arquivo GIF.
#   - filename: Nome do arquivo frame que será extraido. 
#   - extract: Diretório onde deve ser extraido os frames.
# @@ filename terá a mesma string que "path", porém com a extensão PNG.

def extract_gif(gif_path, filename, extract_path):
    try:
        im = Image.open(gif_path)
        raw = '{path:}\\{file:}{count:}.png'

        print(f'Arquivo GIF: \"{gif_path}\".\n')
        
        for frame in range(0, im.n_frames):
            im.seek(frame)
            print('Extraindo para ' + raw.format(path = extract_path, file = filename, count = frame))
            im.save(raw.format(path = extract_path, file = filename, count = frame))
    except FileNotFoundError:
        print('Erro: Arquivo GIF não encontrado.')
        sys.exit(EXIT_FAILURE)
    except:
        print('Erro: Não foi possível completar esta operação. Talvez o arquivo inserido não seja um GIF válido.')
        sys.exit(EXIT_FAILURE)

    print('\nConcluído!')

# Função para processar diretórios, argumentos e extrair os frames do GIF através da função extract_gif().
def process():
    extract_path = '.'
    
    if len(sys.argv) < 2:
        usage()

    gif_path = sys.argv[1]

    if len(sys.argv) == 3:
        extract_path = sys.argv[2]
        create_dir_if_not_exists(extract_path)

    file_without_extension = os.path.splitext(os.path.basename(sys.argv[1]))[0]

    if os.path.isdir(extract_path):
        extract_gif(gif_path, file_without_extension, extract_path)
    else:
        print(f'Erro: O diretório inserido não é um diretório válido.')
        sys.exit(EXIT_FAILURE)

# O início de tudo!
if __name__ == '__main__':
    try:
        process()
    except KeyboardInterrupt:
        print('CTRL-C pressionado. Saindo...')
        sys.exit(EXIT_FAILURE)

