<div align="center"><img img src='/reports/figures/logo.png' width="200"></div> 

<h1 align=center>Projeto: Hackathon CNJ Inova</h1>

### Desafio 1 -  Tempos e produtividade
Como podemos, a partir da base do DataJud, identificar padrões e comparar o andamento de processos em cada unidade judiciária do Brasil, levando em consideração as peculiaridades locais e o nível de complexidade, em razão da competência e da matéria do direito?
#### Problema a ser solucionado
>O CNJ não possui uma ferramenta que possa auxiliá-los a identificar os problemas de desempenho das Unidades Judiciárias semelhantes. Na mesma medida, os Juizes e Desembargadores também não possuem uma ferramenta que possa auxiliá-los a incrementar sua produtividade, identificando onde estão os problemas de sua unidade e sugerindo ações para corrigi-los ou minimizá-los. <br>
>Obs.: [Saiba mais sobre o processo utilizado para definição e formalização do problema](README_PROBLEMA.md)

#### Nossa solução e os resultados gerados
Nossa solução é capaz de identificar e solucionar os gargalos de tramitações processuais de [unidades judiciárias similares](README_CLUSTERIZACAO.md), considerando a colaboração, o alerta de desempenho e a geração de informação para tomada de decisão.

<img src='/reports/figures/funcionalidades.png'>

* [Saiba como usar a solução PANORAMA.](#uso)
* [Saiba mais sobre como identificamos as unidades judiciárias similares](README_CLUSTERIZACAO.md)
* [Conheça a estrutura do projeto e como realizar a instalação.](README_PROJETO.md)
* [Consulte o detalhe da metodologia utilizada no trabalho.](README_METODOLOGIA.md)

#### Principais métricas do modelo
O algoritmo utilizado para encontrar os clusters foi o [DBSCAN](https://en.wikipedia.org/wiki/DBSCAN) e a métrica utilizada para calcular a disntância entre os pontos dos clusters foi a [DISTÂNCIA EUCLIDEANA](https://en.wikipedia.org/wiki/Euclidean_distance).<br>
Para comparar o resultado dos critérios gerados pela combinação de filtros, critérios de agrupamento e parâmetros do algoritmo DBSCAN, utilizamos as seguintes métricas / abordagens:
  * Para cada critério avaliado, calculamos:
      * O percentual de outliers identificados levando em consideração a quantidade de unidades judiciárias utilizadas no critério, **fórmula:** (qtd. unidades no grupo de outliers / qtd. unidades utilizadas no critério)
      * O percentual de clusterização das unidades judiciárias utilizadas no critério, **fórmula:** (qtd. unidades com grupo / qtd. unidades utilizadas no critério).
  * Submetemos cada grupo de clusters a avaliação de um servidor do judiciário (membro da equipe), para avaliar a qualidade do cluster, e calculamos a partir dessa análise:
      * Quantidade de ajustes (unidades judiciárias claramente com grupo equivocado).
  
* [Saiba mais sobre como identificamos as unidades judiciárias similares](README_CLUSTERIZACAO.md)

#### Arquitetura do sistema
<img src='/reports/figures/Solucao_geral.png'>

#### Fluxo de dados
A principal fonte de dados da solução PANORAMA são os dados básicos e movimentações processuais contidos no banco de dados unificado do CNJ, referenciado como DataJud. Após acessar os dados do DataJud, se seguintes macro-operações são realizadas nos dados:
1. Extração e normalização dos dados do formato JSON para estruturas de dados.
2. Obtenção de dados auxiliares: [SGT - Sistema de Gestão das Tabelas Processuais Unificadas](https://www.cnj.jus.br/sgt/consulta_publica_assuntos.php) - Para obtenção dos "de-para" dos assuntos, classes e movimentos processuais.
3. Execução de rotina ETL na ferramenta Pentaho para limpeza, tratamento e enriquecimento dos dados (depara das classes, assuntos e movimentacoes processuais).
 
<img src='/reports/figures/pentaho.png'>

* [Consulte informações detalhadas sobre o fluxo de dados.](README_FLUXODADOS.md)

<a id="uso"></a>
#### Instruções de Uso
Vídeo de demonstração do PANORAMA <br>
[![Video de demonstração do PANORAMA](http://img.youtube.com/vi/PR7vPh5alOY/0.jpg)](https://www.youtube.com/watch?v=PR7vPh5alOY "Panorama")
* [Consulte nosso MANUAL para mais informações sobre o uso da ferramenta PANORAMA.](README_MANUAL.md)

#### Licenças utilizadas
Os scripts foram escritos em python, prezamos por utilizar bibliotecas GRATUÍTAS e CONSOLIDADAS no mercado para prover a qualidade necessária para execução do projeto.

> Obs.: Utilizamos a versão freeware da ferramenta Pentaho Integrator para gerar a ETL de limpeza e enriquecimento dos dados.

#### Áreas de conhecimento e técnicas envolvidas
Abaixo relacionamos as áreas de conhecimento e técnicas utilizadas para desenvolvimento da solução PANORAMA:
  * Inteligência Artificial
    *  Técnicas de Clusterização
       *  Algoritmo utilizado: DBSCAN
  
  * Mineração de Processos
    * Técnicas de descoberta de processos
       * Algoritmo utilizado: Inductive miner




