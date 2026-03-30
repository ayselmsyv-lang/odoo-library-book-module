# Odoo Library Book Module

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

## Demo Data

The module includes demo book records, mainly based on books by:

- Arthur Conan Doyle
- Jules Verne

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
