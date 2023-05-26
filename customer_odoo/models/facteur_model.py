# -*- coding: utf-8 -*-

from odoo import models, fields, api
import json



class AccountMovesFe(models.Model):
    _inherit = 'account.move'




    line_discount = fields.Monetary(
         related='sale_order_id.line_discount',
         
    )
    amount_untaxed = fields.Monetary(
         related='sale_order_id.amount_untaxed',
         
    )
    amount_tax = fields.Monetary(
          related='sale_order_id.amount_tax',
          
    )
    amount_total = fields.Monetary(
         related='sale_order_id.amount_total',
         
    )
    discount_methodsfe = fields.Selection(
         related='sale_order_id.discount_methodsfe',
         
    )
    discount_amountsfe = fields.Float(
         related='sale_order_id.discount_amountsfe',
         
         
    )
    discount_applies = fields.Selection(
         related='sale_order_id.discount_applies',
         
    )
    sale_order_id = fields.Many2one(
         'sale.order',
         inverse="account_move",
         compute='_compute_sale_order_id',
         
    )
    purchase_order_id = fields.Many2one(
         'purchase.order',
         inverse="invoice_ids",
         compute='_compute_sale_order_id',
         
    )

    @api.depends('invoice_origin', 'sale_order_id.line_discount', 'purchase_order_id.line_discount')
    def _compute_sale_order_id(self):
         for record in self:
             if record.invoice_origin:
                 sale_order = self.env['sale.order'].search([('name', '=', record.invoice_origin)], limit=1)
                 purchase_order = self.env['purchase.order'].search([('name', '=', record.invoice_origin)], limit=1)
                 if sale_order:
                     record.sale_order_id = sale_order.id
                     record.discount_applies = sale_order.discount_applies
                     record.discount_amountsfe = sale_order.discount_amountsfe
                     record.discount_methodsfe = sale_order.discount_methodsfe
                     record.amount_total = sale_order.amount_total
                     record.amount_tax = sale_order.amount_tax
                     record.amount_untaxed = sale_order.amount_untaxed
                     record.line_discount = sale_order.line_discount

                 elif purchase_order:
                     record.purchase_order_id = purchase_order.id
                     record.discount_applies = purchase_order.discount_applies
                     record.discount_amountsfe = purchase_order.discount_amountsfe
                     record.discount_methodsfe = purchase_order.discount_methodsfe
                     record.amount_total = purchase_order.amount_total
                     record.amount_tax = purchase_order.amount_tax
                     record.amount_untaxed = purchase_order.amount_untaxed
                     record.line_discount = purchase_order.line_discount

 





class AccountMoveLinesFe(models.Model):
    _inherit = 'account.move.line'

    houwws = fields.One2many('sale.order.line', 'houww', copy=True, auto_join=True)

    discount_amount = fields.Float(
        related='houwws.discount_amount',
    )
    discount_method = fields.Selection(
        related='houwws.discount_method',
    )

    # @api.depends('houwws.discount_amount', 'houwws.discount_method')
    # def _compute_discount_fields(self):
    #     for move_line in self:
    #         sale_lines = move_line.houwws
    #         if sale_lines:
    #             move_line.discount_amount = sale_lines[0].discount_amount
    #             move_line.discount_method = sale_lines[0].discount_method
    #         else:
    #             move_line.discount_amount = 0.0
    #             move_line.discount_method = False







