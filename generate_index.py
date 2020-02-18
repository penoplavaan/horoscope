from horoscope import generate_prophecies
from datetime import datetime as dt

def generate_head(title):
	head = f"""<head>
	<meta charset='utf-8'> 
	<title>{title}</title>
	</head>"""
	return head
	

def generate_body(header, paragraph):
	body=f"""
	<h1>{header}</h1>"""
	for p in paragraph:
		body+=f"""
		<p>{p}</p>
		"""

	return f"<body>{body}</body>" 

def generate_page(head, body):
	page=f"""<html>
	{head}
	{body}
	</html>"""
	return page

def save_page(title, header, paragraph, output="index.html"):
	fp= open(output, "w", encoding="utf-8")
	page = generate_page(
		head=generate_head(title),
		body=generate_body(header, paragraph)
		)
	print(page, file=fp)
	fp.close()

####################

today=dt.now().date()
save_page(
		title="Гороскоп на сегодня", 
		header="Что " + str(today) + " нам готовит?",
		paragraph=generate_prophecies(),
	)


