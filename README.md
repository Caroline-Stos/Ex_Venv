<h1 align="center">CONFIGURANDO AMBIENTE VIRTUAL</h1>


<h2 align="left">1 - BAIXANDO O PROJETO E CRIANDO A VENV</h2>


***Crie um novo diretório para o projeto e o abra utilizando o VSCODE.

***De um git clone deste repositório (Ex_Venv) no github com o comando: git clone https://github.com/Caroline-Stos/Ex_Venv.git;

***No terminal do VSCODE, crie o ambiente virtual a partir do comando: python -m venv "nome_da_sua_venv";

***Navegue pelo terminal até a pasta de Scripts dentro da sua VENV já criada;

***Ative a VENV com o comando: Activate;

***Volte para o diretório do projeto;

***Uma vez que o ambiente virtual está ativado, instale as bibliotecas utilizadas no projeto executando o seguinte comando: pip install -r requirementss.txt;


<h2 align="left">2 - DEFININDO VARIÁVEL DE AMBIENTE</h2>


***Antes de rodar o arquivo python, primeiro defina o caminho para o arquivo de base dos dados utilizados na análise;

***Execute o seguinte comando no terminal + o caminho de onde está salvo o arquivo de base de dados "dados.csv": $Env:DATA_PATH = "seu_caminho_do_diretorio_para_o_arquivo_dados.csv";


<h2 align="left">3 - PRONTO! O projeto já pode ser executado na sua máquina...:D;</h2>


