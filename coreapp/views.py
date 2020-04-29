from django.shortcuts import render
from django.http import HttpResponse
from .models import Herb, Compound, Target, Disease
import numpy as np
from rdkit import Chem
from rdkit.Chem import Descriptors
from rdkit import DataStructs
from .func import smiles_encoder, smiles_decoder
from django.views import View
from .forms import QuerySmiles
import json
# Create your views here.


def index(request):
    context = {'name': [1, 2, 3, 4]}
    mat = smiles_encoder('c1nccc2n1ccc2')
    print(mat.shape)
    print(type(mat))
    return render(request, 'coreapp/index.html')


def herbview(request):
    list_herb = Herb.objects.all()
    context = {'name': list_herb}
    return render(request, 'coreapp/herb.html', context)


def detailherb(request, herb_id):
    h = Herb.objects.get(pk=herb_id)
    context = {'herb': h}
    return render(request, 'coreapp/detail_herb.html', context)


def compoundview(request):
    list_compound = Compound.objects.all()
    list_mwt=[]
    list_logp=[]
    list_tpsa=[]
    list_hacc=[]
    list_hdon=[]
    list_hrot=[]
    for i in range(len(list_compound)):
        mol=Chem.MolFromSmiles(list_compound[i].can_smiles)
        list_mwt.append(round(Descriptors.MolWt(mol),3))
        list_logp.append(round(Descriptors.MolLogP(mol),3))
        list_tpsa.append(round(Descriptors.TPSA(mol),3))
        list_hacc.append(round(Descriptors.NumHAcceptors(mol),3))
        list_hdon.append(round(Descriptors.NumHDonors(mol),3))
        list_hrot.append(round(Descriptors.NumRotatableBonds(mol), 3))

    #list_test = [75, 69, 56, 46, 47, 79, 92, 97, 89, 88, 36, 96, 105, 32, 116, 101, 79, 93, 91, 112]
    #list_test.sort()
    '''list_mwt.sort()
    list_logp.sort()
    list_tpsa.sort()
    list_hacc.sort()'''

    q1 = np.percentile(list_mwt, 25, interpolation='midpoint')
    q2 = np.median(list_mwt)
    q3 = np.percentile(list_mwt, 75, interpolation='midpoint')
    iqr = q3-q1
    high = round(q3 + 1.75*iqr,3)
    low = round(q1 - 1.75*iqr,3)
    box_data = [low,round(q1,3),round(q2,3),round(q3,3),high]

    q1_logp = np.percentile(list_logp, 25, interpolation='midpoint')
    q2_logp = np.median(list_logp)
    q3_logp = np.percentile(list_logp, 75, interpolation='midpoint')
    high_logp = round(q3_logp + 1.75*(q3_logp - q1_logp),3)
    low_logp = round(q1_logp - 1.75*(q3_logp - q1_logp), 3)
    logp_data = [low_logp,round(q1_logp,3),round(q2_logp,3),round(q3_logp,3),high_logp]

    q1_tpsa = np.percentile(list_tpsa, 25, interpolation='midpoint')
    q2_tpsa = np.median(list_tpsa)
    q3_tpsa = np.percentile(list_tpsa, 75, interpolation='midpoint')
    high_tpsa = round(q3_tpsa + 1.75*(q3_tpsa - q1_tpsa),3)
    low_tpsa = round(q1_tpsa - 1.75*(q3_tpsa - q1_tpsa),3)
    tpsa_data = [low_tpsa,round(q1_tpsa,3),round(q2_tpsa,3),round(q3_tpsa,3),high_tpsa]

    q1_hacc = np.percentile(list_hacc, 25, interpolation='midpoint')
    q2_hacc = np.median(list_hacc)
    q3_hacc = np.percentile(list_hacc, 75, interpolation='midpoint')
    high_hacc = round(q3_hacc + 1.75*(q3_hacc - q1_hacc), 3)
    low_hacc = round(q1_hacc - 1.75*(q3_hacc - q1_hacc),3)
    hacc_data = [low_hacc,round(q1_hacc,3),round(q2_hacc,3),round(q3_hacc,3),high_hacc]

    q1_hdon = np.percentile(list_hdon, 25, interpolation='midpoint')
    q2_hdon = np.median(list_hdon)
    q3_hdon = np.percentile(list_hdon, 75, interpolation='midpoint')
    high_hdon = round(q3_hdon + 1.75 * (q3_hdon - q1_hdon), 3)
    low_hdon = round(q1_hdon - 1.75 * (q3_hdon - q1_hdon), 3)
    hdon_data = [low_hdon, round(q1_hdon, 3), round(q2_hdon, 3), round(q3_hdon, 3), high_hdon]

    q1_hrot = np.percentile(list_hrot, 25, interpolation='midpoint')
    q2_hrot = np.median(list_hrot)
    q3_hrot = np.percentile(list_hrot, 75, interpolation='midpoint')
    high_hrot = round(q3_hrot + 1.75 * (q3_hrot - q1_hrot), 3)
    low_hrot = round(q1_hrot - 1.75 * (q3_hrot - q1_hrot), 3)
    hrot_data = [low_hrot, round(q1_hrot, 3), round(q2_hrot, 3), round(q3_hrot, 3), high_hrot]
    print(hacc_data)
    print(hdon_data)
    print(hrot_data)
    context = {'name': list_compound, 'my_data': box_data, 'logp_data': logp_data, 'tpsa_data': tpsa_data, 'hacc_data':
hacc_data, 'hdon_data': hdon_data, 'hrot_data': hrot_data}
    return render(request, 'coreapp/compound.html', context)


def detailcompound(request, compound_id):
    c = Compound.objects.get(pk=compound_id)
    smi_can = Chem.MolFromSmiles(c.can_smiles)
    mwt = round(Descriptors.MolWt(smi_can),3)
    Hacc = Descriptors.NumHAcceptors(smi_can)
    Hdon = Descriptors.NumHDonors(smi_can)
    rot = Descriptors.NumRotatableBonds(smi_can)

    context = {'compound': c, 'Hacc': Hacc, 'Hdon': Hdon, 'mwt': mwt, 'rot': rot}
    print(type(c))
    return render(request, 'coreapp/detail_compound.html', context)


def targetview(request):
    list_target = Target.objects.all()
    context = {'name': list_target}
    return render(request, 'coreapp/target.html', context)


def detailtarget(request, target_id):
    t = Target.objects.get(pk=target_id)
    context = {'target': t}
    return render(request, 'coreapp/detail_target.html', context)


def diseaseview(request):
    list_disease = Disease.objects.all()
    context = {'name': list_disease}
    return render(request, 'coreapp/disease.html', context)


class querycansmiles(View):
    def get(self, request):
        f = QuerySmiles()
        return render(request, 'coreapp/query.html', {'f': f})

    def post(self, request):
        r = QuerySmiles(request.POST)
        if r.is_valid():
            smi_query = r.cleaned_data['smiles_str']
            thr = r.cleaned_data['thresh_hold']
            mol_query = Chem.MolFromSmiles(smi_query)
            list_compound = Compound.objects.filter()
            simi = []
            simi_dict = {}
            for i in range(len(list_compound)):
                moli = Chem.MolFromSmiles(list_compound[i].can_smiles)
                simii = DataStructs.FingerprintSimilarity(Chem.RDKFingerprint(mol_query), Chem.RDKFingerprint(moli))
                simi_dict[list_compound[i].synonym] = round(simii, 4)
                simi.append(round(simii, 4))
            simi.sort()
            for re in simi_dict:
                if simi_dict[re] >= float(thr):
                    print(re, ': ', simi_dict[re])
            # print(simi)
            print(simi_dict)
            print(smi_query)
            print(thr)
            return render(request, 'coreapp/result.html',{})
        else:
            return HttpResponse('not valid')
