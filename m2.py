from inui.elements import *
from inui.svg import *
Html(
    lang='''en''',
    data = (
        Head(

            data = (
                Meta(
                    charset='''UTF-8''',
                ), 
                Meta(
                    name='''viewport''',
                    content='''width=device-width, initial-scale=1.0''',
                ), 
                Title(

                    data = ('''Advanced Text Editor''',)
                ), 
                Link(
                    rel='''stylesheet''',
                    href='''styles.css''',
                ), )
        ), 
        Body(

            data = (
                Div(
                    classs='''editor-container''',
                    data = (
                        Div(
                            classs='''editor''',
                            data = (
                                Textarea(
                                    id='''text-area''',
                                    placeholder='''Type your text here...''',
                                ), 
                                Div(
                                    classs='''controls''',
                                    data = (
                                        Button(
                                            id='''save-button''',
                                            data = ('''Save''',)
                                        ), 
                                        Button(
                                            id='''load-button''',
                                            data = ('''Load''',)
                                        ), )
                                ), )
                        ), )
                ), 
                Script(
                    src='''script.js''',
                ), )
        ), )
)