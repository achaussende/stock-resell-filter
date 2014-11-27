# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2014 Akretion (http://www.akretion.com).
#    @author Adrien CHAUSSENDE <adrien.chaussende@akretion.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################


{
    'name': 'Stock Reseller Filter',
    'version': '1.0',
    'category': 'Generic Modules',
    'description': """
        Add two filters on Delivery Orders view. They allow to select the
        Delivery Orders that have only reselled products (i.e. make_to_stock
        bought products) or that have at least one reselled product.
    """,
    'author': 'Akretion',
    'website': 'http://akretion.com',
    'depends': ['stock',],
    'data': [
        'stock_view.xml',
        ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
