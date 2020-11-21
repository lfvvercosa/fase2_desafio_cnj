var groups = undefined
var selectedGroup = undefined

getGroups((data)=>{
  groups = data
  console.log(groups)
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
          selectGroup(d.x)
        }
    },
    axis: {
        rotated: false,
        x: {
          tick: {
            format: function (x) { return 'gropo '+(groups[x] ? groups[x].identificador : '') }
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
  console.log('selected group = '+ JSON.stringify(selectedGroup))

  getBestCourts(selectedGroup.identificador, (data)=>{
    console.log(JSON.stringify(data.melhoresVaras))
    //best 
    $("#rank_courts").append('<tr class="table-title"><td colspan="7">Varas com os melhores tempos de conclução de processo</td></tr>');
    fillRankTable(data.melhoresVaras)
    //separator
    $("#rank_courts").append('<tr class="ellipses"><td colspan="7"><i class="fas fa-ellipsis-v"></i></td></tr>');
    
    //worst
    $("#rank_courts").append('<tr class="table-title"><td colspan="7">Varas com os piores tempos de conclução de processo</td></tr>')
    fillRankTable(data.pioresVaras)
  })
}

function fillRankTable(courts) {
  var i = 0
  courts.forEach(court => {
    var row = "<tr><td>"+court.ranking+"</td><td>"+court.nome+"</td><th>+"+court.tribunal+
    "</th><td>"+court.tempo+" dias</td><td>"+court.movimentos+" movimentos</td><td>"
    +court.processos+" processos</td><td>"+court.melhorEtapa+"</td><td>"+court.piorEtapa+"</td></tr>"
    $("#rank_courts").append(row);
  });
}
