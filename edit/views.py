from django.shortcuts import render, redirect, get_object_or_404
# from edit.models import *
from kakao.models import Geocafe
from edit.forms import ShopForm


# def shop_list(request):
#     shop = Geocafe.objects.all().order_by('id')
#
#     return render(request, 'edit/shoplist.html', {'shop': shop})


def shop_detail(request, geocafe_id):
    shop = Geocafe.objects.get(pk=geocafe_id)
    # shop = get_object_or_404(ShopInfo, pk=shopinfo_id)
    # shop.save()

    return render(request, 'edit/detail.html', {'shop': shop})


def shop_delete(request, geocafe_id):  # 폐업 인지 아닌지 정보 수정.
    shop = get_object_or_404(Geocafe, pk=geocafe_id)
    Geocafe.objects.filter(id=geocafe_id).delete()

    return render(request, 'edit/delete.html')


def shop_update(request, geocafe_id):
    shop = Geocafe.objects.get(pk=geocafe_id)

    if request.method == 'POST':
        shop_form = ShopForm(request.POST, instance=shop)

        if shop_form.is_valid():
            # Geocafe.objects.filter(id=geocafe_id).delete()
            obj = shop_form.save(commit=False)
            obj.save()
            return redirect('home')

    # GET 방식.
    if request.method == 'GET':
        shop_form = ShopForm(instance=shop)

        return render(request, 'edit/update.html', {'shop_form': shop_form})



def test(request):
    return render(request, 'edit/test.html')