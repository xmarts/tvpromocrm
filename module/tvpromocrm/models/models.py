# -*- coding: utf-8 -*-

from odoo import models, fields, api

class CrmFollowersSale(models.Model):
	_inherit = 'sale.order'

	@api.multi
	def action_confirm(self):
		if self._get_forbidden_state_confirm() & set(self.mapped('state')):
			raise UserError(_(
				'It is not allowed to confirm an order in the following states: %s'
			) % (', '.join(self._get_forbidden_state_confirm())))
		'''for order in self.filtered(lambda order: order.partner_id not in order.message_partner_ids):
			order.message_subscribe([order.partner_id.id])'''
		self.write({
			'state': 'sale',
			'confirmation_date': fields.Datetime.now()
		})
		self._action_confirm()
		if self.env['ir.config_parameter'].sudo().get_param('sale.auto_done_setting'):
			self.action_done()
		return True

class CrmFollowersAccount(models.Model):
	_inherit = 'account.invoice'

	@api.multi
	def invoice_validate(self):
		for invoice in self.filtered(lambda invoice: invoice.partner_id not in invoice.message_partner_ids):
			# invoice.message_subscribe([invoice.partner_id.id])
			# Auto-compute reference, if not already existing and if configured on company
			if not invoice.reference and invoice.type == 'out_invoice':
				invoice.reference = invoice._get_computed_reference()
			# DO NOT FORWARD-PORT.
			# The reference is copied after the move creation because we need the move to get the invoice number but
			# we need the invoice number to get the reference.
			invoice.move_id.ref = invoice.reference
		self._check_duplicate_supplier_reference()

		return self.write({'state': 'open'})
		