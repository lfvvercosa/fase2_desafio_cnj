sigma.canvas.nodes.square = function(node, context, settings) {

  var prefix = settings('prefix') || '',
      size = node[prefix + 'size']

  var width = size * 2//1.7*size
  var height = size * 2//size/2.8

  var gradient = context.createLinearGradient(
    node[prefix+'x'] - size,
    node[prefix+'y'] - height/8,
    node[prefix+'x'] - size,
    node[prefix+'y'] + height/4)
  
  gradient.addColorStop(0, "white")
  gradient.addColorStop(0.3, "#CDCDCD")
  gradient.addColorStop(0.6, "#A9A9A9")
  gradient.addColorStop(1, "#A9A9A9")
  
  context.fillStyle = gradient
  
  context.beginPath()
  context.fillRect(
    node[prefix + 'x'] - size,
    node[prefix + 'y'] - height/8,
    width,
    height/4    
  )
  context.closePath()

  context.fillStyle = "#0C0C0C"

  context.beginPath()
  context.strokeRect(
    node[prefix + 'x'] - size,
    node[prefix + 'y'] - height/8,
    width,
    height/4)
  context.closePath() 

  /* context.fillStyle = "#000000"
  context.beginPath()
  context.arc(node[prefix + 'x'], node[prefix + 'y'], size, 0, 2 * Math.PI)
  context.stroke()
  context.closePath() */
}

/**
 * This example shows how to use the dragNodes plugin.
 */
var i,
    s,
    N = 10,
    g = {
      nodes: [],
      edges: []
    },
    layers = [],
    drawnNodesAtLayer = []
    height = 600,
    width = 800

generateGraph()
//generateTestCase1Graph()

createGraphViewStructure()

setEdgeType()

function generateGraph(){
  for (i = 0; i < N; i++){
    g.nodes.push({
      id: 'n'+i,
      label: 'Node ' + i,
      size: 40,
      type: 'square',
      color: 'red',
      children: [],
      parents: []
    })
  }
  generateRandomEdges()
  generateRandomEdges()
  generateRandomEdges()
  generateRandomEdges()
 
  
  //broken node = [{"id":"n0","label":"Node 0","size":40,"type":"square","color":"red","children":["n0","n5","n7"],"parents":["n5","n7","n1","n2","n8"]},{"id":"n1","label":"Node 1","size":40,"type":"square","color":"red","children":["n2","n0","n4","n3"],"parents":["n3"]},{"id":"n2","label":"Node 2","size":40,"type":"square","color":"red","children":["n7","n6","n0"],"parents":["n1","n6","n8","n5"]},{"id":"n3","label":"Node 3","size":40,"type":"square","color":"red","children":["n1","n7","n9","n3"],"parents":["n8","n9","n1"]},{"id":"n4","label":"Node 4","size":40,"type":"square","color":"red","children":["n6","n4","n8"],"parents":["n1"]},{"id":"n5","label":"Node 5","size":40,"type":"square","color":"red","children":["n0","n8","n2"],"parents":["n0"]},{"id":"n6","label":"Node 6","size":40,"type":"square","color":"red","children":["n2","n7","n8"],"parents":["n4","n9","n2","n7"]},{"id":"n7","label":"Node 7","size":40,"type":"square","color":"red","children":["n0","n6","n8"],"parents":["n2","n3","n6","n0"]},{"id":"n8","label":"Node 8","size":40,"type":"square","color":"red","children":["n2","n3","n0"],"parents":["n5","n4","n6","n7","n9"]},{"id":"n9","label":"Node 9","size":40,"type":"square","color":"red","children":["n6","n3","n8"],"parents":["n3"]}]
  //[{"id":"e-n0-n0","source":"n0","target":"n0","size":5.36674513647357,"color":"#000"},{"id":"e-n1-n2","source":"n1","target":"n2","size":3.283332705241677,"color":"#000"},{"id":"e-n2-n7","source":"n2","target":"n7","size":3.4209068818058883,"color":"#000"},{"id":"e-n3-n1","source":"n3","target":"n1","size":4.130794509500693,"color":"#000"},{"id":"e-n4-n6","source":"n4","target":"n6","size":2.618481295276987,"color":"#000"},{"id":"e-n5-n0","source":"n5","target":"n0","size":1.7906118749470918,"color":"#000"},{"id":"e-n6-n2","source":"n6","target":"n2","size":3.6554965125178116,"color":"#000"},{"id":"e-n7-n0","source":"n7","target":"n0","size":2.354865893594022,"color":"#000"},{"id":"e-n8-n2","source":"n8","target":"n2","size":4.670776276999969,"color":"#000"},{"id":"e-n9-n6","source":"n9","target":"n6","size":1.8528683076469754,"color":"#000"},{"id":"e-n0-n5","source":"n0","target":"n5","size":2.9325531795726922,"color":"#000"},{"id":"e-n1-n0","source":"n1","target":"n0","size":4.947646403845339,"color":"#000"},{"id":"e-n2-n6","source":"n2","target":"n6","size":4.053707074838904,"color":"#000"},{"id":"e-n3-n7","source":"n3","target":"n7","size":3.8107237684010444,"color":"#000"},{"id":"e-n4-n4","source":"n4","target":"n4","size":1.8286256754965349,"color":"#000"},{"id":"e-n5-n8","source":"n5","target":"n8","size":3.6918398202707756,"color":"#000"},{"id":"e-n6-n7","source":"n6","target":"n7","size":1.6229397222545145,"color":"#000"},{"id":"e-n7-n6","source":"n7","target":"n6","size":3.368027124341065,"color":"#000"},{"id":"e-n8-n3","source":"n8","target":"n3","size":3.365067156477072,"color":"#000"},{"id":"e-n9-n3","source":"n9","target":"n3","size":3.6918915116961086,"color":"#000"},{"id":"e-n1-n4","source":"n1","target":"n4","size":3.3108065277548526,"color":"#000"},{"id":"e-n2-n0","source":"n2","target":"n0","size":5.447234407775295,"color":"#000"},{"id":"e-n3-n9","source":"n3","target":"n9","size":5.182598535561795,"color":"#000"},{"id":"e-n0-n7","source":"n0","target":"n7","size":4.473886160732618,"color":"#000"},{"id":"e-n1-n3","source":"n1","target":"n3","size":3.168591828455705,"color":"#000"},{"id":"e-n3-n3","source":"n3","target":"n3","size":2.7119096384330312,"color":"#000"},{"id":"e-n4-n8","source":"n4","target":"n8","size":1.885269902505696,"color":"#000"},{"id":"e-n5-n2","source":"n5","target":"n2","size":2.839181431546505,"color":"#000"},{"id":"e-n6-n8","source":"n6","target":"n8","size":2.6555245164012895,"color":"#000"},{"id":"e-n7-n8","source":"n7","target":"n8","size":5.185362937585698,"color":"#000"},{"id":"e-n8-n0","source":"n8","target":"n0","size":1.9088215714685521,"color":"#000"},{"id":"e-n9-n8","source":"n9","target":"n8","size":1.9957098297673497,"color":"#000"}]

  //g.nodes.forEach(n=>console.log(n.id+" - "+n.children))
  //g.edges.forEach(e=>console.log(e.id))
  //console.log('graph: - '+JSON.stringify(g.nodes))
  //console.log('edges - '+JSON.stringify(g.edges))
}

function generateRandomEdges(){
  g.nodes.forEach(n=>{
    var source = n.id
    var target = getRandomTarget(N, source)
    if(target && !n.children.includes(target)){
      var sNode = getNode(source)
      var tNode = getNode(target)
      sNode.children.push(target)
      if(source != target){
        //console.log('parents of '+target+' before = '+tNode.parents)
        tNode.parents.concat(sNode.parents)
        tNode.parents.push(source)
        //console.log('parents of ' + target + ' = '+tNode.parents)
      }
      g.edges.push({
        id: 'e-' + source+"-"+target,
        source: source,
        target: target,
        size: 1.5 + 4*(Math.random()),
        color: '#000'
      })
    }
  });
}

function getNode(id){
  return g.nodes.find(n=>n.id == id)
}

function setLayers(){
  var root = 'n'+0
  var rootNode = getNode(root)
  rootNode.layer = 0;
  rootNode.label += '-'+rootNode.layer
  var nextNodes = [root]
  while(nextNodes.length > 0){
    var current = getNode(nextNodes.pop())
    current.children.forEach(c=>{
        var child = getNode(c)
        if(child.layer == undefined || (child.layer > current.layer+1/*  && !current.parents.includes(child.id) */)){
          ////console.log('setting layer for '+child.id + ', current.layer is '+current.layer)
          child.layer = current.layer+1
          child.label+= '-'+child.layer
          nextNodes.push(c)
        }
    })
  }
}

function mapLayers(){
  var root = 'n'+0
  var rootNode = getNode(root)
  var visitedNodes = [root]
  var nextNodes = [root]
  while(nextNodes.length > 0){
    var current = getNode(nextNodes.pop())
    visitedNodes.push(current.id)
    if(!layers[current.layer]){
      layers[current.layer] = 1
    }
    else{
      layers[current.layer] += 1
    }
    nextNodes = nextNodes.concat(current.children
    .filter(c=>!visitedNodes.includes(c) && !nextNodes.includes(c)))
  }

  drawnNodesAtLayer = new Array(layers.length)
  for(var i=0; i<drawnNodesAtLayer.length;i++)
    drawnNodesAtLayer[i] = 0

  //for(var i=0; i<layers.length; i++)
    //console.log("mapLyers: "+i+" - "+layers[i])
}

function setHorizontalCount(node, visited){
  visited.push(node.id)
  //console.log('marking '+node.id+" as visited")
  var hCount = 0
  node.children.forEach(c=>{
    if(!visited.includes(c) && getNode(c).layer == node.layer+1){
      //console.log('calling setHorizontalCount for child '+c)
      hCount+=setHorizontalCount(getNode(c), visited)
    }
  })
  if(hCount == 0)
    node.horizontalCount = 1
  else
    node.horizontalCount = hCount
  //console.log('hCount of '+node.id+" is "+node.horizontalCount)
  return node.horizontalCount
}

function createGraphViewStructure(){

  //console.log("setLayers")
  setLayers()
  //console.log("mapLayers")
  mapLayers()
  //console.log("createGraphViewStructure")

  var root = 'n'+0
  var rootNode = getNode(root)
  setHorizontalCount(rootNode, [])

  var squareWidth = 0.15
  var elementsSpace = squareWidth/4
  var rootPositionX = 0.5

  setNodePosition(rootNode, null, 0, squareWidth, elementsSpace, rootPositionX)
  
  var nextNodes = [root]
  var visitedNodes = [root]
  var currentLayer = 0
  
  do {
    var nextIndex = nextNodes.find(n=> n!= undefined && getNode(n).layer==currentLayer)
    var current = nextIndex != undefined ? getNode(nextIndex) : undefined
    if(!current){
      currentLayer++
      if(currentLayer  == layers.length)
        break
      continue
    }
    //console.log('nextIndex = '+nextIndex.substr(1)+", current = "+JSON.stringify(current))
    var childPos = 0
    var childDrawn = 0
    current.children.forEach(c => {
      var cNode = getNode(c)
      if(!visitedNodes.includes(c) && cNode.layer == current.layer+1){
        setNodePosition(cNode, current, childPos, squareWidth, elementsSpace, rootPositionX)
        nextNodes.push(c)
        visitedNodes.push(c)
        childPos++
        childDrawn++
        drawnNodesAtLayer[current.layer+1]+=cNode.horizontalCount
      }
    })
    delete(nextNodes[nextNodes.indexOf(nextIndex)])
  } while(nextNodes.length > 0 && currentLayer < layers.length)
}

function setEdgeType(){
  g.edges.forEach(e => {
    if(!e.type)
      e.type = getEdgeType(getNode(e.source), getNode(e.target))
  })
}

function setNodePosition(node, parent, pos, squareWidth, elementsSpace, rootPositionX){
  if(!node.x || !node.y){
    var rowHeight = 0.35
    if(node.id == 'n'+0){
      node.x = rootPositionX
    }
    else if(parent.horizontalCount == 1)
      node.x = parent.x
    else{
      var totalParentSpace = parent.horizontalCount * (squareWidth + elementsSpace)
      var start = parent.x + squareWidth/2 - totalParentSpace/2
      var nodesInThisLayerForThisParent = parent.children.filter(c=>getNode(c).layer == node.layer).length
      var step = totalParentSpace / nodesInThisLayerForThisParent
      //console.log("step = "+step)
      node.x = start + pos * step
    }
    node.y = node.layer*(rowHeight)
    //console.log("setNodePosition: nodeId = "+node.id+", horizontalCount = "+node.horizontalCount
    //+", totalParentSpace = "+totalParentSpace+", start = "+start+", pos = "+pos
    //+", drawn at layer "+(node.layer)+" = "+drawnNodesAtLayer[node.layer])
    
  }
}

function getRandomTarget(n, source){
  var t = n+'0'
  var tries = 0
  var maxTries = 10 
  while(t == n+'0' && !getNode(source).children.includes(t) && tries < maxTries){
    t = 'n'+(Math.random() * n | 0)
    tries++
  }
  return t == 0 ? undefined : t
}

function getEdgeType(source, target){
  ////console.log("getEdgeType: source = "+source.id+", position = "+source['x']+","+source['y'])
  ////console.log('target position = '+target['x']+","+target['y'])
  var linear = false
  var edgeType = linear ? 'arrow' : 'curvedArrow'
  if(linear){

  }
  else{

  }
  return edgeType
}

// Instantiate sigma left:
sLeft = new sigma({
  graph: g,
  container: 'graph-container-left',
  renderers: [
    {
      container: document.getElementById('graph-container-left'),
      type: 'canvas' // sigma.renderers.canvas works as well
    }
  ],
  settings: {
    edgeLabelSize: 'proportional',
    batchEdgesDrawing: true,
    maxEdgeSize: 4,
    maxNodeSize: 60,
    nodesPowRatio: 0,
    edgesPowRatio: 0,
    zoomingRatio: 1,
    labelSize: ""
  }
})

// Instantiate sigma right:
sRight = new sigma({
  graph: g,
  container: 'graph-container-right',
  renderers: [
    {
      container: document.getElementById('graph-container-right'),
      type: 'canvas' // sigma.renderers.canvas works as well
    }
  ],
  settings: {
    edgeLabelSize: 'proportional',
    batchEdgesDrawing: true,
    maxEdgeSize: 4,
    maxNodeSize: 60,
    nodesPowRatio: 0,
    edgesPowRatio: 0,
    zoomingRatio: 1,
    labelSize: ""
  }
})


// Initialize the dragNodes plugin:
var dragListener = sigma.plugins.dragNodes(sLeft, sLeft.renderers[0])

var dragListener = sigma.plugins.dragNodes(sRight, sRight.renderers[0])