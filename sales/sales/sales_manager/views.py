# -*- coding: utf-8 -*-
"""
Arquivo de views do projeto.
"""

from django.shortcuts import render_to_response
from django.template import RequestContext
from forms import InputDataForm
from models import SalesManager, Invoice
from django.db.models import Sum

def upload(request):
    """
    View que fará o upload do arquivo e enviará para processamento.
    """
    dicionario = {}
    form = InputDataForm
    dicionario['form'] = form
    return render_to_response('base.html',
                              dicionario,
                              context_instance=RequestContext(request))

def processar(request):
    """
    View que fará o processamento do arquivo recebido.
    """
    dicionario = {}
    form = InputDataForm
    dicionario['form'] = form
    if request.POST.get('Arquivo') != u'':
        arquivo = open(request.POST.get('Arquivo'))
        conteudo = arquivo.read()
        registros = conteudo.split('\n')
        del registros[0]
        del registros[-1]
        nota_fiscal = Invoice.objects.create()
        for registro in registros:
            dados = registro.split('    ')
            SalesManager.objects.create(
                purchaser_name=dados[0],
                item_description=dados[2],
                item_price=dados[4],
                purchase_count=dados[6],
                merchant_address=dados[8],
                merchant_name=dados[10],
                invoice=nota_fiscal)

        itens = SalesManager.objects.filter(invoice__pk=nota_fiscal.pk)
        dicionario['itens'] = itens
        valor_total = itens.aggregate(Sum('item_price'))
        dicionario['valor_total'] = valor_total.get('item_price__sum')
    return render_to_response('base.html',
                              dicionario,
                              context_instance=RequestContext(request))
