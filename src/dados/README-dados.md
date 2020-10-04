# Programas utilizados
Os dados referentes as tabelas unificadas processuais estão armazenados num banco SQLite. Nesse sentido, utilizamos a ferramenta **DB Browser for SQLite**
 disponível em https://sqlitebrowser.org/ para gerenciar esse banco de dados.
 
# Transformações nos dados

## Tabelas processuais unificadas
Abaixo segue o passo a passo para gerar os dados referentes a: assuntos, classes e movimentos do CNJ. O primeiro passo é a criação do banco SQLite a partir 
dos arquivos de dump disponibilizados na página do CNJ (https://www.cnj.jus.br/sgt/versoes.php). Após montar o banco de dados, gera-se um script para criação dos dataframes.

### Etapa 1: Criaçao do banco SQLite
1. Abra o arquivo dump_estrutura.sql (da pasta dados/brutos) com um editor de texto e substitua o caractere ` pelo caractere '
2. Abra um conversor de script MySQL para SQLite, como por exemplo: https://ww9.github.io/mysql2sqlite/
3. Cole o conteúdo do arquivo modificado no passo 1 e clique no Botão CONVERT
5. Salve o conteúdo convertido para o arquivo: dump_estruturaSQLite.sql (dentro da pasta dados/provisorios)
6. Com um editor de texto e substitua o caractere ` pelo caractere ', para o arquivo criado no passo 5 e salve o arquivo
7. Informe o nome da tabela para cada criação de indice, conforme especificação abaixo:

De:

>CREATE INDEX '_cod_item' ON '' ('cod_item');
CREATE INDEX '_cod_item_pai' ON '' ('cod_item_pai');
CREATE INDEX '_cod_classe' ON '' ('cod_classe');
CREATE INDEX '_cod_assunto' ON '' ('cod_assunto');
CREATE INDEX '_cod_movimento' ON '' ('cod_movimento');
CREATE INDEX '_FK_complemento' ON '' ('seq_tipo_complemento');
CREATE INDEX '_FK_complemento_movimento' ON '' ('seq_complemento');
CREATE INDEX '_FK2_complemento_movimento' ON '' ('cod_movimento');
CREATE INDEX '_FK_complemento_tabelado' ON '' ('seq_complemento');
CREATE INDEX '_seq_item' ON '' ('cod_movimento');
CREATE INDEX '_seq_tipo_complemento' ON '' ('seq_tipo_complemento');
CREATE UNIQUE INDEX '_uk_teit_tipo_item' ON '' ('seq_item');
CREATE INDEX '_fk_tipo_ramo_justica_teit' ON '' ('seq_tipo_ramo_justica');
CREATE INDEX '_fk_temporalidade_teit' ON '' ('seq_temp');
CREATE INDEX '_fk_itens_teit' ON '' ('seq_item');

Para:

>CREATE INDEX '_cod_item' ON **'itens'** ('cod_item');
CREATE INDEX '_cod_item_pai' ON **'itens'** ('cod_item_pai');
CREATE INDEX '_cod_classe' ON **'classes'** ('cod_classe');
CREATE INDEX '_cod_assunto' ON **'assuntos'** ('cod_assunto');
CREATE INDEX '_cod_movimento' ON **'movimentos'** ('cod_movimento');
CREATE INDEX '_FK_complemento' ON **'complemento'** ('seq_tipo_complemento');
CREATE INDEX '_FK_complemento_movimento' ON **'complemento_movimento'** ('seq_complemento');
CREATE INDEX '_FK2_complemento_movimento' ON **'complemento_movimento'** ('cod_movimento');
CREATE INDEX '_FK_complemento_tabelado' ON **'complemento_tabelado'** ('seq_complemento');
CREATE INDEX '_seq_item' ON **'procedimento_complementos'** ('cod_movimento');
CREATE INDEX '_seq_tipo_complemento' ON **'procedimento_complementos'** ('seq_tipo_complemento');
CREATE UNIQUE INDEX '_uk_teit_tipo_item' ON **'temp_item'** (**'seq_item','tipo_item','seq_tipo_ramo_justica'**);
CREATE INDEX '_fk_tipo_ramo_justica_teit' ON **'temp_item'** ('seq_tipo_ramo_justica');
CREATE INDEX '_fk_temporalidade_teit' ON **'temp_item'** ('seq_temp');
CREATE INDEX '_fk_itens_teit' ON **'temp_item'** ('seq_item', 'tipo_item');

8. Abra o prompt de comando, e vá para a pasta: dados/provisorios
9. Execute o comando para criação da base: sqlite3.exe TPU.db -init dump_estrutura_SQLite.sql
10. Após executar o comando acima, o prompt de comando do sqlite ficará aberto. Digite: **.quit** para fechá-lo.

#### Importação dos dados das tabelas processuais unificadas
1. Abra o arquivo dump_dados.sql (da pasta dados/brutos) com um editor de texto e substitua a segunda linha: SET foreign_key_checks = 0; 
pelo bloco de comandos:

>PRAGMA journal_mode = MEMORY;
PRAGMA synchronous = OFF;
PRAGMA foreign_keys = OFF;
PRAGMA ignore_check_constraints = OFF;
PRAGMA auto_vacuum = NONE;
PRAGMA secure_delete = OFF;

2. substitua a última linha: SET foreign_key_checks = 1; pelo bloco de código abaixo:

>PRAGMA ignore_check_constraints = ON;
PRAGMA foreign_keys = ON;
PRAGMA journal_mode = WAL;
PRAGMA synchronous = NORMAL;

3. Substitua o termo: sgt_consulta. por um espaço em branco
4. Substitua o termo: '5 º, LXVIII e LXXVII;102, I, \"d\" e \"i\' por: '5 º, LXVIII e LXXVII;102, I, \"d\" e \"i\
5. Substitua o termo: 7º a 20,I, \"a\" e 21 (Lei n. 9.507/1997); 9º, I, \"f\' por: 7º a 20,I, \"a\" e 21 (Lei n. 9.507/1997); 9º, I, \"f\
6. Salve o conteúdo do texto para o arquivo: dump_dados_SQLite.sql (dentro da pasta dados/provisorios)
7. Abra o prompt de comando, e vá para a pasta: dados/provisorios
8. Abra o banco de dados criado com o comando: sqlite3.exe TP.db
9. O prompt do sqlite será aberto. Execute o comando para importacao dos dados: .read dump_dados_SQLite.sql
10. Após executar o comando acima, o prompt de comando do sqlite ficará aberto. Digite: **.quit** para fechá-lo.


### Etapa 2: Geração dos dataframes para classe, assunto e movimento
1. Abra o prompt de comando, e vá para a pasta: src/dados
2. Executar o script 01-Criacao_DF_TPU.py

>python 01-Criacao_DF_TPU.py

O script irá gerar na pasta: dados/provisorios, os seguintes arquivos:
* df_assuntos.csv
* df_classes.csv
* df_movimentos.csv
