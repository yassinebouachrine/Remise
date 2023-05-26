# -*- coding: utf-8 -*-

from odoo import models, fields, api
import json




class QuotationsFe(models.Model):
    _inherit = 'sale.order'




    account_move = fields.Many2many(
        'account.move',
    )

    validitydate = fields.Date(string='Date de Validation')
    date_order1 = fields.Datetime(string='Date de devis', default=fields.Date.today)

    discount_applies_choise = [
      ('Ligne de commande','ligne de commande'),
      ('Global','Global'),
    ]
    discount_applies = fields.Selection(discount_applies_choise, string='Remise Appliquer', default='Ligne de commande')

    line_discount = fields.Monetary(string='Remise de ligne', store=True, compute='_amount_all')

    discount_method_choise = [
      ('Fix','fix'),
      ('Percentage','percentage'),
    ]
    discount_methodsfe = fields.Selection(discount_method_choise, string='Method de remise')

    discount_amountsfe = fields.Float(string='Montant de la remise')


    @api.depends('order_line.price_total', 'order_line.discount', 'order_line.price_unit', 'order_line.discount_amount')
    def _amount_all(self):
        """
        Compute the total amounts of the SO.
        """
        for order in self:
            line_discount = 0
            amount_untaxed = amount_tax = 0.0
            for line in order.order_line:
                amount_untaxed += line.price_subtotal
                amount_tax += line.price_tax
                if order.discount_applies == 'Ligne de commande':
                    if line.discount_method == 'Fix':
                         line_discount += line.discount_amount
                         order.line_discount = line_discount
                    elif line.discount_method == 'Percentage':
                         you = line.price_unit - (line.price_unit * (line.discount_amount/100))
                         line_discount += (line.price_unit - you)
                         order.line_discount = line_discount
                if order.discount_applies == 'Global':
                    if order.discount_methodsfe == 'Fix':
                         line_discount = order.discount_amountsfe
                         order.line_discount = line_discount
                    elif order.discount_methodsfe == 'Percentage':
                         you = line.price_unit - (line.price_unit * (order.discount_amountsfe/100))
                         line_discount += (line.price_unit - you)
                         order.line_discount = line_discount 


            order.update({
                'amount_untaxed': amount_untaxed,
                'line_discount': line_discount,
                'amount_tax': amount_tax,
                'amount_total': amount_untaxed + amount_tax + line_discount,
            })
  




class order_linesFe(models.Model):
    _inherit = 'sale.order.line'



    # move_id = fields.Many2many('account.move', string='Account Move')
    # account_move_line = fields.Many2many(
    #     'account.move',
    #     inverse="account_move_id",
    # )

    houww = fields.Many2many('account.move.line', required=True, ondelete='cascade', index=True, copy=False)
    

    discount_amount = fields.Float(string='Montant de la remise', default=0.0)

    discount_method_choise = [
      ('Fix','fix'),
      ('Percentage','percentage'),
    ]   
    discount_method = fields.Selection(discount_method_choise, string='Method de remise')

    @api.depends('product_uom_qty', 'discount', 'price_unit', 'tax_id')
    def _compute_amount(self):
        """
        Compute the amounts of the SO line.
        """
        for line in self:
            line.price_subtotal = line.price_unit 
            price = line.price_unit * (1 - (line.discount or 0.0) / 100.0)
            taxes = line.tax_id.compute_all(price, line.order_id.currency_id, line.product_uom_qty, product=line.product_id, partner=line.order_id.partner_shipping_id)
            line.update({
                'price_tax': sum(t.get('amount', 0.0) for t in taxes.get('taxes', [])),
                'price_total': taxes['total_included'],
                # 'price_subtotal': taxes['total_excluded'],
            })
        
