readCache()
setRankComponent($('#toggle-switch'))
setStatisticsComponent()
setFooterRankComponent()

function setRankComponent(checkBox) {
  var isBottleNeck = !checkBox.checked
  getVaraByID(vara_id, (json)=>{
    var i = 0
    var steps = isBottleNeck ? json.worst_steps : json.best_steps
    var container =  $('.diagnosis').html('')
      
    if(!isBottleNeck){
      container.removeClass('diagnosis-gargalos')
      container.addClass('diagnosis-destaques')
    }
    else {
      container.removeClass('diagnosis-destaques')
      container.addClass('diagnosis-gargalos')
    }
    
    steps.forEach(step =>{
      //console.log(step)
      var origin = step.origin
      var destination = step.destination
      var time = step.med_time + ' dias'
      var position = step.ranking
      var container = $('.diagnosis')
      //button
      container.append('<button id= "button_'+i+'" class="btn-header" type="button" data-toggle="collapse" data-target="#diagnostico_'+i+'" aria-expanded="false" aria-controls="diagnostico_'+i+'" />')
      container = $('#button_'+i)
      container.append('<div id="table-responsive_'+i+'" class="table-responsive">')
      container = $('#table-responsive_'+i)
      container.append('<table id="diagnosis-table_'+i+'" class="diagnosis-table">')
      container = $('#diagnosis-table_'+i)
      container.append('<tr id="row_'+i+'">')
      container = $('#row_'+i)
      container.append('<td id="origin_'+i+'"><i class="fas '+'fa-users'+'"></i>')
      container = $('#origin_'+i)
      container.append('<p class="mb-0">'+origin+'</p>')
      container = $('#row_'+i)
      container.append('<td class="arrow"><i class="fas fa-long-arrow-alt-right"></i></td>')
      container.append('<td id="destination_'+i+'"><i class="fas '+'fa-balance-scale'+'"></i>')
      container = $('#destination_'+i)
      container.append('<p class="m-0">'+destination+'</p>')
      container = $('#row_'+i)
      container.append('<td id="time_'+i+'">')
      container = $('#time_'+i)
      container.append('<p class="m-0"><strong>'+time+'</strong><br>Duração</p>')
      container = $('#row_'+i)
      container.append('<td id="position_'+i+'"><strong>'+position+'º</strong><br>Posição')
      container = $('#position_'+i)
      container.append('<small id="small_'+i+'">')
      cotainer = $('#small_'+i)
      container.append('<span data-toggle="popover" title="Popover title" data-content="And heres some amazing content. Its very engaging. Right?">')
      container.append('<i class="fas fa-info-circle" style="font-size: 1rem">')
      container = $('#row_'+i)
      container.append('<td id="occurrences_'+i+'">')
      container = $('#occurrences_'+i)
      container.append('<p class="m-0"><strong>'+65+'</strong><br>Ocorrêcias</p>')
      container = $('#row_'+i)
      container.append('<td class="chevron"><i class="fas fa-chevron-up"></i></td>')

      //comments

      container = $('.diagnosis')
      container.append('<div class="collapse" id="diagnostico_'+i+'">')
      container = $('#diagnostico_'+i)
      container.append('<div id="diagnosis-comments-div_'+i+'" class="diagnosis-comments">')
      container = $('#diagnosis-comments-div_'+i)
      container.append('<table id="diagnosis-comments_'+i+'">')
      container = $('#diagnosis-comments_'+i)
      container.append('<thead id="thread_'+i+'">')
      container = $('#thread_'+i)
      container.append('<tr id="diagnosis-comments-title_'+i+'">')
      container = $('#diagnosis-comments-title_'+i)
      container.append('<th>Comentário mais curtido</th>')
      container.append('<th style="min-width: 200px;">Unidade jurídico </th>')
      container.append('<th style="min-width: 100px;">Duração</th>')
      container = $('#diagnosis-comments_'+i)
      container.append('<tbody id="tbody-comments_'+i+'">')
      loadComments(i, container, step)  
      i++
    })
  })
}

function loadComments(i, container, step) {
  getBestVarasOnStep(step.step_id,
    vara_id,
    3,
    (json2)=>{
      //console.log(json2.slice(0,3))
      bestVarasOnStep = json2.slice(0.3)
      for(var j=0; j < bestVarasOnStep.length; j++){
        container = $('#tbody-comments_'+i)
        container.append('<tr id="comment_'+i+'_'+j+'">')
        container = $('#comment_'+i+'_'+j)
        container.append('<td id="td_comment_'+i+'_'+j+'">')
        container = $('#td_comment_'+i+'_'+j)
        container.append('<div id="comment_text_'+i+'_'+j+'" class="w-100">')
        container = $('#comment_text_'+i+'_'+j)
        container.append('<p>'+bestVarasOnStep[j].comment)
        container = $('#comment_'+i+'_'+j)
        container.append('<td id="name_'+i+'_'+j+'">')
        container = $('#name_'+i+'_'+j)
        container.append('<span>'+bestVarasOnStep[j].vara_name+'</span>')
        container = $('#comment_'+i+'_'+j)
        container.append('<td class="text-center">'+bestVarasOnStep[j].med_time+' dias</td>')
        //container = $('#comment_'+i+'_'+j)
        //container.append('<td id="like_'+i+'_'+j+'" >')
        //container = $('$#like_'+i+'_'+j)
        
        container = $('#comment_'+i+'_'+j)
        container.vara_id = bestVarasOnStep[j].vara_id
        /* container.click(function(e){
          comparing_id = e.currentTarget.vara_id
          saveCache()
          window.location.replace("http://desafio-cnj-frontend.herokuapp.com/pages/comparing-courts.html");
        }) */
      }
    })
                /*<td>
                  <button class="ranking-like" type="button">
                    <input id="toggle-heart-1" type="checkbox" />
                    <label for="toggle-heart-1">
                      <i class="far fa-heart heart-empty"></i>
                      <i class="fas fa-heart heart-full"></i>
                    </label>
                  </button>
                  <small class="d-block text-truncate"> 12 curtidas</small>

                </td>
                <td>
                  <button class="ranking-chat">
                    <input id="toggle-comment-1" type="checkbox" />
                    <label for="toggle-comment-1">

                      <i class="far fa-comments comments-empty"></i>
                      <i class="fas fa-comments comments-full"></i>
                    </label>
                  </button>
                  <small class="d-block text-truncate"> 12 respostas</small>

                </td>

              </tr>
              
            </tbody>
          </table>
        </div>
      </div> */
}

function setBestRankComponent() {
  
  getVaraByID(vara_id,(json)=>{
    //best movements component
    $('#best-mov-1-source').html(json.best_steps[0].origin)
    $('#best-mov-1-description').html(json.best_steps[0].med_time + ' dias')
    $('#best-mov-1-dest').html(json.best_steps[0].destination)
    $('#best-mov-1-position').html(json.best_steps[0].ranking+'°')

    $('#best-mov-2-source').html(json.best_steps[1].origin)
    $('#best-mov-2-description').html(json.best_steps[1].med_time + ' dias')
    $('#best-mov-2-dest').html(json.best_steps[1].destination)
    $('#best-mov-2-position').html(json.best_steps[1].ranking+'°')

    $('#best-mov-3-source').html(json.best_steps[2].origin)
    $('#best-mov-3-description').html(json.best_steps[2].med_time + ' dias')
    $('#best-mov-3-dest').html(json.best_steps[2].destination)
    $('#best-mov-3-position').html(json.best_steps[2].ranking+'°')

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
    $('#statistics-duration-title-1').html('Baixa do processo')
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