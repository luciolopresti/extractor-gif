# extractor-gif

Language: PT-BR

Um script para extrair "frames" de um GIF.
O formato GIF é composto por várias imagens, que juntas formam uma espécie de um "mini vídeo". E a intenção deste script, é extrair estas imagens, que são chamadas de "frames".

# Primeiramente, é necessário instalar o Python caso não o tenha em sua máquina.
Para Linux, execute o comando abaixo:
`sudo apt install python3` - para Debian e derivados;

Caso seu computador possua o Microsoft Windows, visite o site https://www.python.org/ e faça o download do instalador.

# Antes de executar este script, é necessário instalar a dependência deste script.
Para instalar a dependência do script, execute o comando:
`pip install Pillow` 

Para executar o script, execute o comando:
`python extractor-gif.py <Arquivo GIF> [Diretório]`, onde `[Diretório]` é opcional.

Se deseja extrair os *frames* de um GIF para um determinado diretório, acrescente o nome do diretório após inserir o arquivo do GIF. Caso o diretório não exista, ele será criado. Um exemplo: `python extractor-gif.py lua.gif lua`. O script criará a pasta `lua` caso não exista.

Se o diretório atual for `Documents` e nenhum diretório for específicado, os *frames* serão extraidos em `Documents`.

Qualquer ajuda será bem-vinda! 
