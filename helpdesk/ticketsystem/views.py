from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def create_ticket(request):
    pass
@login_required
def ticket_list(request):
    pass
@login_required
def ticket_detail(request,ticket_id):
    pass
