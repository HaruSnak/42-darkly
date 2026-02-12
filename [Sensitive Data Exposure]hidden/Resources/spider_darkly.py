import scrapy

class DarklySpider(scrapy.Spider):
	name = 'darkly'
	#ATTENTION : REMPLACER X.X.X.X PAR L'IP DE LA MACHINE
	start_urls = ['http://X.X.X.X/.hidden/']

	def parse(self, response):
		for link in response.css('a::attr(href)').getall():
			if link == '../':
				continue
			if link == 'README':
				yield response.follow(link, self.parse_readme)
			elif link.endswith('/'):
				yield response.follow(link, self.parse)

	def parse_readme(self, response):
		content = response.text.strip()
		trolls = ["Toujours", "encore", "proche", "voisin", "aide", "bon"]

		if not any(troll in content for troll in trolls):
			yield {'flag': content, 'url': response.url}