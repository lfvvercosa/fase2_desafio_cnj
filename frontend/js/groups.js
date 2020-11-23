var groups = undefined
var selectedGroup = undefined
var bestCourts = undefined
var worstCourts = undefined
var warningCourts = undefined

var movements = ['Distribuição','Conclusão','Despacho','Decisão','Julgamento','Trânsito em julgado','Baixa ou arquivamento', 'Audiencia', 'Citação', 'Outros']
var best_distribuicao = undefined
var best_conclusao = undefined
var best_despacho = undefined
var best_decisao = undefined
var best_julgamento = undefined
var best_transito_em_julgado = undefined
var best_baixa_ou_arquivamento = undefined
var best_audiencia = undefined
var best_citacao = undefined
var best_outros = undefined

var worst_distribuicao = undefined
var worst_conclusao = undefined
var worst_despacho = undefined
var worst_decisao = undefined
var worst_julgamento = undefined
var worst_transito_em_julgado = undefined
var worst_baixa_ou_arquivamento = undefined
var worst_audiencia = undefined
var worst_citacao = undefined
var worst_outros = undefined

var warning_distribuicao = undefined
var warning_conclusao = undefined
var warning_despacho = undefined
var warning_decisao = undefined
var warning_julgamento = undefined
var warning_transito_em_julgado = undefined
var warning_baixa_ou_arquivamento = undefined
var warning_audiencia = undefined
var warning_citacao = undefined
var warning_outros = undefined

getGroups((data)=>{
  groups = data
  fillCboGroupFilter()

  c3.generate({
    data: {
        columns: [getDataColumns()],
        types: {
            alertas: 'bar',
        },
        onclick: function(d, element) {
          selectGroup(groups[d.x])
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

function selectGroupById(selector) {
  var id = selector.options[selector.selectedIndex].value
  selectGroup(groups.find((g)=>g.identificador == id))
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
    bestCourts = data.varas.slice(0,5)
    fillRankTable(bestCourts, "", false, "best")
    //separator
    $("#rank_courts").append('<tr class="ellipses"><td colspan="7"><i class="fas fa-ellipsis-v"></i></td></tr>');
    //worst
    $("#rank_courts").append('<tr class="table-title"><td colspan="7">Varas com os piores tempos de conclução de processo</td></tr>')
    worstCourts = data.varas.slice(data.varas.length-5, data.varas.length)

    warningCourts = data.varasEmAlerta

    console.log(warningCourts)

    fillRankTable(worstCourts, "", true, "worst")
    
    fillCourtFilter()

    fillMovementsChart()

    fillMap()

  })
}

function fillRankTable(courts, filter, isBottleNeck, tableName) {
  var colorClass = isBottleNeck ? 'uj-alerta' : 'uj-destaque'
  var buttonClass = isBottleNeck ? 'warning' : 'award'
  var icon = isBottleNeck ? 'bullhorn' : 'bullhorn'
  courts.forEach(court => {
    if(!filter || filter == "Todos" || (filter == court.tribunal)) {
      var row = '<tr class='+colorClass+'><td id='+tableName+'_rank_'+court.vara_id+'>'+court.ranking+'</td><td>'+court.name+'</td><th>'+court.tribunal+
      '</th><td id='+tableName+'_days_'+court.vara_id+'>'+court.days_finish_process+' dias</td><td id='+tableName+'_movements_'+court.vara_id+'>'+court.movements+'</td><td id='+tableName+'_processes_'+court.vara_id+'>'
      +court.finished_processes+'</td><td id='+tableName+'_best_movements_'+court.vara_id+'>'+court.melhorEtapa+'</td><td id='+tableName+'_worst_movements_'+court.vara_id+'>'+court.piorEtapa+'</td>'
      +'<td><button class="modal-button modal-button-'+buttonClass+'" type=button data-toggle=tooltip'
      +' title="Enviar alerta para este tribunal"><span data-toggle=modal data-target=#alertasSugeridos>'
      +'<i class="fas fa-'+icon+'"></i></span></button></td></tr>'
      
      $("#rank_courts").append(row);

      $('#'+tableName+'_rank_'+court.vara_id).click(e=>{
        vara_id = e.currentTarget.id
        saveCache()
        window.location.replace("file:///home/fernando/Development/web/fase2_desafio_cnj/frontend/vara.html");       
      })

      $('#'+tableName+'_days_'+court.vara_id).click(e=>{
        vara_id = e.currentTarget.id
        saveCache()
        window.location.replace("file:///home/fernando/Development/web/fase2_desafio_cnj/frontend/vara.html");       
      })
      
      $('#'+tableName+'_movements_'+court.vara_id).click(e=>{
        vara_id = e.currentTarget.id
        saveCache()
        window.location.replace("file:///home/fernando/Development/web/fase2_desafio_cnj/frontend/vara.html");       
      })

      $('#'+tableName+'_processes_'+court.vara_id).click(e=>{
        vara_id = e.currentTarget.id
        saveCache()
        window.location.replace("file:///home/fernando/Development/web/fase2_desafio_cnj/frontend/vara.html");       
      })

      $('#'+tableName+'_best_movements'+court.vara_id).click(e=>{
        vara_id = e.currentTarget.id
        saveCache()
        window.location.replace("file:///home/fernando/Development/web/fase2_desafio_cnj/frontend/vara.html");       
      })

      $('#'+tableName+'_worst_movements_'+court.vara_id).click(e=>{
        vara_id = e.currentTarget.id
        saveCache()
        window.location.replace("file:///home/fernando/Development/web/fase2_desafio_cnj/frontend/vara.html");       
      })
    }
  });
}

function fillMovementsChart() {
  best_distribuicao = ["Distribuição"]
  best_conclusao = ["Conclusão"]
  best_despacho = ["Despacho"]
  best_decisao = ["Decisão"]
  best_julgamento = ["Julgamento"]
  best_transito_em_julgado = ["Trânsito em julgado"]
  best_baixa_ou_arquivamento = ["Baixa ou arquivamento"]
  best_audiencia = ["Audiencia"]
  best_citacao = ["Citação"]
  best_outros = ["Outros"]

  bestCourts.forEach(vara => {
      fillBestMovementTimes(vara)
  })

  c3.generate({
      data: {
          columns: [best_distribuicao, best_conclusao, best_despacho, best_decisao,
              best_julgamento, best_transito_em_julgado, best_baixa_ou_arquivamento, best_audiencia
          , best_citacao, best_outros],
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
              title: function (d) { return bestCourts[d].nome }
          }
      },
      axis: {
        y: {
          label: {
            text: 'Número de dias',
            position: 'outer-middle'
          }
        },
      },
      bindto: '#chart_best'
    });

    worst_distribuicao = ["Distribuição"]
    worst_conclusao = ["Conclusão"]
    worst_despacho = ["Despacho"]
    worst_decisao = ["Decisão"]
    worst_julgamento = ["Julgamento"]
    worst_transito_em_julgado = ["Trânsito em julgado"]
    worst_baixa_ou_arquivamento = ["Baixa ou arquivamento"]
    worst_audiencia = ["Audiencia"]
    worst_citacao = ["Citação"]
    worst_outros = ["Outros"]

    worstCourts.forEach(vara => {
      fillWorstMovementTimes(vara)
    })

    c3.generate({
      data: {
          columns: [worst_distribuicao, worst_conclusao, worst_despacho, worst_decisao,
              worst_julgamento, worst_transito_em_julgado, worst_baixa_ou_arquivamento, worst_audiencia
          , worst_citacao, worst_outros],
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
              title: function (d) { return worstCourts[d].nome }
          }
      },
      axis: {
        y: {
          label: {
            text: 'Número de dias',
            position: 'outer-middle'
          }
        }
      },
      bindto: '#chart_worst'
    });
}

function getValidValue(value) {
  if(value == -1)
      value = 0
  return value
}

function fillBestMovementTimes(json) {
  if(json.time_distribuicao && json.time_distribuicao != null)
    best_distribuicao.push(getValidValue(json.time_distribuicao))
  else
    best_distribuicao.push(0)
  if(json.time_conclusao && json.time_conclusao != null)
    best_conclusao.push(getValidValue(json.time_conclusao))
  else
    best_conclusao.push(0)
  if(json.time_despacho && json.time_despacho != null)
    best_despacho.push(getValidValue(json.time_despacho))
  else
    best_despacho.push(0)
  if(json.time_decisao && json.time_decisao != null)
    best_decisao.push(getValidValue(json.time_decisao))
  else
    best_decisao.push(0)
  if(json.time_julgamento && json.time_julgamento != null)
    best_julgamento.push(getValidValue(json.time_julgamento))
  else
    best_julgamento.push(0)
  if(json.time_transito_em_julgado && json.time_transito_em_julgado != null)
    best_transito_em_julgado.push(getValidValue(json.time_transito_em_julgado))
  else
    best_transito_em_julgado.push(0)
  if(json.time_baixa_ou_arquivamento && json.time_baixa_ou_arquivamento != null)
    best_baixa_ou_arquivamento.push(getValidValue(json.time_baixa_ou_arquivamento))
  else
    best_baixa_ou_arquivamento.push(0)
  if(json.time_audiencia && json.audiencia != null)
    best_audiencia.push(getValidValue(json.audiencia))
  else
    best_audiencia.push(0)
  if(json.time_citacao && json.citacao != null)
    best_citacao.push(getValidValue(json.citacao))
  else
    best_citacao.push(0)
  if(json.time_outros && json.outros!= null)
    best_outros.push(getValidValue(json.outros))
  else
    best_outros.push(0)
}

function fillWorstMovementTimes(json) {
  if(json.time_distribuicao && json.time_distribuicao != null)
    worst_distribuicao.push(getValidValue(json.time_distribuicao))
  else
    worst_distribuicao.push(0)
  if(json.time_conclusao && json.time_conclusao != null)
    worst_conclusao.push(getValidValue(json.time_conclusao))
  else
    worst_conclusao.push(0)
  if(json.time_despacho && json.time_despacho != null)
    worst_despacho.push(getValidValue(json.time_despacho))
  else
    worst_despacho.push(0)
  if(json.time_decisao && json.time_decisao != null)
    worst_decisao.push(getValidValue(json.time_decisao))
  else
    worst_decisao.push(0)
  if(json.time_julgamento && json.time_julgamento != null)
    worst_julgamento.push(getValidValue(json.time_julgamento))
  else
    worst_julgamento.push(0)
  if(json.time_transito_em_julgado && json.time_transito_em_julgado != null)
    worst_transito_em_julgado.push(getValidValue(json.time_transito_em_julgado))
  else
    worst_transito_em_julgado.push(0)
  if(json.time_baixa_ou_arquivamento && json.time_baixa_ou_arquivamento != null)
    worst_baixa_ou_arquivamento.push(getValidValue(json.time_baixa_ou_arquivamento))
  else
    worst_baixa_ou_arquivamento.push(0)
  if(json.time_audiencia && json.audiencia != null)
    worst_audiencia.push(getValidValue(json.audiencia))
  else
    worst_audiencia.push(0)
  if(json.time_citacao && json.citacao != null)
    worst_citacao.push(getValidValue(json.citacao))
  else
    worst_citacao.push(0)
  if(json.time_outros && json.outros!= null)
    worst_outros.push(getValidValue(json.outros))
  else
    worst_outros.push(0)
}

function fillMap() {
  var locations = []
  selectedGroup.varas.forEach((vara)=>{
    locations.push([vara.nome, vara.latitude, vara.longitude])  
  })
  populateMap(map, infowindow, locations)
}

function fillCboGroupFilter() {
  $('#cboGroup').html('<option value=""></option>')
  groups.forEach((group) => {
    $('#cboGroup').append('<option value="'+group.identificador+'">'+group.identificador+'</option>')
  })
}

function fillCourtFilter() {
  $('#cboTribunal').html('')
  $('#cboTribunal').append('<option value="Todos">Todos</option>')
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
  fillRankTable(bestCourts, court, false, "best")
  //separator
  $("#rank_courts").append('<tr class="ellipses"><td colspan="7"><i class="fas fa-ellipsis-v"></i></td></tr>');
  //worst
  $("#rank_courts").append('<tr class="table-title"><td colspan="7">Varas com os piores tempos de conclução de processo</td></tr>')
  fillRankTable(worstCourts, court, true, "worst")
}