###############################################################################
#
#    Copyright (c) 2019 Eynes/E-MIPS (www.eynes.com.ar)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program. If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################

{
    "name": "Sales by jurisdiction",
    "category": "L10N AR",
    "version": "11.0.1.0.0",
    "author": "Eynes/E-MIPS",
    "license": "AGPL-3",
    "description": "Report Sales by Jurisdiction in XLS",
    "depends": [
        "base_period",
        "l10n_ar_perceptions",
        "account",
        "report_xlsx",
        "report_xlsx_helper",
    ],
    "data": [
        "security/ir.model.access.csv",
        "wizard/sales_by_jurisdiction_view.xml",
        "views/default_jurisdiction_config_view.xml",
    ],
    "installable": True,
    "application": True,
}
