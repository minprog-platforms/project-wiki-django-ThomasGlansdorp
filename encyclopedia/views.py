from django.http import Http404
from django.shortcuts import render, redirect

from . import util


def index(request):
    all_entries = util.list_entries()
    query = request.GET.get("q", "")
    if query is not "" and query in all_entries:
        return redirect(f"wiki/{query}")
    entries = []
    for entry in all_entries:
        if query in entry:
            entries.append(entry)
    return render(request, "encyclopedia/index.html", {
        "entries": entries
    })


def wiki_entry(request, title):
    entry_content = util.get_entry(title)
    if entry_content is None:
        raise Http404("requested page not found")
    return render(request, "encyclopedia/entry.html", {
        "entry": util.get_entry(title),
        "entry_title": title
    })

