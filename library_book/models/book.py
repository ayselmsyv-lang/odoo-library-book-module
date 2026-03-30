from odoo import models, fields

class LibraryBook(models.Model):
    _name='library.book'
    _description='Library Book'

    title=fields.Char(string='Title', required=True)
    author=fields.Char(string='Author')
    category=fields.Char(string='Category')
    book_id=fields.Integer(string='Book ID', required=True)
    available=fields.Boolean(string='Available',default=True)
    