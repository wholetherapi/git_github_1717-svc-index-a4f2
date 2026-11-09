# Service Index — Catalog API

This document is the authoritative inventory of the HTTP routes exposed by the catalog service.
It is generated from the active source tree using the entry rules below.

Source branch: main

## Entry rules

1. Emit exactly one row for every public route declared with `@route(<METHOD>, <PATH>)` in `catalog/*.py`.
2. Exclude routes whose path starts with `/internal/` and any handler decorated with `@internal_only`.
3. Determine the status with the following precedence (highest first):
   - `planned` — the handler raises `NotImplementedError`.
   - `deprecated` — the handler is decorated with `@deprecated`.
   - `experimental` — the handler is decorated with `@experimental`.
   - `stable` — every other handler (including those decorated with `@stable`).
4. Sort rows by module path (lexicographic), then by HTTP method, then by route path.
5. Columns, in order: `Module | Method | Path | Handler | Status`.

## Route inventory

| Module | Method | Path | Handler | Status |
| --- | --- | --- | --- | --- |
| catalog/accounts.py | GET | /accounts | list_accounts | stable |
| catalog/accounts.py | GET | /accounts/{account_id} | get_account | stable |
| catalog/accounts.py | PATCH | /accounts/{account_id} | update_account | stable |
| catalog/accounts.py | POST | /accounts | create_account | stable |
| catalog/billing.py | GET | /billing/invoices | list_invoices | stable |
| catalog/billing.py | GET | /billing/invoices/{invoice_id} | get_invoice | stable |
| catalog/billing.py | POST | /billing/invoices | create_invoice | experimental |
| catalog/billing.py | POST | /billing/invoices/{invoice_id}/void | void_invoice | deprecated |
| catalog/reports.py | GET | /reports/daily | daily_report | deprecated |
| catalog/reports.py | GET | /reports/monthly | monthly_report | planned |
| catalog/support.py | GET | /support/tickets | list_tickets | stable |
| catalog/support.py | GET | /support/tickets/{ticket_id} | get_ticket | stable |
| catalog/support.py | POST | /support/tickets | open_ticket | stable |
| catalog/webhooks.py | POST | /webhooks/github | github_webhook | stable |
| catalog/webhooks.py | POST | /webhooks/stripe | stripe_webhook | experimental |
