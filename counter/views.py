from django.shortcuts import render, redirect
from .models import Food, User, Consume
from django.contrib import messages
from datetime import datetime
from django.utils import timezone


# Create your views here.
def index(request):
    foods = Food.objects.all()
    try:
        user = request.user
        consumed_foods = Consume.objects.filter(user=user)
    except:
        consumed_foods = {}

    # creating context to render
    context = {
        "foods" : foods,
        "consumed_foods": consumed_foods
    }

    # when form is submitted
    if request.method == 'POST':
        food_passed = False #flag for verfiying selected food

        try:
            # verification
            food_pk = int(request.POST.get('food_consumed'))
            food = Food.objects.get(pk=food_pk)
            food_passed = True # passed
        except:
            # error due to invalid food_pk so send it as message
            messages.warning(request, "Invalid food selected.")

        # adding food consumed by user in Consumed only if food is verified
        if food_passed:
            try:
                # checking user
                user = request.user
                consumed = Consume(user=user, food=food, consumed_at=timezone.now())
                consumed.save()

                # sending success message as food is consumed
                messages.success(request, f'🎉Yayy! {user} consumed {food.name}')
            except Exception as e:
                # exception caught, send user error
                print(e)
                messages.warning(request, "User not logged in.")



    return render(request, 'counter/index.html', context=context)


def add_food(request):
    import json
    with open('counter/foods.json') as r:
        data = json.load(r)

    count = 0
    for food in data:
        name = f'{food["name"]} - {food["serving_size"]}'

        try:
            search = Food.objects.get(name=name)
        except:
            f = Food(
                name=name,
                carbohydrates=food["carbohydrates"],
                protein=food["protein"],
                fat=food["fat"],
                fiber=food["fiber"],
                calories=food["calories"]
            )

            f.save()
            count += 1
    messages.success(request, f'{count} foods added successfully.')
    foods = Food.objects.all()

    # creating context to render
    context = {
        "foods" : foods
    }
    return render(request, 'counter/index.html', context=context)


def delete_consume(request, id):
    try:
        consumed_food = Consume.objects.get(pk=id)
        consumed_food.delete()
        messages.success(request, f'{consumed_food.food.name} removed!')
    except:
        messages.warning(request, f'Invalid consumed item')
    return redirect('/')
