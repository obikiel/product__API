# API Documentation
## Base URL:
 Local Development: http://127.0.0.1:8000/
 live : https://obioma-g4afcwaqdugagkbk.canadacentral-01.azurewebsites.net/api/products/

## 1. Create a Product

Endpoint: https://obioma-g4afcwaqdugagkbk.canadacentral-01.azurewebsites.net/api/products/
Method: POST
Description: Create a new product.
Request:
Content-Type: application/json
Body:
        json
        {
        "id" : 1,
        "name": "Product Name",
        }

Response:
Success (201 Created):

    json
    {
    "id": 1,
    "name": "Product Name",
    }



2. ## Retrieve All Products

Endpoint: https://obioma-g4afcwaqdugagkbk.canadacentral-01.azurewebsites.net/api/products/get/
Method: GET
Description: Retrieve all available products.
Response:
Success (200 OK):
json
[
  {
    "id": 1,
    "name": "Product 1",
  },
  
  {
    "id": 2,
    "name": "Product 2",
  }
]

## 3. Retrieve Product by ID

Endpoint: (https://obioma-g4afcwaqdugagkbk.canadacentral-01.azurewebsites.net/api/products/<int:id>/)
Method: GET
Description: Retrieve a specific product by its ID.
Path Parameter:
id: The ID of the product.
Response:
Success (200 OK):

json

{
  "id": 1,
  "name": "Product 1",
}

Error (404 Not Found):

json
Copy code
{
  "error": "Product not found"
}

## 4. Update a Product

Endpoint: /products/update/
Method: PUT
Description: Update an existing product using its ID.
Request:
Content-Type: application/json
Body:
json

{
  "id": 1,
  "name": "Updated Product",
  "description": "Updated Description",
  "price": 120.00
}
Response:
Success (200 OK):

json

{
  "id": 1,
  "name": "Updated Product",
  "description": "Updated Description",
  "price": 120.00
}


## 5. Update a Product by ID

Endpoint: /products/update/<int:id>/
Method: PUT
Description: Update a product by specifying its ID in the URL.
Path Parameter:
id: The ID of the product.
Request:
Content-Type: application/json
Body (similar to the above):
json

{
  "name": "Updated Product",
  
}

## 6. Delete a Product
Endpoint: /products/delete/
Method: DELETE
Description: Delete a product using its ID.
Request:
Content-Type: application/json
Body:
json
Copy code
{
  "id": 1
}
Response:
Success (204 No Content):

No content in the response.

## 7. Delete a Product by ID

Endpoint: /products/delete/<int:id>/
Method: DELETE
Description: Delete a product by specifying its ID in the URL.
Response:
Success (204 No Content):

No content in the response.
Error (404 Not Found):

json
Copy code
{
  "error": "Product not found"
}

Error Handling
400 Bad Request: Returned when the request body is invalid or incomplete.
404 Not Found: Returned when a product with the given ID does not exist.
500 Internal Server Error: Returned when there is a server-side issue (such as an unexpected failure in the application).
