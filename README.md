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

<img src='/reports/figures/crisp-dm.png'>

<a id="entendimento_negocio"></a>
## Entendimento do Negócio
A primeira etapa do modelo CRISP-DM é o entendimento do negócio, abaixo descrevemos um briefing do desafio extraído do documento oficial do Hackathon: DESAFIO ENAP - CNJ INOVA Briefing.pdf

**Desafio:** Como podemos, a partir da base do DataJud, identificar padrões e comparar o andamento de processos em cada unidade judiciária do Brasil, levando em consideração as peculiaridades locais e o nível de comlexidade, em razão da competência e da matéria do direito?

**Complemento:** judiciárias, nas diferentes localidades e regiões do Brasil. A consequência direta é a dificuldade em proporcionar transparência, tanto interna quanto externa, necessária aos dados que são produzidos pelas unidades judiciárias, e a impossibilidade de gerenciar soluções para os gargalos, que não conseguem ser devidamente identificados.

Outro material particularmente interessante, disponibilizado pelo Hackathon foi o Estudos CNJ casos e relatos - personas.pdf, do qual pudemos extrair algumas necessidades dos usuários:

Após esse primeiro entendimento do desafio e das necessidades dos usuários, mergulhamos no entendimento do negócio em sí, para tanto conversamos com algumas pessoas atuantes no direito (advogados, servidores), fizemos diversas pesquisas na internet e também utilizamos como referência o relatório: [**Justiça em números 2020**](https://www.cnj.jus.br/pesquisas-judiciarias/justica-em-numeros/) do CNJ, no qual reproduzimos abaixo algumas informações importantes, extraídas do documento citado, para entendimento da justiça no Brasil.

### O poder judiciário
O Poder Judiciário brasileiro divide-se em cinco ramos: Justiça Estadual, Justiça do Trabalho, Justiça Federal,
Justiça Eleitoral e Justiça Militar. Cada um desses ramos possui órgãos, que são organizados em instâncias. Também fazem parte do Judiciário os tribunais superiores, o Supremo Tribunal Federal e o Conselho Nacional de Justiça, que, como citado, por possuírem seus próprios relatórios e estatísticas e, portanto, não serão abordados neste diagnóstico.

Diante disso, segue sumário explicativo das competências e da estrutura de cada segmento de justiça e dos
quatro tribunais superiores: STJ, STM, TSE e TST.

### justiça Estadual
<img src='/reports/figures/justiça.png'>

### justiça do Trabalho
<img src='/reports/figures/justiça_trabalho.png'>

### Justiça Federal
<img src='/reports/figures/justiça_federal.png'>

### Justiça Eleitoral
<img src='/reports/figures/justiça_eleitoral.png'>

### Justiça Militar (Estadual e da União)
<img src='/reports/figures/justiça_militar_estadual.png'>
<img src='/reports/figures/justiça_militar_uniao.png'>

### Justiça Tribunais Superiores
<img src='/reports/figures/justiça_tribunais.png'>
<img src='/reports/figures/justiça_tribunais2.png'>

<a id="definicao_problema"></a>
### Definição do problema
Analisando os documentos disponibilizados pelo Hackathon: **DESAFIO ENAP - CNJ INOVA Briefing.pdf** e **Estudos CNJ casos e relatos - personas.pdf** pudemos entender melhor o contexto geral do problema e as necessidades dos principais Stakeholders envolvidos. Diante de tantas possibilidades, decidimos restringir o escopo do projeto para atender essencialmente as necessidades identificadas da **persona do JUIZ/DESEMBARGADOR**, que:
> Cuida, atualmente, de uma vara com <font color=red>80.000 processos</font>, sendo a maioria físicos, sente que sua equipe está motivada e quer gerar resultados, mas diante da quantidade de **processos pendentes de julgamento** e da administração da sua unidade judiciária, **vê-se absolutamente sem tempo**.

> Desejos:<br>
* Entender **onde estão os <font color=red>problemas da sua unidade judiciária</font>** para poder consertá-los e <font color=blue>incrementar sua produtividade</font>.
* Quer que sua produtividade fosse <font color=blue>**comparada com seus semelhantes</font>**, levando em consideração as competências, a situação atual e os recursos disponíveis.
* **<font color=blue>Receber relatórios estatísticos</font>** que o norteiam sobre o desenvolvimento dos julgados, para saber se sua equipe está produzindo bem gostaria também de melhorar a triagem dos processos, por meio de melhor cadastramento, para poder otimizar seus julgados pelo julgamento “em bloco”.

>Dores:<br>
* **Comparam sua unidade judiciária** com outras que **<font color=red>desempenham funções diferentes</font>**
* Os processos que chegam até ele frequentemente mal cadastrados e com dados equivocados que o forçam a buscar dados na petição inicial para sanear o cadastramento. (DESAFIO 2).

Nesse sentido, formalizamos o problema como:

>**PROBLEMA:**
Os Juizes e Desembargadores não possuem uma ferramenta que possa auxiliá-los a incrementar sua produtividade, identificando onde estão os problemas de sua unidade e sugerindo ações para corrigi-los ou minimizá-los. 

Através da formalização do problema, pudemos identificar vários sub-problemas (desafios) que deveriam ser endereçados para que o problema pudesse ser resolvido.
* Identificar indicadores de produtividade relevantes
* Definir uma forma de simplificar e comparar os processos de unidades distintas
* Definir um critério de agrupamento de unidades judiciárias semelhantes levando em consideração as competências, situação atual e os recursos disponíveis da unidade judiciária


### Busca dos dados
A principal fonte de dados para o Hackathon serão os dados básicos e movimentações processuais contidos no banco de dados unificado do CNJ, referenciado como DataJud, que será disponibilizado no formato Json, conforme informações apresentadas no [Webinar - dados](https://youtu.be/VBDGxGxgTPw). Adicionalmente identificamos as possíveis fontes de dados:
* **[IBGE - Instituto Brasileiro de Geografia e Estatística](https://www.ibge.gov.br/explica/codigos-dos-municipios.php)** - Para obtenção de informações quanto aos municípios brasileiros.
* **[SGT - Sistema de Gestão das Tabelas Processuais Unificadas](https://www.cnj.jus.br/sgt/consulta_publica_assuntos.php)** - Para obtenção dos "depara" dos assuntos, classes e movimentos processuais
* **[CNJ - Conselho Nacional de Justiça](https://paineis.cnj.jus.br/QvAJAXZfc/opendoc.htm?document=qvw_l%2FPainelCNJ.qvw&host=QVS%40neodimio03&anonymous=true&sheet=shResumoDespFT)** - Consulta aos paineis da justiça para obtenção de dados referentes a produtividade e demais informações sobre a justiça.

## Bibliotecas utilizadas
### PM4Py
PM4Py é a plataforma de mineração de processos de código aberto líder escrita em Python.

>$ pip install pm4py

# Como executar o projeto

