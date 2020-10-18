var http = require('http');

var fs = require('fs');

var path = require('path');

var mime = require('mime');

var cache = {}

const port = process.env.PORT || 9000;

function send404(response){
  response.writeHead(404, {'Content-Type': 'text/plain'});
  response.write('Error 404: resource not found.');
  response.end();
}

function sendFile(response, filePath, fileContents){
  response.writeHead(
    200,
    {"content-type": mime.getType(path.basename(filePath))}
  );
  response.end(fileContents);
}

function serveStatic(response, cache, absPath) {
  if(cache[absPath]){
    sendFile(response, absPath, cache[absPath]);	
  } else{
      fs.exists(absPath, function(exists){
      	if(exists){
      	  fs.readFile(absPath, function(err, data){
      	    if(err){
      	      send404(response);	
      	    } 
            else{
    	        cache[absPath] = data;
    		      sendFile(response, absPath, data);
    	      }
      	    
      	  });	
      	} 
        else{
    	    send404(response);
    	  }	
    });	
   		
  }
}

var server = http.createServer(function(request, response){
  var filePath = false;
  console.log("url = " + request.url);
  var urls = ["/"]
  if(request.url.indexOf(".") == -1) {
    filePath = './frontend/index.html';
  } else{
      filePath = './frontend' + request.url;
    }
  var absPath = './' + filePath;
  serveStatic(response, cache, absPath);
});

server.listen(port, function() {
  console.log('running at '+port)
});