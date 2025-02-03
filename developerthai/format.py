from IPython.display import display, HTML

def num_format(num, decimal=2):
	return format(num, f',.{decimal}f')

def display_fraction(prefix, dividen, divider):
	html_text = \
    		f'<table> \
    		<tr style="background:#fff !important"> \
       			<td rowspan="2">{prefix}</td> \
        			<td style="border-bottom:solid 1px black;text-align:center">{dividen}<td> \
    		</tr> \
    		<tr> \
       	 		<td>{divider}</td> \
    		<tr> \
    		</table>'
        
	display(HTML(html_text))

def display_html(text):
	display(HTML(text))