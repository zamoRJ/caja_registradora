from odoo import models, fields, api


class CashRegisterMoves(models.Model):
    _name = 'cash.register.moves'
    _descripcion='Register in a history the movements in the cash register'
    _order='date desc'
 
    type = fields.Selection(string='Movement type', selection=[('i','Entry'),('e','Egress')],required=True)
    amount = fields.Float(string='Amount', required=True)
    balance = fields.Float(string='Balance',help='Current balance',compute='_balance')
    contact = fields.Many2one('res.partner', required=True)
    date = fields.Datetime('Creation Date')

    @api.onchange('balance','amount','type','date')
    def _balance(self):
        domain = []
        for record in self:
            domain.append([
            ('type','=','i'),
            ('date','<=',record.date),
            ])
            entries = self.search(domain)
            total = entries.mapped('amount')
            total_entries = sum(total) + record.amount

        domain = [
          ('type','=','e'),
          ('date','<=',record.date),
        ]
        egress = self.search(domain)
        total = egress.mapped('amount') 
        total_egress = sum(total) + record.amount 

        if total_entries < total_egress:
          record.balance = 0
        else:
          record.balance = total_entries - total_egress
