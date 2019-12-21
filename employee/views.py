from django.shortcuts import render
import pdb
import datetime
import random 

# Create your views here.
from django.shortcuts import render, redirect
from employee.forms import  FamilyForm, IndividualForm, SearchForm, FamilyForm1, IndividualForm1
from employee.models import Individual, Family
import os
import pdfrw
from pdfrw import PdfReader, PdfWriter, PageMerge, IndirectPdfDict
from django.http import HttpResponse
from django.http import FileResponse
from employee.filters import FamilyFilter, IndividualFilter
import json
ANNOT_KEY = '/Annots'
ANNOT_FIELD_KEY = '/T'
ANNOT_VAL_KEY = '/V'
ANNOT_RECT_KEY = '/Rect'
SUBTYPE_KEY = '/Subtype'
WIDGET_SUBTYPE_KEY = '/Widget'
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Create your views here.
def fam_new(request):
    if request.method == "POST":
        form = FamilyForm1(request.POST)
        try:
            form.save()
            return redirect('/fam_show')
        except:
            pass
    else:
        form = FamilyForm()
    return render(request, 'fam_add.html', {'form': form})


def fam_show(request):
    files=[]
    out_dir = os.path.join(BASE_DIR,'scale.pdf')
    out_dir1 = os.path.join(BASE_DIR,'sam.pdf')
    if request.method=="POST":
        if 'print' in request.POST:
            for item in request.POST.getlist('my_object'):
                data =  fam_print(item)
                path=write_fillable_pdf('family.pdf',out_dir1, data)
                files.append(path)
            path=concatenate(files,out_dir)
            file= FileResponse(open(path,'rb'))
            return file
    Families = Family.objects.all()
    return render(request, 'fam_show.html', {'Families': Families})
    # family_filter = FamilyFilter(request.GET, queryset=Families)
    


def fam_edit(request, id):
    famili = Family.objects.get(Fid=id)
    return render(request, 'fam_edit.html', {'famili': famili})


def fam_update(request, id):
    famili = Family.objects.get(Fid=id)
    form = FamilyForm(request.POST, instance=famili)
    form.save()
    return redirect("/fam_show")
    

def fam_destroy(request, id):
    famili = Family.objects.get(Fid=id)
    famili.delete()
    return redirect("/fam_show")

# Create your views here.
def ind_new(request):
    if request.method == "POST":
        form = IndividualForm1(request.POST)
        try:
            form.save()
            return redirect('/ind_show')
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
    form.save()
    return redirect("/ind_show")
    

def write_fillable_pdf(file, output_pdf_path, data_dict):
    out_dir = os.path.join(BASE_DIR,"tmp/"+str(random.randrange(20, 50, 3))+data_dict['Fid']+".pdf")
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
    return out_dir


def ind_print(id):

    Indili = Individual.objects.get(Fid=id)
    Indili.pc = Indili.pc + 1
    Indili.save()

    data ={
        'Fid': 'AH/HC-I/0'+ str(Indili.Fid),
        'Fname': Indili.Fname,
        'Faadhar': Indili.Faadhar,
        'Fcontact': Indili.Fcontact,
        'Faddress1': Indili.Faddress1,
        'Faddress2':Indili.Faddress2,
        'Faddress3':Indili.Faddress3,
        'Fration':Indili.Fration,
        'Farogya':Indili.Farogya,
        'Faadhar1': Indili.Faadhar,
        'from_date': 'From:'+str((Indili.from_date).strftime("%b %d %Y")),
        'to_date': 'To:'+str((Indili.to_date).strftime("%b %d %Y")),
    }
    return data

def fam_print(id):

    Famili = Family.objects.get(Fid=id)
    Famili.pc = Famili.pc + 1
    Famili.save()
    data ={
        'Fid': 'AH/HC-F/0'+ str(Famili.Fid),
        'Fname': Famili.Fname,
        'Faadhar': Famili.Faadhar,
        'Fcontact': Famili.Fcontact,
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
        'Member_4_aadhar':Famili.Member_4_aadhar,
        'Faadhar1': Famili.Faadhar,
        'from_date': 'From:'+str((Famili.from_date).strftime("%b %d %Y")),
        'to_date': 'To:'+str((Famili.to_date).strftime("%b %d %Y")),
    }
    return data

def ind_show(request):
    files=[]
    out_dir = os.path.join(BASE_DIR,'scale1.pdf')
    out_dir1 = os.path.join(BASE_DIR,'sam1.pdf')
    if request.method=="POST":
        if 'print' in request.POST:
            for item in request.POST.getlist('my_object'):
                data =  fam_print(item)
                path=write_fillable_pdf('self.pdf',out_dir1, data)
                files.append(path)
            path=concatenate(files,out_dir)
            file= FileResponse(open(path,'rb'))
            return file
    Individuals = Individual.objects.all()
    return render(request, "ind_show.html", {'Individuals':Individuals})


def ind_destroy(request, id):
    indili = Individual.objects.get(Fid=id)
    indili.delete()
    return redirect("/ind_show")

def back(request):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    out_dir = os.path.join(BASE_DIR,"back.pdf")
    filer = open(out_dir, 'rb')
    resp=FileResponse(filer)
    return resp

def concatenate(paths, path1):
    writer = PdfWriter()
    out_dir = os.path.join(BASE_DIR,"sample.pdf")

    for path in paths:
        reader = PdfReader(path)
        writer.addpages(reader.pages)
 
    writer.trailer.Info = IndirectPdfDict(
        Title='Merged',
        Author='Bhargava Ganti',
        Subject='PDF Combinations',
        Creator='The Concatenator'
    )
 
    writer.write(out_dir)
    return out_dir