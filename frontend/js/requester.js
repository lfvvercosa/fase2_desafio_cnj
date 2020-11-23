var urlBase = 'http://backend-cnj-time4.herokuapp.com/api/v1/'

function getCourtLocations(callback){
    getBestVaras(vara_id, 10, (json) => {
    var locations = [
        [json[0].name, json[0].latitude, json[0].longitude, 1],
        [json[1].name, json[1].latitude, json[1].longitude, 1],
        [json[2].name, json[2].latitude, json[2].longitude, 1],
        [json[3].name, json[3].latitude, json[3].longitude, 1],
        [json[4].name, json[4].latitude, json[4].longitude, 1],
        [json[5].name, json[5].latitude, json[5].longitude, 1],
        [json[6].name, json[6].latitude, json[6].longitude, 1],
        [json[7].name, json[7].latitude, json[7].longitude, 1],
        [json[8].name, json[8].latitude, json[8].longitude, 1],
        [json[9].name, json[9].latitude, json[9].longitude, 1]
        ]
    callback(locations)
    })
}

function getVaras() {
  if(courts.length > 0)
    return courts
  var url = urlBase + 'varas'
  jQuery.get(url, (data)=>{
    courts = data
  });
}

function getVaraByID(vara_id, callback) {
  if(court_details){
    callback(court_details)
    return
  }
  var url = urlBase + 'varas/' + vara_id
  jQuery.get(url, (data)=>{
    court_details = data
    callback(data)
  });
}

function getBestVarasOnStep(step_id, vara_id, amount_of_varas, callback) {
  var url = urlBase + 'varas/bestVarasOnStep/?step_id=' + step_id + '&amount_of_varas=' + amount_of_varas + '&vara_id=' + vara_id
  jQuery.get(url, (data)=>{
    bestVarasOnStep = data
    callback(data)
  });
}

function getBestVaras(vara_id, amount_of_varas, callback) {
  var url = urlBase + 'processes/bestVaras/?vara_id=' + vara_id + '&amount_of_varas=' + amount_of_varas
  jQuery.get(url, (data)=>{
    callback(data)
  });
}

function getGraphData(vara_id_1, vara_id_2, callback) {
  var url = urlBase + 'varas/' + vara_id_1 + '/compareGraphWith/' + vara_id_2 + '/1'
  jQuery.get(url, (data)=>{
    callback(data)
  });
}

function getGroups(callback) {
  var url = urlBase + 'grupos/'
  jQuery.get(url, (data)=>{
    callback(data)
  });
}

function getCourtsFromGroup(groupId, callback) {
  var url = urlBase + 'grupos/'+groupId
  jQuery.get(url, (data)=>{
    callback(data)
  });
}