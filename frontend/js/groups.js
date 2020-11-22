var groups = undefined
var selectedGroup = undefined
var bestCourts = undefined
var worstCourts = undefined

var movements = ['Distribuição','Conclusão','Despacho','Decisão','Julgamento','Trânsito em julgado','Baixa ou arquivamento', 'Audiencia', 'Citação', 'Outros']
var time_distribuicao = undefined
var time_conclusao = undefined
var time_despacho = undefined
var time_decisao = undefined
var time_julgamento = undefined
var time_transito_em_julgado = undefined
var time_baixa_ou_arquivamento = undefined
var time_audiencia = undefined
var time_citacao = undefined
var time_outros = undefined

getGroups((data)=>{
  groups = data
  c3.generate({
    data: {
        columns: [getDataColumns()],
        types: {
            alertas: 'bar',
        },
        onclick: function(d, element) {
          selectGroup(groups[d.x])
        },
        onmouseover: function(d) {
          if(d.x)
            selectGroup(d.x)
        }
    },
    axis: {
        rotated: false,
        x: {
          tick: {
            format: function (x) { return 'grupo '+(groups[x] ? groups[x].identificador : '') }
          }
        }
    },
    bindto: '#chart_alerts'
  });
  selectGroup(groups[0])
})

function getDataColumns(){
  var columns = ['alertas']
  groups.forEach(g => {
    columns.push(g.varas_em_alerta)
  });
  return columns
}

function selectGroup(group) {
  selectedGroup = group
  $('#group_name').html('Grupo ' + selectedGroup.identificador)
  $('#group_members').html('Membros ' + selectedGroup.total_varas)
  $('#group_time').html('Tempo ' + selectedGroup.total_varas)

  getBestCourts(selectedGroup.identificador, (data)=>{
    $("#rank_courts").html("")
    //best 
    $("#rank_courts").append('<tr class="table-title"><td colspan="7">Varas com os melhores tempos de conclução de processo</td></tr>');
    fillRankTable(data.melhoresVaras)
    bestCourts = data.melhoresVaras
    //separator
    $("#rank_courts").append('<tr class="ellipses"><td colspan="7"><i class="fas fa-ellipsis-v"></i></td></tr>');
    //worst
    $("#rank_courts").append('<tr class="table-title"><td colspan="7">Varas com os piores tempos de conclução de processo</td></tr>')
    fillRankTable(data.pioresVaras)
    worstCourts = data.pioresVaras
    
    fillCourtFilter()

    fillMovementsChart()

    fillMap()

  })
}

function fillRankTable(courts, filter) {
  courts.forEach(court => {
    if(!filter || filter == "" || (filter == court.tribunal)) {
      var row = "<tr id="+court.identificador+"><td>"+court.ranking+"</td><td>"+court.nome+"</td><th>"+court.tribunal+
      "</th><td>"+court.tempo+" dias</td><td>"+court.movimentos+"</td><td>"
      +court.processos+"</td><td>"+court.melhorEtapa+"</td><td>"+court.piorEtapa+"</td></tr>"
      $("#rank_courts").append(row);
      $('#'+court.identificador).click(e=>{
        vara_id = e.currentTarget.id
        saveCache()
        window.location.replace("file:///home/fernando/Development/web/fase2_desafio_cnj/frontend/index.html");       
      }) 
    }
  });
}

function fillMovementsChart() {
  time_distribuicao = ["Distribuição"]
  time_conclusao = ["Conclusão"]
  time_despacho = ["Despacho"]
  time_decisao = ["Decisão"]
  time_julgamento = ["Julgamento"]
  time_transito_em_julgado = ["Trânsito em julgado"]
  time_baixa_ou_arquivamento = ["Baixa ou arquivamento"]
  time_audiencia = ["Audiencia"]
  time_citacao = ["Citação"]
  time_outros = ["Outros"]

  bestCourts.slice(0,5).forEach(vara => {
    vara.porcentagemMacroetapas.forEach(json => {
      fillMovementTimes(json)
    });
  })

  worstCourts.slice(0,5).forEach(vara => {
    vara.porcentagemMacroetapas.forEach(json => {
      fillMovementTimes(json)
    });
  })
  
  c3.generate({
      data: {
          columns: [time_distribuicao, time_conclusao, time_despacho, time_decisao,
              time_julgamento, time_transito_em_julgado, time_baixa_ou_arquivamento, time_audiencia
          , time_citacao, time_outros],
          type: 'bar',
          groups: [movements]
          //groups: [result.map(court => court.name)]
      },
      grid: {
          y: {
              lines: [{value:0}]
          }
      },
      tooltip: {
          format: {
              title: function (d) { return d < 5 ? bestCourts.slice(0,5)[d].nome : worstCourts.slice(0,5)[d-5].nome }
          }
      },
      axis: {
        y: {
          label: {
            text: 'Número de dias',
            position: 'outer-middle'
          }
        }
      }
    });
}

function getValidValue(value) {
  if(value == -1)
      value = 0
  return value
}

function fillMovementTimes(json) {
  if(json.time_distribuicao && json.time_distribuicao != null)
      time_distribuicao.push(getValidValue(json.time_distribuicao))
  else
      time_distribuicao.push(0)
  if(json.time_conclusao && json.time_conclusao != null)
      time_conclusao.push(getValidValue(json.time_conclusao))
  else
      time_conclusao.push(0)
  if(json.time_despacho && json.time_despacho != null)
      time_despacho.push(getValidValue(json.time_despacho))
  else
      time_despacho.push(0)
  if(json.time_decisao && json.time_decisao != null)
      time_decisao.push(getValidValue(json.time_decisao))
  else
      time_decisao.push(0)
  if(json.time_julgamento && json.time_julgamento != null)
      time_julgamento.push(getValidValue(json.time_julgamento))
  else
      time_julgamento.push(0)
  if(json.time_transito_em_julgado && json.time_transito_em_julgado != null)
      time_transito_em_julgado.push(getValidValue(json.time_transito_em_julgado))
  else
      time_transito_em_julgado.push(0)
  if(json.time_baixa_ou_arquivamento && json.time_baixa_ou_arquivamento != null)
      time_baixa_ou_arquivamento.push(getValidValue(json.time_baixa_ou_arquivamento))
  else
      time_baixa_ou_arquivamento.push(0)
  if(json.time_audiencia && json.audiencia != null)
      time_audiencia.push(getValidValue(json.audiencia))
  else
      time_audiencia.push(0)
  if(json.time_citacao && json.citacao != null)
      time_citacao.push(getValidValue(json.citacao))
  else
      time_citacao.push(0)
  if(json.time_outros && json.outros!= null)
      time_outros.push(getValidValue(json.outros))
  else
      time_outros.push(0)
}

function fillMap() {
  var locations = []
  selectedGroup.varas.forEach((vara)=>{
    locations.push([vara.nome, vara.latitude, vara.longitude])  
  })
  populateMap(map, infowindow, locations)
}

function fillCourtFilter() {
  $('#cboTribunal').html('<option value=""></option>')
  var courts = []
  bestCourts.forEach(court => {
    if(court.tribunal && !courts.includes(court.tribunal))
      courts.push(court.tribunal)
  });
  worstCourts.forEach(court => {
    if(court.tribunal && !courts.includes(court.tribunal))
      courts.push(court.tribunal)
  });
  courts.forEach((court) => {
    $('#cboTribunal').append('<option value="'+court+'">'+court+'</option>')
  })
}

function filterCourt() {
  var selector = $('#cboTribunal')[0]
  var court =  selector.options[selector.selectedIndex].value
  $("#rank_courts").html("")

  //best 
  $("#rank_courts").append('<tr class="table-title"><td colspan="7">Varas com os melhores tempos de conclução de processo</td></tr>');
  fillRankTable(bestCourts, court)
  //separator
  $("#rank_courts").append('<tr class="ellipses"><td colspan="7"><i class="fas fa-ellipsis-v"></i></td></tr>');
  //worst
  $("#rank_courts").append('<tr class="table-title"><td colspan="7">Varas com os piores tempos de conclução de processo</td></tr>')
  fillRankTable(worstCourts, court)
}