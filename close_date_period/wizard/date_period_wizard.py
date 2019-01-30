# -*- coding: utf-8 -*-
###############################################################################
#   Copyright (c) 2019 Eynes/E-mips (Julian Corso)
#   License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
###############################################################################

import logging

from odoo import models, api, fields, _, exceptions
# from odoo.exceptions import except_orm
# from odoo.addons.decimal_precision import decimal_precision as dp
# from odoo.tools import DEFAULT_SERVER_DATE_FORMAT, \
#         DEFAULT_SERVER_DATETIME_FORMAT, float_compare


_logger = logging.getLogger(__name__)


class CloseDatePeriodWizard(models.TransientModel):
    _name = 'close.date.period.wizard'

    journal_ids = fields.Many2many(
        comodel_name='account.journal',
        relation='close_period_journal_rel',
        column1='close_period_id', column2='journal_id',
        string='Journals')
    closed_journal_ids = fields.Many2many(
        comodel_name='account.journal',
        relation='already_closed_period_journal_rel',
        column1='close_period_id', column2='journal_id',
        default=lambda s: s._get_default_closed_journals(),
        string='Journals')

    @api.multi
    def button_close(self):
        active_ids = self.env.context.get('active_ids')
        date_period_id = self.env['date.period'].browse(active_ids)
        self.journal_ids += self.closed_journal_ids
        date_period_id.write({'journal_ids':[(6, 0, self.journal_ids.ids)]})
    
    @api.model
    def _get_default_closed_journals(self):
        active_ids = self.env.context.get('active_ids')
        date_period_id = self.env['date.period'].browse(active_ids)
        return date_period_id.journal_ids.ids
