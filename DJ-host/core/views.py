import os
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import FileUpload
from django .contrib.auth.models import User
from django.http import HttpResponse, Http404
def home(request):
    return render(request, 'home.html')

# Login view
def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(username=email, password=password)  
        if user is not None:
            login(request, user)
            print(f'Logged in as: {request.user.username}')
            return redirect('/dashbord/')  
        else:
            messages.error(request, 'Please check your username and password.')
            print('Please check your username and password.')

    return render(request, 'login.html')

# Signup view
def signup(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create(username=email)
        user.set_password(password)
        user.save()
        login(request,user)
        messages.success(request, "Signup successful. You can now log in.")
        return redirect('/file/')
    
    return render(request, 'singup.html')

# Files upload view
@login_required(login_url="/login/")
def files(request):
    if request.method == 'POST':
        user_uploaded_file = request.FILES.get('file')

        if user_uploaded_file:
            # Ensure the file is a ZIP file
            if not user_uploaded_file.name.endswith('.zip'):
                messages.error(request, 'Only ZIP files are allowed.')
                return render(request, 'file.html', {'username': request.user.username})
            
            # Save the file to the database using the FileUpload model
            try:
                obj = FileUpload.objects.create(user=request.user, file=user_uploaded_file)
                obj.save()
                messages.success(request, 'File uploaded and extracted successfully!')
                return redirect('/dashbord/')  # Redirect to the dashboard after upload
            except Exception as e:
                messages.error(request, f"Error processing the file: {str(e)}")
                return render(request, 'gg.html', {'username': request.user.username})
        else:
            messages.error(request, 'Please select a file to upload.')
            return render(request, 'file.html', {'username': request.user.username})

    return render(request, 'file.html', {'username': request.user.username})

# Dashboard view
@login_required(login_url="/login/")
def dash(request):
    return render(request, 'dash.html')

# Render uploaded file
def render_uploaded_file(request, username):
    user_extract_path = os.path.join(
        settings.MEDIA_ROOT,
        username,
        'extracted'
    )
    print(f"User extract path: {user_extract_path}")
    
    try:
        # Check if the directory exists
        if not os.path.isdir(user_extract_path):
            raise Http404("User extracted directory not found.")
        
        # Locate the index.html or the first .html file in the directory recursively
        target_file = find_html_file(user_extract_path)
        
        if target_file:
            with open(target_file, 'r') as file:
                html_content = file.read()
            
            # Fix paths for CSS and JS files
            html_content = fix_static_paths(html_content, user_extract_path, username)
            return HttpResponse(html_content)
        else:
            raise Http404("No .html files found in the user's extracted directory.")
    except Exception as e:
        return HttpResponse(f"Error rendering file: {str(e)}")

# Helper function to find HTML file
def find_html_file(directory):
    for root, _, files in os.walk(directory):
        # Prioritize index.html
        for file in files:
            if file == "index.html":
                return os.path.join(root, file)
        # Fallback to any .html file
        for file in files:
            if file.endswith(".html"):
                return os.path.join(root, file)
    return None

# Helper function to fix static file paths in HTML content
def fix_static_paths(html_content, user_extract_path, username):
    from bs4 import BeautifulSoup
    
    soup = BeautifulSoup(html_content, 'html.parser')
    
    for link in soup.find_all('link', {'rel': 'stylesheet'}):
        href = link.get('href')
        if href and not href.startswith(('http://', 'https://', settings.MEDIA_URL)):
            new_href = os.path.join(settings.MEDIA_URL, username, 'extracted', href)
            link['href'] = new_href
    
    for script in soup.find_all('script', {'src': True}):
        src = script.get('src')
        if src and not src.startswith(('http://', 'https://', settings.MEDIA_URL)):
            new_src = os.path.join(settings.MEDIA_URL, username, 'extracted', src)
            script['src'] = new_src
    
    return str(soup)


def user_logout(request):
    logout(request)
    return redirect ('/')