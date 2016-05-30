var fs = require('fs');
var path = require('path');
var sharp = require('sharp');
sharp.simd(true);

var targetHeight = [1000.0, 750.0, 500.0, 250.0, 100.0, 1000.0, 750.0, 500.0, 1000.0, 750.0, 500.0, 250.0, 100.0, 1000.0, 750.0, 500.0]

//read all files in the input directory
fs.readdir(process.argv[2], function(err, files) {
    if(err) return;

    for(var f in files) {
        
        setTimeout((function(filename) {
            return function() {
                var i = sharp(path.join(process.argv[2], filename));

                i.metadata()
                .then(function(metadata) {
                    for(var h in targetHeight) {
                        var ratio = targetHeight[h]/metadata.height;
                        var targetWidth = metadata.width * ratio;

                        (function(h,w) {
                            i
                            .rotate(90)
                            .resize(h, w)
                            .crop(sharp.gravity.center)
                            .toFile(path.join(__dirname, process.argv[3], h+"_"+filename));    
                        })(parseInt(targetHeight[h], 10), parseInt(targetWidth, 10));

                    }
                });                          
            };
            
        })(files[f]), 0*f);
    }
})
