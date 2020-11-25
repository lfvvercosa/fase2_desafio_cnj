
var tempCourts = []

getVarasCallback((data)=>{
  tempCourts = data
  fillChooseCourtSelector(data)
})

function fillChooseCourtSelector(courts) {
  $('#varas_selector').html('<option value=""></option>')
  courts.forEach((court) => {
    $('#varas_selector').append('<option value="'+court.vara_id+'">'+court.name+'</option>')
  })
}

function login() {
  var user_name = $('#user_name')[0].value
  var selector = $('#varas_selector')[0]
  var id = selector.options[selector.selectedIndex].value
  var court =  tempCourts.find(c=>c.vara_id == id)
  user = {"court": JSON.stringify(court), "name": user_name}
  saveCache()
  var urlBase = window.location.href
  window.location = urlBase + 'index.html'
}