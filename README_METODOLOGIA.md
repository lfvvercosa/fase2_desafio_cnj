# Metodologia do Projeto

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

Após o feedback obtidos na segunda etapa do desafio, foi adicionada a persona do CNJ, de modo a incluir na ferramenta uma visão macro dos problemas de desempenho das várias unidades judiciárias do Brasil, e não somente o painel da unidade judiciária de um Juíz / Desembargador específico.

Nesse sentido, formalizamos o problema como:

>**PROBLEMA:**
O CNJ não possui uma ferramenta que possa auxiliá-los a identificar os problemas de desempenho das Unidades Judiciárias semelhantes. Na mesma medida, os Juizes e Desembargadores também não possuem uma ferramenta que possa auxiliá-los a incrementar sua produtividade, identificando onde estão os problemas de sua unidade e sugerindo ações para corrigi-los ou minimizá-los. 

Através da formalização do problema, pudemos identificar vários sub-problemas (desafios) que deveriam ser endereçados para que o problema pudesse ser resolvido.
* Identificar indicadores de produtividade relevantes
* Definir uma forma de simplificar e comparar os processos de unidades distintas
* Definir um critério de agrupamento de unidades judiciárias semelhantes levando em consideração as competências, situação atual e os recursos disponíveis da unidade judiciária


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

>**PROBLEMA:**
O CNJ não possui uma ferramenta que possa auxiliá-los a identificar os problemas de desempenho das Unidades Judiciárias semelhantes. Na mesma medida, os Juizes e Desembargadores também não possuem uma ferramenta que possa auxiliá-los a incrementar sua produtividade, identificando onde estão os problemas de sua unidade e sugerindo ações para corrigi-los ou minimizá-los. 

A ideia geral é fornecer uma plataforma onde o Pesquisador do CNJ possa identificar as unidades judiciárias com baixo desempenho e o Juiz / Desembargador possa consultar a produtividade, identificar os problemas de sua unidade judiciária, bem como obter insigths sobre como incrementar sua produtividade através da comparação e troca de experiência com outras unidades judiciárias semelhantes a sua.

#### Arquitetura geral
<img src='/reports/figures/Solucao_geral.png'>

### Simplificação dos movimentos: CRIAÇÃO DA FEATURE MACRO-ETAPAS
Para a feature de identificação e comparação de gargalos entre as unidades judiciárias, fizemos uma simplificação nos fluxos processuais, criado o conceito de Macro-Etapas (Marcos), segundo a seguinte condificação (que será configurável pelo usuário):
>**Macro-Etapas (Marcos):**
>* DISTRIBUIÇÃO
>   * Código de movimento = 26
> * CONCLUSÃO
>   * Código de movimento = 51 - conclusão
> * CITAÇÃO
>   * Breadscrum = 14:48:1228 (qualquer movimento com essa hierarquia)
> * APRECIAÇÃO DE TUTELA DE URGENCIA OU MEDIDA LIMINAR
>   * Código de movimento = 332 - concessao -> antecipacao de tutela
>   * Código de movimento = 785 - nao-concessao -> antecipação de tutela
>   * Código de movimento = 889 - concessao em parte -> antecipaçao de tutela
> * DESPACHO
>   * Breadscrum = 1:11009 (qualquer movimento com essa hierarquia)
> * DECISÃO
>   * Breadscrum = 1:3 (qualquer movimento com essa hierarquia)
> * AUDIÊNCIA
>   * Breadscrum = 14:48:970 (qualquer movimento com essa hierarquia)
> * JULGAMENTO/SENTENÇA
>   * Breadscrum = 1:193 (qualquer movimento com essa hierarquia)
> * TRÂNSITO EM JULGADO
>   * Código de movimento = 848
> * BAIXA / ARQUIVAMENTO
>   * Código de movimento = 22 - baixa
>   * Código de movimento = 246 - arquivamento definitivo

### Modelagem do Critério de Agrupamento das Unidades Judiciárias

Antes de propor possíveis critérios de agrupamento, faz-se necessário revisitar o documento das personas, do qual extraímos o trecho abaixo com alguns insigths sobre o possível critério de agrupamento das unidades judiciárias semelhantes.
> "...Gostaria de entender onde estão os problemas da sua unidade
judiciária para poder consertá-los e <font color=red> incrementar sua produtividade</font>.
Antônio fica muito irritado quando comparam sua unidade judiciária
com outras que desempenham funções diferentes. _Gostaria que
sua produtividade fosse comparada com seus semelhantes_ , levando em
consideração as <font color=red>competências</font>, a <font color=red>situação atual</font> e os <font color=red>recursos disponíveis</font>..." **RELATO 1 - JUIZ / DESEMBARGADOR.**

Com base nas informações extraídas no texto acima, podemos perceber 3 macro direcionamentos para os critérios: competência, situação atual e recursos disponíveis. Abaixo elencamos como endereçamos cada questão referente a cada tópico. 
* **Comparar com base na competência** = Poderíamos utilizar o campo: dadosBasicos.competencia, disponibilizado no json, contudo, percebemos conforme relatado na sessão de [entendimento dos dados](#entendimento_dados), que a variedade e inexistência de um depara relacionado as competências inviabilizaria a utilização desse campo para tal finalidade. No entanto, através de consultas a especialistas do direito, identificamos que as competências são configuradas por cada Tribunal, normalmente com base na associação das informações de **classe processual** e **assunto**, campos disponíveis no json do DataJud.<p>
* **Comparar com base na situação atual:** Como levantado na sessão do [entendimento dos dados](#entendimento_dados), existe uma base de dados do CNJ onde aproximadamente [638 variáveis](https://www.cnj.jus.br/pesquisas-judiciarias/justica-em-numeros/documentos-justica-em-numeros/) relacionadas aos tribunais são catalogadas e disponibilizadas para consulta. Dessa base de dados identificamos algumas variáveis candidatas: Estoque, Casos novos e casos pendentes, que poderiam ser utilizadas como referência a situação atual da UNIDADE JUDICIÁRIA. <p>
* **Comparar com base nos recursos disponíveis:** Com relação aos recursos disponíveis, também podemos utilizar as variáveis: força de trabalho de servidores e magistrados, uma das [638 variáveis](https://www.cnj.jus.br/pesquisas-judiciarias/justica-em-numeros/documentos-justica-em-numeros/) disponibilizadas pelo CNJ que poderiam ser utilizadas como referência aos recursos disponíveis da UNIDADE JUDICIÁRIA 
    
> **OBSERVAÇÃO:** Um ponto de atenção é que o código das unidades judiciárias das variáveis citadas do CNJ não correspondem aos códigos das unidades do arquivo json, nesse sentido deve-se verificar a possibilidade de cruzar as informações através do nome das unidades judiciárias.

Disponibilizar uma ferramenta que permita ao usuário interno (**Equipe de pesquisa do CNJ**) <font color=red>criar e testar novos critérios de agrupamento de unidades judiciárias</font>, faz parte do escopo de entregas da nossa solução. Com essa ferramenta será possível analisar o impacto de diversas configurações sobre possíveis agrupamentos, que poderão ser salvos e carregados para futura análise.    

A criação, análise e teste de novos possíveis cenários passa por 3 etapas: FILTRO, AGRUPAMENTO e CLUSTERIZAÇÃO (agrupamento através de variáveis numéricas). Ao menos uma das três fases deve ser configurada.
    
A arquitetura básica do processo de crição de novos critérios de agrupamento está demonstrada na imagem abaixo:
<img src='/reports/figures/arquitetura_criterio.png'>

**1ª Etapa: Filtro** <br>
    Nesta etapa podemos definir o escopo inicial do critério, segundo as variáveis de **Justiça**, **Grau**, **Assunto Raiz** e **Classe processual Raiz** em qualquer combinação. Podemos definir diversas combinações de critérios, como por  exemplo:

> **Somente uma Justiça (sem grau):** Filtrar somente as unidades da Justiça Estadual sem levar em consideração o grau
    
> **Duas ou mais Justiças (com grau):** Filtrar a Justiça Estadual e Federal, do 1º e 2º graus.
    
> **Assunto Raiz:** Filtrar na Justiça Estadual, os assuntos: "899 - Direito Civil" e "1156 - Direito do Consumidor"

> **Classe processual Raiz:** Filtrar na Justiça Federal, as classes "2:1106 - Processo de Conhecimento"

**2ª Etapa: Agrupamento** <br>
    Esta etapa refere-se ao primeiro nível de agrupamento realizado para construção dos critérios. Na fase anterior, restringimos as unidades judiciárias que fariam parte do critério, já nesta etapa, podemos ou não informar como as unidades judiciárias serão agrupadas segundo variáveis categóricas (não numéricas), tais como **Justiça** e **Grau**. Ao final desta etapa já teríamos as unidades agrupadas. Contudo, como iremos observar na próxima etapa, o agrupamento das unidades judiciárias apenas por Justiça Estadual e 1º grau (por exemplo) muito provavelmente não será um critério de agrupamento justo para as unidades, por não considerar a **MATÉRIA** e **COMPETENCIA** das unidades. Neste sentido, podemos utilizar a 3ª etapa para criar o segundo nível de agrupamento dentro do nível criado nesta etapa (Justiça Estadual + 1º grau).
    
**3ª Etapa: Clusterização** <br>
    Clusterizar é o termo utilizado para criar grupos de objetos semelhantes a partir de variáveis numéricas. 
> Para a clusterização (3º etapa) utilizamos a técnica estatística de análise multivariada denominada análise de componentes principais. A partir da sua aplicação, passa a ser possível reduzir o número de dimensõe em análise (quantidade de variáveis escolhidas na 3ª etapa) de modo que um número pequeno de componentes (digamos, 1, 2 ou até 3, a depender da quantidade de variáveis em análise) consegue explicar uma proporção satisfatória da variância populacional, ou seja, cerca de 80% a 90% dos dados. 
* **Análise de Componentes Principais (ACP)**<br>
Trata-se de método de análise multivariada, utilizada para resumir grande número de variáveis em poucas dimensões. É uma tentativa de compreender relações complexas impossíveis de serem trabalhadas com métodos univariados ou bivariados, permitindo, assim, visualizações gráficas e análises mais aprofundadas por parte do pesquisador. _Fonte: [Justiça em Números 2020]( https://www.cnj.jus.br/pesquisas-judiciarias/justica-em-numeros/))_

Considerando que as variáveis utilizadas possuem escalas distintas e para que todas pudessem ter o mesmo peso de influência no modelo, faz-se necessário uma etapa de "Escala / normalização" das variáveis, que se resume à substituição da matriz de covariância pela de correlação.
    Dentre as variáveis numéricas que podemos combinar e utilizar nesta etapa, podemos citar: Assunto (Raiz ou não), Classe processual (Raiz ou não), e qualquer combinação das [638 variáveis](https://www.cnj.jus.br/pesquisas-judiciarias/justica-em-numeros/documentos-justica-em-numeros/) disponibilizadas pelo CNJ.

>Faz-se necessário a definição do termo RAIZ (utilizado tanto para assunto, como para Classe processual). Levando em consideração o SGT (Sistema de Gestão de Tabelas Processuais Unificadas)  do CNJ (disponível em https://www.cnj.jus.br/sgt/consulta_publica_classes.php), podemos perceber que os assuntos, classes processuais e movimentos estão organizados em uma hierarquia. Definimos como RAIZ, o item (assunto, classe ou movimento) no primeiro nível da hierarquia a qual pertence o item em questão. 

> Tomemos como exemplo o assunto: 7619 - Consórcio, que possui a seguinte hierarquia:<br>
> * 1156 - Direito do consumidor
>   * 7771 - Contratos de consumo
>     * 7619 - Consórcio <br>
> Teríamos como Assunto Raiz o "1156 - Direito do consumidor".

#### DEFINIÇÃO DO CRITÉRIO DE AGRUPAMENTO DAS UNIDADES JUDICIÁRIAS SEMELHANTES
O agrupamento das unidades judiciárias tem por objetivo criar parâmetros de comparação de forma a respeitar as características distintas existentes de cada unidade judiciária, bem como suas semelhanças, considerando o ramo de justiça, grau, matéria, competência, situação atual e recursos disponíveis.
    
Devido a restrições de tempo (entrega da primeira versão funcional - Primeira etapa do hackathon) e capacidade computacional (devido ao grande volume de dados), optamos por restringir o máximo possível os critérios de agrupamento, de modo que a solução pudesse ser demonstrada (factível) e ao mesmo tempo insigths importantes pudessem ser extraídos. 
    
Desta forma, a definição simplificada do critério que veremos a seguir, tem como objetivo apenas demonstrar a capacidade e viabilidade da ferramenta e não de exaurir e aprofundar a combinação de parâmetros, de modo a extrair o melhor agrupamento das unidades judiciárias. Trata-se portanto, de uma PROVA DE CONCEITO da capacidade da ferramenta em questão. 

As configurações SIMPLIFICADAS utilizadas em cada etapa foram:
> **1ª Etapa: Filtro -** No âmbito da JUSTIÇA ESTADUAL.<br>
> **2ª Etapa: Agrupamento -** No âmbito do 1º GRAU <br>
<img src='/reports/figures/fiscal_fazenda.png'>
    
> **3ª Etapa: Clusterização -** Variável ASSUNTO RAIZ. 
A escolha da variável ASSUNTO RAIZ, mostrou-se interessante pois de forma simplificada, endereça a questão de comparar MATÉRIA e de certa forma COMPETÊNCIA (uma vez que a competência normalmente é definida pela composição da CLASSE PROCESSUAL e ASSUNTO), dessa forma o _primeiro direcionamento_ **"Comparar com base na competência"** seria atendido.<br>
    
> Para endereçar o _segundo direcionamento_ **"Comparar com base na situação atual"** (também de forma indireta), fizemos uma transformação na variável ASSUNTO RAIZ, contabilizando as ocorrências em cada unidade judiciária
    <img src='/reports/figures/grupo_assunto.png'>
    Para depois serem transformados em coluna (aumento das dimensões)
    <img src='/reports/figures/analise_criterios.png'> <br>

> Logo em seguinda a etapa de Escalar / Padronizar os dados foi executada e o algoritmo de clusterização DBSCan foi utilizado para obter os grupos de cada unidade judiciária.
<img src='/reports/figures/dbscan.png'><br><br>
    
O terceiro direcionamento **"Comparar com base nos recursos disponíveis"** devera ser implementado na segunda etapa do Hackathon.

## Avaliação
Uma parte importante da metodologia CRISP-DM é a validação do modelo gerado com os usuários especialistas para que o mesmo possa ser melhorado. Durante esta fase, é comum, voltarmos para qualquer fase da metodologia, não somente para a fase de ENTENDIMENTO DO NEGÓCIO como a imagem do CRISP-DM demonstra, uma vez que sua representação é meramente didática.

### Feedback dos especialistas
Para facilitar a avaliação dos resultados gerados pelos diversos modelos gerados, foi desenvolvida (ainda em draft) uma interface interna para que o usuário possa justamente com o Cientista de Dados, visualizar graficamente os grupos criados (diagrama de dispersão), bem como os dados que o compõe: Unidade Judiciária, Justiça, Grau, e as variáveis utilizadas para clusterização. 

<img src='/reports/figures/analise_cluster.png'>

> Com opções previstas de escolher o critério e filtrar os clusters
<img src='/reports/figures/filtro_cluster.png'>

### Redefinição / Otimização do modelo
Conforme o feedback ou insigth do Especialista e do Cientista de Dados, pode ser necessário a redefinição de novos FILTROS, AGRUPAMENTOS ou ainda ESCOLHA DE NOVAS VARIÁVEIS DE CLUSTERIZAÇÃO. Não raro a depender do resultado:
> Uma nova fonte de dados pode ser necessária para enriquecer os dados e por consequencia talvez melhorar o resultado da clusterização.

> Uma melhoria ou ajuste na etapa de pré-processamento (limpeza, agregação) dos dados seja necessária. 

> A escolha de outro algoritmo de clusterização mais eficiente e aderente as características dos dados.

> Ou em algumas situações, será neessário apenas uma otimização no parâmetro do algoritimo de clusterização

Especificamente para o nosso caso, ajustamos os parâmetros eps e num_sample do algoritmo utilizado: DBScan.
<img src='/reports/figures/otimizar_dbscan.png'>


## Entrada produção
Optamos por utiliza o Heroku (plataforma em nuvem como um serviço que suporta várias linguagens de programação) para disponibilizar nossa aplicação.

>**Acesso a solução:**     http://panorama-fase2.herokuapp.com

>**Apresentação da solução:**  

## Próximos passos

>**Solução: Configuração dos critérios -**
Com essa ferramenta o Pesquisador do CNJ poderá criar, testar e configurar novos critérios de agrupamento, analisando o impacto da combinação de parâmetros de filtragem, agrupamento e clusterização no resultado dos grupos criados. Permitindo que estudos sejam realizados no sentido de aprimorar os critérios de comparação entre unidades judiciárias semelhantes.

>**Solução: Configuração dos critérios -**
Com a análise do TRACE (sequencia de atividades) dos processos da unidade judiciária, temos condições de predizer o tempo esperado que um determinado processo a partir de sua tarefa atual, chegue a uma determinada tarefa (normalmente a tarefa de término do processo, que pode ser JULGAMENTO, TRANSITO EM JULGADO, BAIXA / ARQUIVAMENTO DEFINITIVO ou qualquer outra tarefa desejada). Com base nessa infomação é possível:
>* Exibir nas telas do PJE (por exemplo: autos do processo), o tempo esperado para conclusão do processo.
>* Exibir mensagem de alertas que notifiquem ao usuário interno do PJE (servidores e magistrados) quando um determinado processo estiver perto de atrasar ou já tiver atrasado.

