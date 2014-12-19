title: circular image with css
date: 2014-05-09 21:00:24
category: web
Summary: I recently added a circular image on the header of this page. In fact, this is not a circular image at all. But thanks to the new CSS, it is rendered as a circular image. It is done as a background image, but that does not matter for the purpose of this article. 

I recently added a circular image on the header of this page. In fact, this is not a circular image at all. But thanks to the new CSS, it is rendered as a circular image. It is done as a background image, but that does not matter for the purpose of this article anyway. 

What did I do? First I have a little div in the html page:

<code class="html"><pre>
&lt;div class="circular-logo">&lt;/div&gt;
</pre></code>

The fun part is not in the html, but in the css stylesheet:

<code class="html"><pre>
.circular-logo {
	width: 100px;
	height: 100px;
	border-radius: 50px;
	-webkit-border-radius: 50px;
	-moz-border-radius: 50px;
	background: url(/my/image.jpg) no-repeat;
	box-shadow: 0 0 8px rgba(0, 0, 0, .8);
	-webkit-box-shadow: 0 0 8px rgba(0, 0, 0, .8);
	-moz-box-shadow: 0 0 8px rgba(0, 0, 0, .8);
}
</pre></code>

Simple as it is.
