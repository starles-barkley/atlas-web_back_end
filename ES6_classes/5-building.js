export default Building {
  constructor(sqft) {
    if (this.constructor !== Building) {
      if (!(this.evacuationWarningMessage)) {
        throw new Error('Class extending Building must override evacuationWarningMessage');
      }
    }
    this.sqft = sqft;
  }