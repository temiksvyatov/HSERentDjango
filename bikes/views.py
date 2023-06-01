from django.shortcuts import render, get_object_or_404
from .models import Bike
from django.core.paginator import Paginator


# Create your views here.
def bikes(request):
    bikes = Bike.objects.order_by('-created_date')
    paginator = Paginator(bikes, 4)
    page = request.GET.get('page')
    paged_bikes = paginator.get_page(page)

    model_search = Bike.objects.values_list('model', flat=True).distinct()
    city_search = Bike.objects.values_list('city', flat=True).distinct()
    year_search = Bike.objects.values_list('year', flat=True).distinct()
    body_style_search = Bike.objects.values_list('body_style', flat=True).distinct()

    data = {
        'bikes': paged_bikes,
        'model_search': model_search,
        'city_search': city_search,
        'year_search': year_search,
        'body_style_search': body_style_search,
    }
    return render(request, 'bikes/bikes.html', data)


def bike_detail(request, id):
    single_bike = get_object_or_404(Bike, pk=id)

    data = {
        'single_bike': single_bike,
    }
    return render(request, 'bikes/bike_detail.html', data)


def search(request):
    bikes = Bike.objects.order_by('-created_date')

    model_search = Bike.objects.values_list('model', flat=True).distinct()
    city_search = Bike.objects.values_list('city', flat=True).distinct()
    year_search = Bike.objects.values_list('year', flat=True).distinct()
    body_style_search = Bike.objects.values_list('body_style', flat=True).distinct()

    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            bikes = bikes.filter(description__icontains=keyword)

    if 'model' in request.GET:
        model = request.GET['model']
        if model:
            bikes = bikes.filter(model__iexact=model)

    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            bikes = bikes.filter(city__iexact=city)

    if 'year' in request.GET:
        year = request.GET['year']
        if year:
            bikes = bikes.filter(year__iexact=year)

    if 'body_style' in request.GET:
        body_style = request.GET['body_style']
        if body_style:
            bikes = bikes.filter(body_style__iexact=body_style)

    if 'min_price' in request.GET:
        min_price = request.GET['min_price']
        max_price = request.GET['max_price']
        if max_price:
            bikes = bikes.filter(price__gte=min_price, price__lte=max_price)

    data = {
        'bikes': bikes,
        'model_search': model_search,
        'city_search': city_search,
        'year_search': year_search,
        'body_style_search': body_style_search,
    }
    return render(request, 'bikes/search.html', data)
