from django.shortcuts import render
import json
from kakao.models import Geocafe
from django.db.models import Q

def index(request):
    # cafe_list = Geocafe.objects.all(pk=geocafe_id)
    cafe_list = Geocafe.objects.all()

    search_key = request.GET.get('search_key')
    if search_key :
        cafe_list = cafe_list.filter(name__icontains=search_key)
        cafe_list_1 = list(cafe_list.values())
        cafe_list_2 = cafe_list_1[0:1000]
        cafeJson = json.dumps(cafe_list_2, ensure_ascii=False)
        return render(request, 'index.html', {'cafeJson': cafeJson})
    else:
        cafe_list_1 = list(cafe_list.values())
        cafe_list_2 = cafe_list_1[0:1000]
        cafeJson = json.dumps(cafe_list_2, ensure_ascii=False)
        return render(request, 'index.html', {'cafeJson': cafeJson})

# 로그인
def home(request):
    return render(request, 'index.html')
