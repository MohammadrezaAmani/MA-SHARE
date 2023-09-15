"base"
from inui.elements import *
from .header import header
from .footer import footer


def base(body: str = None):
    "base style"
    return str(
        Html(
            lang="""en""",
            data=(
                Head(
                    data=(
                        Meta(
                            charset="""utf-8""",
                        ),
                        Title(data=("""check file manager - Bootdey.com""",)),
                        Meta(
                            name="""viewport""",
                            content="""width=device-width, initial-scale=1""",
                        ),
                        Link(
                            href="""./assets/css/bootstrap.min.css""",
                            rel="""stylesheet""",
                        ),
                        Style(
                            typee="""text/css""",
                            data=(
                                """
body{margin-top:20px;}
.file-manager-actions {
    display: -ms-flexbox;
    display: flex;
    -ms-flex-wrap: wrap;
    flex-wrap: wrap;
    -ms-flex-pack: justify;
    justify-content: space-between;
}
.file-manager-actions > * {
    display: -ms-flexbox;
    display: flex;
    -ms-flex-wrap: wrap;
    flex-wrap: wrap;
}
.file-manager-container {
    display: -ms-flexbox;
    display: flex;
    -ms-flex-wrap: wrap;
    flex-wrap: wrap;
}
.file-item {
    position: relative;
    z-index: 1;
    -ms-flex: 0 0 auto;
    flex: 0 0 auto;
    border: 1px solid #eee;
    cursor: pointer;
}
.file-item:hover,
.file-item.focused {
    border-color: rgba(0, 0, 0, 0.05);
}
.file-item.focused {
    z-index: 2;
}
.file-item * {
    -ms-flex-negative: 0;
    flex-shrink: 0;
    text-decoration:none;
}
.dark-style .file-item:hover,
.dark-style .file-item.focused {
    border-color: rgba(255, 255, 255, 0.2);
}
.file-item-checkbox {
    margin: 0 !important;
}
.file-item-select-bg {
    position: absolute;
    top: 0;
    right: 0;
    bottom: 0;
    left: 0;
    z-index: -1;
    opacity: 0;
}
.file-item-img {
    background-color: transparent;
    background-position: center center;
    background-size: cover;
}
.file-item-name {
    display: block;
    overflow: hidden;
}
.file-manager-col-view .file-item {
    margin: 0 0.25rem 0.25rem 0;
    padding: 1.25rem 0 1rem 0;
    width: 9rem;
    text-align: center;
}
[dir="rtl"] .file-manager-col-view .file-item {
    margin-right: 0;
    margin-left: 0.25rem;
}
.file-manager-col-view .file-item-img,
.file-manager-col-view .file-item-icon {
    display: block;
    margin: 0 auto 0.75rem auto;
    width: 4rem;
    height: 4rem;
    font-size: 2.5rem;
    line-height: 4rem;
}
.file-manager-col-view .file-item-level-up {
    font-size: 1.5rem;
}
.file-manager-col-view .file-item-checkbox,
.file-manager-col-view .file-item-actions {
    position: absolute;
    top: 6px;
}
.file-manager-col-view .file-item-checkbox {
    left: 6px;
}
[dir="rtl"] .file-manager-col-view .file-item-checkbox {
    right: 6px;
    left: auto;
}
.file-manager-col-view .file-item-actions {
    right: 6px;
}
[dir="rtl"] .file-manager-col-view .file-item-actions {
    right: auto;
    left: 6px;
}
.file-manager-col-view .file-item-name {
    width: 100%;
}
.file-manager-col-view .file-manager-row-header,
.file-manager-col-view .file-item-changed {
    display: none;
}
.file-manager-row-view .file-manager-row-header,
.file-manager-row-view .file-item {
    display: -ms-flexbox;
    display: flex;
    -ms-flex-align: center;
    align-items: center;
    margin: 0 0 0.125rem 0;
    padding: 0.25rem 3rem 0.25rem 2.25em;
    width: 100%;
}
[dir="rtl"] .file-manager-row-view .file-manager-row-header,
[dir="rtl"] .file-manager-row-view .file-item {
    padding-right: 2.25em;
    padding-left: 3rem;
}
.file-manager-row-view .file-item-img,
.file-manager-row-view .file-item-icon {
    display: block;
    margin: 0 1rem;
    width: 2rem;
    height: 2rem;
    text-align: center;
    font-size: 1.25rem;
    line-height: 2rem;
}
.file-manager-row-view .file-item-level-up {
    font-size: 1rem;
}
.file-manager-row-view .file-item-checkbox,
.file-manager-row-view .file-item-actions {
    position: absolute;
    top: 50%;
    -webkit-transform: translateY(-50%);
    transform: translateY(-50%);
}
.file-manager-row-view .file-item-checkbox {
    left: 10px;
}
[dir="rtl"] .file-manager-row-view .file-item-checkbox {
    right: 10px;
    left: auto;
}
.file-manager-row-view .file-item-actions {
    right: 10px;
}
[dir="rtl"] .file-manager-row-view .file-item-actions {
    right: auto;
    left: 10px;
}
.file-manager-row-view .file-item-changed {
    display: none;
    margin-left: auto;
    width: 10rem;
}
[dir="rtl"] .file-manager-row-view .file-item-changed {
    margin-right: auto;
    margin-left: 0;
}
.file-manager-row-view .file-item-name {
    width: calc(100% - 4rem);
}
.file-manager-row-view .file-manager-row-header {
    border-bottom: 2px solid rgba(0, 0, 0, 0.05);
    font-weight: bold;
}
.file-manager-row-view .file-manager-row-header .file-item-name {
    margin-left: 4rem;
}
[dir="rtl"] .file-manager-row-view .file-manager-row-header .file-item-name {
    margin-right: 4rem;
    margin-left: 0;
}
.light-style .file-item-name {
    color: #4e5155 !important;
}
.light-style .file-item.selected .file-item-select-bg {
    opacity: 0.15;
}
@media (min-width: 768px) {
    .light-style .file-manager-row-view .file-item-changed {
        display: block;
    }
    .light-style .file-manager-row-view .file-item-name {
        width: calc(100% - 15rem);
    }
}
@media (min-width: 992px) {
    .light-style .file-manager-col-view .file-item-checkbox,
    .light-style .file-manager-col-view .file-item-actions {
        opacity: 0;
    }
    .light-style .file-manager-col-view .file-item:hover .file-item-checkbox,
    .light-style .file-manager-col-view .file-item.focused .file-item-checkbox,
    .light-style .file-manager-col-view .file-item.selected .file-item-checkbox,
    .light-style .file-manager-col-view .file-item:hover .file-item-actions,
    .light-style .file-manager-col-view .file-item.focused .file-item-actions,
    .light-style .file-manager-col-view .file-item.selected .file-item-actions {
        opacity: 1;
    }
}
.material-style .file-item-name {
    color: #4e5155 !important;
}
.material-style .file-item.selected .file-item-select-bg {
    opacity: 0.15;
}
@media (min-width: 768px) {
    .material-style .file-manager-row-view .file-item-changed {
        display: block;
    }
    .material-style .file-manager-row-view .file-item-name {
        width: calc(100% - 15rem);
    }
}
@media (min-width: 992px) {
    .material-style .file-manager-col-view .file-item-checkbox,
    .material-style .file-manager-col-view .file-item-actions {
        opacity: 0;
    }
    .material-style .file-manager-col-view .file-item:hover .file-item-checkbox,
    .material-style .file-manager-col-view .file-item.focused .file-item-checkbox,
    .material-style .file-manager-col-view .file-item.selected .file-item-checkbox,
    .material-style .file-manager-col-view .file-item:hover .file-item-actions,
    .material-style .file-manager-col-view .file-item.focused .file-item-actions,
    .material-style .file-manager-col-view .file-item.selected .file-item-actions {
        opacity: 1;
    }
}
.dark-style .file-item-name {
    color: #fff !important;
}
.dark-style .file-item.selected .file-item-select-bg {
    opacity: 0.15;
}
@media (min-width: 768px) {
    .dark-style .file-manager-row-view .file-item-changed {
        display: block;
    }
    .dark-style .file-manager-row-view .file-item-name {
        width: calc(100% - 15rem);
    }
}
@media (min-width: 992px) {
    .dark-style .file-manager-col-view .file-item-checkbox,
    .dark-style .file-manager-col-view .file-item-actions {
        opacity: 0;
    }
    .dark-style .file-manager-col-view .file-item:hover .file-item-checkbox,
    .dark-style .file-manager-col-view .file-item.focused .file-item-checkbox,
    .dark-style .file-manager-col-view .file-item.selected .file-item-checkbox,
    .dark-style .file-manager-col-view .file-item:hover .file-item-actions,
    .dark-style .file-manager-col-view .file-item.focused .file-item-actions,
    .dark-style .file-manager-col-view .file-item.selected .file-item-actions {
        opacity: 1;
    }
}

    """,
                            ),
                        ),
                    )
                ),
                Body(
                    data=(
                        Link(
                            rel="""stylesheet""",
                            href="""https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.13.1/css/all.min.css""",
                            integrity="""sha256-2XFplPlrFClt0bIdPgpz8H7ojnk10H69xRqd9+uTShA=""",
                            crossorigin="""anonymous""",
                        ),
                        Link(
                            rel="""stylesheet""",
                            href="""https://cdnjs.cloudflare.com/ajax/libs/ionicons/4.5.6/css/ionicons.min.css""",
                            integrity="""sha512-0/rEDduZGrqo4riUlwqyuHDQzp2D1ZCgH/gFIfjMIL5az8so6ZiXyhf1Rg8i6xsjv+z/Ubc4tt1thLigEcu6Ug==""",
                            crossorigin="""anonymous""",
                            referrerpolicy="""no-referrer""",
                        ),
                        Div(
                            classs="""container flex-grow-1 light-style container-p-y""",
                            data=(
                                Div(
                                    classs="""container-m-nx container-m-ny bg-lightest mb-3""",
                                    data=(
                                        Ol(
                                            classs="""breadcrumb text-big container-p-x py-3 m-0""",
                                            data=(
                                                Li(
                                                    classs="""breadcrumb-item""",
                                                    data=(
                                                        A(
                                                            href="""javascript:void(0)""",
                                                            data=("""home""",),
                                                        ),
                                                    ),
                                                ),
                                                Li(
                                                    classs="""breadcrumb-item""",
                                                    data=(
                                                        A(
                                                            href="""javascript:void(0)""",
                                                            data=("""projects""",),
                                                        ),
                                                    ),
                                                ),
                                                Li(
                                                    classs="""breadcrumb-item active""",
                                                    data=("""site""",),
                                                ),
                                            ),
                                        ),
                                        Hr(
                                            classs="""m-0""",
                                        ),
                                        Div(
                                            classs="""file-manager-actions container-p-x py-2""",
                                            data=(
                                                Div(
                                                    data=(
                                                        Button(
                                                            typee="""button""",
                                                            classs="""btn btn-primary mr-2""",
                                                            data=(
                                                                I(
                                                                    classs="""ion ion-md-cloud-upload""",
                                                                ),
                                                            ),
                                                        ),
                                                        Button(
                                                            typee="""button""",
                                                            classs="""btn btn-secondary icon-btn mr-2""",
                                                            disabled="""disabled""",
                                                            data=(
                                                                I(
                                                                    classs="""ion ion-md-cloud-download""",
                                                                ),
                                                            ),
                                                        ),
                                                        Div(
                                                            classs="""btn-group mr-2""",
                                                            data=(
                                                                Button(
                                                                    typee="""button""",
                                                                    classs="""btn btn-default md-btn-flat dropdown-toggle px-2""",
                                                                    data_toggle="""dropdown""",
                                                                    data=(
                                                                        I(
                                                                            classs="""ion ion-ios-settings""",
                                                                        ),
                                                                    ),
                                                                ),
                                                                Div(
                                                                    classs="""dropdown-menu""",
                                                                    data=(
                                                                        A(
                                                                            classs="""dropdown-item""",
                                                                            href="""javascript:void(0)""",
                                                                            data=(
                                                                                """Move""",
                                                                            ),
                                                                        ),
                                                                        A(
                                                                            classs="""dropdown-item""",
                                                                            href="""javascript:void(0)""",
                                                                            data=(
                                                                                """Copy""",
                                                                            ),
                                                                        ),
                                                                        A(
                                                                            classs="""dropdown-item""",
                                                                            href="""javascript:void(0)""",
                                                                            data=(
                                                                                """Remove""",
                                                                            ),
                                                                        ),
                                                                    ),
                                                                ),
                                                            ),
                                                        ),
                                                    )
                                                ),
                                                Div(
                                                    data=(
                                                        Div(
                                                            classs="""btn-group btn-group-toggle""",
                                                            data_toggle="""buttons""",
                                                            data=(
                                                                Label(
                                                                    classs="""btn btn-default icon-btn md-btn-flat active""",
                                                                    data=(
                                                                        Input(
                                                                            typee="""radio""",
                                                                            name="""file-manager-view""",
                                                                            value="""file-manager-col-view""",
                                                                            checked="""checked""",
                                                                        ),
                                                                        Span(
                                                                            classs="""ion ion-md-apps""",
                                                                        ),
                                                                    ),
                                                                ),
                                                                Label(
                                                                    classs="""btn btn-default icon-btn md-btn-flat""",
                                                                    data=(
                                                                        Input(
                                                                            typee="""radio""",
                                                                            name="""file-manager-view""",
                                                                            value="""file-manager-row-view""",
                                                                        ),
                                                                        Span(
                                                                            classs="""ion ion-md-menu""",
                                                                        ),
                                                                    ),
                                                                ),
                                                            ),
                                                        ),
                                                    )
                                                ),
                                            ),
                                        ),
                                        Hr(
                                            classs="""m-0""",
                                        ),
                                    ),
                                ),
                                Div(
                                    classs="""file-manager-container file-manager-col-view""",
                                    data=(
                                        Div(
                                            classs="""file-manager-row-header""",
                                            data=(
                                                Div(
                                                    classs="""file-item-name pb-2""",
                                                    data=("""Filename""",),
                                                ),
                                                Div(
                                                    classs="""file-item-changed pb-2""",
                                                    data=("""Changed""",),
                                                ),
                                            ),
                                        ),
                                        Div(
                                            classs="""file-item""",
                                            data=(
                                                Div(
                                                    classs="""file-item-icon file-item-level-up fas fa-level-up-alt text-secondary""",
                                                ),
                                                A(
                                                    href="""javascript:void(0)""",
                                                    classs="""file-item-name""",
                                                    data=(
                                                        """
..
""",
                                                    ),
                                                ),
                                            ),
                                        ),
                                        Div(
                                            classs="""file-item""",
                                            data=(
                                                Div(
                                                    classs="""file-item-select-bg bg-primary""",
                                                ),
                                                Label(
                                                    classs="""file-item-checkbox custom-control custom-checkbox""",
                                                    data=(
                                                        Input(
                                                            typee="""checkbox""",
                                                            classs="""custom-control-input""",
                                                        ),
                                                        Span(
                                                            classs="""custom-control-label""",
                                                        ),
                                                    ),
                                                ),
                                                Div(
                                                    classs="""file-item-icon far fa-folder text-secondary""",
                                                ),
                                                A(
                                                    href="""javascript:void(0)""",
                                                    classs="""file-item-name""",
                                                    data=(
                                                        """
Images
""",
                                                    ),
                                                ),
                                                Div(
                                                    classs="""file-item-changed""",
                                                    data=("""02/13/2018""",),
                                                ),
                                                Div(
                                                    classs="""file-item-actions btn-group""",
                                                    data=(
                                                        Button(
                                                            typee="""button""",
                                                            classs="""btn btn-default btn-sm rounded-pill icon-btn borderless md-btn-flat hide-arrow dropdown-toggle""",
                                                            data_toggle="""dropdown""",
                                                            data=(
                                                                I(
                                                                    classs="""ion ion-ios-more""",
                                                                ),
                                                            ),
                                                        ),
                                                        Div(
                                                            classs="""dropdown-menu dropdown-menu-right""",
                                                            data=(
                                                                A(
                                                                    classs="""dropdown-item""",
                                                                    href="""javascript:void(0)""",
                                                                    data=(
                                                                        """Rename""",
                                                                    ),
                                                                ),
                                                                A(
                                                                    classs="""dropdown-item""",
                                                                    href="""javascript:void(0)""",
                                                                    data=("""Move""",),
                                                                ),
                                                                A(
                                                                    classs="""dropdown-item""",
                                                                    href="""javascript:void(0)""",
                                                                    data=("""Copy""",),
                                                                ),
                                                                A(
                                                                    classs="""dropdown-item""",
                                                                    href="""javascript:void(0)""",
                                                                    data=(
                                                                        """Remove""",
                                                                    ),
                                                                ),
                                                            ),
                                                        ),
                                                    ),
                                                ),
                                            ),
                                        ),
                                        Div(
                                            classs="""file-item""",
                                            data=(
                                                Div(
                                                    classs="""file-item-select-bg bg-primary""",
                                                ),
                                                Label(
                                                    classs="""file-item-checkbox custom-control custom-checkbox""",
                                                    data=(
                                                        Input(
                                                            typee="""checkbox""",
                                                            classs="""custom-control-input""",
                                                        ),
                                                        Span(
                                                            classs="""custom-control-label""",
                                                        ),
                                                    ),
                                                ),
                                                Div(
                                                    classs="""file-item-icon far fa-folder text-secondary""",
                                                ),
                                                A(
                                                    href="""javascript:void(0)""",
                                                    classs="""file-item-name""",
                                                    data=(
                                                        """
Scripts
""",
                                                    ),
                                                ),
                                                Div(
                                                    classs="""file-item-changed""",
                                                    data=("""02/14/2018""",),
                                                ),
                                                Div(
                                                    classs="""file-item-actions btn-group""",
                                                    data=(
                                                        Button(
                                                            typee="""button""",
                                                            classs="""btn btn-default btn-sm rounded-pill icon-btn borderless md-btn-flat hide-arrow dropdown-toggle""",
                                                            data_toggle="""dropdown""",
                                                            data=(
                                                                I(
                                                                    classs="""ion ion-ios-more""",
                                                                ),
                                                            ),
                                                        ),
                                                        Div(
                                                            classs="""dropdown-menu dropdown-menu-right""",
                                                            data=(
                                                                A(
                                                                    classs="""dropdown-item""",
                                                                    href="""javascript:void(0)""",
                                                                    data=(
                                                                        """Rename""",
                                                                    ),
                                                                ),
                                                                A(
                                                                    classs="""dropdown-item""",
                                                                    href="""javascript:void(0)""",
                                                                    data=("""Move""",),
                                                                ),
                                                                A(
                                                                    classs="""dropdown-item""",
                                                                    href="""javascript:void(0)""",
                                                                    data=("""Copy""",),
                                                                ),
                                                                A(
                                                                    classs="""dropdown-item""",
                                                                    href="""javascript:void(0)""",
                                                                    data=(
                                                                        """Remove""",
                                                                    ),
                                                                ),
                                                            ),
                                                        ),
                                                    ),
                                                ),
                                            ),
                                        ),
                                        Div(
                                            classs="""file-item""",
                                            data=(
                                                Div(
                                                    classs="""file-item-select-bg bg-primary""",
                                                ),
                                                Label(
                                                    classs="""file-item-checkbox custom-control custom-checkbox""",
                                                    data=(
                                                        Input(
                                                            typee="""checkbox""",
                                                            classs="""custom-control-input""",
                                                        ),
                                                        Span(
                                                            classs="""custom-control-label""",
                                                        ),
                                                    ),
                                                ),
                                                Div(
                                                    classs="""file-item-icon far fa-folder text-secondary""",
                                                ),
                                                A(
                                                    href="""javascript:void(0)""",
                                                    classs="""file-item-name""",
                                                    data=(
                                                        """
Utils
""",
                                                    ),
                                                ),
                                                Div(
                                                    classs="""file-item-changed""",
                                                    data=("""02/15/2018""",),
                                                ),
                                                Div(
                                                    classs="""file-item-actions btn-group""",
                                                    data=(
                                                        Button(
                                                            typee="""button""",
                                                            classs="""btn btn-default btn-sm rounded-pill icon-btn borderless md-btn-flat hide-arrow dropdown-toggle""",
                                                            data_toggle="""dropdown""",
                                                            data=(
                                                                I(
                                                                    classs="""ion ion-ios-more""",
                                                                ),
                                                            ),
                                                        ),
                                                        Div(
                                                            classs="""dropdown-menu dropdown-menu-right""",
                                                            data=(
                                                                A(
                                                                    classs="""dropdown-item""",
                                                                    href="""javascript:void(0)""",
                                                                    data=(
                                                                        """Rename""",
                                                                    ),
                                                                ),
                                                                A(
                                                                    classs="""dropdown-item""",
                                                                    href="""javascript:void(0)""",
                                                                    data=("""Move""",),
                                                                ),
                                                                A(
                                                                    classs="""dropdown-item""",
                                                                    href="""javascript:void(0)""",
                                                                    data=("""Copy""",),
                                                                ),
                                                                A(
                                                                    classs="""dropdown-item""",
                                                                    href="""javascript:void(0)""",
                                                                    data=(
                                                                        """Remove""",
                                                                    ),
                                                                ),
                                                            ),
                                                        ),
                                                    ),
                                                ),
                                            ),
                                        ),
                                        Div(
                                            classs="""file-item""",
                                            data=(
                                                Div(
                                                    classs="""file-item-select-bg bg-primary""",
                                                ),
                                                Label(
                                                    classs="""file-item-checkbox custom-control custom-checkbox""",
                                                    data=(
                                                        Input(
                                                            typee="""checkbox""",
                                                            classs="""custom-control-input""",
                                                        ),
                                                        Span(
                                                            classs="""custom-control-label""",
                                                        ),
                                                    ),
                                                ),
                                                Div(
                                                    classs="""file-item-icon far fa-file-archive text-secondary""",
                                                ),
                                                A(
                                                    href="""javascript:void(0)""",
                                                    classs="""file-item-name""",
                                                    data=(
                                                        """
Archive.zip
""",
                                                    ),
                                                ),
                                                Div(
                                                    classs="""file-item-changed""",
                                                    data=("""02/16/2018""",),
                                                ),
                                                Div(
                                                    classs="""file-item-actions btn-group""",
                                                    data=(
                                                        Button(
                                                            typee="""button""",
                                                            classs="""btn btn-default btn-sm rounded-pill icon-btn borderless md-btn-flat hide-arrow dropdown-toggle""",
                                                            data_toggle="""dropdown""",
                                                            data=(
                                                                I(
                                                                    classs="""ion ion-ios-more""",
                                                                ),
                                                            ),
                                                        ),
                                                        Div(
                                                            classs="""dropdown-menu dropdown-menu-right""",
                                                            data=(
                                                                A(
                                                                    classs="""dropdown-item""",
                                                                    href="""javascript:void(0)""",
                                                                    data=(
                                                                        """Rename""",
                                                                    ),
                                                                ),
                                                                A(
                                                                    classs="""dropdown-item""",
                                                                    href="""javascript:void(0)""",
                                                                    data=("""Move""",),
                                                                ),
                                                                A(
                                                                    classs="""dropdown-item""",
                                                                    href="""javascript:void(0)""",
                                                                    data=("""Copy""",),
                                                                ),
                                                                A(
                                                                    classs="""dropdown-item""",
                                                                    href="""javascript:void(0)""",
                                                                    data=(
                                                                        """Remove""",
                                                                    ),
                                                                ),
                                                            ),
                                                        ),
                                                    ),
                                                ),
                                            ),
                                        ),
                                        Div(
                                            classs="""file-item""",
                                            data=(
                                                Div(
                                                    classs="""file-item-select-bg bg-primary""",
                                                ),
                                                Label(
                                                    classs="""file-item-checkbox custom-control custom-checkbox""",
                                                    data=(
                                                        Input(
                                                            typee="""checkbox""",
                                                            classs="""custom-control-input""",
                                                        ),
                                                        Span(
                                                            classs="""custom-control-label""",
                                                        ),
                                                    ),
                                                ),
                                                Div(
                                                    classs="""file-item-icon fab fa-js text-secondary""",
                                                ),
                                                A(
                                                    href="""javascript:void(0)""",
                                                    classs="""file-item-name""",
                                                    data=(
                                                        """
Build.js
""",
                                                    ),
                                                ),
                                                Div(
                                                    classs="""file-item-changed""",
                                                    data=("""02/17/2018""",),
                                                ),
                                                Div(
                                                    classs="""file-item-actions btn-group""",
                                                    data=(
                                                        Button(
                                                            typee="""button""",
                                                            classs="""btn btn-default btn-sm rounded-pill icon-btn borderless md-btn-flat hide-arrow dropdown-toggle""",
                                                            data_toggle="""dropdown""",
                                                            data=(
                                                                I(
                                                                    classs="""ion ion-ios-more""",
                                                                ),
                                                            ),
                                                        ),
                                                        Div(
                                                            classs="""dropdown-menu dropdown-menu-right""",
                                                            data=(
                                                                A(
                                                                    classs="""dropdown-item""",
                                                                    href="""javascript:void(0)""",
                                                                    data=(
                                                                        """Rename""",
                                                                    ),
                                                                ),
                                                                A(
                                                                    classs="""dropdown-item""",
                                                                    href="""javascript:void(0)""",
                                                                    data=("""Move""",),
                                                                ),
                                                                A(
                                                                    classs="""dropdown-item""",
                                                                    href="""javascript:void(0)""",
                                                                    data=("""Copy""",),
                                                                ),
                                                                A(
                                                                    classs="""dropdown-item""",
                                                                    href="""javascript:void(0)""",
                                                                    data=(
                                                                        """Remove""",
                                                                    ),
                                                                ),
                                                            ),
                                                        ),
                                                    ),
                                                ),
                                            ),
                                        ),
                                        Div(
                                            classs="""file-item""",
                                            data=(
                                                Div(
                                                    classs="""file-item-select-bg bg-primary""",
                                                ),
                                                Label(
                                                    classs="""file-item-checkbox custom-control custom-checkbox""",
                                                    data=(
                                                        Input(
                                                            typee="""checkbox""",
                                                            classs="""custom-control-input""",
                                                        ),
                                                        Span(
                                                            classs="""custom-control-label""",
                                                        ),
                                                    ),
                                                ),
                                                Div(
                                                    classs="""file-item-icon far fa-file-word text-secondary""",
                                                ),
                                                A(
                                                    href="""javascript:void(0)""",
                                                    classs="""file-item-name""",
                                                    data=(
                                                        """
Checklist.doc
""",
                                                    ),
                                                ),
                                                Div(
                                                    classs="""file-item-changed""",
                                                    data=("""02/18/2018""",),
                                                ),
                                                Div(
                                                    classs="""file-item-actions btn-group""",
                                                    data=(
                                                        Button(
                                                            typee="""button""",
                                                            classs="""btn btn-default btn-sm rounded-pill icon-btn borderless md-btn-flat hide-arrow dropdown-toggle""",
                                                            data_toggle="""dropdown""",
                                                            data=(
                                                                I(
                                                                    classs="""ion ion-ios-more""",
                                                                ),
                                                            ),
                                                        ),
                                                        Div(
                                                            classs="""dropdown-menu dropdown-menu-right""",
                                                            data=(
                                                                A(
                                                                    classs="""dropdown-item""",
                                                                    href="""javascript:void(0)""",
                                                                    data=(
                                                                        """Rename""",
                                                                    ),
                                                                ),
                                                                A(
                                                                    classs="""dropdown-item""",
                                                                    href="""javascript:void(0)""",
                                                                    data=("""Move""",),
                                                                ),
                                                                A(
                                                                    classs="""dropdown-item""",
                                                                    href="""javascript:void(0)""",
                                                                    data=("""Copy""",),
                                                                ),
                                                                A(
                                                                    classs="""dropdown-item""",
                                                                    href="""javascript:void(0)""",
                                                                    data=(
                                                                        """Remove""",
                                                                    ),
                                                                ),
                                                            ),
                                                        ),
                                                    ),
                                                ),
                                            ),
                                        ),
                                        Div(
                                            classs="""file-item""",
                                            data=(
                                                Div(
                                                    classs="""file-item-select-bg bg-primary""",
                                                ),
                                                Label(
                                                    classs="""file-item-checkbox custom-control custom-checkbox""",
                                                    data=(
                                                        Input(
                                                            typee="""checkbox""",
                                                            classs="""custom-control-input""",
                                                        ),
                                                        Span(
                                                            classs="""custom-control-label""",
                                                        ),
                                                    ),
                                                ),
                                                Div(
                                                    classs="""file-item-icon fab fa-html5 text-secondary""",
                                                ),
                                                A(
                                                    href="""javascript:void(0)""",
                                                    classs="""file-item-name""",
                                                    data=(
                                                        """
Index.html
""",
                                                    ),
                                                ),
                                                Div(
                                                    classs="""file-item-changed""",
                                                    data=("""02/19/2018""",),
                                                ),
                                                Div(
                                                    classs="""file-item-actions btn-group""",
                                                    data=(
                                                        Button(
                                                            typee="""button""",
                                                            classs="""btn btn-default btn-sm rounded-pill icon-btn borderless md-btn-flat hide-arrow dropdown-toggle""",
                                                            data_toggle="""dropdown""",
                                                            data=(
                                                                I(
                                                                    classs="""ion ion-ios-more""",
                                                                ),
                                                            ),
                                                        ),
                                                        Div(
                                                            classs="""dropdown-menu dropdown-menu-right""",
                                                            data=(
                                                                A(
                                                                    classs="""dropdown-item""",
                                                                    href="""javascript:void(0)""",
                                                                    data=(
                                                                        """Rename""",
                                                                    ),
                                                                ),
                                                                A(
                                                                    classs="""dropdown-item""",
                                                                    href="""javascript:void(0)""",
                                                                    data=("""Move""",),
                                                                ),
                                                                A(
                                                                    classs="""dropdown-item""",
                                                                    href="""javascript:void(0)""",
                                                                    data=("""Copy""",),
                                                                ),
                                                                A(
                                                                    classs="""dropdown-item""",
                                                                    href="""javascript:void(0)""",
                                                                    data=(
                                                                        """Remove""",
                                                                    ),
                                                                ),
                                                            ),
                                                        ),
                                                    ),
                                                ),
                                            ),
                                        ),
                                        Div(
                                            classs="""file-item""",
                                            data=(
                                                Div(
                                                    classs="""file-item-select-bg bg-primary""",
                                                ),
                                                Label(
                                                    classs="""file-item-checkbox custom-control custom-checkbox""",
                                                    data=(
                                                        Input(
                                                            typee="""checkbox""",
                                                            classs="""custom-control-input""",
                                                        ),
                                                        Span(
                                                            classs="""custom-control-label""",
                                                        ),
                                                    ),
                                                ),
                                                Div(
                                                    classs="""file-item-img""",
                                                    style="""background-image: url(https://bootdey.com/img/Content/avatar/avatar1.png);""",
                                                ),
                                                A(
                                                    href="""javascript:void(0)""",
                                                    classs="""file-item-name""",
                                                    data=(
                                                        """
Image-1.jpg
""",
                                                    ),
                                                ),
                                                Div(
                                                    classs="""file-item-changed""",
                                                    data=("""02/20/2018""",),
                                                ),
                                                Div(
                                                    classs="""file-item-actions btn-group""",
                                                    data=(
                                                        Button(
                                                            typee="""button""",
                                                            classs="""btn btn-default btn-sm rounded-pill icon-btn borderless md-btn-flat hide-arrow dropdown-toggle""",
                                                            data_toggle="""dropdown""",
                                                            data=(
                                                                I(
                                                                    classs="""ion ion-ios-more""",
                                                                ),
                                                            ),
                                                        ),
                                                        Div(
                                                            classs="""dropdown-menu dropdown-menu-right""",
                                                            data=(
                                                                A(
                                                                    classs="""dropdown-item""",
                                                                    href="""javascript:void(0)""",
                                                                    data=(
                                                                        """Rename""",
                                                                    ),
                                                                ),
                                                                A(
                                                                    classs="""dropdown-item""",
                                                                    href="""javascript:void(0)""",
                                                                    data=("""Move""",),
                                                                ),
                                                                A(
                                                                    classs="""dropdown-item""",
                                                                    href="""javascript:void(0)""",
                                                                    data=("""Copy""",),
                                                                ),
                                                                A(
                                                                    classs="""dropdown-item""",
                                                                    href="""javascript:void(0)""",
                                                                    data=(
                                                                        """Remove""",
                                                                    ),
                                                                ),
                                                            ),
                                                        ),
                                                    ),
                                                ),
                                            ),
                                        ),
                                        Div(
                                            classs="""file-item""",
                                            data=(
                                                Div(
                                                    classs="""file-item-select-bg bg-primary""",
                                                ),
                                                Label(
                                                    classs="""file-item-checkbox custom-control custom-checkbox""",
                                                    data=(
                                                        Input(
                                                            typee="""checkbox""",
                                                            classs="""custom-control-input""",
                                                        ),
                                                        Span(
                                                            classs="""custom-control-label""",
                                                        ),
                                                    ),
                                                ),
                                                Div(
                                                    classs="""file-item-img""",
                                                    style="""background-image: url(https://bootdey.com/img/Content/avatar/avatar6.png);""",
                                                ),
                                                A(
                                                    href="""javascript:void(0)""",
                                                    classs="""file-item-name""",
                                                    data=(
                                                        """
Image-2.png
""",
                                                    ),
                                                ),
                                                Div(
                                                    classs="""file-item-changed""",
                                                    data=("""02/21/2018""",),
                                                ),
                                                Div(
                                                    classs="""file-item-actions btn-group""",
                                                    data=(
                                                        Button(
                                                            typee="""button""",
                                                            classs="""btn btn-default btn-sm rounded-pill icon-btn borderless md-btn-flat hide-arrow dropdown-toggle""",
                                                            data_toggle="""dropdown""",
                                                            data=(
                                                                I(
                                                                    classs="""ion ion-ios-more""",
                                                                ),
                                                            ),
                                                        ),
                                                        Div(
                                                            classs="""dropdown-menu dropdown-menu-right""",
                                                            data=(
                                                                A(
                                                                    classs="""dropdown-item""",
                                                                    href="""javascript:void(0)""",
                                                                    data=(
                                                                        """Rename""",
                                                                    ),
                                                                ),
                                                                A(
                                                                    classs="""dropdown-item""",
                                                                    href="""javascript:void(0)""",
                                                                    data=("""Move""",),
                                                                ),
                                                                A(
                                                                    classs="""dropdown-item""",
                                                                    href="""javascript:void(0)""",
                                                                    data=("""Copy""",),
                                                                ),
                                                                A(
                                                                    classs="""dropdown-item""",
                                                                    href="""javascript:void(0)""",
                                                                    data=(
                                                                        """Remove""",
                                                                    ),
                                                                ),
                                                            ),
                                                        ),
                                                    ),
                                                ),
                                            ),
                                        ),
                                        Div(
                                            classs="""file-item""",
                                            data=(
                                                Div(
                                                    classs="""file-item-select-bg bg-primary""",
                                                ),
                                                Label(
                                                    classs="""file-item-checkbox custom-control custom-checkbox""",
                                                    data=(
                                                        Input(
                                                            typee="""checkbox""",
                                                            classs="""custom-control-input""",
                                                        ),
                                                        Span(
                                                            classs="""custom-control-label""",
                                                        ),
                                                    ),
                                                ),
                                                Div(
                                                    classs="""file-item-img""",
                                                    style="""background-image: url(https://bootdey.com/img/Content/avatar/avatar4.png);""",
                                                ),
                                                A(
                                                    href="""javascript:void(0)""",
                                                    classs="""file-item-name""",
                                                    data=(
                                                        """
Image-3.gif
""",
                                                    ),
                                                ),
                                                Div(
                                                    classs="""file-item-changed""",
                                                    data=("""02/22/2018""",),
                                                ),
                                                Div(
                                                    classs="""file-item-actions btn-group""",
                                                    data=(
                                                        Button(
                                                            typee="""button""",
                                                            classs="""btn btn-default btn-sm rounded-pill icon-btn borderless md-btn-flat hide-arrow dropdown-toggle""",
                                                            data_toggle="""dropdown""",
                                                            data=(
                                                                I(
                                                                    classs="""ion ion-ios-more""",
                                                                ),
                                                            ),
                                                        ),
                                                        Div(
                                                            classs="""dropdown-menu dropdown-menu-right""",
                                                            data=(
                                                                A(
                                                                    classs="""dropdown-item""",
                                                                    href="""javascript:void(0)""",
                                                                    data=(
                                                                        """Rename""",
                                                                    ),
                                                                ),
                                                                A(
                                                                    classs="""dropdown-item""",
                                                                    href="""javascript:void(0)""",
                                                                    data=("""Move""",),
                                                                ),
                                                                A(
                                                                    classs="""dropdown-item""",
                                                                    href="""javascript:void(0)""",
                                                                    data=("""Copy""",),
                                                                ),
                                                                A(
                                                                    classs="""dropdown-item""",
                                                                    href="""javascript:void(0)""",
                                                                    data=(
                                                                        """Remove""",
                                                                    ),
                                                                ),
                                                            ),
                                                        ),
                                                    ),
                                                ),
                                            ),
                                        ),
                                        Div(
                                            classs="""file-item""",
                                            data=(
                                                Div(
                                                    classs="""file-item-select-bg bg-primary""",
                                                ),
                                                Label(
                                                    classs="""file-item-checkbox custom-control custom-checkbox""",
                                                    data=(
                                                        Input(
                                                            typee="""checkbox""",
                                                            classs="""custom-control-input""",
                                                        ),
                                                        Span(
                                                            classs="""custom-control-label""",
                                                        ),
                                                    ),
                                                ),
                                                Div(
                                                    classs="""file-item-icon fab fa-js text-secondary""",
                                                ),
                                                A(
                                                    href="""javascript:void(0)""",
                                                    classs="""file-item-name""",
                                                    data=(
                                                        """
Main.js
""",
                                                    ),
                                                ),
                                                Div(
                                                    classs="""file-item-changed""",
                                                    data=("""02/23/2018""",),
                                                ),
                                                Div(
                                                    classs="""file-item-actions btn-group""",
                                                    data=(
                                                        Button(
                                                            typee="""button""",
                                                            classs="""btn btn-default btn-sm rounded-pill icon-btn borderless md-btn-flat hide-arrow dropdown-toggle""",
                                                            data_toggle="""dropdown""",
                                                            data=(
                                                                I(
                                                                    classs="""ion ion-ios-more""",
                                                                ),
                                                            ),
                                                        ),
                                                        Div(
                                                            classs="""dropdown-menu dropdown-menu-right""",
                                                            data=(
                                                                A(
                                                                    classs="""dropdown-item""",
                                                                    href="""javascript:void(0)""",
                                                                    data=(
                                                                        """Rename""",
                                                                    ),
                                                                ),
                                                                A(
                                                                    classs="""dropdown-item""",
                                                                    href="""javascript:void(0)""",
                                                                    data=("""Move""",),
                                                                ),
                                                                A(
                                                                    classs="""dropdown-item""",
                                                                    href="""javascript:void(0)""",
                                                                    data=("""Copy""",),
                                                                ),
                                                                A(
                                                                    classs="""dropdown-item""",
                                                                    href="""javascript:void(0)""",
                                                                    data=(
                                                                        """Remove""",
                                                                    ),
                                                                ),
                                                            ),
                                                        ),
                                                    ),
                                                ),
                                            ),
                                        ),
                                        Div(
                                            classs="""file-item""",
                                            data=(
                                                Div(
                                                    classs="""file-item-select-bg bg-primary""",
                                                ),
                                                Label(
                                                    classs="""file-item-checkbox custom-control custom-checkbox""",
                                                    data=(
                                                        Input(
                                                            typee="""checkbox""",
                                                            classs="""custom-control-input""",
                                                        ),
                                                        Span(
                                                            classs="""custom-control-label""",
                                                        ),
                                                    ),
                                                ),
                                                Div(
                                                    classs="""file-item-icon far fa-file text-secondary""",
                                                ),
                                                A(
                                                    href="""javascript:void(0)""",
                                                    classs="""file-item-name""",
                                                    data=(
                                                        """
MAKEFILE
""",
                                                    ),
                                                ),
                                                Div(
                                                    classs="""file-item-changed""",
                                                    data=("""02/24/2018""",),
                                                ),
                                                Div(
                                                    classs="""file-item-actions btn-group""",
                                                    data=(
                                                        Button(
                                                            typee="""button""",
                                                            classs="""btn btn-default btn-sm rounded-pill icon-btn borderless md-btn-flat hide-arrow dropdown-toggle""",
                                                            data_toggle="""dropdown""",
                                                            data=(
                                                                I(
                                                                    classs="""ion ion-ios-more""",
                                                                ),
                                                            ),
                                                        ),
                                                        Div(
                                                            classs="""dropdown-menu dropdown-menu-right""",
                                                            data=(
                                                                A(
                                                                    classs="""dropdown-item""",
                                                                    href="""javascript:void(0)""",
                                                                    data=(
                                                                        """Rename""",
                                                                    ),
                                                                ),
                                                                A(
                                                                    classs="""dropdown-item""",
                                                                    href="""javascript:void(0)""",
                                                                    data=("""Move""",),
                                                                ),
                                                                A(
                                                                    classs="""dropdown-item""",
                                                                    href="""javascript:void(0)""",
                                                                    data=("""Copy""",),
                                                                ),
                                                                A(
                                                                    classs="""dropdown-item""",
                                                                    href="""javascript:void(0)""",
                                                                    data=(
                                                                        """Remove""",
                                                                    ),
                                                                ),
                                                            ),
                                                        ),
                                                    ),
                                                ),
                                            ),
                                        ),
                                        Div(
                                            classs="""file-item""",
                                            data=(
                                                Div(
                                                    classs="""file-item-select-bg bg-primary""",
                                                ),
                                                Label(
                                                    classs="""file-item-checkbox custom-control custom-checkbox""",
                                                    data=(
                                                        Input(
                                                            typee="""checkbox""",
                                                            classs="""custom-control-input""",
                                                        ),
                                                        Span(
                                                            classs="""custom-control-label""",
                                                        ),
                                                    ),
                                                ),
                                                Div(
                                                    classs="""file-item-icon far fa-file-pdf text-secondary""",
                                                ),
                                                A(
                                                    href="""javascript:void(0)""",
                                                    classs="""file-item-name""",
                                                    data=(
                                                        """
Presentation.pdf
""",
                                                    ),
                                                ),
                                                Div(
                                                    classs="""file-item-changed""",
                                                    data=("""02/25/2018""",),
                                                ),
                                                Div(
                                                    classs="""file-item-actions btn-group""",
                                                    data=(
                                                        Button(
                                                            typee="""button""",
                                                            classs="""btn btn-default btn-sm rounded-pill icon-btn borderless md-btn-flat hide-arrow dropdown-toggle""",
                                                            data_toggle="""dropdown""",
                                                            data=(
                                                                I(
                                                                    classs="""ion ion-ios-more""",
                                                                ),
                                                            ),
                                                        ),
                                                        Div(
                                                            classs="""dropdown-menu dropdown-menu-right""",
                                                            data=(
                                                                A(
                                                                    classs="""dropdown-item""",
                                                                    href="""javascript:void(0)""",
                                                                    data=(
                                                                        """Rename""",
                                                                    ),
                                                                ),
                                                                A(
                                                                    classs="""dropdown-item""",
                                                                    href="""javascript:void(0)""",
                                                                    data=("""Move""",),
                                                                ),
                                                                A(
                                                                    classs="""dropdown-item""",
                                                                    href="""javascript:void(0)""",
                                                                    data=("""Copy""",),
                                                                ),
                                                                A(
                                                                    classs="""dropdown-item""",
                                                                    href="""javascript:void(0)""",
                                                                    data=(
                                                                        """Remove""",
                                                                    ),
                                                                ),
                                                            ),
                                                        ),
                                                    ),
                                                ),
                                            ),
                                        ),
                                        Div(
                                            classs="""file-item""",
                                            data=(
                                                Div(
                                                    classs="""file-item-select-bg bg-primary""",
                                                ),
                                                Label(
                                                    classs="""file-item-checkbox custom-control custom-checkbox""",
                                                    data=(
                                                        Input(
                                                            typee="""checkbox""",
                                                            classs="""custom-control-input""",
                                                        ),
                                                        Span(
                                                            classs="""custom-control-label""",
                                                        ),
                                                    ),
                                                ),
                                                Div(
                                                    classs="""file-item-icon far fa-file-alt text-secondary""",
                                                ),
                                                A(
                                                    href="""javascript:void(0)""",
                                                    classs="""file-item-name""",
                                                    data=(
                                                        """
README.txt
""",
                                                    ),
                                                ),
                                                Div(
                                                    classs="""file-item-changed""",
                                                    data=("""02/26/2018""",),
                                                ),
                                                Div(
                                                    classs="""file-item-actions btn-group""",
                                                    data=(
                                                        Button(
                                                            typee="""button""",
                                                            classs="""btn btn-default btn-sm rounded-pill icon-btn borderless md-btn-flat hide-arrow dropdown-toggle""",
                                                            data_toggle="""dropdown""",
                                                            data=(
                                                                I(
                                                                    classs="""ion ion-ios-more""",
                                                                ),
                                                            ),
                                                        ),
                                                        Div(
                                                            classs="""dropdown-menu dropdown-menu-right""",
                                                            data=(
                                                                A(
                                                                    classs="""dropdown-item""",
                                                                    href="""javascript:void(0)""",
                                                                    data=(
                                                                        """Rename""",
                                                                    ),
                                                                ),
                                                                A(
                                                                    classs="""dropdown-item""",
                                                                    href="""javascript:void(0)""",
                                                                    data=("""Move""",),
                                                                ),
                                                                A(
                                                                    classs="""dropdown-item""",
                                                                    href="""javascript:void(0)""",
                                                                    data=("""Copy""",),
                                                                ),
                                                                A(
                                                                    classs="""dropdown-item""",
                                                                    href="""javascript:void(0)""",
                                                                    data=(
                                                                        """Remove""",
                                                                    ),
                                                                ),
                                                            ),
                                                        ),
                                                    ),
                                                ),
                                            ),
                                        ),
                                        Div(
                                            classs="""file-item""",
                                            data=(
                                                Div(
                                                    classs="""file-item-select-bg bg-primary""",
                                                ),
                                                Label(
                                                    classs="""file-item-checkbox custom-control custom-checkbox""",
                                                    data=(
                                                        Input(
                                                            typee="""checkbox""",
                                                            classs="""custom-control-input""",
                                                        ),
                                                        Span(
                                                            classs="""custom-control-label""",
                                                        ),
                                                    ),
                                                ),
                                                Div(
                                                    classs="""file-item-icon fab fa-css3 text-secondary""",
                                                ),
                                                A(
                                                    href="""javascript:void(0)""",
                                                    classs="""file-item-name""",
                                                    data=(
                                                        """
Style.css
""",
                                                    ),
                                                ),
                                                Div(
                                                    classs="""file-item-changed""",
                                                    data=("""02/27/2018""",),
                                                ),
                                                Div(
                                                    classs="""file-item-actions btn-group""",
                                                    data=(
                                                        Button(
                                                            typee="""button""",
                                                            classs="""btn btn-default btn-sm rounded-pill icon-btn borderless md-btn-flat hide-arrow dropdown-toggle""",
                                                            data_toggle="""dropdown""",
                                                            data=(
                                                                I(
                                                                    classs="""ion ion-ios-more""",
                                                                ),
                                                            ),
                                                        ),
                                                        Div(
                                                            classs="""dropdown-menu dropdown-menu-right""",
                                                            data=(
                                                                A(
                                                                    classs="""dropdown-item""",
                                                                    href="""javascript:void(0)""",
                                                                    data=(
                                                                        """Rename""",
                                                                    ),
                                                                ),
                                                                A(
                                                                    classs="""dropdown-item""",
                                                                    href="""javascript:void(0)""",
                                                                    data=("""Move""",),
                                                                ),
                                                                A(
                                                                    classs="""dropdown-item""",
                                                                    href="""javascript:void(0)""",
                                                                    data=("""Copy""",),
                                                                ),
                                                                A(
                                                                    classs="""dropdown-item""",
                                                                    href="""javascript:void(0)""",
                                                                    data=(
                                                                        """Remove""",
                                                                    ),
                                                                ),
                                                            ),
                                                        ),
                                                    ),
                                                ),
                                            ),
                                        ),
                                        Div(
                                            classs="""file-item""",
                                            data=(
                                                Div(
                                                    classs="""file-item-select-bg bg-primary""",
                                                ),
                                                Label(
                                                    classs="""file-item-checkbox custom-control custom-checkbox""",
                                                    data=(
                                                        Input(
                                                            typee="""checkbox""",
                                                            classs="""custom-control-input""",
                                                        ),
                                                        Span(
                                                            classs="""custom-control-label""",
                                                        ),
                                                    ),
                                                ),
                                                Div(
                                                    classs="""file-item-icon far fa-file-audio text-secondary""",
                                                ),
                                                A(
                                                    href="""javascript:void(0)""",
                                                    classs="""file-item-name""",
                                                    data=(
                                                        """
Test.mp3
""",
                                                    ),
                                                ),
                                                Div(
                                                    classs="""file-item-changed""",
                                                    data=("""02/28/2018""",),
                                                ),
                                                Div(
                                                    classs="""file-item-actions btn-group""",
                                                    data=(
                                                        Button(
                                                            typee="""button""",
                                                            classs="""btn btn-default btn-sm rounded-pill icon-btn borderless md-btn-flat hide-arrow dropdown-toggle""",
                                                            data_toggle="""dropdown""",
                                                            data=(
                                                                I(
                                                                    classs="""ion ion-ios-more""",
                                                                ),
                                                            ),
                                                        ),
                                                        Div(
                                                            classs="""dropdown-menu dropdown-menu-right""",
                                                            data=(
                                                                A(
                                                                    classs="""dropdown-item""",
                                                                    href="""javascript:void(0)""",
                                                                    data=(
                                                                        """Rename""",
                                                                    ),
                                                                ),
                                                                A(
                                                                    classs="""dropdown-item""",
                                                                    href="""javascript:void(0)""",
                                                                    data=("""Move""",),
                                                                ),
                                                                A(
                                                                    classs="""dropdown-item""",
                                                                    href="""javascript:void(0)""",
                                                                    data=("""Copy""",),
                                                                ),
                                                                A(
                                                                    classs="""dropdown-item""",
                                                                    href="""javascript:void(0)""",
                                                                    data=(
                                                                        """Remove""",
                                                                    ),
                                                                ),
                                                            ),
                                                        ),
                                                    ),
                                                ),
                                            ),
                                        ),
                                        Div(
                                            classs="""file-item""",
                                            data=(
                                                Div(
                                                    classs="""file-item-select-bg bg-primary""",
                                                ),
                                                Label(
                                                    classs="""file-item-checkbox custom-control custom-checkbox""",
                                                    data=(
                                                        Input(
                                                            typee="""checkbox""",
                                                            classs="""custom-control-input""",
                                                        ),
                                                        Span(
                                                            classs="""custom-control-label""",
                                                        ),
                                                    ),
                                                ),
                                                Div(
                                                    classs="""file-item-icon far fa-file-video text-secondary""",
                                                ),
                                                A(
                                                    href="""javascript:void(0)""",
                                                    classs="""file-item-name""",
                                                    data=(
                                                        """
Tutorial.avi
""",
                                                    ),
                                                ),
                                                Div(
                                                    classs="""file-item-changed""",
                                                    data=("""03/01/2018""",),
                                                ),
                                                Div(
                                                    classs="""file-item-actions btn-group""",
                                                    data=(
                                                        Button(
                                                            typee="""button""",
                                                            classs="""btn btn-default btn-sm rounded-pill icon-btn borderless md-btn-flat hide-arrow dropdown-toggle""",
                                                            data_toggle="""dropdown""",
                                                            data=(
                                                                I(
                                                                    classs="""ion ion-ios-more""",
                                                                ),
                                                            ),
                                                        ),
                                                        Div(
                                                            classs="""dropdown-menu dropdown-menu-right""",
                                                            data=(
                                                                A(
                                                                    classs="""dropdown-item""",
                                                                    href="""javascript:void(0)""",
                                                                    data=(
                                                                        """Rename""",
                                                                    ),
                                                                ),
                                                                A(
                                                                    classs="""dropdown-item""",
                                                                    href="""javascript:void(0)""",
                                                                    data=("""Move""",),
                                                                ),
                                                                A(
                                                                    classs="""dropdown-item""",
                                                                    href="""javascript:void(0)""",
                                                                    data=("""Copy""",),
                                                                ),
                                                                A(
                                                                    classs="""dropdown-item""",
                                                                    href="""javascript:void(0)""",
                                                                    data=(
                                                                        """Remove""",
                                                                    ),
                                                                ),
                                                            ),
                                                        ),
                                                    ),
                                                ),
                                            ),
                                        ),
                                    ),
                                ),
                            ),
                        ),
                        Script(
                            src="""https://code.jquery.com/jquery-1.10.2.min.js""",
                        ),
                        Script(
                            src="./assets/js/bootstrap.min.js"
                        ),
                        Script(typee="""text/javascript""", data=()),
                    )
                ),
            ),
        )
    )
