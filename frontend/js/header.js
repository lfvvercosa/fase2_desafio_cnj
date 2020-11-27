readCache()
setHeaderComponent()

function setHeaderComponent() {
  
  getVaraByID(vara_id, (json)=>{
    //position
    $('#position-number').html(json.ranking+'ª')
    
    //court-name
    $('#court-name').html(json.name)
    
    //user
    $('#username').text('Antônio')
    $('#user-position').text('juiz/Desembargador')

    //group
    $('#group-amount').text('GRUPO ('+json.group.amount_of_varas+' órgãos)')
  })
  $('#group-el-1').text('Justiça Estadual')
  $('#group-el-2').text('1° Grau')
  $('#group-el-3').text('Execução Fiscal')

  $('#medal').hover(function(){
    // $('#position-number').html('Mudar aa Vara')
    $('#position-number').addClass('mudar-vara')
    $('.position-text').html('Mudar de vara')
  }, function(){
    $('#position-number').html(court_details.ranking+'ª')
    // $('#position-number').css('font-size', '3rem')
    $('.position-text').html('colocada')
  }) 
};