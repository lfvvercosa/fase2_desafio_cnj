<a id="menu"></a>
## Instruções de Uso.
Abaixo segue um sumário com os principais tópicos para utilização da ferramenta.<br>
  1. **Introdução a solução**<br>
     1.1 **[Conheça a solução PANORAMA](#introducao)** - Principais características da solução PANORAMA.<br>
     1.2 **[Macro-Etapas](#macro-etapas)** - Simplificação dos movimentos para comparação de desempenhos.<br>
  2. **[Solução: Tempo e produtividade](#tempo-produtividade)** - Principal módulo do PANORAMA.<br>
     2.1 **[Login](#login)** - Como acessar a solução PANORAMA<br>
     2.2 **[Visão geral das unidades judiciárias](#cnj)** - Uso da ferramenta na perspectiva do usuário PESQUISADOR CNJ.   <br>
          2.2.1 **[Exibindo todos os alertas](#alertas)** - Como identificar todos os alertas gerados pela solução?<br>
          2.2.2 **[Escolhendo outros grupos](#grupos)** - Como verificar a situação de outros grupos?<br>
          2.2.3 **[Identificando os problemas](#baixo-desempenho)** - Como identificar as unidades judiciárias com problemas?<br>
          2.2.4 **[Interagindo com as unidades](#notificar)** - Como entrar em contato com as unidades para realizar notificações?<br>
          2.2.5 **[Localizando as unidades](#localizar)** - Onde estao localizadas as unidades judiciárias desse grupo?<br>
     2.3 **[Visão da unidade judiciária](#juiz)** - Uso da ferramenta na perspectiva do usuário JUÍZ / DESEMBARGADOR ou do PESQUISADOR CNJ (drill-down da visão geral).<br>
  3. **[Solução: Configuração dos critérios](#config)** - Módulo de apoio responsável pelo gerenciamento dos critérios de clusterização.<br>

<a id="introducao"></a>
#### 1.1 Conheça a solução PANORAMA
As imagens abaixo descrevem de forma suscinta as principais características da solução PANORAMA, suas macro-funcionalidades e macro-etapas.
<img src='/reports/figures/funcionalidades.png'>

Uma vez vencido o desafio de agrupar as unidades judiciárias semelhantes (conforme competência, situação atual e recursos disponíveis das unidades), faz-se necessário encontrar uma forma simples e assertiva de comparar os diversos padrões de execução dos processos nas unidades judiciárias pertencentes a cada grupo clusterizado. Nesse sentido, resolvemos agrupar as diversas movimentações existentes em macro-etapas que façam sentido no domínio de negócio das unidades judiciárias. <br>
<br>[Voltar para o menu](#menu)

<a id="macro-etapas"></a>
### 1.2 Simplificação dos movimentos: CRIAÇÃO DA FEATURE MACRO-ETAPAS
Para a feature de identificação e comparação de gargalos entre as unidades judiciárias, fizemos uma simplificação nos fluxos processuais, criado o conceito de Macro-Etapas (Marcos), segundo a seguinte condificação (que será configurável pelo usuário):
>Desta forma, criamos as seguintes macro-etapas: <br>
>**Macro-Etapas (Marcos):**
>* **DISTRIBUIÇÃO**<br>
> **Descrição:** Momento em que o processo foi atribuído a determinado Juízo, após os procedimentos de protocolo, de cadastramento, de autuação e de distribuição.<br>
> **Simplificação realizada:** Código de movimento = 26 - Distribuição
> * **CONCLUSÃO**<br>
> **Descrição:** Entrega ou remessa de um processo ao juiz, para que esse lavre nele despacho ou sentença.<br>
> **Simplificação realizada:** Código de movimento = 51 - conclusão
> * **CITAÇÃO**<br>
> **Descrição:** Ato processual no qual a parte ré é comunicada de que se lhe está sendo movido um processo e a partir da qual a relação triangular deste se fecha, com os três sujeitos envolvidos no litígio devidamente ligados: autor, réu e juiz — ou interessados e juiz.<br>
> **Simplificação realizada:** Breadscrum = 14:48:1228 (qualquer movimento com essa hierarquia)
> * **APRECIAÇÃO DE TUTELA DE URGENCIA OU MEDIDA LIMINAR**<br>
> **Descrição:** É uma ordem judicial provisória no início do litígio, da lide, da disputa.<br>
> **Simplificação realizada:**
>   * Código de movimento = 332 - concessao -> antecipacao de tutela
>   * Código de movimento = 785 - nao-concessao -> antecipação de tutela
>   * Código de movimento = 889 - concessao em parte -> antecipaçao de tutela
> * **DESPACHO**<br>
> **Descrição:** Ato do magistrado que não seja sentença, tampouco decisão interlocutória, praticado no processo, em virtude de ofício ou requerimento das partes. Essa providência constitui ato de ordenação (organização, arrumação, disposição) do processo, sobre o qual não incide decisão, tampouco matéria para recurso.<br>
> **Simplificação realizada:** Breadscrum = 1:11009 (qualquer movimento com essa hierarquia)
> * **DECISÃO**<br>
> **Descrição:** Ato processual praticado pelo juiz no processo, que decide uma questão incidente sem resolução do mérito, isto é, sem dar uma solução final à lide proposta em juízo.<br>
> **Simplificação realizada:** Breadscrum = 1:3 (qualquer movimento com essa hierarquia)
> * **AUDIÊNCIA**<br>
> **Descrição:** Sessão solene por determinação de juízes ou tribunais, para a realização de atos processuais.<br>
> **Simplificação realizada:** Breadscrum = 14:48:970 (qualquer movimento com essa hierarquia)
> * **JULGAMENTO/SENTENÇA**<br>
> **Descrição:** Ato de julgar ou decidir uma causa com a absolvição ou a condenação do réu; pronunciamento, por meio do qual o juízo competente, singular ou coletivo, após apreciar o mérito da questão principal ou incidente, acolhe ou não o pedido, condenando nas custas e em honorários advocatícios a parte que sucumbe.<br>
> **Simplificação realizada:** Breadscrum = 1:193 (qualquer movimento com essa hierarquia)
> * **TRÂNSITO EM JULGADO**<br>
> **Descrição:** Condição final de uma sentença contra a qual não ocorreu recurso de lei, quando, via de consequência, tornou-se coisa julgada.<br>
> **Simplificação realizada:** Código de movimento = 848
> * **BAIXA / ARQUIVAMENTO**<br>
> **Descrição:** Fase processual que indica o término do processo, ou seja, teve uma decisão judicial final.<br>
> **Simplificação realizada:**
>   * Código de movimento = 22 - baixa
>   * Código de movimento = 246 - arquivamento definitivo. 

<br>[Voltar para o menu](#menu)

<a id="tempo-produtividade"></a>
### 2. Solução: Painel de Tempos e Produtividade
Esta interface permite que tanto o pesquisador do CNJ possa acompanhar o desempenho das unidades judiciárias brasileiras, fazendo intervenções quando necessário, como o Juiz / Desembargador poderá acompanhar o desempenho da sua unidade judiciária, identificando facilmente onde estão os gargalos de sua unidade judiciária, bem como comparar seu desempenho com outras unidades similares, criando um ambiente de interação e colaboração de boas práticas com as demais unidades judiciárias brasileiras.

<a id="login"></a>
#### 2.1 Realizando o login na solução PANORAMA
A solução PANORAMA pode ser acessada pelo endereço: http://panorama-fase2.herokuapp.com <br>

> Obs.: Para esta fase, não existe nenhuma validação quanto aos dados inseridos, sendo necessário apenas informar os campos obrigatórios.

Ao clicar no link acima, você será direcionado para a tela de login da ferramenta, conforme imagem abaixo, onde destacamos os campos que fazem parte do login.<br>
<img src='/reports/figures/login.png'>

A solução foi pensada para estar em conformidade com as exigências da LEI GERAL DE PROTEÇÃO DE DADOS (LGPD), como pode ser observado pela POLÍTICA DE PRIVACIDADE contida na tela de login.

<br>[Voltar para o menu](#menu)

<a id="cnj"></a>
#### 2.2 Visão geral das unidades judiciárias
> * **Usuário alvo:** Pesquisador do CNJ.
> * **Objetivo do módulo:** Prover informações sobre tempo e produtividade das unidades judiciárias similares.
Abaixo destacamos cada componente do módulo, fornecendo um breve comentário sobre o componente e sua utilização.

<img src='/reports/figures/solucao_1.png'>

A seguir uma descrição dos principais componentes desta solução enumerados nas figuras acima:

* **Filtros**
    * Nessa sessão podemos consultar os filtros utilizados para montagem do critério de clusterização utilizado e temos a oportunidade de refinar consultar as informações de grupos específicos. Também é possível, clicando no botão "TODOS OS GRUPOS", verificar a quantidade de alertas gerados para cada grupo, com a possibilidade de filtrar as informações grupo mediante clique na barra do gráfico (conforme mostra a imagem abaixo).

    <img scr='/reports/figures/filtro.png'>

* **Informações do grupo**
    * Aqui exibimos o nome do grupo, a quantidade de unidades judiciárias que fazem parte do grupo e o tempo médio de conclusão dos processos do grupo.
* **Unidades judiciárias em ALERTA**
    * Nesta sessão exibimos uma tabela com as unidades judiciárias que estão com alertas, seja pelo baixo desempenho frente a outras unidades similares de seu grupo, ou pela existência de movimentações estranhas (incomum) ou devido existência de Outliers. <br>
    Nesta tabela podemos identificar:
     * a UNIDADE JUDICIÁRIA, 
     * o TRIBUNAL a que ela faz parte, 
     * o TEMPO MÉDIO de conclusão dos processos, 
     * a quantidade média de MOVIMENTAÇÕES, 
     * a quantidade de PROCESSOS, 
     * e as MELHORES e PIORES ETAPAS da UNIDADE.
    
    > Aqui o Pesquisador do CNJ tem a possibilidade de interagir com o Tribunal da unidade judiciária com alerta, enviando um e-mail notificando o baixo desempenho identificado e solicitando esclarecimentos quanto aos dados apurados.

* **Melhores unidades judiciárias**
    * Nesta sessão exibimos uma tabela com as unidades judiciárias de melhor desempenho do grupo.<br>
    Nesta tabela podemos identificar:
     * a UNIDADE JUDICIÁRIA, 
     * o TRIBUNAL a que ela faz parte, 
     * o TEMPO MÉDIO de conclusão dos processos, 
     * a quantidade média de MOVIMENTAÇÕES, 
     * a quantidade de PROCESSOS, 
     * e as MELHORES e PIORES ETAPAS da UNIDADE.
    
    > Aqui o Pesquisador do CNJ tem a possibilidade de interagir com o Tribunal da unidade judiciária com alerta, enviando um e-mail de parabenização pelo desempenho alcançado e solicitando que a unidade compartilhe as boas práticas adotadas.
* **Piores unidades judiciárias**
    * Similar a sessão de Alertas, nesta sessão exibimos uma tabela com as unidades judiciárias que estão com baixo desempenho. <br>
    Nesta tabela podemos identificar:
     * a UNIDADE JUDICIÁRIA, 
     * o TRIBUNAL a que ela faz parte, 
     * o TEMPO MÉDIO de conclusão dos processos, 
     * a quantidade média de MOVIMENTAÇÕES, 
     * a quantidade de PROCESSOS, 
     * e as MELHORES e PIORES ETAPAS da UNIDADE.
    
    > Aqui o Pesquisador do CNJ tem a possibilidade de interagir com o Tribunal da unidade judiciária com alerta, enviando um e-mail notificando o baixo desempenho identificado e solicitando esclarecimentos quanto aos dados apurados.
    
    > Aqui o Pesquisador do CNJ tem a possibilidade de interagir com o Tribunal da unidade judiciária com alerta, enviando um e-mail notificando o baixo desempenho identificado e solicitando esclarecimentos quanto aos dados apurados.
* **Tempo percentual das MacroEtapas (Unidades de melhor x pior desempenho)**
    * Contém o detalhamento dos tempos médio processuais em cada macroetapa das unidades judiciárias com melhor e pior desempenho para efeitos de comparação detalhada por macroetapa.
* **Localização geográfica das unidades que fazem parte do grupo**
    * Distribui cada unidade judiciária do grupo no mapa do Brasil para facilitar análise geográfica dos grupos.

**Curiosidade**: É possível obter o detalhamento das informações, basta clicar no nome da unidade judiciária para que as informações detalhadas de tempo e produtividade da unidade judiciária sejam carregadas.

<br>[Voltar para o menu](#menu)

<a id="alertas"></a>
#### 2.2.1 Como identificar todos os alertas gerados pela solução?
Logo quando o usuário PESQUISADOR DO CNJ loga na solução, a ferramenta carrega os dados de um grupo (cluster) de unidades judiciárias semelhantes para análise do usuário. Contudo é possível que o usuário queria escolher outro grupo para analisar (para tanto, deve-se utilizar o filtro de grupo localizado no top da página) ou ainda consultar todos os alertas emitidos pela ferramenta. <br>
Neste caso, o usuário deve clicar no botão amarelo "Todos os grupos", localizado no topo da página, ao lado do filtro por grupo (conforme demonstra a imagem abaixo).<br>
<img src='/reports/figures/todosgrupos.png'><br>
Após clicar no botão, o sistema vai exibir um gráfico com o total de alertas emitidos para cada grupo. Caso o usuário queira consultar as informações de um grupo específico, basta clicar na barra do gráfico referente ao grupo desejado, que as informações do grupo serão carregadas na tela. <br>
<img src='/reports/figures/todosgrupos_clique.png'>


<br>[Voltar para o menu](#menu)

<a id="grupos"></a>
#### 2.2.2 Como verificar a situação de outros grupos?
Para analisar os dados de outros grupos, basta utilizar o filtro de grupo (localizado no topo da página) ou clicar no grupo desejado exibido no [gráfico de alertas](#alertas) 
<br>[Voltar para o menu](#menu)


<a id="baixo-desempenho"></a>
#### 2.2.3 Como identificar as unidades judiciárias com problemas?
As unidades judiciárias com problemas são exibidas em dois lugares: 
* Unidades judiciárias em ALERTA
* Unidades judiciárias com pior desempenho

Conforme sinalizado na imagem abaixo<br>
<img src='/reports/figures/baixodesempenho.png'><br>

> Obs.: Em ambas as situações é possível interagir com o Tribunal ao qual a unidade pertence, através da funcionalidade de [notificações](#notificar)

<br>[Voltar para o menu](#menu)

<a id="notificar"></a>
#### 2.2.4 Como entrar em contato com as unidades para realizar notificações?
Uma vez tendo localizado as unidades que possuam alertas, baixo desempenho ou que apresentaram um desempenho acima da média, é possível para o usuário PESQUISADOR CNJ, enviar mensagens para o Tribunal ao qual as respectivas unidades judiciárias fazem parte, seja para notificar o baixo desempenho e solicitar uma justificativa, quanto para parabenizar o desempenho e solicitar que as boas práticas empregadas sejam compartilhadas com outras unidades, conforme podemos observar na imagem abaixo:<br>
<img src='/reports/figures/mensagens.png'>
<br>[Voltar para o menu](#menu)

<a id="localizar"></a>
#### 2.2.5 Onde estao localizadas as unidades judiciárias desse grupo?
O PESQUISADOR do CNJ também pode, facilmente, identificar a localização geográfica de cada unidade que compõe o grupo que está sendo analisado. Para tanto basta interagir com o último componente localizado no final da página.<br>
<img src='/reports/figures/localizacao.png'>
<br>[Voltar para o menu](#menu)

<a id="juiz"></a>
#### 2.3 Visão específica da unidade judiciária
> * **Usuário alvo:** 
>   * Juíz / Desembargador.
>   * Servidores da unidade judiciária.
>   * Pesquisador do CNJ.
> * **Objetivo do módulo:** Prover informações detalhadas de tempo e produtividade da unidade judiciária em questão, para que os gestores possam identificar oportunidades de melhoria, trocar experiência / boas práticas com outras unidades judiciárias semelhantes.

Abaixo destacamos cada componente do módulo, fornecendo um breve comentário sobre o componente e sua utilização.
<img src='/reports/figures/solucao_2.png'>

A seguir uma descrição dos principais componentes desta solução enumerados nas figuras acima:

* **Informações da unidade judiciária**
    * Exibe o nome da unidade judiciária e o tribunal ao qual ela pertence.
* **Posição Geral**
    * Colocação geral de sua unidade judicial em relação ao seu grupo. Essa colocação é medida como o tempo médio em dias que os processos da unidade judicial demoram para serem baixados ou arquivados.
* **Estatísticas gerais de desempenho**
    * Nesta sessão exibimos três métricas da unidade judiciária: 
       * TEMPO PARA BAIXA DO PROCESSO: tempo médio decorrido entre a DISTRIBUIÇÃO DO PROCESSO e sua BAIXA do acervo da unidade judiciária.<br>
       * MOVIMENTAÇÕES POR PROCESSO: quantidade média de movimentações geradas por processo.<br>
       * PROCESSOS JULGADOS: quantidade de processos julgados.  
* **Etapa com MELHOR desempenho**
    * MacroEtapa com melhor tempo médio. Destaque da unidade judiciária.
* **Etapa com PIOR desempenho**
    * MacroEtapa com pior tempo médio. Ponto de atenção da unidade judiciária.       
* **Seletor da visão de macroetapa**
    * Controle que determina qual informação será exibida na sessão de GESTÃO DE TRAMITAÇÃO PROCESSUAL, serão exibidos os gargalos da unidade ou os destaques?
* **Gestão de tramitação processual**
    * Principal funcionalidade deste módulo. Permite que o usuário obtença informações detalhadas do desempenho da unidade judiciária, notadamente:
       * Informa a qual MACROETAPA referem-se as informações a seguir.
       * Duração média entre as MACROETAPAS sinalizadas.
       * Posição da unidade judiciária frente outras unidades similares (pertencentes ao mesmo grupo), em relação as MACROETAPAS sinalizadas.
       * Quantidade de ocorrências registradas entre as MACROETAPAS sinalizadas.
* **Feedbacks / Insights**
    * Contém os comentários de outras unidades judiciárias em relação as MACROETAPAS sinalizadas, serve como fonte de boas práticas e colaboração entre as unidades. É possível interagir com outras unidades através dos comentários.

* **Gráfico das unidades de melhor desempenho**
    * Destacam o pior e menor gargalo da unidade judicial referente às macroetapas.
* **Gráfico das unidades com desempenho semelhantes**
    * Destacam a duração média da baixa do processo em dias, movimentação média do processo e total de processos julgados
<br>[Voltar para o menu](#menu)


<a id="config"></a>
### 3. Solução: Criação, análise e configuração dos critérios
Abaixo podemos consultar algumas telas utilizadas para criar, configurar os critérios e realizar a análise dos grupos obtidos. 
<img src='/reports/figures/tela_grupo.png'> <br>
<img src='/reports/figures/tela_grupo2.png'> <br>

[Voltar para o menu](#menu)
