# -*- coding: utf-8 -*-
from odoo import tools
from odoo import models, fields, api, _


class SaleOfOutStockReportExtendd(models.Model):
    _name = "visiontrack.sale_out_stock_report_extend"
    _description = "VT Sale Out of Stock Report Extention"
    _auto = False
    # _rec_name = 'sale_id'
    
    # name = fields.Many2one('sale.order', readonly=True, string='Sale Order')
    partner_id = fields.Many2one('res.partner', readonly=True)
    currency_id = fields.Many2one('res.currency', readonly=True)
    amount_untaxed = fields.Monetary(currency_field='currency_id', readonly=True, string='Sale Total (Untaxed)')
    warehouse_id = fields.Many2one('stock.warehouse', readonly=True, string='Warehouse')

    def _query(self):
        return """
            select currency_id, amount_untaxed, warehouse_id, partner_id from sale_order so
        """

    def init(self):
        # self._table = visiontrack_sale_out_stock_report
        tools.drop_view_if_exists(self.env.cr, self._table)
        self.env.cr.execute("""CREATE or REPLACE VIEW %s as (%s)""" % (self._table, self._query()))
