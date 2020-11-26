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
* **Comparar com base na situação atual:** Como levantado na sessão do [entendimento dos dados](README_METODOLOGIA.md#entendimento_dados), existe uma base de dados do CNJ onde aproximadamente [638 variáveis](https://www.cnj.jus.br/pesquisas-judiciarias/justica-em-numeros/documentos-justica-em-numeros/) relacionadas aos tribunais são catalogadas e disponibilizadas para consulta. Dessa base de dados identificamos algumas variáveis candidatas: Estoque, Casos novos e casos pendentes, que poderiam ser utilizadas como referência a situação atual da UNIDADE JUDICIÁRIA. <p>
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

Abaixo segue imagem da configuração realizada na primeira etapa <br>
<img src='/reports/figures/etapa1.png'> <br>

**2ª Etapa: Agrupamento** <br>
    Esta etapa refere-se ao primeiro nível de agrupamento realizado para construção dos critérios. Na fase anterior, restringimos as unidades judiciárias que fariam parte do critério, já nesta etapa, podemos ou não informar como as unidades judiciárias serão agrupadas segundo variáveis categóricas (não numéricas), tais como **Justiça** e **Grau**. Ao final desta etapa já teríamos as unidades agrupadas. Contudo, como iremos observar na próxima etapa, o agrupamento das unidades judiciárias apenas por Justiça Estadual e 1º grau (por exemplo) muito provavelmente não será um critério de agrupamento justo para as unidades, por não considerar a **MATÉRIA** e **COMPETENCIA** das unidades. Neste sentido, podemos utilizar a 3ª etapa para criar o segundo nível de agrupamento dentro do nível criado nesta etapa (Justiça Estadual + 1º grau).

Abaixo segue imagem da configuração realizada na segunda etapa <br>
<img src='/reports/figures/Etapa2.png'><br>
    
**3ª Etapa: Clusterização** <br>
    Clusterizar é o termo utilizado para criar grupos de objetos semelhantes a partir de variáveis numéricas. 
> Para a clusterização (3º etapa) utilizamos a técnica estatística de análise multivariada denominada análise de componentes principais. A partir da sua aplicação, passa a ser possível reduzir o número de dimensõe em análise (quantidade de variáveis escolhidas na 3ª etapa) de modo que um número pequeno de componentes (digamos, 1, 2 ou até 3, a depender da quantidade de variáveis em análise) consegue explicar uma proporção satisfatória da variância populacional, ou seja, cerca de 80% a 90% dos dados. 

Abaixo segue imagem da configuração realizada na terceira etapa <br>
<img src='/reports/figures/Etapa3.png'><br>

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
A escolha da variável ASSUNTO RAIZ combinada com CLASSE RAÍZ, mostrou-se interessante pois de forma simplificada, endereça a questão de comparar MATÉRIA e de certa forma COMPETÊNCIA (uma vez que a competência normalmente é definida pela composição da CLASSE PROCESSUAL e ASSUNTO), dessa forma o _primeiro direcionamento_ **"Comparar com base na competência"** seria atendido.<br>
    
> Para endereçar o _segundo direcionamento_ **"Comparar com base na situação atual"** (também de forma indireta), fizemos uma transformação na variável ASSUNTO RAIZ e CLASSE PROCESSUAL RAIZ, contabilizando as ocorrências em cada unidade judiciária
    Para depois serem transformados em coluna (aumento das dimensões)
    <img src='/reports/figures/analise_criterios.png'> <br>

> Logo em seguinda a etapa de Escalar / Padronizar os dados foi executada e o algoritmo de clusterização DBSCan foi utilizado para obter os grupos de cada unidade judiciária.
A análise consistiu basicamente em realizar várias combinações de filtro, agrupamento e parametrizações do modelo DBSCAN e identificar os outliers (unidades judiciárias que não conseguiram ser classificadas satisfatoriamente pelo algoritmo) e características de cada grupo gerado para identificar inconsistências gritantes.
<img src='/reports/figures/Analise.png'><br>
Após gerar várias combinações de critérios, passamos a fazer uma análise statística dos critérios gerados, levando em consideração, entre outros:
* Quantidade de grupos formados
* Quantidade de Outliers encontrados
* Percentual de clusterização das unidades judiciárias
* Percentual de Outliers em relação ao total de unidades judiciárias utilizadas
* Distribuição das unidades judiciárias nos grupos
<img src='/reports/figures/comparacao.png'><br><br>

<img src='/reports/figures/dbscan.png'><br><br>
    
O terceiro direcionamento **"Comparar com base nos recursos disponíveis"** devera ser implementado na segunda etapa do Hackathon.
