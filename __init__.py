# This file is part of account_bank module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import Pool
from .account import *
from . import payment


def register():
    Pool.register(
        PaymentType,
        BankAccount,
        Party,
        Invoice,
        Reconciliation,
        Line,
        CompensationMoveStart,
        payment.Journal,
        payment.Group,
        payment.Payment,
        payment.PayLine,
        module='account_bank', type_='model')
    Pool.register(
        CompensationMove,
        module='account_bank', type_='wizard')
