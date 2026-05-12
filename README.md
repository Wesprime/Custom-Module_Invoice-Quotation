# Wesprime Odoo Report Templates

This repository contains two Odoo 17 add-ons for branded PDF document generation:

- `wesprime_quote_report`
- `wesprime_invoice_report`

Both modules are built as lightweight QWeb reporting add-ons. They do not add custom Python business logic. Their main purpose is to replace standard Odoo printouts with presentation-style PDFs that match Wesprime branding.

## Repository Snapshot

| Module | Purpose | Target Model | Dependency | Print Action |
| --- | --- | --- | --- | --- |
| `wesprime_quote_report` | Branded quotation PDF | `sale.order` | `sale` | `Wesprime Quotation` |
| `wesprime_invoice_report` | Branded tax invoice PDF | `account.move` | `account` | `Wesprime Invoice` |

## What Is Included

### `wesprime_quote_report`

This module adds a custom quotation report for Sales Orders.

It includes:

- A full-width branded header image
- A quotation title and summary section
- Client details pulled from the partner record
- A service summary table from quotation lines
- Amount in words
- Totals section
- Fixed terms and conditions
- Banking details and signature blocks
- A branded footer using company information

### `wesprime_invoice_report`

This module adds a custom tax invoice report for Customer Invoices.

It includes:

- A full-width branded header image
- A `Tax Invoice` title and invoice summary section
- Billing details pulled from the invoice partner
- An item table with `Description`, `Quantity`, `Unit Price`, and `Subtotal`
- Amount in words using `currency_id.amount_to_text(amount_total)`
- Totals section
- Banking details and signature blocks
- A branded footer using company information

## Invoice Module Field Mapping

The invoice module was created by adapting the quotation report structure to `account.move`.

| Quote Logic | Invoice Logic |
| --- | --- |
| `sale.order` | `account.move` |
| `order_line` | `invoice_line_ids` |
| `date_order` | `invoice_date` |
| `validity_date` | `invoice_date_due` |
| `user_id` | `invoice_user_id` |

The invoice report also filters out `display_type` lines so sections and notes are skipped in the main pricing table.

## Repository Structure

| Path | Purpose |
| --- | --- |
| `wesprime_quote_report/__manifest__.py` | Quote module metadata |
| `wesprime_quote_report/data/paperformat.xml` | Quote paper format |
| `wesprime_quote_report/report/quotation_report.xml` | Quote QWeb template |
| `wesprime_quote_report/report/report_action.xml` | Quote print action |
| `wesprime_quote_report/static/src/img/` | Quote header and signature images |
| `wesprime_invoice_report/__manifest__.py` | Invoice module metadata |
| `wesprime_invoice_report/data/paperformat.xml` | Invoice paper format |
| `wesprime_invoice_report/report/invoice_report.xml` | Invoice QWeb template |
| `wesprime_invoice_report/report/report_action.xml` | Invoice print action |
| `wesprime_invoice_report/static/src/img/` | Invoice header and signature images |

## Shared Implementation Notes

Both modules use a modern sky blue branding palette:
- Primary Sky Blue: #38BDF8
- Light Background Blue: #E0F2FE
- Professional Dark Blue Text: #0369A1

Signatures are displayed as horizontal enterprise-style images with controlled sizing (max-width: 150px, max-height: 52px) for optimal PDF rendering.

Both modules follow the same overall pattern:

- Odoo 17 QWeb PDF reports
- Dedicated A4 paper format
- Hardcoded report language: `en_US`
- Static header and signature image assets
- Company-based footer details
- No Python models, wizards, or computed helpers

Both modules use the same paper format settings:

- Format: `A4`
- Orientation: `Portrait`
- Top margin: `8`
- Bottom margin: `10`
- Left margin: `7`
- Right margin: `7`
- DPI: `96`
- Shrinking disabled: `True`

## Installation

1. Place both module folders inside your Odoo `addons_path`.
2. Restart the Odoo server.
3. Update the Apps list.
4. Install either or both modules:
   - `Wesprime Quote Report`
   - `Wesprime Invoice Report`

## Usage

### Quotation Report

1. Open a Sales Order or Quotation.
2. Use the `Print` menu.
3. Select `Wesprime Quotation`.

### Invoice Report

1. Open a Customer Invoice.
2. Use the `Print` menu.
3. Select `Wesprime Invoice`.

## Current Hardcoded Behavior

These details are currently hardcoded in one or both templates:

- Report language is fixed to `en_US`
- Subtitle text under the main heading
- Introductory note text
- Terms and conditions in the quotation report
- Banking details including bank name and account number
- QR area is only a placeholder
- Prepared and approved signatures are static PNG files
- Footer tagline text

This means the modules are easy to deploy, but some commercial details should be moved into configurable Odoo fields if the reports need to vary by company, user, or document type.

## Design Notes

- `wesprime_quote_report` keeps the original presentation-heavy custom styling approach.
- `wesprime_invoice_report` follows the same visual direction but is organized using a cleaner Bootstrap-friendly layout for Odoo 17.
- The invoice module reuses the same branding assets so both printouts look consistent.

## Customization Guide

If you want to extend the reports later, these are the main files to change:

- Edit quote layout in `wesprime_quote_report/report/quotation_report.xml`
- Edit invoice layout in `wesprime_invoice_report/report/invoice_report.xml`
- Change margins or page setup in each module’s `data/paperformat.xml`
- Rename print actions in each module’s `report/report_action.xml`
- Replace header and signature images under each module’s `static/src/img/`

## Practical Notes For Future Work

- Split the larger QWeb templates into smaller reusable template blocks if the reports continue to grow
- Move banking details into company settings or a related configuration model
- Replace static signatures with configurable company or employee signature fields
- Add real QR code generation if approval or payment workflows require it
- Make static legal or commercial text configurable from Odoo
- Add multilingual behavior instead of forcing `en_US`

## Summary

This repository now contains a small, focused reporting bundle for Odoo 17:

- `wesprime_quote_report` for branded quotations on `sale.order`
- `wesprime_invoice_report` for branded invoices on `account.move`

Both modules are straightforward XML-based add-ons, easy to maintain, and ready for further branding or functional enhancements.
