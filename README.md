# The-Moroccan-News-Corpus

The present corpus was part of a summer internship. We use scrapy spiders/crawlers module to crawl the Moroccan newspaper websites and save all the scraped data to either json or text files. The built spiders/crawlers for the following news websites:
<h3>Moroccan News websites</h3>
<li>http://ahdath.info/</li>
<li>https://www.akhbarona.com/</li>
<li>https://www.alayam24.com/</li>
<li>https://www.almaghribtoday.net/</li>
<li>https://www.barlamane.com/</li>
<li>https://dalil-rif.com/</li>
<li> https://www.febrayer.com/</li>
<li>https://www.goud.ma/</li>
<li>https://www.hespress.com/</li>
<li>https://ar.hibapress.com/</li>
<li>http://kifache.com/</li>
<li>www.maghress.com</li>
<li>https://www.menara.ma/</li>
<li>https://www.almaghreb24.com/</li>
<li>https://maroctelegraph.com/</li>
<li>https://www.nadorcity.com/</li>
<li>https://tanja24.com/</li>
<li>http://telexpresse.com/</li>
<li>http://ar.le360.ma/</li>
<li>http://www.alyaoum24.com/</li>
<li>http://www.2m.ma/ar/</li>
<li>https://ar.yabiladi.com/</li>

<h3>How to use spiders/crawlers?</h3>
Every folder represents the project folder for every newspaper.<br>
To scrape any data from any of the newspapers above,<br> 
<li>Download its project folder.</li>
<li>On the command line, change directory to the project folder</li>
<li>Invoke the following command to start scrabing the website: <code> scrapy crawl < name of the spider > -o < name of the file >.json</code></li>

<h3>Note</h3>
Every spider/crawler automatically saves a text file in addition to either json files or xml files that you determine when you run your spider in the command line.
