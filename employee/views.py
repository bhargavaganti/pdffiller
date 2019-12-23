from django.shortcuts import render
import pdb
import datetime
import random 
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.shortcuts import render, redirect
from employee.forms import  FamilyForm, IndividualForm, SearchForm, FamilyForm1, IndividualForm1
from employee.models import Individual, Family
import os
import pdfrw
from pdfrw import PdfReader, PdfWriter, PageMerge, IndirectPdfDict, PdfName
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


@login_required
# Create your views here for family Health CArd.
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
            path=merge_pdf_files_pdfrw(files,out_dir)
            file= FileResponse(open(path,'rb'))
            return file
    Families = Family.objects.all()
    return render(request, 'fam_show.html', {'Families': Families})

@login_required
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

@login_required
def fam_edit(request, id):
    famili = Family.objects.get(Fid=id)
    return render(request, 'fam_edit.html', {'famili': famili})

@login_required
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

@login_required 
def fam_destroy(request, id):
    famili = Family.objects.get(Fid=id)
    famili.delete()
    return redirect("/fam_show")

@login_required
def fam_paid(request, id):
    famili = Family.objects.get(Fid=id)
    if famili.paid is False:
        famili.paid = True
        famili.save()
    return redirect("/fam_show")

# Create your views here for Individual Health Cards.
@login_required
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

@login_required
def ind_edit(request, id):
    indili = Individual.objects.get(Fid=id)
    return render(request, 'ind_edit.html', {'indily': indili})

@login_required
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


@login_required
def ind_show(request):
    files=[]
    out_dir = os.path.join(BASE_DIR,'scale1.pdf')
    out_dir1 = os.path.join(BASE_DIR,'sam1.pdf')
    if request.method=="POST":
        if 'print' in request.POST:
            for item in request.POST.getlist('my_object'):
                data =  ind_print(item)
                path=write_fillable_pdf('self.pdf',out_dir1, data)
                files.append(path)
            path=merge_pdf_files_pdfrw(files,out_dir)
            file= FileResponse(open(path,'rb'))
            return file
    Individuals = Individual.objects.all()
    return render(request, "ind_show.html", {'Individuals':Individuals})

@login_required
def ind_destroy(request, id):
    indili = Individual.objects.get(Fid=id)
    indili.delete()
    return redirect("/ind_show")

@login_required
def ind_paid(request, id):
    indili = Individual.objects.get(Fid=id)
    if indili.paid is False:
        indili.paid = True
        indili.save(update_fields=["paid"])
    return redirect("/ind_show")

# Create your views here for Generic Functions.

@login_required
def back(request):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    out_dir = os.path.join(BASE_DIR,"back.pdf")
    filer = open(out_dir, 'rb')
    resp=FileResponse(filer)
    return resp

def write_fillable_pdf(file, output_pdf_path, data_dict):
    out_dir = os.path.join(BASE_DIR,"tmp/"+str(random.randrange(20, 200, 3))+".pdf")
    INVOICE_TEMPLATE_PATH = os.path.join(BASE_DIR,file)
    template_pdf = pdfrw.PdfReader(INVOICE_TEMPLATE_PATH)
    annotations = template_pdf.pages[0][ANNOT_KEY]
    for annotation in annotations:
        if annotation[SUBTYPE_KEY] == WIDGET_SUBTYPE_KEY:
            if annotation[ANNOT_FIELD_KEY]:
                key = annotation[ANNOT_FIELD_KEY][1:-1]
                template_pdf.Root.AcroForm.update(pdfrw.PdfDict(NeedAppearances=pdfrw.PdfObject('true')))
                if key in data_dict.keys():
                    annotation.update(pdfrw.PdfDict(AP=''))
                    annotation.update(
                        pdfrw.PdfDict(V='{}'.format(data_dict[key]))
                    )
    pdfrw.PdfWriter().write(out_dir, template_pdf)
    return out_dir

def merge_pdf_files_pdfrw(pdf_files, output_filename):
  output = PdfWriter()
  num = 0
  output_acroform = None
  for pdf in pdf_files:
      input = PdfReader(pdf,verbose=False)
      output.addpages(input.pages)
      if PdfName('AcroForm') in input[PdfName('Root')].keys():  # Not all PDFs have an AcroForm node
          source_acroform = input[PdfName('Root')][PdfName('AcroForm')]
          if PdfName('Fields') in source_acroform:
              output_formfields = source_acroform[PdfName('Fields')]
          else:
              output_formfields = []
          num2 = 0
          for form_field in output_formfields:
              key = PdfName('T')
              old_name = form_field[key].replace('(','').replace(')','')  # Field names are in the "(name)" format
              form_field[key] = 'FILE_{n}_FIELD_{m}_{on}'.format(n=num, m=num2, on=old_name)
              num2 += 1
          if output_acroform == None:
              # copy the first AcroForm node
              output_acroform = source_acroform
          else:
              for key in source_acroform.keys():
                  # Add new AcroForms keys if output_acroform already existing
                  if key not in output_acroform:
                      output_acroform[key] = source_acroform[key]
              # Add missing font entries in /DR node of source file
              if (PdfName('DR') in source_acroform.keys()) and (PdfName('Font') in source_acroform[PdfName('DR')].keys()):
                  if PdfName('Font') not in output_acroform[PdfName('DR')].keys():
                      # if output_acroform is missing entirely the /Font node under an existing /DR, simply add it
                      output_acroform[PdfName('DR')][PdfName('Font')] = source_acroform[PdfName('DR')][PdfName('Font')]
                  else:
                      # else add new fonts only
                      for font_key in source_acroform[PdfName('DR')][PdfName('Font')].keys():
                          if font_key not in output_acroform[PdfName('DR')][PdfName('Font')]:
                              output_acroform[PdfName('DR')][PdfName('Font')][font_key] = source_acroform[PdfName('DR')][PdfName('Font')][font_key]
          if PdfName('Fields') not in output_acroform:
              output_acroform[PdfName('Fields')] = output_formfields
          else:
              # Add new fields
              output_acroform[PdfName('Fields')] += output_formfields
      num +=1
  output.trailer[PdfName('Root')][PdfName('AcroForm')] = output_acroform
  output.write(output_filename)
  return output_filename


