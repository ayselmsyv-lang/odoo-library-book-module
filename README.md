# Odoo Library Book Module
<img width="1920" height="998" alt="image" src="https://github.com/user-attachments/assets/3c8855f4-d162-47b3-84cd-cbac18dc82b3" />


A simple custom Odoo module for managing library books.

This module was created as part of my internship task to demonstrate my understanding of Odoo module structure, model creation, XML views, menu integration, and demo data.

## Features

- Custom model: `library.book`
- Book fields:
  - Title
  - Author
  - Category
  - Book ID
  - Available
- List view
- Form view
- Menu and action integration
- Demo book records

## Module Purpose

The goal of this module is to provide a basic library book management interface in Odoo and show how a simple custom module can be built and installed.
<img width="1325" height="497" alt="image" src="https://github.com/user-attachments/assets/e2799f12-f768-4a49-8e9a-0177afa1e880" />


## Demo Data

The module includes demo book records, mainly based on books by:

- Arthur Conan Doyle
- Jules Verne

## Troubleshooting / Issues I Solved

 - PostgreSQL connection issue
 - pgAdmin4.db migration problem
- addons_path misconfiguration
- database initialization issue
- pkg_resources / dependency problem
- module detected but uninstallable
- practice_db was not initialized as an Odoo database

## Project Structure

```bash
library_book/
├── __init__.py
├── __manifest__.py
├── models/
│   ├── __init__.py
│   └── book.py
├── views/
│   └── book_views.xml
├── security/
│   └── ir.model.access.csv
└── data/
    └── book_demo.xml

