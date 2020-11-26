## Fontes de dados
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
Abaixo outros filtros realizados nos dados ao longo do projeto:  
  * **Filtro nos processos:** Só foram considerados processos:
    *  Movimentação de início (Distribuição) e movimento de término (Baixa ou Arquivamento definitivo) compreendidos entre os anos de 2000 e 2020.
    *  Justiça Estadual
    *  1º Grau
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
Para depois serem transformados em coluna (aumento das dimensões)

<img src='/reports/figures/analise_criterios.png'> <br>

