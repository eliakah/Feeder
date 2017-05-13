<h1>Feeder</h1>

Feeder and it’s implementing classes are used to import a data source and format the data for the Parser module. 
<ul>
<b>The Feeder interface</b> is a model of how the data import should be implemented in order to successfully interact with the other modules and provide them with appropriately structured data

<li><b>The Feed class</b> allows for more functionality in regards to how the data provided can be accessed </li>

<li><b>The RssFeeder class</b> implementing the Feeder interface, is a class which, using the `feedparser` library generates RSS feeds from a list of links in a given text file. The information retrieved from each feed is formatted as a `Feed` instance then stored in a data structure which other modules can easily access. </li>

<li><b>The DocFeeder class</b> implementing the Feeder interface, is a class which recursively accesses each file in a given directory. The information retrieved from each file is formated as `Feed` instances then stored in a data structure which other modules can easily access. </li> 
</ul>

<center><b>This interface and its implementations are part of a research project</b></center>
