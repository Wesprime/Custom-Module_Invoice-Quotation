# Wesprime Quote Report

This repository contains a single Odoo add-on: `wesprime_quote_report`.

The module adds a branded PDF quotation report for Sales Orders in Odoo 17. It is designed for service-led quotations and replaces the plain default output with a presentation-style PDF that includes a custom header, client details, service summary, totals, terms, banking details, and signature blocks.

## Project Snapshot

- Module name: `wesprime_quote_report`
- Odoo version: `17.0`
- Dependency: `sale`
- Report type: `QWeb PDF`
- Target model: `sale.order`
- License: `LGPL-3`

## What The Module Does

After installation, the module adds a new print action called `Wesprime Quotation` on Sales Orders. When triggered, Odoo generates a PDF using a custom QWeb template and a dedicated paper format.

The report currently includes:

- A full-width branded header image
- A quotation summary block with number, issue date, preparer, and validity date
- Client details pulled from the customer record
- A fixed introductory message
- A service summary table built from quotation lines
- Amount in words
- Net total, tax, and grand total
- Fixed terms and conditions
- Banking and signature sections
- A branded footer using company information

## How It Is Wired

The module is intentionally simple and has no Python business logic beyond the standard add-on scaffold.

| File | Purpose |
| --- | --- |
| `wesprime_quote_report/__manifest__.py` | Declares the module, dependency on `sale`, and loads XML data files |
| `wesprime_quote_report/__init__.py` | Empty module initializer |
| `wesprime_quote_report/data/paperformat.xml` | Defines the dedicated A4 paper format and tight report margins |
| `wesprime_quote_report/report/report_action.xml` | Registers the PDF report action on `sale.order` |
| `wesprime_quote_report/report/quotation_report.xml` | Contains the full QWeb report layout, styling, and data bindings |
| `wesprime_quote_report/static/src/img/quotation_header.png` | Header banner used at the top of the PDF |
| `wesprime_quote_report/static/src/img/signature_prepared.png` | Static image used in the Prepared By block |
| `wesprime_quote_report/static/src/img/signature_approved.png` | Static image used in the Approved By block |

## Data Used In The PDF

The report pulls values from the sales order, customer, company, currency, and order lines.

| Section | Source |
| --- | --- |
| Quotation number | `sale.order.name` |
| Issue date | `sale.order.date_order` |
| Valid until | `sale.order.validity_date` |
| Prepared by | `sale.order.user_id.name` |
| Client name | `sale.order.partner_id.name` |
| Contact person | `partner_id.parent_id.name` fallback to `partner_id.name` |
| Client address | `partner_id.street`, `street2`, `city`, `zip`, `country_id.name` |
| Contact details | `partner_id.phone`, `mobile`, `email` |
| Services | `order_line` records excluding `display_type` lines |
| Service title | `line.product_id.display_name` fallback to `line.name` |
| Service description | `line.name` |
| Pricing | `line.price_unit`, `line.price_subtotal` |
| Totals | `amount_untaxed`, `amount_tax`, `amount_total` |
| Amount in words | `currency_id.amount_to_text(amount_total)` |
| Footer company info | `company.name`, `phone`, `email`, `website`, `city`, `country_id.name`, `company_registry` |

## Installation

1. Place `wesprime_quote_report` inside your Odoo `addons_path`.
2. Restart the Odoo server.
3. Update the Apps list.
4. Install `Wesprime Quote Report`.

## Usage

1. Open a Sales Order or Quotation.
2. Use the `Print` menu.
3. Select `Wesprime Quotation`.
4. Odoo will generate the branded PDF.

## Current Behavior You Should Know

These details are hardcoded in the current implementation and are important if you plan to extend or reuse the module:

- The report language is fixed to `en_US`.
- The subtitle below the main title is fixed text.
- The introductory note is fixed text.
- The terms and conditions block is fixed text.
- The bank name and account number are hardcoded in the QWeb template.
- The QR section is only a placeholder and does not generate a real QR code.
- The prepared and approved signatures are static PNG files, not dynamic employee signatures.
- Comments in the template mention future watermark, digital approval metadata, and page numbering, but those features are not implemented yet.

## Paper Format

The module ships with a dedicated A4 paper format tuned for this report:

- Orientation: `Portrait`
- Top margin: `8`
- Bottom margin: `10`
- Left margin: `7`
- Right margin: `7`
- DPI: `96`
- Shrinking disabled: `True`

This is meant to keep the header aligned and preserve layout consistency in the generated PDF.

## Customization Guide

If you need to change the output later, these are the main places to edit:

- Update branding or layout in `wesprime_quote_report/report/quotation_report.xml`
- Replace header or signature images in `wesprime_quote_report/static/src/img/`
- Change page size or margins in `wesprime_quote_report/data/paperformat.xml`
- Rename the print action or output filename in `wesprime_quote_report/report/report_action.xml`
- Add more dynamic fields by extending the QWeb template bindings

## Practical Notes For Future Work

- There is no custom Python model, wizard, or computed helper in this add-on.
- Most future work will happen in the XML template, not Python.
- Because the template is monolithic, larger enhancements may be easier if you split sections into smaller reusable QWeb templates.
- If bank details, signatures, or terms should vary by company, user, or quotation, they should be moved from hardcoded template values into real Odoo fields.
- If multilingual output is required, the `t-lang` behavior should be made dynamic instead of fixed to `en_US`.

## Recommended Next Improvements

- Move bank details into company settings or a related model
- Replace static signatures with configurable company or employee signature fields
- Add a real QR code if payment or approval workflows require it
- Make terms and intro content configurable from Odoo
- Split the single report template into smaller named sections for easier maintenance

## Summary

This project is a clean, single-purpose Odoo reporting add-on. Its main value is the branded QWeb PDF for sales quotations. The implementation is straightforward, asset-driven, and easy to maintain, but several commercial details are currently hardcoded inside the report template and should be parameterized if the module is going to evolve further.
