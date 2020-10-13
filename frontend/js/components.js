function groupInfoWidth(word) {
  var width = 1.2 * word.length
  //console.log('width for '+word + ' = '+width+", len = "+word.length)
  return width
}

function setGroupInfoWidth(){
  var i, $infos = $('.rounded-info');
  for (i=0; i<$infos.length; i++)    {
    var word =  $infos.eq(i).html()
    var index = word.indexOf('>') + 1
    word = word.substr(index)
    index = word.indexOf('<')
    word = word.substr(0, index)
    var width = groupInfoWidth(word);
    $infos.eq(i).css("width", width + "rem")
  }
}

setGroupInfoWidth()