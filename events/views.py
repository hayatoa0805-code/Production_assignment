from django.shortcuts import render, redirect
from .models import Event
from goods.models import Goods
from .forms import EventForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

# Create your views here.
@login_required
def events_home_view(request):
    records = Event.objects.filter(user=request.user).order_by('-date')
    return render(request, 'events/events_home.html', {'records': records})

@login_required
def event_add_view(request):
    if request.method == "POST":
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save(commit=False)
            event.user = request.user
            event.save()
            return redirect('events:events_home')
    else:
        form = EventForm()
    return render(
        request,
        "events/events_add.html",
        {
            'form':form
        })

@login_required
def event_image_view(request, event_id):
    event = get_object_or_404(Event,event_id=event_id, user=request.user)
    event_id = event.event_id
    event_image = event.event_image

    return render(
        request,
        'events/events_image.html', 
        {
        'event': event,
        'event_id': event_id,
        'event_image':event_image,
    }
    )
@login_required
def events_detail_view(request,event_id):
    event = get_object_or_404(Event,event_id=event_id, user=request.user)
    return render(
        request,
        'events/events_detail.html',
        {
            'event':event,
            'event_id':event.event_id
        }
    )

@login_required
def events_edit_view(request, event_id):
    event = get_object_or_404(Event,event_id=event_id, user=request.user)

    if request.method == "POST":
        form = EventForm(request.POST, request.FILES,instance = event)
        if form.is_valid():
            event = form.save(commit=False)
            event.user = request.user
            event.save()
            return redirect('events:events_detail',event_id = event_id)
    else:
        form = EventForm(instance = event)
    return render(
        request,
        'events/events_edit.html',
        {
            'event':event,
            'event_id':event.event_id,
            'form':form
        }
    )

@login_required
def events_delete_view(request, event_id):
    event = get_object_or_404(Event,event_id=event_id, user=request.user)
    if request.method == "POST":
        event.delete()
        return redirect("events:events_home")
    
    return render(
        request,
        'events/events_delete.html',
        {
            'event':event,
            'event_id':event_id
        }
    )

@login_required
def goods_detail_view(request,event_id):
    event = get_object_or_404(Event,event_id=event_id, user=request.user)
    goods = Goods.objects.filter(user=request.user,event_id=event_id).order_by('goods_id')
    
    events_dict = {}

    for item in goods:
        event_name = item.event.title

        if event_name not in events_dict:
            events_dict[event_name] = {
                "goods_list": [],
                "goods_total": 0,
                "event_id": item.event_id,
            }

        events_dict[event_name]["goods_list"].append({
            "goods_name": item.goods_name,
            "price": item.price,
            "num": item.num,
            "total_price": item.total_price,
            "goods_id":item.goods_id
        })

        events_dict[event_name]["goods_total"] += item.total_price
    return render (request,"events/goods_detail.html",{"goods":goods,"event":event,"events_dict":events_dict,})

@login_required
def goods_plus_view(request, event_id, goods_id):
    goods = get_object_or_404(
        Goods,
        goods_id=goods_id,
        event__event_id=event_id,
        user=request.user
    )
    goods.num += 1
    goods.save()
    return redirect('events:goods_detail', event_id=event_id)

@login_required
def goods_minus_view(request, event_id, goods_id):
    goods = get_object_or_404(
        Goods,
        goods_id=goods_id,
        event__event_id=event_id,
        user=request.user
    )
    if goods.num > 1:
        goods.num -= 1
        goods.save()
    return redirect('events:goods_detail', event_id=event_id)