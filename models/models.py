# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class caja_registradora(models.Model):
#     _name = 'caja_registradora.caja_registradora'
#     _description = 'caja_registradora.caja_registradora'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
from email.policy import default
from time import strftime
from odoo import models, fields, api
from datetime import *
# from odoo.exceptions import *
import logging
logger = logging.getLogger(__name__)



class movimientos(models.Model):
    _name = 'caja_registradora.movimientos'
    _descripcion='Register in a history the movements in the cash register'
    _order='date desc'
    type= fields.Selection(string='Movement type', selection=[('i','Entry'),('e','Egress')],required=True)
    amount=fields.Float(string='Amount', required=True)
    balance=fields.Float(string='Balance',help='Current balance',compute='_balance')
    contact=fields.Many2one('res.partner', required=True)
    date=fields.Datetime('Creation Date')
    @api.onchange('balance','amount','type','date')
    def _balance(self):
      for record in self:
        entries=[
          ('type','=','i'),
          ('date','<=',record.date),
        ]
        datai=self.search(entries)
        totali=datai.mapped('amount')
        suma_ingresos=sum(totali)+record.amount

        egress=[
          ('type','=','e'),
          ('date','<=',record.date),
        ]
        datae=self.search(egress)
        totale=datae.mapped('amount') 
        suma_egresos=sum(totale)+record.amount 

        if suma_ingresos<suma_egresos:
          # error with
          # raise Warning('Egress is > than Balance')
          record.balance=0
        else:
          record.balance=suma_ingresos-suma_egresos


    @api.model
    def create(self, values):
        values['date'] = datetime.now()
        res = super(movimientos, self).create(values)
        logger.info(res)
        logger.info(values)
        return res
