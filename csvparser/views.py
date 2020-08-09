import csv, io
import logging
from django.shortcuts import render
from django.contrib import messages
from .models import UserProfile
from utils.helpers import change_date_format
logger = logging.getLogger(__name__)

def profile_upload(request):
    template = "profile_upload.html"
    data = UserProfile.objects.all()

    prompt = {
        'profiles': data
    }
    if request.method == "GET":
        return render(request, template, prompt)
    csv_file = request.FILES['file']
    data_set = csv_file.read().decode('UTF-8')

    io_string = io.StringIO(data_set)
    next(io_string)

    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = UserProfile.objects.update_or_create(
            first_name=column[0],
            last_name=column[1],
            birthday=change_date_format(column[2]),
            registration_date=change_date_format(column[3])
        )

    context = {}
    return render(request, template, context)

