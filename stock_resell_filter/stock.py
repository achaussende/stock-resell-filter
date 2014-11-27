# -*- coding: utf-8 -*-
##############################################################################
#
#  licence AGPL version 3 or later
#  see licence in __openerp__.py or http://www.gnu.org/licenses/agpl-3.0.txt
#  Copyright (C) 2014 Akretion (http://www.akretion.com).
#  @author Adrien CHAUSSENDE <adrien.chaussende@akretion.com>
#
##############################################################################

from osv import orm, fields


class StockPicking(orm.Model):
    _inherit = 'stock.picking'

    def _has_only_make_to_stock(self, cr, uid, ids, name, args, context=None):
        result = {}
        for picking in self.browse(cr, uid, ids, context=context):
            if picking.make_to_stock_only:
                result[picking.id] = picking.make_to_stock_only
            else:
                result[picking.id] = True
            for move in picking.move_lines:
                result[picking.id] = result[picking.id] and \
                    (move.product_id.procure_method == 'make_to_stock')
        return result

    def _get_picking_from_stock_move(self, cr, uid, ids, context=None):
        move_obj = self.pool.get('stock.move')
        picking_ids = []
        for move in move_obj.browse(cr, uid, ids, context=context):
            if move.picking_id:
                picking_ids.append(move.picking_id.id)
        return picking_ids

    _columns = {
        'make_to_stock_only': fields.function(
            _has_only_make_to_stock, string='Reselled Only Products',
            type='boolean',
            store={
                'stock.move': (_get_picking_from_stock_move, ['product_id'],
                               10)
            }
        )
    }
