setRankComponent()
setStatisticsComponent()
setFooterRankComponent()

function setRankComponent() {
  setBottleneckRankComponent()
  setBestRankComponent()
}

function setBottleneckRankComponent() {
  getVaraByID((json)=>{
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
  })
  $('#bottleneck-mov-1-position').html('13'+'°')
  $('#bottleneck-mov-2-position').html('13'+'°')
  $('#bottleneck-mov-3-position').html('13'+'°')

  //bottoleneck table
  $('#table-bottleneck-row-1-name').html('wefnweonfewnfo')
  $('#table-bottleneck-row-1-duration').html('3 meses')
  $('#table-bottleneck-row-1-comments').html('wenfwfoni fwfnwenfiowen woifnwoif')

  //table-bottleneck-row-2-name
  //table-bottleneck-row-2-duration
  //table-bottleneck-row-2-comments

  //table-bottleneck-row-3-name
  //table-bottleneck-row-3-duration
  //table-bottleneck-row-3-comments

  //table-bottleneck-row-4-name
  //table-bottleneck-row-4-duration
  //table-bottleneck-row-4-comments

  //table-bottleneck-row-5-name
  //table-bottleneck-row-5-duration
  //table-bottleneck-row-5-comments

  //table-bottleneck-row-6-name
  //table-bottleneck-row-6-duration
  //table-bottleneck-row-6-comments

  //table-bottleneck-row-7-name
  //table-bottleneck-row-7-duration
  //table-bottleneck-row-7-comments
  
  //table-bottleneck-row-8-name
  //table-bottleneck-row-8-duration
  //table-bottleneck-row-8-comments

  //table-bottleneck-row-9-name
  //table-bottleneck-row-9-duration
  //table-bottleneck-row-9-comments
  
}

function setBestRankComponent() {
  getVaraByID((json)=>{
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
  })
  //best movements component
  //best-mov-1-position
  //best-mov-2-position
  //best-mov-3-position

  //best movements table
  //table-best-row-1-name
  //table-best-row-1-duration
  //table-best-row-1-comments
  
  //table-best-row-2-name
  //table-best-row-2-duration
  //table-best-row-2-comments
  
  //table-best-row-3-name
  //table-best-row-3-duration
  //table-best-row-3-comments
  
  //table-best-row-4-name
  //table-best-row-4-duration
  //table-best-row-4-comments
  
  //table-best-row-5-name
  //table-best-row-5-duration
  //table-best-row-5-comments
  
  //table-best-row-6-name
  //table-best-row-6-duration
  //table-best-row-6-comments
  
  //table-best-row-7-name
  //table-best-row-7-duration
  //table-best-row-7-comments
  
  //table-best-row-8-name
  //table-best-row-8-duration
  //table-best-row-8-comments

  //table-best-row-9-name
  //table-best-row-9-duration
  //table-best-row-9-comments
}

function setStatisticsComponent(){
  getVaraByID((json)=> {
    //worst
    $('#statistics-wrost-title-1').html('Pior <br>desempenho')
    $('#statistics-wrost-value').html(json.worst_steps[0].origin)
    $('#statistics-wrost-position').html('19' + '° de 120 varas')
    //statistics-wrost-title-2
    //statistics-wrost-position

    //best
    $('#statistics-best-title-1').html('Melhor <br>desempenho')
    $('#statistics-best-value').html(json.best_steps[0].origin)
    //statistics-best-title-2
    //statistics-best-position

    //duration
    $('#statistics-duration-title-1').html('Duração da <br>baixa do processo')
    $('#statistics-duration-value').html(json.days_finish_process)
    //statistics-duration-title-2
    //statistics-duration-position

    //movements
    $('#statistics-moves-title-1').html('Movimentação <br>por processo')
    $('#statistics-moves-value').html(json.movements)
    //statistics-moves-title-2

    //finished
    $('#statistics-finished-title-1').html('Processos <br>julgados')
    $('#statistics-finished-value').html(json.finished_processes)
    //statistics-finished-title-2
    //statistics-finished-position
  })
}

function setFooterRankComponent() {
  // $('#best-time-1').html('')
  //best-time-2
  //best-time-3
  //best-time-4
  //best-time-5
  //best-time-6
  //best-time-7
  //best-time-8
  //best-time-9
  //best-time-10
}
