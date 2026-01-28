from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from events.models import Event
from .models import Goods
from .forms import GoodsForm,GoodsIdForm

# Create your views here.

@login_required
def goods_home_view(request):
    goods = Goods.objects.filter(user=request.user).order_by('goods_id')
    events_dict = {}

    for item in goods:
        event_name = item.event.title

        if event_name not in events_dict:
            events_dict[event_name] = {
                "goods_list": [],
                "event_total": 0,
                "event_id": item.event_id,
            }

        events_dict[event_name]["goods_list"].append({
            "goods_name": item.goods_name,
            "price": item.price,
            "num": item.num,
            "total_price": item.total_price,
            "goods_id":item.goods_id
        })

        events_dict[event_name]["event_total"] += item.total_price

    return render(
        request,
        "goods/goods_home.html",
        {
            "events_dict": events_dict
        }
    )

@login_required
def goods_add_view(request):
    if request.method =="POST":
        form = GoodsForm(request.POST,request.FILES)
        if form.is_valid():
            goods = form.save(commit=False)
            goods.user = request.user
            goods.save()
            return redirect('goods:goods_home')
    else:
        form = GoodsForm()
    return render (request,"goods/goods_add.html",{"form":form})

@login_required
def goods_id_add_view(request, event_id):
    event = get_object_or_404(Event, event_id=event_id, user=request.user)

    if request.method =="POST":
        form = GoodsIdForm(request.POST,request.FILES)
        if form.is_valid():
            goods = form.save(commit=False)
            goods.user = request.user
            goods.event = event
            goods.save()
            return redirect(
                'events:events_detail',
                event_id = event.event_id
                )
    else:
        form = GoodsIdForm()
    return render (
        request,
        "goods/goods_id_add.html",
        {
            "form": form,
            "event_id": event_id,
            "event": event
            }
        )

@login_required
def goods_edit_view(request, event_id, goods_id):
    event = get_object_or_404(
        Event,
        event_id=event_id,
        user=request.user
    )

    goods = get_object_or_404(
        Goods,
        goods_id=goods_id,
        event__event_id=event_id,
        user=request.user
    )

    if request.method == "POST":
        form = GoodsForm(request.POST, request.FILES, instance=goods)
        if form.is_valid():
            form.save()
            return redirect('events:goods_detail', event_id=event_id)
    else:
        form = GoodsForm(instance=goods)

    return render(
        request,
        'goods/goods_edit.html',
        {
        'form': form,
        'event': event,
        'goods': goods,
        }
        )

@login_required
def goods_delete_view(request, event_id, goods_id):
    goods = get_object_or_404(
        Goods,
        goods_id=goods_id,
        event__event_id=event_id,
        user=request.user
    )

    if request.method == "POST":
        goods.delete()
        return redirect(
            'events:events_detail',
            event_id=event_id
            )

    return render(
        request,
        'goods/goods_delete_confirm.html',
        {
        'goods': goods,
        'event_id': event_id,
        }
        )