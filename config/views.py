from django.shortcuts import render
from records.search.record_search import BirthRecordSearch, DeathRecordSearch

def search_birth_records(request):
    if request.htmx:
        filters = {
            "first_name": request.GET.get("first_name", ""),
            "last_name": request.GET.get("last_name", ""),
            "birth_county": request.GET.get("birth_county", ""),
        }
        results = BirthRecordSearch.search(filters)
        context = {"results": results}
        return render(request, 'birth_results.html', context)
    else:
        return render(request, 'search_birth.html')
    
def search_death_records(request):
    if request.htmx:
        filters = {
            "first_name": request.GET.get("first_name", ""),
            "last_name": request.GET.get("last_name", ""),
            "death_county": request.GET.get("death_county", ""),
        }
        results = DeathRecordSearch.search(filters)
        context = {"results": results}
        return render(request, 'death_results.html', context)
    else:
        return render(request, 'search_death.html')

def search_marriage_records(request):
    if request.htmx:
        context = {'results': []}
        return render(request, 'marriage_results.html', context)
    else:
        return render(request, 'search_marriage.html')
