from django.shortcuts import render

def render_home(req):
  return render(req, 'home.html')
