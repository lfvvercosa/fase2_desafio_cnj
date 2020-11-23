var selectableIds = [20, 34, 85]
var vara_id = -1
var comparing_id = -1
var courts = []
var court_details = undefined
var bestVarasOnStep = []
var groups = undefined
var selectedGroup = undefined

function changeId() {
  var number = Math.round(Math.random() * (selectableIds.length-1))
  vara_id = selectableIds[number]
  saveCache()
}

function saveCache() {
  window.localStorage.setItem('vara_id', vara_id);
  window.localStorage.setItem('comparing_id', comparing_id);
  window.localStorage.setItem('selectedGroup', selectedGroup);
  console.log('saving ' + selectedGroup )
}

function readCache() {
  vara_id = window.localStorage.getItem('vara_id')
  comparing_id = window.localStorage.getItem('comparing_id') 
  selectedGroup = window.localStorage.getItem('selectedGroup')
  console.log('read ' + selectedGroup )
}