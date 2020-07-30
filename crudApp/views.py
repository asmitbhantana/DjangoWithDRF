from django.shortcuts import render

from .models import UserInfo
from .froms import UserInfoModelForm

from django.shortcuts import get_object_or_404, redirect


# Create your views here.
def list_all_user(request):
    data = UserInfo.objects.all()
    context = {
        'data': data,
    }
    return render(request, 'crudApp/list.html', context=context)


def detail_view_of_user(request, user_id):
    data = get_object_or_404(UserInfo, id=user_id)
    context = {'usr_object': data, }
    return render(request, 'crudApp/detail.html', context=context)


def create_user_info(request):
    if request.method == 'POST':
        form = UserInfoModelForm(request.POST)
        if form.is_valid():
            print("Valid Form")
            print(form.cleaned_data)
            form.save()
            return redirect('crudApp:user_list')
        else:
            print("Form is invalid!")
    form = UserInfoModelForm
    context = {
        'form': form
    }
    return render(request, 'crudApp/create.html', context=context)


def update_user_info(request, user_id):
    usr_object = get_object_or_404(UserInfo, id=user_id)
    if request.method == 'POST':
        form = UserInfoModelForm(request.POST, instance=usr_object)
        if form.is_valid():
            print("Valid Form")
            print(form.cleaned_data)
            form.save()
            return redirect('crudApp:user_detail', user_id)
        else:
            print("Form is invalid!")
    form = UserInfoModelForm(instance=usr_object)
    context = {
        'form': form
    }
    return render(request, 'crudApp/update.html', context=context)


def delete_user_info(request, user_id):
    usr_object = get_object_or_404(UserInfo, id=user_id)
    usr_object.delete()

    return redirect('crudApp:user_list')
