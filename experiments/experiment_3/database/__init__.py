from pathlib import Path
from snowballing import config

### Database path. Do not change it unless you know what you are doing
config.DATABASE_DIR = Path(__file__).parent.resolve()

### Text editior path
config.TEXT_EDITOR = "C:\\Program Files\\Sublime Text 3\\sublime_text.exe"
### Text editor argument for opening in a given line.
### Use a format string with arguments {year_path} and {line}
config.LINE_PARAMS = "{year_path}:{line}"

### List of possible work class tuples
### Each tuple has the follwing elements:
###   Class Name
###   Category name
###   Graph visibility (Options: display, hide, always_hide)
###   Graph node color
###   Graph node text color
config.CLASSES = [
    ("WorkSnowball", "snowball", "display", "#6DCE9E", "white"),
    ("WorkUnrelated", "unrelated", "hide", "#DE9BF9", "white"),
    ("Work", "work", "hide", "#FFD86E", "black"),
    ("WorkOk", "ok", "hide", "#68BDF6", "white"),
    ("WorkNoFile", "nofile", "hide", "#A5ABB6", "white"),
    ("WorkLang", "lang", "hide", "#ff8040", "white"),
    ("Site", "site", "hide", "#000080", "white"),
    ("Email", "site", "hide", "#000080", "white"),
]
### Default class for insertion
config.DEFAULT_CLASS = "Work"

### Similary Ration for matching places
config.SIMILARITY_RATIO = 0.8

### Debug fields during BibTeX export
config.DEBUG_FIELDS = True

### List of exportable work fields to BibTeX
config.WORK_FIELDS = [
    "entrytype", "year", "name", "authors", "place",
    "booktitle", "bookauthors", "edition", "available",
    "volume", "number", "section", "pp", "article",
    "doi", "isbn",  "proceedings", "issn",
    "organization", "publisher", "school", "institution", "track",
    "ref", "local", "editors", "awards",
    "special", "website", "link", "scholar", "shorttitle", "address", "dglibrary", "references", "citations",

    "scopus", "acm", "ieee", "gs", "sciencedirect", "elcompendex", "webofscience", "springer",
    "placex", "seed_set", "selected_snowballing", "final_selected", "selected_order", 
    "scopus2015", "acm2015", "ieee2015", "sciencedirect2015", "elcompendex2015", "webofscience2015", "springer2015",
    "googlescholar2016", "scopus2016", "springer2016", "acm2016", "sciencedirect2016", "wiley2016", "webofscience2016", "ieee2016",
    "gs2016",
    #seed_set = estudo que pertence ao seed set;
    #selected_snowballing = estudo selecionado durante o snowballing;
    #final_selected = estudo selecionado após aplicação do snowballing, segundo critério de exclusão do artigo reproduzido;
    #selected_order = ordem de seleção no artigo reproduzido;
    #scopus2015 = estudo recuperado pela biblioteca digital scopus em 2015 (proveniencia entregue pelos autores).
]

### Ignore fields when exporting to BibTeX
### Regexes that starts with ^ and ends with $
config.BIBTEX_IGNORE_FIELDS = [
    "excerpt", "month", "bookname", "url", "ID", 

    # Tool
    "_.*", "force_.*", "file.*", "category", "alias", "aliases", "scholar_ok",
    "scholar", "cluster_id", "scholar_id", "display", "metakey", "due", "tyear",
    "citation_file", "notes", "tracking", "snowball", "request", "draw",
    "may_be_related_to", "ignore", "generate_title", "note",

    # Extra
    "summary", "star", "approach_name", "other1", "document_type", "source", "art_number",
    "keyword", "acmid", "artnumber", "location", "numpages", "series", "editor", "issue_date",
    "journal", "day", "key", "page_count", "articleno", "copyright", "language", "bookgroupauthor",
    "uniqueid","scopus_search","springer_search", "wiley_search","sciencedirect_search",
    "acm_search","webofscience_search","ieee_search", "googlescholar_search","planilha_googlescholar2016", 
    "planilha_scopus2016", "planilha_springer2016", "planilha_acm2016", "planilha_sciencedirect2016", 
    "planilha_wiley2016", "planilha_webofscience2016", "planilha_ieee2016",

 
]


### Map Work to BibTeX
config.WORK_BIBTEX_MAP = {
    "name": lambda x: "title",
    "authors": lambda x: "author",
    "local": lambda x: "address",
    "organization": lambda x: "publisher",
    "pp": lambda x: "pages",
    "entrytype": lambda x: "ENTRYTYPE",
    "place": lambda x: {
        "incollection": "booktitle",
        "inproceedings": "booktitle",
        "misc": "booktitle",
        "article": "journal",
        "conference": "inproceedings",
        "inbook": "",
        "book": "",
        "mastersthesis": "",
        "phdthesis": "",
        "techreport": "",
        "Thesis": "",
        "": ""
    }.get(getattr(x, "entrytype", ""), "")
}

### List of rows with form buttons (I suggest using no more than 4 per row)
### The form button is a tuple with two elements:
###  Label
###   Map of form widgets to value
config.FORM_BUTTONS = [
    [
        (
            "Unrelated: Scripts", {
                "due_widget": "Unrelated to scripts",
                "file_field_widget": True,
            }
        ),
        (
            "Unrelated: Provenance", {
                "due_widget": "Unrelated to provenance",
                "file_field_widget": True,
            }
        ),
        (
            "Both", {
                "due_widget": "Unrelated to scripts. Unrelated to provenance",
                "file_field_widget": True,
            }
        ),
        (
            "Ok", {
                "work_type_widget": "WorkOk",
                "file_field_widget": True,
            }
        ),
    ],
]

### List of text fields in forms
### Each tuple has 3 fields
###   Label
###   Work attribute
###   Widget variable (use none if you do not want a variable)
config.FORM_TEXT_FIELDS = [
    ("Related", "may_be_related_to", None),
    ("Display", "display", None),
    ("Summary", "summary", None),
    ("Star", "star", None),
    ("Link", "link", None),
]

### Module setting. Do not change it
from . import places, work, citations, groups

config.MODULES["places"] = places
config.MODULES["work"] = work
config.MODULES["citations"] = citations
config.MODULES["groups"] = groups

