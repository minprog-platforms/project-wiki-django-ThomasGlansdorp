from django.http import Http404
from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    entry_content = util.get_entry(title)
    if entry_content is None:
        raise Http404("requested page not found")
    return render(request, "encyclopedia/entry.html", {
        "entry": util.get_entry(title),
        "entry_title": title
    })

