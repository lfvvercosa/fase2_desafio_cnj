var urlBase = 'http://backend-cnj-time4.herokuapp.com/api/v1/'

function getCourtList(){
  var locations = [
    ['Paulista', -7.9184546, -34.8209559, 1]
  ]
  return locations  
}

function getVaras() {
  var url = urlBase + 'varas'
  jQuery.get(url, (data)=>{
    console.log(data)
  });
}

function getVaraByID(vara_id, callback) {
  var url = urlBase + 'varas/' + vara_id
  jQuery.get(url, (data)=>{
    console.log(data)
    callback(data)
  });
}

function getBestVarasOnStep(step_id, vara_id, amount_of_varas, callback) {
  var url = urlBase + 'varas/bestVarasOnStep/?step_id=' + step_id + '&amount_of_varas=' + amount_of_varas + '&vara_id=' + vara_id
  jQuery.get(url, (data)=>{
    console.log(data)
    callback(data)
  });
}

function getBestVaras(vara_id, amount_of_varas, callback) {
  var url = urlBase + 'processes/bestVaras/?vara_id=' + vara_id + '&amount_of_varas=' + amount_of_varas
  jQuery.get(url, (data)=>{
    console.log(data)
    callback(data)
  });
}
