# Projeto: Hackathon CNJ Inova - DESAFIO 1

## O projeto
Projeto do Desafio de Process Mining do Hackaton CNJ

## Organizacao do Projeto
------------
    ├── backend                         <- Arquivos dos serviços utilizados pela aplicação
    ├── data
    │   ├── external                    <- Dados obtidos de terceiros (não CNJ) 
    │   ├── interim                     <- Dados intermediários que sofreram alguma transformação.
    │   ├── log                         <- Dados referentes aos logs.
    │   ├── processed                   <- Conjuntos de dados canônicos para modelagem.
    │   └── raw                         <- Dados originais, brutos (não processados).
    ├── frontend                        <- Arquivos referentes a interface da aplicação
    ├── models                          <- Modelos treinados e serializados, previsões de modelos ou resumos de modelos
    ├── notebooks                       <- Jupyter notebooks. A convenção de nomenclatura é um número (para ordenação
    ├── references                      <- Dicionários de dados, manuais e todos os outros materiais explicativos.
    ├── reports                         <- Análise gerada como HTML, PDF, LaTeX, etc.
    │   └── figures                     <- Gráficos e figuras gerados para serem usados em relatórios
    ├── src                             <- Código-fonte para uso neste projeto.
    │   ├── data                        <- Scripts para criação ou geração dos dados
    │   ├── discovery                   <- Scripts para descoberta dos processos
    │   ├── features                    <- Scripts para transformar dados brutos em recursos para modelagem
    │   ├── models                      <- Scripts para treinar modelos e, em seguida, usar modelos treinados para fazer previsões
    │   └── visualization               <- Scripts para criar visualizações exploratórias e orientadas a resultados
    ├── test                            <- Testes realizados durante o projeto
    ├── utils                           <- Bibliotecas uteis ao projeto
    ├── requirements.txt                <- O arquivo de requisitos para reproduzir o ambiente de análise, por ex. gerado com `pip freeze > requirements.txt`
    ├── README.md                       <- README principal para os desenvolvedores deste projeto.
    └── .gitignore                      <- Arquivos ignorados pelo git.
    
## Metodologia do Projeto

O CRISP-DM (CRoss-Industry Standard Process for Data Mining) é uma metodologia de mineração de dados abrangente e um modelo de processo que auxilia a qualquer um - novatos a especialistas em mineração de dados - com um plano completo para conduzir um projeto de mineração de dados. CRISP-DM divide o ciclo de vida de um projeto de mineração de dados em seis fases: compreensão do negócio, compreensão de dados, preparação de dados, modelagem, avaliação e implantação. A Figura abaixo mostra as fases do CRISP-DM. As setas indicam as dependências mais
importantes e freqüentes entre as fases, enquanto o círculo externo simboliza a natureza cíclica de mineração de dados em si e ilustra que as lições aprendidas durante o processo de mineração de dados e da solução implantada pode desencadear novas questões de negócios, muitas vezes mais focadas.

<img src='reports/figures/CRISP-DM.png'>
![CRISP-DM](reports/figures/CRISP-DM.png)


## Bibliotecas utilizadas
### PM4Py
PM4Py é a plataforma de mineração de processos de código aberto líder escrita em Python.

>$ pip install pm4py

# Como executar o projeto

