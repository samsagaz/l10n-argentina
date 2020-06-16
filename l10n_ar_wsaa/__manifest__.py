###############################################################################
#
#    Copyright (c) 2018 Eynes/E-MIPS (www.eynes.com.ar)
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
    "name": "WSAA (Web Service Afip Authentication)",
    "category": "L10N AR",
    "version": "13.0.1.0.0",
    "author": "Eynes/E-MIPS",
    "license": "AGPL-3",
    "description": "Authentication for AFIP Web Services",
    "depends": [
        "base",
        "account",
        "l10n_ar_point_of_sale",
    ],
    "data": [
        "security/ir.model.access.csv",
        "wizard/wsaa_config_renewal.xml",
        "views/wsaa_view.xml",
        "views/certificate_request_view.xml",
    ],
    "installable": True,
    "application": True,
    "external_dependencies": {
        "python": ["M2Crypto", "OpenSSL"]
        }

}
