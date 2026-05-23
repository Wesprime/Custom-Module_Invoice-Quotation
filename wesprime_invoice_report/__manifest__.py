# -*- coding: utf-8 -*-
{
    "name": "Wesprime Invoice Report",
    "version": "17.0.1.0.0",
    "summary": "Premium branded invoice PDF report for customer invoices",
    "category": "Accounting/Accounting",
    "author": "Wesprime",
    "website": "https://www.wesprime.com",
    "license": "LGPL-3",
    "depends": ["account"],
    "external_dependencies": {
        "python": ["qrcode"],
    },
    "data": [
        "data/paperformat.xml",
        "report/invoice_report.xml",
        "report/report_action.xml",
    ],
    "installable": True,
    "application": False,
}
