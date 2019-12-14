from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from employee.forms import  FamilyForm, IndividualForm
from employee.models import Individual, Family
import os
import pdb
import pdfrw
from django.http import HttpResponse
from django.http import FileResponse
ANNOT_KEY = '/Annots'
ANNOT_FIELD_KEY = '/T'
ANNOT_VAL_KEY = '/V'
ANNOT_RECT_KEY = '/Rect'
SUBTYPE_KEY = '/Subtype'
WIDGET_SUBTYPE_KEY = '/Widget'

# Create your views here.
def fam_new(request):
    if request.method == "POST":
        pdb.set_trace()
        form = FamilyForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/')
            except:
                pass
    else:
        form = FamilyForm()
    return render(request, 'fam_add.html', {'form': form})


def fam_show(request):
    Families = Family.objects.all()
    Individuals = Individual.objects.all()
    return render(request, "fam_show.html", {'Families': Families, 'Individuals':Individuals})


def fam_edit(request, id):
    famili = Family.objects.get(Fid=id)
    return render(request, 'fam_edit.html', {'famili': famili})


def fam_update(request, id):
    famili = Family.objects.get(Fid=id)
    form = FamilyForm(request.POST, instance=famili)
    if form.is_valid():
        form.save()
        return redirect("/")
    return render(request, 'fam_edit.html', {'famili': famili})


def fam_destroy(request, id):
    famili = Family.objects.get(Fid=id)
    famili.delete()
    return redirect("/")

# Create your views here.
def ind_new(request):
    if request.method == "POST":
        form = IndividualForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/')
            except:
                pass
    else:
        form = IndividualForm()
    return render(request, 'ind_add.html', {'form': form})


def ind_edit(request, id):
    indili = Family.objects.get(Fid=id)
    return render(request, 'ind_edit.html', {'indily': indili})


def ind_update(request, id):
    Indili = Individuals.objects.get(Fid=id)
    form = IndividualForm(request.POST, instance=Indili)
    if form.is_valid():
        form.save()
        return redirect("/")
    return render(request, 'ind_edit.html', {'Indili': Indili})


def write_fillable_pdf(file, output_pdf_path, data_dict):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    out_dir = os.path.join(BASE_DIR,"tmp/"+data_dict['Faadhar']+".pdf")
    INVOICE_TEMPLATE_PATH = os.path.join(BASE_DIR,file)
    template_pdf = pdfrw.PdfReader(INVOICE_TEMPLATE_PATH)
    annotations = template_pdf.pages[0][ANNOT_KEY]
    for annotation in annotations:
        if annotation[SUBTYPE_KEY] == WIDGET_SUBTYPE_KEY:
            if annotation[ANNOT_FIELD_KEY]:
                key = annotation[ANNOT_FIELD_KEY][1:-1]
                if key in data_dict.keys():
                    annotation.update(
                        pdfrw.PdfDict(V='{}'.format(data_dict[key]))
                    )
    pdfrw.PdfWriter().write(out_dir, template_pdf)
    filer = open(out_dir, 'rb')
    resp=FileResponse(filer)
    return resp


def ind_print(request, id):
    Indili = Individuals.objects.get(Fid=id)
    data ={
        'Fid': 'AH/HC/I00'+ str(Indili.Fid),
        'Fname': Indili.Fname,
        'Fcontact': Indili.Fcontact,
        'Faadhar': Indili.Faadhar,
        'Faddress1': Indili.Faddress1,
        'Faddress2':Indili.Faddress2,
        'Faddress3':Indili.Faddress3,
        'Fration':Indili.Fration,
        'Farogya':Indili.Farogya
    }

    filer= write_fillable_pdf('indi.pdf','output.pdf', data)
    return filer

def fam_print(request, id):
    Famili = Family.objects.get(Fid=id)
    data ={
        'Fid': 'AH/HC/S00'+ str(Famili.Fid),
        'Fname': Famili.Fname,
        'Fcontact': Famili.Fcontact,
        'Faadhar': Famili.Faadhar,
        'Faddress1': Famili.Faddress1,
        'Faddress2':Famili.Faddress2,
        'Faddress3':Famili.Faddress3,
        'Fration':Famili.Fration,
        'Farogya':Famili.Farogya,
        'Member_1_name':Famili.Member_1_name,
        'Member_2_name':Famili.Member_2_name,
        'Member_3_name':Famili.Member_3_name,
        'Member_4_name':Famili.Member_4_name,
        'Member_1_aadhar':Famili.Member_1_aadhar,
        'Member_2_aadhar':Famili.Member_2_aadhar,
        'Member_3_aadhar':Famili.Member_3_aadhar,
        'Member_4_aadhar':Famili.Member_4_aadhar
    }
   
    filer=write_fillable_pdf('fami.pdf','output.pdf', data)
    return filer


def ind_destroy(request, id):
    indili = Family.objects.get(Fid=id)
    indili.delete()
    return redirect("/")