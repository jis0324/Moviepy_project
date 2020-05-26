from django.shortcuts import render, redirect

def home(request):
  data = { 
    'page' : 'index', 
    "user" : request.user
  }
  if request.user.is_authenticated:
    print(request.user.username)
    print(request.user.email)
    print(request.user.password)
    print(request.user.name)
  else:
    print('NOT LOGIN')
  return render(request, 'home/index.html', data)

def services(request):

  data = { 
    'page' : 'service', 
    "user" : request.user
  }
  return render(request, 'home/services.html', data)

def about(request):

  data = { 
    'page' : 'about', 
    "user" : request.user
  }
  return render( request, 'home/about.html', data)

def contact(request):

  data = { 
    'page' : 'contact', 
    "user" : request.user
  }
  return render( request, 'home/contact.html', data)

def uploads(request, type):

  data = { 
    'upload_type' : type,
    "user" : request.user
  }
  if request.method == 'GET':
    request.session['type_'] = type
    return render( request, 'home/uploads.html', data )

  if request.method == 'POST':
    print('POST************')


# def handle_login(request):
#   user = request.user
#   print("user.user_type", user.__dict__)
#   try:
      # if user.is_superuser or user.user_type == 'superadmin':
      #     return redirect('/superadmin/')

      # if user.user_type == 'customer':
      #     return redirect('/customer/')
          
      # else:
      #     # import pdb;pdb.set_trace()
      #     # default
      #     print("Error .. Not valid login type ")
  #         return redirect('/accounts/logout/')
  # except:
  #     print("Not logged in .. redirect to login")
  #     return redirect('account_login')   
  # pass
