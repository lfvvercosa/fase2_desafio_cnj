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
}

var i,
    g = {
      nodes: [],
      edges: []
    },
    layers = [],
    drawnNodesAtLayer = []
    root = undefined

getGraphData(42, 43, generateGraph)

function generateGraph(data){

  var edgesGraphLeft = data[0].arestas

  for (i = 0; i < edgesGraphLeft.length; i++){
    var edge = edgesGraphLeft[i]
    if(!getNode(edge.origem)){
      g.nodes.push({
        id: edge.origem,
        label: edge.origem,
        size: 40,
        type: 'square',
        color: 'red',
        children: [],
        parents: []
      })
      if(edge.origem == data[0].root){
        root = edge.origem
        //console.log('root is '+root + "("+edge.origem+")")
      }
      //console.log(edge.origem)
    }
    if(!getNode(edge.destino)){
      g.nodes.push({
        id: edge.destino,
        label: edge.destino,
        size: 40,
        type: 'square',
        color: 'red',
        children: [],
        parents: []
      })
      if(edge.destino == data[0].root){
        root = edge.destino
        //console.log('root is '+root + "("+edge.destino+")")
      }
      //console.log(edge.destino)
    }
  }

  for (i = 0; i < edgesGraphLeft.length; i++){
    var edge = edgesGraphLeft[i]
    g.edges.push({
      id: 'e-' + edge.origem+"-"+edge.destino,
      source: edge.origem,
      target: edge.destino,
      size: 1.5 + 4*(Math.random()),
      color: '#000'
    })
    var sNode = getNode(edge.origem)
    var tNode = getNode(edge.destino)
    sNode.children.push(edge.destino)
    if(edge.origem != edge.destino){
      //console.log('parents of '+target+' before = '+tNode.parents)
      tNode.parents.concat(sNode.parents)
      tNode.parents.push(edge.origem)
      //console.log('parents of ' + target + ' = '+tNode.parents)
    }
    //console.log(edge.origem+"-"+edge.destino) 
  }

  createGraphViewStructure()

  setEdgeType()

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
      maxNodeSize: 50,
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
      maxNodeSize: 50,
      nodesPowRatio: 0,
      edgesPowRatio: 0,
      zoomingRatio: 1,
      labelSize: ""
    }
  })

  // Initialize the dragNodes plugin:
  sigma.plugins.dragNodes(sLeft, sLeft.renderers[0])

  sigma.plugins.dragNodes(sRight, sRight.renderers[0])

  /* var noverlapListenerLeft = sLeft.configNoverlap({
    nodeMargin: 0.1,
    scaleNodes: 1.05,
    gridSize: 75,
    easing: 'quadraticInOut', // animation transition function
    duration: 10   // animation duration. Long here for the purposes of this example only
  });

  var noverlapListenerRight = sRight.configNoverlap({
    nodeMargin: 0.1,
    scaleNodes: 1.05,
    gridSize: 75,
    easing: 'quadraticInOut', // animation transition function
    duration: 10  // animation duration. Long here for the purposes of this example only
  }); */

  // Start the layout:
  //sLeft.startNoverlap();
  //sRight.startNoverlap();
  

  function getNode(id){
    return g.nodes.find(n=>n.id == id)
  }

  function setLayers(){
    var rootNode = getNode(root)
    rootNode.layer = 0;
    //rootNode.label += '-'+rootNode.layer
    var nextNodes = [root]
    while(nextNodes.length > 0){
      var next = nextNodes.pop()
      var current = getNode(next)
      current.children.forEach(c=>{
          var child = getNode(c)
          if(child.layer == undefined || (child.layer > current.layer+1/*  && !current.parents.includes(child.id) */)){
            ////console.log('setting layer for '+child.id + ', current.layer is '+current.layer)
            child.layer = current.layer+1
            //child.label+= '-'+child.layer
            nextNodes.push(c)
          }
      })
    }
  }

  function mapLayers(){
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
      if(node.id == root){
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
      /* console.log("setNodePosition: nodeId = "+node.id+", horizontalCount = "+node.horizontalCount
      +", totalParentSpace = "+totalParentSpace+", start = "+start+", pos = "+pos
      +", drawn at layer "+(node.layer)+" = "+drawnNodesAtLayer[node.layer]) */
    }
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

}