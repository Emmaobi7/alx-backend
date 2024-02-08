const express = require('express')
const app = express()
const { promisify } = require('util')
const port = 1245;
import { createClient } from 'redis';
const client = createClient();

const listProducts = [
  {id: 1, name: 'Suitcase 250', price: 50, stock: 4},
  {id: 2, name: 'Suitcase 450', price: 100, stock: 10},
  {id: 3, name: 'Suitcase 650', price: 350, stock: 2},
  {id: 4, name: 'Suitcase 1050', price: 550, stock: 5}
]


function getItemById(id) {
  return listProducts[id];
}

function reserveStockById(itemId, stock) {
  const setAsync = promisify(client.set).bind(client)
  return setAsync(`item.${itemId}`, stock)
}

async function getCurrentReservedStockById(itemId) {
  const stock = await client.get(`item.${itemId}`)
  return stock;
}


app.get('/list_products', function(req, res) {
  res.json(listProducts)
})

app.get('/list_products/:itemId', async function(req, res) {
  const requestId = req.params.itemId;
  const product = getItemById(requestId)

  if (product) {
    const p = await getCurrentReservedStockById(requestId)
    res.json(product)
  } else {
    res.json({"status": "Product not found"})
  }
})

app.listen(port);
