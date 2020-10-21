setRankComponent()
setStatisticsComponent()
setFooterRankComponent()

function setRankComponent() {
  setBottleneckRankComponent()
  setBestRankComponent()
}

function setBottleneckRankComponent() {
  getVaraByID(vara_id, (json)=>{
    $('#bottleneck-mov-1-source').html(json.worst_steps[0].origin)
    $('#bottleneck-mov-1-description').html(json.worst_steps[0].med_time)
    $('#bottleneck-mov-1-dest').html(json.worst_steps[0].destination)

    $('#bottleneck-mov-2-source').html(json.worst_steps[1].origin)
    $('#bottleneck-mov-2-description').html(json.worst_steps[1].med_time)
    $('#bottleneck-mov-2-dest').html(json.worst_steps[1].destination)

    $('#bottleneck-mov-3-source').html(json.worst_steps[2].origin)
    $('#bottleneck-mov-3-description').html(json.worst_steps[2].med_time)
    $('#bottleneck-mov-3-dest').html(json.worst_steps[2].destination)

    //bottoleneck table
    $('#table-bottleneck-tab1').html(json.worst_steps[0].origin + '-' + json.worst_steps[0].destination)
    $('#table-bottleneck-tab2').html(json.worst_steps[1].origin + '-' + json.worst_steps[1].destination)
    $('#table-bottleneck-tab3').html(json.worst_steps[2].origin + '-' + json.worst_steps[2].destination)

    $('#table-bottleneck-tab1').click(function(){
      setBottleneckTable(json, vara_id, 0)
      $('#table-bottleneck-tab2').removeClass('rank-table-tabs-item-selected')
      $('#table-bottleneck-tab3').removeClass('rank-table-tabs-item-selected')
      $('#table-bottleneck-tab1').addClass('rank-table-tabs-item-selected')
    })

    $('#table-bottleneck-tab2').click(function(){
      setBottleneckTable(json, vara_id, 1)
      $('#table-bottleneck-tab1').removeClass('rank-table-tabs-item-selected')
      $('#table-bottleneck-tab3').removeClass('rank-table-tabs-item-selected')
      $('#table-bottleneck-tab2').addClass('rank-table-tabs-item-selected')
    })

    $('#table-bottleneck-tab3').click(function(){
      setBottleneckTable(json, vara_id, 2)
      $('#table-bottleneck-tab1').removeClass('rank-table-tabs-item-selected')
      $('#table-bottleneck-tab2').removeClass('rank-table-tabs-item-selected')
      $('#table-bottleneck-tab3').addClass('rank-table-tabs-item-selected')
    })

    setBottleneckTable(json, vara_id, 0)    
    
  })
  $('#bottleneck-mov-1-position').html('13'+'°')
  $('#bottleneck-mov-2-position').html('13'+'°')
  $('#bottleneck-mov-3-position').html('13'+'°')
}

function setBestRankComponent() {
  
  getVaraByID(vara_id,(json)=>{
    //best movements component
    $('#best-mov-1-source').html(json.best_steps[0].origin)
    $('#best-mov-1-description').html(json.best_steps[0].med_time)
    $('#best-mov-1-dest').html(json.best_steps[0].destination)

    $('#best-mov-2-source').html(json.best_steps[1].origin)
    $('#best-mov-2-description').html(json.best_steps[1].med_time)
    $('#best-mov-2-dest').html(json.best_steps[1].destination)

    $('#best-mov-3-source').html(json.best_steps[2].origin)
    $('#best-mov-3-description').html(json.best_steps[2].med_time)
    $('#best-mov-3-dest').html(json.best_steps[2].destination)

    //best movements table
    $('#table-best-tab1').html(json.best_steps[0].origin + '-' + json.best_steps[0].destination)
    $('#table-best-tab2').html(json.best_steps[1].origin + '-' + json.best_steps[1].destination)
    $('#table-best-tab3').html(json.best_steps[2].origin + '-' + json.best_steps[2].destination)

    setBestTable(json, vara_id, 0)  
    
    $('#table-best-tab1').click(function(){
      setBestTable(json, vara_id, 0)
      $('#table-best-tab2').removeClass('rank-table-tabs-item-selected')
      $('#table-best-tab3').removeClass('rank-table-tabs-item-selected')
      $('#table-best-tab1').addClass('rank-table-tabs-item-selected')
    })

    $('#table-best-tab2').click(function(){
      setBestTable(json, vara_id, 1)
      $('#table-best-tab1').removeClass('rank-table-tabs-item-selected')
      $('#table-best-tab3').removeClass('rank-table-tabs-item-selected')
      $('#table-best-tab2').addClass('rank-table-tabs-item-selected')
    })

    $('#table-best-tab3').click(function(){
      setBestTable(json, vara_id, 2)
      $('#table-best-tab1').removeClass('rank-table-tabs-item-selected')
      $('#table-best-tab2').removeClass('rank-table-tabs-item-selected')
      $('#table-best-tab3').addClass('rank-table-tabs-item-selected')
    })

  })
  //best movements component
  //best-mov-1-position
  //best-mov-2-position
  //best-mov-3-position
}

function setStatisticsComponent(){
  getVaraByID(vara_id, (json)=> {
    //worst
    $('#statistics-wrost-title-1').html('Pior <br>desempenho')
    $('#statistics-wrost-value').html(json.worst_steps[0].origin)
    $('#statistics-wrost-position').html('1' + '° de ' + json.group.amount_of_varas + ' varas')
    //statistics-wrost-title-2

    //best
    $('#statistics-best-title-1').html('Melhor <br>desempenho')
    $('#statistics-best-value').html(json.best_steps[0].origin)
    $('#statistics-best-position').html('1' + '° de ' + json.group.amount_of_varas + ' varas')
    //statistics-best-title-2

    //duration
    $('#statistics-duration-title-1').html('Duração da <br>baixa do processo')
    $('#statistics-duration-value').html(json.days_finish_process + ' dias')
    $('#statistics-duration-position').html('1' + '° de ' + json.group.amount_of_varas + ' varas')
    //statistics-duration-title-2

    //movements
    $('#statistics-moves-title-1').html('Movimentação <br>por processo')
    $('#statistics-moves-value').html(json.movements)
    //statistics-moves-title-2

    //finished
    $('#statistics-finished-title-1').html('Processos <br>julgados')
    $('#statistics-finished-value').html(json.finished_processes)
    $('#statistics-finished-position').html('1' + '° de ' + json.group.amount_of_varas + ' varas')
    //statistics-finished-title-2
  })
}

function setFooterRankComponent() {
    getBestVaras(vara_id, 10, (json)=>{
        $('#best-time-1').html('1º - ' + json[0].name)
        $('#best-time-2').html('2º - ' + json[1].name)
        $('#best-time-3').html('3º - ' + json[2].name)
        $('#best-time-4').html('4º - ' + json[3].name)
        $('#best-time-5').html('5º - ' + json[4].name)
        $('#best-time-6').html('6º - ' + json[5].name)
        $('#best-time-7').html('7º - ' + json[6].name)
        $('#best-time-8').html('8º - ' + json[7].name)
        $('#best-time-9').html('9º - ' + json[8].name)
        $('#best-time-10').html('10º - ' + json[9].name)
    })
}

function setBottleneckTable(json, vara_id, step){
  getBestVarasOnStep(json.worst_steps[step].step_id,
    vara_id,
    10,
    (json2)=>{
      bestVarasOnStep = json2
      for(var i=0; i < 10; i++){
        $('#table-bottleneck-row-'+(i+1)+'-name').html(bestVarasOnStep[i].vara_name)
        $('#table-bottleneck-row-'+(i+1)+'-duration').html(bestVarasOnStep[i].med_time)
        $('#table-bottleneck-row-'+(i+1)+'-comments').html(bestVarasOnStep[i].comment)
        $('#table-bottleneck-row-'+(i+1)).click(function(e){
          var index = e.currentTarget.id.replace('table-bottleneck-row-', '')
          comparing_id = bestVarasOnStep[index-1].vara_id
          window.location.replace("http://desafio-cnj-frontend.herokuapp.com/pages/comparing-courts.html");
        })
      }
    })
}

function setBestTable(json, vara_id, step){
  // Best varas on best step 1
  getBestVarasOnStep(json.best_steps[step].step_id,
    vara_id,
    10,
    (json2)=>{
      for(var i=0; i < 10; i++){
        $('#table-best-row-'+(i+1)+'-name').html(json2[i].vara_name)
        $('#table-best-row-'+(i+1)+'-duration').html(json2[i].med_time)
        $('#table-best-row-'+(i+1)+'-comments').html(json2[i].comment)
        $('#table-best-row-'+(i+1)).click(function(){
          var index = e.currentTarget.id.replace('table-best-row-', '')
          comparing_id = json2[index-1].vara_id
          window.location.replace("http://desafio-cnj-frontend.herokuapp.com/pages/comparing-courts.html");
        })
      }
    })
}