from django.http import HttpResponse
from django.shortcuts import render
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import io

from django.template.loader import render_to_string
from django.http import HttpResponse
import tempfile


def home(request):
    return render(request, "form.html")

import pdfkit
from django.http import HttpResponse
from django.template.loader import render_to_string

path_to_wkhtml = r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"
config = pdfkit.configuration(wkhtmltopdf=path_to_wkhtml)

def generate_pdf(request):
    if request.method == "POST":
        context = {
            # Person 1 Details
            "person1_name": request.POST.get("person1_name"),
            "person1_dob": request.POST.get("person1_dob"),
            "person1_birth_time": request.POST.get("person1_birth_time"),
            "person1_birth_place": request.POST.get("person1_birth_place"),
            "person1_rashi": request.POST.get("person1_rashi"),
            "person1_nakshatra": request.POST.get("person1_nakshatra"),
            
            # Person 2 Details
            "person2_name": request.POST.get("person2_name"),
            "person2_dob": request.POST.get("person2_dob"),
            "person2_birth_time": request.POST.get("person2_birth_time"),
            "person2_birth_place": request.POST.get("person2_birth_place"),
            "person2_rashi": request.POST.get("person2_rashi"),
            "person2_nakshatra": request.POST.get("person2_nakshatra"),
            
            # Guna Matching Score
            "guna_score": request.POST.get("guna_score"),
            "summary": request.POST.get("summary"),
        }

        return render(request, "pdf_template.html", context)

    return HttpResponse("Invalid Request")