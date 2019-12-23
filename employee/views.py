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
from PyPDF2 import PdfFileMerger
from PyPDF2.generic import BooleanObject, NameObject, IndirectObject, NumberObject
from io import BytesIO
import PyPDF2
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



# Create your views here for family Health CArd.
def fam_show(request):
    files=[]
    out_dir = os.path.join(BASE_DIR,'scale.pdf')
    out_dir1 = os.path.join(BASE_DIR,'sam.pdf')
    if request.method=="POST":
        if 'print' in request.POST:
            for item in request.POST.getlist('my_object'):
                data =  fam_print(item)
                pdb.set_trace()
                path=write_fillable_pdf('family1.pdf',out_dir1, data)
                files.append(path)
            path=merger(files)
            file= FileResponse(open(path,'rb'))
            return file
    Families = Family.objects.all()
    return render(request, 'fam_show.html', {'Families': Families})


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


def fam_edit(request, id):
    famili = Family.objects.get(Fid=id)
    return render(request, 'fam_edit.html', {'famili': famili})


def fam_update(request, id):
    famili = Family.objects.get(Fid=id)
    form = FamilyForm(request.POST, instance=famili)
    form.save()
    return redirect("/fam_show")
    
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
 
def fam_destroy(request, id):
    famili = Family.objects.get(Fid=id)
    famili.delete()
    return redirect("/fam_show")

def fam_paid(request, id):
    famili = Family.objects.get(Fid=id)
    if famili.paid is False:
        famili.paid = True
        famili.save()
    return redirect("/fam_show")

# Create your views here for Individual Health Cards.

def ind_new(request):
    if request.method == "POST":
        form = IndividualForm1(request.POST)
        try:
            form.save()
            return redirect('/ind_show')
        except:
            pass
    else:
        form = IndividualForm1()
        return render(request, 'ind_add.html', {'form': form})


def ind_edit(request, id):
    indili = Individual.objects.get(Fid=id)
    return render(request, 'ind_edit.html', {'indily': indili})


def ind_update(request, id):
    Indili = Individual.objects.get(Fid=id)
    form = IndividualForm1(request.POST, instance=Indili)
    form.save()
    return redirect("/ind_show")

def ind_print(id):

    Indili = Individual.objects.get(Fid=id)
    Indili.pc = Indili.pc + 1
    Indili.save()

    data ={
        'Fid': 'AH/HC-I/0'+ str(Indili.Fid),
        'Fname1': Indili.Fname,
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



def ind_show(request):
    files=[]
    out_dir = os.path.join(BASE_DIR,'scale1.pdf')
    out_dir1 = os.path.join(BASE_DIR,'sam1.pdf')
    if request.method=="POST":
        if 'print' in request.POST:
            for item in request.POST.getlist('my_object'):
                data =  ind_print(item)
                path=write_fillable_pdf('self1.pdf',out_dir1, data)
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

def ind_paid(request, id):
    indili = Individual.objects.get(Fid=id)
    if indili.paid is False:
        indili.paid = True
        indili.save(update_fields=["paid"])
    return redirect("/ind_show")

# Create your views here for Generic Functions.

def back(request):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    out_dir = os.path.join(BASE_DIR,"back.pdf")
    filer = open(out_dir, 'rb')
    resp=FileResponse(filer)
    return resp

def write_fillable_pdf(file, output_pdf_path, data_dict):
    out_dir = os.path.join(BASE_DIR,"tmp/"+str(random.randrange(20, 200, 3))+".pdf")
    INVOICE_TEMPLATE_PATH = os.path.join(BASE_DIR,file)
    input_stream = open(INVOICE_TEMPLATE_PATH, "rb")
    pdf_reader = PyPDF2.PdfFileReader(input_stream, strict=False)
    if "/AcroForm" in pdf_reader.trailer["/Root"]:
        pdf_reader.trailer["/Root"]["/AcroForm"].update(
            {NameObject("/NeedAppearances"): BooleanObject(True)})
    pdf_writer = PyPDF2.PdfFileWriter()
    set_need_appearances_writer(pdf_writer)
    if "/AcroForm" in pdf_writer._root_object:
        # Acro form is form field, set needs appearances to fix printing issues
        pdf_writer._root_object["/AcroForm"].update(
            {NameObject("/NeedAppearances"): BooleanObject(True)})
    pdf_writer.addPage(pdf_reader.getPage(0))
    page = pdf_writer.getPage(0)
    pdf_writer.updatePageFormFieldValues(page, data_dict)
    for j in range(0, len(page['/Annots'])):
        writer_annot = page['/Annots'][j].getObject()
        for field in data_dict:
            # -----------------------------------------------------BOOYAH!
            if writer_annot.get('/T') == field:
                writer_annot.update({
                    NameObject("/Ff"): NumberObject(1)
                })
             # -----------------------------------------------------
    output_stream = BytesIO()
    pdf_writer.write(output_stream)
    with open(out_dir,'wb') as d: ## Open temporary file as bytes
        d.write(output_stream.read())
    input_stream.close()
    return out_dir

def merger(input_paths):
    output_path = os.path.join(BASE_DIR,"sample.pdf")
    pdf_merger = PdfFileMerger()
    file_handles = []
 
    for path in input_paths:
        pdf_merger.append(path)
 
    with open(output_path, 'wb') as fileobj:
        pdb.set_trace()
        pdf_merger.write(fileobj)
        return output_path



def pdf(request):
    template = os.path.join(BASE_DIR,"family1.pdf")

    outfile = os.path.join(BASE_DIR,"sample.pdf")

    input_stream = open(template, "rb")
    pdf_reader = PyPDF2.PdfFileReader(input_stream, strict=False)
    if "/AcroForm" in pdf_reader.trailer["/Root"]:
        pdf_reader.trailer["/Root"]["/AcroForm"].update(
            {NameObject("/NeedAppearances"): BooleanObject(True)})

    pdf_writer = PyPDF2.PdfFileWriter()
    set_need_appearances_writer(pdf_writer)
    if "/AcroForm" in pdf_writer._root_object:
        # Acro form is form field, set needs appearances to fix printing issues
        pdf_writer._root_object["/AcroForm"].update(
            {NameObject("/NeedAppearances"): BooleanObject(True)})

    data_dict = {
        'Fid': 'John\n',
        'Fname1': 'Smith\n',
        'Faadhar': 'mail@mail.com\n',
        'Fcontact': '889-998-9967\n',
        'Faddress1': 'Amazing Inc.\n',
        'Faddress2': 'Dev\n',
        'Faddress3': '123 Main Way\n',
        'Fration': 'Johannesburg\n',
        'Farogya': 'New Mexico\n',
        'Faadhar1': 96705,
        'from_date': 'USA\n',
        'to_date': 'Who cares...\n'

    }

    pdf_writer.addPage(pdf_reader.getPage(0))
    page = pdf_writer.getPage(0)
    pdf_writer.updatePageFormFieldValues(page, data_dict)
    for j in range(0, len(page['/Annots'])):
        writer_annot = page['/Annots'][j].getObject()
        for field in data_dict:
            # -----------------------------------------------------BOOYAH!
            if writer_annot.get('/T') == field:
                writer_annot.update({
                    NameObject("/Ff"): NumberObject(1)
                })
             # -----------------------------------------------------
    output_stream = BytesIO()
    pdf_writer.write(output_stream)

    response = HttpResponse(output_stream.getvalue(), content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="completed.pdf"'
    input_stream.close()

    return response


def set_need_appearances_writer(writer):
    try:
        catalog = writer._root_object
        # get the AcroForm tree and add "/NeedAppearances attribute
        if "/AcroForm" not in catalog:
            writer._root_object.update({
                NameObject("/AcroForm"): IndirectObject(len(writer._objects), 0, writer)})

        need_appearances = NameObject("/NeedAppearances")
        writer._root_object["/AcroForm"][need_appearances] = BooleanObject(True)


    except Exception as e:
        print('set_need_appearances_writer() catch : ', repr(e))

    return writer  
