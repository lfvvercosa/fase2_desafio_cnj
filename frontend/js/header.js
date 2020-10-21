setHeaderComponent()

function setHeaderComponent() {
  
  getVaraByID(vara_id, (json)=>{
    //position
    $('#position-number').html(json.ranking+'ª')
    
    //court-name
    $('#court-name').html(json.name)
    
    //user
    $('#username').text('ANTONIO')
    $('#user-position').text('juiz/Desembargador')

    //group
    $('#group-amount').text('GRUPO ('+json.group.amount_of_varas+' órgãos)')
  })
  $('#group-el-1').text('Justiça Estadual')
  $('#group-el-2').text('1° Grau')
  $('#group-el-3').text('Execução Fiscal')
}
