from inui.toinui import HtmlToInui as hti

ht = hti()
ht.fromFile("m.html")
ht.save("m2.py")
