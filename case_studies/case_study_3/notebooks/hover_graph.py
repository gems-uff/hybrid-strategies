from snowballing.graph import Graph
from IPython.display import display, HTML, Javascript
from collections import defaultdict
from snowballing.operations import load_citations
import json


class HoverGraph(Graph):
    def display(self, *args):
        result = super(HoverGraph, self).display(*args)
        with self.output_widget:
            backward = defaultdict(list)
            forward = defaultdict(list)
            for cit in load_citations():
                backward[cit.work.metakey].append(cit.citation.metakey)
                forward[cit.citation.metakey].append(cit.work.metakey)
            display(HTML("""
            <textarea id='text-%s'></textarea> 
            """ % (self.graph_name,)))
            display(HTML("""
            <style>
            .backward-hover {
                stroke: red !important;
                stroke-width: 3px !important;
            }
            .forward-hover {
                stroke: green !important;
                stroke-width: 3px !important;
            }
            
            </style>
            
            """))
            code = """
                var backward = %s;
                var forward = %s;
                $("body").on("mouseover", "rect", function(){
                    var text = $('#text-%s');
                    text.val("");
                    var list = this.id + "\\n\\n";
                    var blist = backward[this.id];
                    var flist = forward[this.id];
                    if (blist != undefined) {
                        list += "Backward:\\n";
                        blist.forEach(function(value) {
                            var element = $("." + value)[0];
                            list += value + "\\n";
                            if (element != undefined) {
                                element.classList.add("backward-hover");
                            }
                        })
                        list += "\\n";
                    }
                    if (flist != undefined) {
                        list += "Forward:\\n";
                        flist.forEach(function(value) {
                            var element = $("." + value)[0];
                            list += value + "\\n";
                            if (element != undefined) {
                                element.classList.add("forward-hover");
                            }
                        })
                    }
                    text.val(list);
                });
                $("body").on("mouseout", "rect", function(){
                    var elements = $(".backward-hover, .forward-hover");
                    elements.each(function(index){
                        var element = elements[index];
                        element.classList.remove("forward-hover");
                        element.classList.remove("backward-hover");
                    })

                });
            
            """ % (json.dumps(backward), json.dumps(forward), self.graph_name)
            
            display(Javascript(code))
        return result
