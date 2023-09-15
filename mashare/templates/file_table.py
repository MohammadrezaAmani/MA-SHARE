from inui.toinui import HtmlToInui as hti

h = hti()
h.fromFile("html.html")
h.save("m.py")
