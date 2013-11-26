# -*- coding: utf-8 -*-
"""
Declaraçao da classe onde serão salvos todos os dados referentes às vendas.
"""

from django.db import models
from datetime import datetime


class Invoice(models.Model):
    """
    Cada objeto desta classe representará uma nota fiscal, referente
    aos dados contidos em cada arquivo processado.
    """
    date_upload = models.DateTimeField(
        u'Data de upload',
        default=datetime.now(),
        auto_now_add=True,
        null=False,
        blank=False
    )


class SalesManager(models.Model):
    """
    Classe para o armazenamento dos dados de cada venda.
    """
    purchaser_name = models.CharField(
        u'Comprador',
        max_length=100
    )
    item_description = models.CharField(
        u'Descrição do item',
        max_length=200
    )
    item_price = models.DecimalField(
        u'Preço unitário do item',
        max_digits=9,
        decimal_places=2
    )
    purchase_count = models.PositiveSmallIntegerField(
        u'Quantidade de itens',
    )
    merchant_address = models.CharField(
        u'Endereço do comprador',
        max_length=200
    )
    merchant_name = models.CharField(
        u'Nome do comprador',
        max_length=100
    )
    invoice = models.ForeignKey(
        Invoice
    )
