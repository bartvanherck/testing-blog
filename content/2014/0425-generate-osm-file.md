title: generate osm file
date: 2014-04-25 20:22:00
Category: other
Summary: I did download a planet file from my country. What I want now is an extract for the city I live in. This is also very simple.

I did download a planet file from my country. What I want now is an extract for the city I live in. This is also very simple.

<code class="bash"><pre>
$ osmosis --read-pbf-fast file=country.osm.pbf --bounding-polygon \
file=mycity.poly completeWays=yes --write-xml file="city.osm"
</pre></code>

Now I can convert this osm file to geojson, with other [tools I am writing](/2014/04/15/2014/converting-openstreetmap-xml-files-to-geojson-with-a-node-application). I will upload it to github someday, so I do not lose my code for it.
