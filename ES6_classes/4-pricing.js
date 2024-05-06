import Currency from './3-currency';

export default class Pricing {
  constructor(amount, currency) {
    this.amount = amount;
    this.currency = currency;
  }

  set amount (val) {
    if (typeof (val) ===  'number') {
      this._amount = val;
    } else {
      throw TypeError("Amount must be a number");
    }
  }

  get amount() {
    return this._amount;
  }
  set currency(val) {
    if (val instanceof Currency) {
      this._currency = val;
    } else {
      throw TypeError('Currency must be a currency');
    }
  }

  get currency() {
    return this._currency;
  }
