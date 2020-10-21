<div align="center"><img img src='/reports/figures/logo.png' width="200"></div> 

<h1 align=center>Projeto: Hackathon CNJ Inova - DESAFIO 1</h1>

## O projeto
Projeto do Desafio de Process Mining do Hackaton CNJ

## Organizacao do Projeto 

### git: https://github.com/lfvvercosa/desafio_cnj

------------
    ├── data
    │   ├── external                    <- Dados obtidos de terceiros (não CNJ) 
    │   ├── interim                     <- Dados intermediários que sofreram alguma transformação.
    │   ├── log                         <- Dados referentes aos logs.
    │   ├── processed                   <- Conjuntos de dados canônicos para modelagem.
    │   └── raw                         <- Dados originais, brutos (não processados).
    ├── frontend                        <- Arquivos referentes a interface da aplicação
    ├── notebooks                       <- Jupyter notebooks. A convenção de nomenclatura é um número (para ordenação
    ├── references                      <- Dicionários de dados, manuais e todos os outros materiais explicativos.
    ├── reports                         <- Análise gerada como HTML, PDF, LaTeX, etc.
    │   └── figures                     <- Gráficos e figuras gerados para serem usados em relatórios
    ├── src                             <- Código-fonte para uso neste projeto.
    │   ├── data                        <- Scripts para criação ou geração dos dados
    ├── log                             <- Modelos utilizados na etapa de pré-processamento
    ├── visualization                   <- Modelos utilizados na etapa de pré-processamento
    ├── process                         <- Modelos utilizados na etapa de pré-processamento
    │   ├── CreateJSONDB.py             <- Script para geração de .json's para popular o banco de dados do backend
    │   ├── MacroSteps.py               <- Classe responsável pela criação das macroetapas
    ├── test                            <- Scripts de testes realizados durante o projeto
    ├── utils                           <- Classes úteis à etapa de pré-processamento
    ├── README.md                       <- README principal contendo a descrição das principais etapas e arquivos do projeto
    ├── swagger.yaml                    <- Definição dos endpoints do backend (o backend está no repósitorio git: gabriel-bandeira/backend-desafio-cnj)
    ├── tabelas.dbdiagram               <- Definição das tabelas do banco de dados
    └── .gitignore                      <- Arquivos ignorados pelo git
    
### git: https://github.com/gabriel-bandeira/backend-desafio-cnj

------------
    ├── panorama                        
    │   ├── settings.py                 <- Arquivo de configurações
    │   ├── urls.py                     <- Endpoints do banco de dados
    ├── performance                     <- App django da aplicação
    │   ├── models.py                   <- Modelos django do banco de dados
    │   ├── urls.py                     <- Endpoints do banco de dados
    │   ├── views.py                    <- Views django referentes aos endpoints
    ├── requirements.txt                <- Especifica dependências do Django a serem instaladas com o comando 'pip'

## Bibliotecas e Framework utilizados

### PM4Py
PM4Py é a plataforma de mineração de processos de código aberto líder escrita em Python.
>$ pip install pm4py

### Django
Django é um framework web em python que encoraga desenvolvimento rápido e limpo.
>$ pip install Django

### Scikit-learn
Scikit-learn is a machine learning python library
>$ pip install -U scikit-learn


## Como executar o projeto   

Nosso time subiu os servidores do backend e do front-end na plataforma gratuira Heroku. Dessa forma, é possível acessar nossa solução, batizada de Panorama, utilizando o seguinte endereço web:
    http://desafio-cnj-frontend.herokuapp.com/
    
**OBS(1)**: É importante destacar limitação da versão gratuita da plataforma Heroku. Ela restringe o número de conexões máximas ao banco de dados, sendo assim, após extendido uso, o banco de dados pode ficar indisponível por alguns minutos. 

**OBS(2)**: O primeiro acesso à solução será geralmente mais lento que os seguintes, pois o banco de dados entra em modo hibernação na plataforma Heroku, após algum tempo de inatividade.

No mais, listamos aqui os principais passos para executar nossa solução do início:

1. Utilização de sistema operacional Linux
2. Instalação do banco de dados PostgreSQL
    1. Seguir tutorial: https://www.digitalocean.com/community/tutorials/how-to-use-postgresql-with-your-django-application-on-ubuntu-14-04
    2. Criar banco de dados chamado 'panorama', usuário 'panorama' e senha 'panorama'
3. Instalação do backend Django
    1. O projeto do backend está disponível em: git: gabriel-bandeira/backend-desafio-cnj
    2. Instalar dependências utilizando o comando 'pip install -r requirements.txt'
    3. Executar script MacroSteps.py em: git: lfvvercosa/desafio_cnj para geração dos jsons
    4. Popular o banco de dados com o jsons presentes na pasta Fixtures utilizando o comando 'python manage.py loaddata <nome_do_json>' na seguinte ordem:
        1. base5_comments.json
        2. base5_groups.json
        3. base5_varas.json
        4. base5_steps_config.json
        5. base5_steps.json
    5. Executar o backend com o comando 'python manage.py runserver'
4. Instalação do front-end
    1. Instalar o Node.js
    2. executar Npm install
    3. executar Npm run start
    4. abrir endereço localhost:9000 no browser


## Metodologia do Projeto

Em nosso projeto nós utilizamos a metodologia CRISP-DM (CRoss-Industry Standard Process for Data Mining). Ela é uma metodologia de mineração de dados capaz de transformar os dados da empresa em conhecimento e informações de gerenciamento. CRISP-DM divide o ciclo de vida de um projeto de mineração de dados em seis fases: compreensão do negócio, compreensão de dados, preparação de dados, modelagem, avaliação e implantação. A Figura abaixo ilustra as fases do CRISP-DM. A seguir discutimos brevemente como abordamos cada uma dessas etapas.

<img src='/reports/figures/crisp-dm.png'>

<a id="entendimento_negocio"></a>
## Entendimento do Negócio
A primeira etapa do modelo CRISP-DM é o entendimento do negócio, abaixo descrevemos um briefing do desafio extraído do documento oficial do Hackathon: DESAFIO ENAP - CNJ INOVA Briefing.pdf

**Desafio:** Como podemos, a partir da base do DataJud, identificar padrões e comparar o andamento de processos em cada unidade judiciária do Brasil, levando em consideração as peculiaridades locais e o nível de comlexidade, em razão da competência e da matéria do direito?

**Complemento:** judiciárias, nas diferentes localidades e regiões do Brasil. A consequência direta é a dificuldade em proporcionar transparência, tanto interna quanto externa, necessária aos dados que são produzidos pelas unidades judiciárias, e a impossibilidade de gerenciar soluções para os gargalos, que não conseguem ser devidamente identificados.

Outro material particularmente interessante, disponibilizado pelo Hackathon foi o Estudos CNJ casos e relatos - personas.pdf, do qual pudemos extrair algumas necessidades dos usuários:

Após esse primeiro entendimento do desafio e das necessidades dos usuários, mergulhamos no entendimento do negócio em sí, para tanto conversamos com algumas pessoas atuantes no direito (advogados, servidores), fizemos diversas pesquisas na internet e também utilizamos como referência o relatório: [**Justiça em números 2020**](https://www.cnj.jus.br/pesquisas-judiciarias/justica-em-numeros/) do CNJ, no qual reproduzimos abaixo algumas informações importantes ao projeto.

### O poder judiciário
O Poder Judiciário brasileiro divide-se em cinco ramos: Justiça Estadual, Justiça do Trabalho, Justiça Federal,
Justiça Eleitoral e Justiça Militar. Cada um desses ramos possui órgãos, que são organizados em instâncias. Também fazem parte do Judiciário os tribunais superiores, o Supremo Tribunal Federal e o Conselho Nacional de Justiça, que, como citado, por possuírem seus próprios relatórios e estatísticas e, portanto, não serão abordados neste diagnóstico.

Diante disso, segue sumário explicativo das competências e da estrutura de cada segmento de justiça e dos
quatro tribunais superiores: STJ, STM, TSE e TST.

### justiça Estadual
<img src='/reports/figures/justiça.png'>

<a id="definicao_problema"></a>
### Definição do problema
Analisando os documentos disponibilizados pelo Hackathon: **DESAFIO ENAP - CNJ INOVA Briefing.pdf** e **Estudos CNJ casos e relatos - personas.pdf** pudemos entender melhor o contexto geral do problema e as necessidades dos principais Stakeholders envolvidos. Decidimos restringir o escopo do projeto para atender essencialmente as necessidades identificadas da **persona do JUIZ/DESEMBARGADOR**, que:
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


### Fontes de dados
A principal fonte de dados para o Hackathon foram os dados básicos e movimentações processuais contidos no banco de dados unificado do CNJ, referenciado como DataJud, que será disponibilizado no formato Json, conforme informações apresentadas no [Webinar - dados](https://youtu.be/VBDGxGxgTPw). Adicionalmente identificamos as possíveis fontes de dados:
* **[IBGE - Instituto Brasileiro de Geografia e Estatística](https://www.ibge.gov.br/explica/codigos-dos-municipios.php)** - Para obtenção de informações quanto aos municípios brasileiros.
* **[SGT - Sistema de Gestão das Tabelas Processuais Unificadas](https://www.cnj.jus.br/sgt/consulta_publica_assuntos.php)** - Para obtenção dos "de-para" dos assuntos, classes e movimentos processuais
* **[CNJ - Conselho Nacional de Justiça](https://paineis.cnj.jus.br/QvAJAXZfc/opendoc.htm?document=qvw_l%2FPainelCNJ.qvw&host=QVS%40neodimio03&anonymous=true&sheet=shResumoDespFT)** - Consulta aos paineis da justiça para obtenção de dados referentes a produtividade e demais informações sobre a justiça.

<a id="entendimento_dados"></a>
## Entendimento dos dados
Antes de receber os arquivos de dados (json), fizemos uso dos seguintes documentos (disponibilizados pelo Hackathon) para conhecer e entender a estrutura e conteúdo dos dados.
* **Informacoes Complementares CNJ Inova - Desafios e Dados.pdf**.
* **Glossário-Datajud-Processos** 

Quando do recebimento dos dados e após estudar a estrutura dos arquivos, elaboramos script para extração e normalização dos dados. Elaboramos duas tabelas: a primeira com os dados básicos das Unidades Judiciárias e outra contendo informações detalhadas das movimentações dos processos. Entretanto, notamos que os arquivos abaixo não obedeciam a estrutura de dados definidos pela organização (optamos por não considerar esses dados nesse momento):

>* processos-tjgo_5.json
>* processos-tjgo_6.json
>* processos-tjms_4.json
>* processos-tjrj_10.json
>* processos-tjrj_11.json
>* processos-tjrj_12.json
>* processos-tjrj_5.json
>* processos-tjrj_6.json
>* processos-tjrj_7.json
>* processos-tjrj_8.json
>* processos-tjrj_9.json

<a id="preparacao_dados"></a>
## Preparação dos dados
De posse dos dois arquivos .csv rodamos um fluxo de ETL na ferramenta Pentaho para limpeza, tratamento e enriquecimento dos dados (depara das classes, assuntos e movimentacoes processuais).

<img src='/reports/figures/pentaho.png'>

Abaixo seguem algumas transformações realizadas a partir de algumas ideias (simplificações e criação de features) e necessidades identificadas durante o projeto.

### Filtros
Conforme vimos na sessão [Entendimento do Negócio](#entendimento_negocio),o escopo do projeto foi delimitado quanto a _oportunidades de melhoria de tempos e produtividades_ **nas unidades judiciárias de EXECUÇÃO FISCAL** (<font color=red>pois são as principais responsáveis pela alta taxa de congestionamento do Poder Judiciário</font>, conforme relatório do CNJ [Justiça em Números 2020]( https://www.cnj.jus.br/pesquisas-judiciarias/justica-em-numeros/))
Abaixo outros filtros realizados nos dados ao longo do projeto:  
  * **Filtro nos processos:** Só foram considerados processos:
    *  Movimentação de início (Distribuição) e movimento de término (Baixa ou Arquivamento definitivo) compreendidos entre os anos de 2000 e 2020.
    *  Processos com classe "Execução Fiscal"
    *  Grau 1
    *  Que continham o movimento "Distribuição" e não continham o movimento "Reativação"

### Limpeza dos dados
Foram removidos do log instâncias de processo com dados inconsistentes como datas, campos nulos ou zerados.

### Transformações realizadas

#### Criação de campo (breadscrum) nas tabelas auxiliares do SGT: Classe, Assunto e Movimento
Levando em consideração o [SGT - Sistema de Gestão de Tabelas Processuais Unificadas](https://www.cnj.jus.br/sgt/consulta_publica_classes.php) do CNJ, podemos perceber que os assuntos, classes processuais e movimentos estão organizados em uma hierarquia. Os seguintes mapeamentos de classes filhas em classes pais foram realizadas nesse projeto:

* Movimentos filhos de Decisão foram mapeados para Decisão
* Movimentos filhos de Despacho foram mapeados para Despacho
* Movimentos filhos de Julgamento foram mapeados para Julgamento
* Movimentos de Baixa ou Arquivamento foram mapeados para Baixa/Arquivamento

Essa informação foi importante para a simplificação do modelo, contorno da restrição quanto a capacidade de processamento dos dados (devido ao grande volume) e principalmente para simplificação das tarefas do fluxo (agrupamento de movimentos).

#### Sumarização das variáveis ASSUNTO RAIZ, CLASSE RAIZ
Os dados utilizados para a etapa de clusterização das unidades judiciárias foram as variáveis ASSUNTO e CLASSE processual, encontradas nas estruturas: dadosBasicos.assunto e dadosBasicos.classeProcessual. Nós contabilizamos as ocorrências de cada ASSUNTO e CLASSE processual nas unidade judiciárias.
<img src='/reports/figures/grupo_assunto.png'>
Para depois serem transformados em coluna (aumento das dimensões)
<img src='/reports/figures/analise_criterios.png'> <br>


## Modelagem

<a id="modelagem_solucao"></a>
### Modelagem da Solução
Conforme descrito na sessão [Definição do Problema](#definicao_problema), a solução basicamente atenderá as necessidades da **persona do JUIZ/DESEMBARGADOR**, formalizada no problema abaixo:

>**PROBLEMA:** Os Juizes e Desembargadores não possuem uma ferramenta que possa auxiliá-los a incrementar sua produtividade, identificando onde estão os problemas de sua unidade e sugerindo ações para corrigi-los ou minimizá-los. 

A ideia geral é fornecer uma plataforma onde o Juiz / Desembargador possa consultar a produtividade, identificar os problemas de sua unidade judiciária, bem como obter insigths sobre como incrementar sua produtividade através da comparação e troca de experiência com outras unidades judiciárias semelhantes a sua.

#### Arquitetura geral
<img src='/reports/figures/Solucao_geral.png'>

#### Solução: Painel de Tempos e Produtividade
Com esta interface o Juiz / Desembargador poderá acompanhar o desempenho da sua unidade judiciária em relação a outras unidades judiciárias semelhantes, em relação as dimensões: tempo e produtividade.

<img src='/reports/figures/solucao_1.png'>
<img src='/reports/figures/solucao_2.png'>

A seguir, descrição dos principais componentes desta solução enumerados nas figuras acima.

* **Posição Geral**
    * Colocação geral de sua unidade judicial em relação ao seu grupo. Essa colocação é medida como o tempo médio em dias que os processos da unidade judicial demoram para serem baixados ou arquivados.
* **Grupo da Unidade Judiciária**
    * O grupo da unidade judicial é calculado utilizando algoritmos inteligentes de clusterização. Nossa clusterização em particular, leva em conta a frequência dos Assuntos e Classes processuais dos processos julgados em cada unidade judicial. Foram selecionadas uma vara de cada grupo para exemplificação.
* **Identificação dos gargalos**
    * Maiores gargalos, em dias, da unidade judicial. Os gargalos se referem às macroetapas do processo mapeadas no tópico Transformações Realizadas.
* **Pontos de destaque**
    * Menores gargalos, em dias, da unidade judicial. Ou seja, as etapas em que a unidade judicial é mais eficiente.
* **Feedbacks / Insights**
    * Contém ranking das varas do mesmo grupo da unidade judicial, com relação aos Pontos de destaque e gargalos. Exemplo: Se o maior gargalo da unidade judicial em questão é "Julgamento" -> "Baixa Definitiva", então o ranking conterá as melhores unidades judiciais na transição "Julgamento" -> "Baixa Definitiva". Além disso, o ranking também contém comentários dos juízes das outras varas compartilhando estratégias e insights sobre a eficiência de sua unidade judicial na transição.
* **Estatísticas desempenho**
    * Destacam o pior e menor gargalo da unidade judicial referente às macroetapas.
* **Estatísticas do fluxo**
    * Destacam a duração média da baixa do processo em dias, movimentação média do processo e total de processos julgados
* **Média dos tempos processuais**
    * Exibem o tempo médio dos processos em cada macroetapa. São exibidas as top cinco unidades judiciais por tempo médio de duração de processo, a unidade judicial analisada e seus vizinhos imediatos acima e abaixo. Uma observação importante é que o tempo total exibido não reflete necessariamente o tempo médio de duração do processo, visto que nem todas as instâncias de processo passam pelas mesmas macroetapas.
* **Localização Unidades Semelhantes**
    * Exibe as top cinco unidades judiciais por tempo médio de duração de processo, a unidade judicial analisada e seus vizinhos imediatos acima e abaixo. Além disso, destaca a localização dessas unidades judiciais no mapa do Brasil.
* **Meu processo**
    * (Não implementado) Exibe o fluxo dos macroprocessos da unidade judicial em formato de grafo. O peso das arestas representa a frequência das transições ou o tempo em dias.
* **Melhor processo do meu grupo**
    * (Não implementado) Exibe o fluxo dos macroprocessos da unidade judicial de melhor colocação. A ideia é que o juiz possa comparar o seu processo visualmente com o da melhor vara de seu grupo.
* **Sugestões de melhoria**
    * Sugestões de melhorias no processo como um todo fornecidas pelo juiz da vara comparada.
* **Ranking das unidades judiciárias**
    * Exibe as top cinco unidades judiciais por tempo médio de duração de processo, a unidade judicial analisada e seus vizinhos imediatos acima e abaixo.

**OBS**: É possível alternar para uma vara de outro grupo clicando na medalha localizada no canto superior esquerdo.

## Entrada produção
Optamos por utiliza o Heroku (plataforma em nuvem como um serviço que suporta várias linguagens de programação) para disponibilizar nossa aplicação.

>**Acesso a solução:** http://desafio-cnj-frontend.herokuapp.com/

>**Apresentação da solução:** 

## Próximos passos

>**Solução: Configuração dos critérios -**
Com essa ferramenta o Pesquisador do CNJ poderá criar, testar e configurar novos critérios de agrupamento, analisando o impacto da combinação de parâmetros de filtragem, agrupamento e clusterização no resultado dos grupos criados. Permitindo que estudos sejam realizados no sentido de aprimorar os critérios de comparação entre unidades judiciárias semelhantes.

>**Solução: Configuração dos critérios -**
Com a análise do TRACE (sequencia de atividades) dos processos da unidade judiciária, temos condições de predizer o tempo esperado que um determinado processo a partir de sua tarefa atual, chegue a uma determinada tarefa (normalmente a tarefa de término do processo, que pode ser JULGAMENTO, TRANSITO EM JULGADO, BAIXA / ARQUIVAMENTO DEFINITIVO ou qualquer outra tarefa desejada). Com base nessa infomação é possível:
>* Exibir nas telas do PJE (por exemplo: autos do processo), o tempo esperado para conclusão do processo.
>* Exibir mensagem de alertas que notifiquem ao usuário interno do PJE (servidores e magistrados) quando um determinado processo estiver perto de atrasar ou já tiver atrasado.



