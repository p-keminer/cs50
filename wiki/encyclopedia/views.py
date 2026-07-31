from django.shortcuts import render,redirect
from django.http import HttpResponseNotFound
import markdown2
from random import choice
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    content = util.get_entry(title)
    if content is None:
        return HttpResponseNotFound("Entry not found!")
    else:
        return render(request, "encyclopedia/entry.html", {
            "title" : title,
            "content" : markdown2.markdown(content)
        })
    
def search(request):
    query = request.GET.get("q")
    content = util.get_entry(query)
    results = get_search_results(query)
    if content is None:
        return render(request, "encyclopedia/search.html", {
            "title" : query,
            "results" : results
        })
    else:
        return render(request, "encyclopedia/entry.html", {
            "title" : query,
            "content" : markdown2.markdown(content)
        })
    
def get_search_results(title):
    results = []
    for name in util.list_entries():
        if title.lower() in name.lower():
            results.append(name)
    return results

def new(request):
    return render(request, "encyclopedia/new.html", {
        })

def create(request):
    title = request.POST.get("title")
    content = request.POST.get("content")
    if len(get_search_results(title)) == 0:
        util.save_entry(title,content)
        return redirect("entry", title=title)
    else:
        return HttpResponseNotFound("Entry already existing")

def edit(request, title):
    content = util.get_entry(title)
    return render(request, "encyclopedia/edit.html", {
            "title" : title,
            "content" : content
        })

def save(request, title):
    content = request.POST.get("content")
    util.save_entry(title, content)
    return redirect("entry", title=title)

def random(request):
    entries = util.list_entries()
    random_page = choice(entries)
    return redirect("entry", title=random_page)
    