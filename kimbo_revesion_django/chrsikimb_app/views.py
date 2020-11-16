from django.shortcuts import render
from chrsikimb_app.models import User


from .forms import NewUserForm
# Create your views here.

def index(request):
    return render(request, 'chrsikimb_app/index.html')

def users(request):

    # user_list = User.objects.order_by('first_name')
    # user_dict = {'users': user_list}
    # return render(request, 'chrsikimb_app/users.html', context=user_dict)

    form = NewUserForm()

    if request.method =="POST":
        form =NewUserForm(request.POST)
        print(form)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('ERROR FORM INVALID')

    return render(request, 'chrsikimb_app/users.html', {'form':form})
