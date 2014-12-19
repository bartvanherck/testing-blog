title: convert openstreetmap files to geojson 
tags: javascript, nodejs
category: web
date: 2014-04-15 21:06:00
Summary: I recently found a nice project named osm2geojson. This project can convert openstreetmap xml files, or OSM files to geo-json format. In my projects, 

I recently found a nice project named [osm2geojson](https://github.com/rclark/osm2geojson). This project can convert openstreetmap xml files, or **OSM** files to geo-json format. Because in my projects, I normally do not need a complete conversion, but only a subset. For example, I only need the streets (identified by a tag called Highways) So I created a little node application for myself.

The code is as simple as this for my purpose:

<code class="javascript">
<pre>#!/bin/env node

osm2geojson = require("osm2geojson")(function (feature) {
    return feature.properties.highway !== undefined;
});

var argv = require('optimist').options('f',{
        alias: 'file',
        default: '',
        describe: 'an input file'
}).argv;
var request = require('request');
var fs= require('fs');
var input = null;

if (argv.file !== ''){
    console.log(argv.file);
    input = fs.createReadStream(argv.file);
}

if (!input) return console.log('There was no input recieved');
input.pipe(osm2geojson).pipe(process.stdout);
</pre></code>

Now I just launch the application by running my file, that is called parse.js


<code class="bash"><pre>
$ node ./parser.js -f ./inputfile.osm
</pre></code>
