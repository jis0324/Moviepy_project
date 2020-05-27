from django.shortcuts import render, redirect

def home(request):
  data = { 
    'page' : 'index', 
  }
  return render(request, 'home/index.html', data)

def services(request):

  data = { 
    'page' : 'service', 
  }
  return render(request, 'home/services.html', data)

def about(request):

  data = { 
    'page' : 'about', 
  }
  return render( request, 'home/about.html', data)

def contact(request):

  data = { 
    'page' : 'contact', 
  }
  return render( request, 'home/contact.html', data)

def uploads(request, type):

  data = { 
    'upload_type' : type,
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
