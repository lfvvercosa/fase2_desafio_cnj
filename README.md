# desafio_cnj
Projeto do Desafio de Process Mining do Hackaton CNJ

## Organizacao do Projeto
------------
    ├── dados
    │   │
    │   ├── brutos                      <- Dados originais, brutos (não processados).
    │   │   ├── dump_estrutura.sql      <- Estrutura das tabelas processuais unificadas (Classe, assunto, movimento)
    │   │   └── dump_dados.sql          <- Dados das tabelas processuais unificadas (inserts)
    │   │
    │   ├── externos                    <- Dados obtidos de terceiros (não CNJ)
    │   │   └── RELATORIO...ICIPIO.xls  <- Tabela dos municípios do brasil (fonte IBGE)
    │   │
    │   ├── processados                 <- Conjuntos de dados canônicos para modelagem.
    │   │
    │   └── provisorios                 <- Dados intermediários que sofreram alguma transformação.
    │       ├── df_assuntos.csv         <- Dados dos assuntos gerado pelo script 01-Criacao_DF_TPU.py a partir do banco TPU.db
    │       ├── df_classes.csv          <- Dados das classes gerado pelo script 01-Criacao_DF_TPU.py a partir do banco TPU.db
    │       ├── df_movimentos.csv       <- Dados dos movimentos gerado pelo script 01-Criacao_DF_TPU.py a partir do banco TPU.db
    │       ├── dump_dados...Lite.sql   <- Inserts das tabelas processuais unificadas para o banco SQLIte
    │       ├── dump_estrutu..Lite.sql  <- Estrutura de banco para as tabelas processuais unificadas para o banco SQLite
    │       └── TPU.db                  <- (arquivo 13Gb), não incluso no Git. Banco SQLite com os dados das tabelas processuais unificadas
    │
    ├── modelos                         <- Modelos treinados e serializados, previsões de modelos ou resumos de modelos
    │
    ├── notebooks                       <- Jupyter notebooks. A convenção de nomenclatura é um número (para ordenação),
    │                                      as iniciais do criador e uma breve descrição delimitada por `-`, por exemplo
    │                                      `1.0-jqp-initial-data-exploration`.  
    │
    ├── referencias                     <- Dicionários de dados, manuais e todos os outros materiais explicativos.
    │   ├── Conventional...beta2.pdf│   <- Guia para padronização das mensagens no Git.
    │   ├── DESAFIO EN...Briefing.pdf   <- DESAFIO ENAP - CNJ INOVA Briefing.pdf
    │   ├── Estudos C...personas.pdf    <- Estudos CNJ casos e relatos - personas.pdf  Informações Complementares CNJ Inova - Desafios e Dados.pdf
    │   └── Informacoes C...Dados.pdf   <- Informacoes Complementares CNJ Inova - Desafios e Dados.pdf
    │
    ├── relatorios                      <- Análise gerada como HTML, PDF, LaTeX, etc.
    │   └── figuras                     <- Gráficos e figuras gerados para serem usados em relatórios
    │
    ├── src                             <- Código-fonte para uso neste projeto.
    │   │
    │   ├── dados                       <- Scripts para criação ou geração dos dados
    │   │   ├── README-dados.md         <- Explicações das transformação nos dados. Dados brutos (brutos ou externos) para dados transformados (provisorios ou processados)
    │   │   └── 01-Criacao_DF_TPU.py    <- Script para geração dos dataframes referentes as tabelas processuais unificadas (classe, assunto, movimento)
    │   │
    │   ├── recursos                    <- Scripts para transformar dados brutos em recursos para modelagem
    │   │
    │   ├── modelos                     <- Scripts para treinar modelos e, em seguida, usar modelos treinados para fazer previsões
    │   │
    │   └── visualizacao                <- Scripts para criar visualizações exploratórias e orientadas a resultados
    │
    ├── requirements.txt                <- O arquivo de requisitos para reproduzir o ambiente de análise, por ex. gerado com `pip freeze > requirements.txt`
    ├── README.md                       <- README principal para os desenvolvedores deste projeto.
    └── .gitignore                      <- Arquivos ignorados pelo git.

## Bibliotecas utilizadas
### PM4Py
PM4Py é a plataforma de mineração de processos de código aberto líder escrita em Python.

>$ pip install pm4py

### psycopg2
Psycopg é o adaptador de banco de dados PostgreSQL mais popular para a linguagem de programação Python. Suas principais características são a implementação completa da especificação Python DB API 2.0 e a segurança de thread (vários threads podem compartilhar a mesma conexão). Ele foi projetado para aplicativos altamente multithread que criam e destroem muitos cursores e fazem um grande número de “INSERT” s ou “UPDATE” s simultâneos.

>$ pip install psycopg2


# Como executar o projeto

