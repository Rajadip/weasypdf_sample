from django.template.loader import render_to_string
from weasyprint import HTML
from django.http import HttpResponse

# Create your views here.
def index(request):

    data = {
            "First Name":["Rajadip","Ruturaj","Pranali"],
            "Last Name":["Patil","Salokhe","Jadhav"],
            "Email":["raj@g.c","rutu@g.c","panu@g.c"],
            "Age":[21,22,23],
            "Salary":[3.5,4,4.5],
            "Gender":["Male","Male","Female"],
            "Date of Birth":["01 Jan, 1995","01 Feb,1995","03 March, 1995"],
            "City":["Kolhapur","Pune","Mumbai"],
            "Pincode":["461012","411022","400125"]
            }

    html_template = render_to_string("reporting/rajadip_assignment.html",{'data':data})
    pdf_file = HTML(string=html_template, base_url=request.build_absolute_uri()).write_pdf()
    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = 'filename="home_page.pdf"'
    return response
