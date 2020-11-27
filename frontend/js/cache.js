var vara_id = -1
var comparing_id = -1
var courts = []
var court_details = undefined
var bestVarasOnStep = []
var groups = undefined
var selectedGroup = {}
var user = {}

function saveCache() {
  window.localStorage.setItem('vara_id', vara_id);
  window.localStorage.setItem('comparing_id', comparing_id);
  window.localStorage.setItem('selectedGroup', JSON.stringify(selectedGroup));
  window.localStorage.setItem('user', JSON.stringify(user))
}

function readCache() {
  vara_id = window.localStorage.getItem('vara_id')
  comparing_id = window.localStorage.getItem('comparing_id') 
  selectedGroup = JSON.parse(window.localStorage.getItem('selectedGroup'))
  user = JSON.parse(window.localStorage.getItem('user'))
}