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

function getVaraByID(callback) {
  var id = 1
  var url = urlBase + 'varas/' + id
  jQuery.get(url, (data)=>{
    console.log(data)
    callback(data)
  });
}

