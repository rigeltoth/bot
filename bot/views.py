from django.shortcuts import render

def render_bots(req):
  return render(req, 'bots.html')
