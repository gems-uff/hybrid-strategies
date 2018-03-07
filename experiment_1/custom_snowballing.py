from snowballing import config
from ipywidgets import HBox, VBox
from itertools import zip_longest
from snowballing.snowballing import ArticleNavigator
from snowballing.snowballing import ForwardSnowballing

class UnrelatedInsert(ArticleNavigator):

    def __init__(self, database, *args, **kwargs):
        
        super(UnrelatedInsert, self).__init__(*args, **kwargs)
        self.create_custom_text((database, database, "database_widget"),)
        
        widgets = [
            self.work_type_widget, self.file_field_widget,
            self.due_widget, self.place_widget,
            self.year_widget, self.prefix_widget,
            self.pdfpage_widget,
        ] + self.custom_widgets

        hboxes = [
            HBox([
                self.previous_article_widget,
                self.reload_article_widget,
                self.next_article_widget
            ]),
        ]

        iterable = iter(widgets)
        for w1, w2 in zip_longest(iterable, iterable):
            hboxes.append(HBox([w1] + ([w2] if w2 else [])))

        hboxes.append(HBox([
            self.reload_article_widget,
            self.selector_widget,
            self.article_number_widget
        ]))

        hboxes.append(self.output_widget)

        self.view = VBox(hboxes)
        self.database_widget.value = "1"
        
    def erase_article_form(self):
        super(UnrelatedInsert, self).erase_article_form()
        self.work_type_widget.value = "WorkUnrelated"
        if hasattr(self, "database_widget"):
            self.database_widget.value = "1"

    def show_article(self, article, nwork, info):
        info['placex'] = info.get('place1')
        if not 'place' in info:
            info['place'] = 'FAKE'
        return super().show_article(article, nwork, info)

def decorate_erase(self, original):
    def erase_article_form():
        original()
        self.work_type_widget.value = "WorkUnrelated"
    return erase_article_form

class UnrelatedForward(ForwardSnowballing):
    
    def __init__(self, *args, **kwargs):
        super(UnrelatedForward, self).__init__(*args, **kwargs)
        self.navigator.erase_article_form = decorate_erase(self.navigator, self.navigator.erase_article_form)
        self.navigator.erase_article_form()
