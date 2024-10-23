const express = require('express');
const app = express();


app.use(express.json());

app.get('/', (req, res) => {
  res.send('Welcome to the payment system');
});

app.get('/cart/:id(\\d+)', (req, res) => {
  const cartId = req.params.id;
  res.send(`Payment methods for cart ${cartId}`);
});

app.get('/available_payments', (req, res) => {
  res.json({
    payment_methods: {
      credit_cards: true,
      paypal: false,
    },
  });
});

app.post('/login', (req, res) => {
  const { userName } = req.body;
  if (!userName) {
    res.status(400).send('Username is required');
  } else {
    res.send(`Welcome ${userName}`);
  }
});

app.listen(7865, () => {
  console.log('API available on localhost port 7865');
});

module.exports = app;