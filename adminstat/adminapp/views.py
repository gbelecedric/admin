from django.shortcuts import render
from .models import EmailSubscriber
from django.utils import timezone
from datetime import timedelta
import random
# Create your views here.
def index(request):

    for i in range(0, 100):
        EmailSubscriber.objects.create(email=f"user_{i}@email.com", created_at=timezone.now() - timedelta(days=random.randint(0, 100)))
    ...

    data = {

    }
    return render(request,'pages/index.html', data)