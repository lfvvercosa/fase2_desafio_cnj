readCache()
console.log(user)
setRankComponent($('#toggle-switch'))
setStatisticsComponent()

var comment = {}

function getStepName(step){
  if(step == "Outros"){
    return "Apreciação inicial"
  }else{
    return step
  }
}

function setRankComponent(checkBox) {
  var isBottleNeck = checkBox == undefined || checkBox.checked == undefined || checkBox.checked
  getVaraByID(vara_id, (json) => {
    var i = 0
    var steps = isBottleNeck ? json.worst_steps : json.best_steps

    document.title = json.name

    $('#vara_name').html(json.name)
    $('#vara_name2').html(json.name)
    $('#court_name').html(json.tribunal)
    $('#court_name2').html(json.tribunal)
    $('#group_name').html(selectedGroup.group_name)
    $('#court_rank').html(json.ranking)
    $('#comment_title').html('Que legal! Adicionar um comentário construtivo faz parte das boas práticas do CNJ')

    var container = $('.diagnosis').html('')

    if (!isBottleNeck) {
      container.removeClass('diagnosis-gargalos')
      container.addClass('diagnosis-destaques')
    }
    else {
      container.removeClass('diagnosis-destaques')
      container.addClass('diagnosis-gargalos')
    }

    steps.forEach(step => {
      //console.log(step)
      var origin = getStepName(step.origin)
      var destination = getStepName(step.destination)
      var time = step.med_time + ' dias'
      var position = step.ranking
      var frequency = step.frequency
      var container = $('.diagnosis')
      //button
      container.append('<button id= "button_' + i + '" class="btn-tramitacao" type="button" data-toggle="collapse" data-target="#diagnostico_' + i + '" aria-expanded="false" aria-controls="diagnostico_' + i + '" />')
      container = $('#button_' + i)
      container.append('<div id="table-responsive_' + i + '" class="table-responsive">')
      container = $('#table-responsive_' + i)
      container.append('<table id="diagnosis-table_' + i + '" class="diagnosis-table">')
      container = $('#diagnosis-table_' + i)
      container.append('<tr id="row_' + i + '">')
      container = $('#row_' + i)
      container.append('<td class="origin" id="origin_' + i + '"><i class="fas ' + getIcon(origin) + '"></i>')
      container = $('#origin_' + i)
      container.append('<p class="mb-0">' + origin + '</p>')
      container = $('#row_' + i)
      container.append('<td class="arrow"><i class="fas fa-long-arrow-alt-right"></i></td>')
      container.append('<td class="destination" id="destination_' + i + '"><i class="fas ' + getIcon(destination) + '"></i>')
      container = $('#destination_' + i)
      container.append('<p class="m-0">' + destination + '</p>')
      container = $('#row_' + i)
      container.append('<td class="time" id="time_' + i + '">')
      container = $('#time_' + i)
      container.append('<p class="m-0"><strong>' + time + '</strong><br>Duração</p>')
      container = $('#row_' + i)
      container.append('<td class="position" id="position_' + i + '"><strong>' + position + 'º</strong><br>Posição')
      container = $('#position_' + i)
      container.append('<small id="small_' + i + '">')
      cotainer = $('#small_' + i)
      container.append('<span data-toggle="popover" title="Popover title" data-content="And heres some amazing content. Its very engaging. Right?">')
      container.append('<i class="fas fa-info-circle" style="font-size: 1rem">')
      container = $('#row_' + i)
      container.append('<td class="occurrences" id="occurrences_' + i + '">')
      container = $('#occurrences_' + i)
      container.append('<p class="m-0"><strong>'+frequency+'</strong><br>Ocorrêcias</p>')
      container = $('#row_' + i)
      container.append('<td class="chevron"><i class="fas fa-chevron-up"></i></td>')

      //comments

      container = $('.diagnosis')
      container.append('<div class="collapse" id="diagnostico_' + i + '">')
      container = $('#diagnostico_' + i)
      container.append('<div id="diagnosis-comments-div_' + i + '" class="diagnosis-comments">')
      container = $('#diagnosis-comments-div_' + i)
      container.append('<table class="text-center" id="diagnosis-comments_' + i + '">')
      container = $('#diagnosis-comments_' + i)
      container.append('<thead id="thread_' + i + '">')
      container = $('#thread_' + i)
      container.append('<tr id="diagnosis-comments-title_' + i + '">')
      container = $('#diagnosis-comments-title_' + i)
      container.append('<th style="width: 50%">Comentário mais curtido</th>')
      container.append('<th style="width: 30%">Unidade Judiciária </th>')
      container.append('<th style="width: 15%;">Duração</th>')
      container.append('<th style="width: 5%;">Comentar</th>')
      container = $('#diagnosis-comments_' + i)
      container.append('<tbody id="tbody-comments_' + i + '">')
      loadComments(i, container, step)
      i++
    })
  })
}

function loadComments(i, container, step) {
  getBestVarasOnStep(step.step_id,
    vara_id,
    3,
    (json2) => {
      bestVarasOnStep = json2
      for (var j = 0; j < bestVarasOnStep.length; j++) {
        container = $('#tbody-comments_' + i)
        container.append('<tr id="comment_' + i + '_' + j + '">')
        container = $('#comment_' + i + '_' + j)
        container.append('<td id="td_comment_' + i + '_' + j + '">')
        container = $('#td_comment_' + i + '_' + j)
        container.append('<div id="comment_text_' + i + '_' + j + '">')
        container = $('#comment_text_' + i + '_' + j)
        container.append('<p>' + bestVarasOnStep[j].comment)
        container = $('#comment_' + i + '_' + j)
        container.append('<td id="name_' + i + '_' + j + '">')
        container = $('#name_' + i + '_' + j)
        container.append('<span>' + bestVarasOnStep[j].vara_name + '</span>')
        container = $('#comment_' + i + '_' + j)
        container.append('<td class="text-center">' + bestVarasOnStep[j].med_time + ' dias</td>')
        container = $('#comment_'+i+'_'+j)
        container.append('<td id="insert_comment_'+i+'_'+j+'" ><button class="modal-button modal-button-comment" type="button" data-toggle="tooltip" title="Responder ao comentário"><span id="'+step.step_id+';'+bestVarasOnStep[j].vara_id+ ';'+bestVarasOnStep[j].vara_name +'" onclick="configPopup(this)" data-toggle="modal" data-target="#comment-replay"><i  class="fas fa-comments"></i></span></button>')
        container = $('#insert_comment_'+i+'_'+j)

        container = $('#comment_' + i + '_' + j)
        container.vara_id = bestVarasOnStep[j].vara_id
      }
    })
}

function setStatisticsComponent() {
  getVaraByID(vara_id, (json) => {
    //worst
    $('#statistics-wrost-title-1').html('Etapa com  <br/>pior desempenho')
    $('#statistics-wrost-value').html(getStepName(json.worst_steps[0].origin))
    $('#statistics-wrost-position').html('1' + '° de ' + json.group.amount_of_varas + ' varas')
    //statistics-wrost-title-2

    //best
    $('#statistics-best-title-1').html('Etapa com <br/> melhor desempenho')
    $('#statistics-best-value').html(getStepName(json.best_steps[0].origin))
    $('#statistics-best-position').html('1' + '° de ' + json.group.amount_of_varas + ' varas')
    //statistics-best-title-2

    //duration
    $('#statistics-duration-title-1').html('Tempo para Baixa do Processo')
    $('#statistics-duration-value').html(json.days_finish_process + ' dias')
    // $('#statistics-duration-position').html('1' + '° de ' + json.group.amount_of_varas + ' varas')
    //statistics-duration-title-2

    //movements
    $('#statistics-moves-title-1').html('Movimentações por processo')
    $('#statistics-moves-value').html(json.movements)
    //statistics-moves-title-2

    //finished
    $('#statistics-finished-title-1').html('Processos <br>julgados')
    $('#statistics-finished-value').html(json.finished_processes)
    $('#statistics-finished-position').html('1' + '° de ' + json.group.amount_of_varas + ' varas')
    //statistics-finished-title-2
  })
}

function getIcon(origin) {
  var movements = ['Distribuição','Conclusão','Despacho','Decisão','Julgamento','Trânsito em julgado','Baixa/Arquivamento', 'Audiência', 'Citação', 'Outros']
  switch(origin){
    case movements[0] : return 'fa-expand-arrows-alt'
    case movements[1] : return 'fa-check-circle'
    case movements[2] : return 'fa-pen-fancy'
    case movements[3] : return 'fa-brain'
    case movements[4] : return 'fa-balance-scale'
    case movements[5] : return 'fa-sign-out-alt'
    case movements[6] : return 'fa-gavel'
    case movements[7] : return 'fa-users'
    case movements[8] : return 'fa-quote-right'
    case movements[9] : return 'fa-users'
  }
}

function send() {
  var commentBody = $('#comment-body')[0].value
  comment.comment = ""+commentBody
  console.log(comment)
  postComment(comment)
  $('#comment-replay').modal('hide')
}

function configPopup(e) {
  console.log(e)
  console.log(e.id)
  var info = e.id.split(';')
  console.log(user)
  var c = JSON.parse(user.court)
  comment = {vara_id: c.vara_id, step_id: info[0], comment: ''}
  console.log(comment)
  $('#user_name').html(user.name)
  $('#vara_name3').html(c.name)
  $('#vara_name4').html(c.name)
}
