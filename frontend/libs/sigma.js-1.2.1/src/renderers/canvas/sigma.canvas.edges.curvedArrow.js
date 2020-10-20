;(function() {
  'use strict';

  sigma.utils.pkg('sigma.canvas.edges');

  /**
   * This edge renderer will display edges as curves with arrow heading.
   *
   * @param  {object}                   edge         The edge object.
   * @param  {object}                   source node  The edge source node.
   * @param  {object}                   target node  The edge target node.
   * @param  {CanvasRenderingContext2D} context      The canvas context.
   * @param  {configurable}             settings     The settings function.
   */
  sigma.canvas.edges.curvedArrow =
    function(edge, source, target, context, settings) {
      var color = edge.color,
          prefix = settings('prefix') || '',
          edgeColor = settings('edgeColor'),
          defaultNodeColor = settings('defaultNodeColor'),
          defaultEdgeColor = settings('defaultEdgeColor'),
          cp = {},
          size = edge[prefix + 'size'] || 1,
          tSize = target[prefix + 'size'],
          sX = source[prefix + 'x'],
          sY = source[prefix + 'y'],
          tX = target[prefix + 'x'],
          tY = target[prefix + 'y'],
          beta = Math.atan2(tY-sY, tX-sX),
          bAngle = beta * 180 / Math.PI,
          aSize = Math.max(size * 2.5, settings('minArrowSize')),
          d,
          aX,
          aY,
          vX,
          vY;
        
      if(bAngle < 0)
        bAngle += 360
      
      if(bAngle != 90 || bAngle != 180){
        if(bAngle >= 0 && bAngle < 90){
          console.log('1')
          var aAngle = 90 - bAngle,
          alfa = aAngle*Math.PI/180,
          l = size*(1/Math.abs(Math.cos(alfa)) - 1)
          tSize += l*4
          tX = tX + l*Math.abs(Math.cos(beta))
          tY = tY - l*Math.abs(Math.sin(beta))
        }
        else if(bAngle >= 90 && bAngle < 180) {
          console.log('2')
          var aAngle = 180 - bAngle,
          alfa = aAngle*Math.PI/180,
          l = size*(1/Math.abs(Math.cos(alfa)) - 1)
          tSize += l*4
          tX = tX - l*Math.abs(Math.cos(beta))
          tY = tY - l*Math.abs(Math.sin(beta))
        }
        else if(bAngle >= 180 && bAngle < 270) {
          console.log('3')
          var aAngle = 270 - bAngle,
          alfa = aAngle*Math.PI/180,
          l = size*(1/Math.abs(Math.cos(alfa)) - 1)
          tSize += l*4
          tX = tX - l*Math.abs(Math.cos(beta))
          tY = tY + l*Math.abs(Math.sin(beta))
        }
        else if(bAngle >= 270 && bAngle < 360) {
          console.log('4')
          var aAngle = 360 - bAngle,
          alfa = aAngle*Math.PI/180,
          l = size*(1/Math.abs(Math.cos(alfa)) - 1)
          tSize += l*4
          tX = tX + l*Math.abs(Math.cos(beta))
          tY = tY - l*Math.abs(Math.sin(beta))
        }    
        else {
          console.log('5 - '+bAngle)
        }
      }
      else {
        console.log('6 - '+bAngle)
      }

    cp = (source.id === target.id) ?
      sigma.utils.getSelfLoopControlPoints(sX, sY, tSize) :
      sigma.utils.getQuadraticControlPoint(sX, sY, tX, tY);

    if (source.id === target.id) {
      d = Math.sqrt(Math.pow(tX - cp.x1, 2) + Math.pow(tY - cp.y1, 2));
      aX = cp.x1 + (tX - cp.x1) * (d - aSize - tSize) / d;
      aY = cp.y1 + (tY - cp.y1) * (d - aSize - tSize) / d;
      vX = (tX - cp.x1) * aSize / d;
      vY = (tY - cp.y1) * aSize / d;
    }
    else {
      d = Math.sqrt(Math.pow(tX - cp.x, 2) + Math.pow(tY - cp.y, 2));
      aX = cp.x + (tX - cp.x) * (d - aSize - tSize) / d;
      aY = cp.y + (tY - cp.y) * (d - aSize - tSize) / d;
      vX = (tX - cp.x) * aSize / d;
      vY = (tY - cp.y) * aSize / d;
    }

    if (!color)
      switch (edgeColor) {
        case 'source':
          color = source.color || defaultNodeColor;
          break;
        case 'target':
          color = target.color || defaultNodeColor;
          break;
        default:
          color = defaultEdgeColor;
          break;
      }

    context.strokeStYle = color;
    context.lineWidth = size;
    context.beginPath();
    context.moveTo(sX, sY);
    if (source.id === target.id) {
      context.bezierCurveTo(cp.x2, cp.y2, cp.x1, cp.y1, aX, aY);
    } else {
      context.quadraticCurveTo(cp.x, cp.y, aX, aY);
    }
    context.stroke();

    context.fillStYle = color;
    context.beginPath();
    context.moveTo(aX + vX, aY + vY);
    context.lineTo(aX + vY * 0.6, aY - vX * 0.6);
    context.lineTo(aX - vY * 0.6, aY + vX * 0.6);
    context.lineTo(aX + vX, aY + vY);
    context.closePath();
    context.fill();
  };
})();
