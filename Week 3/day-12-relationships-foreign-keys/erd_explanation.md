# ERD Explanation

## 1. What are the main entities in this project?

The main entities are **customers**, **products**, **orders**, and **order_items**. Each table stores a different type of business information and has a specific purpose.

## 2. Which table should store customers?

The **customers** table should store customer information such as their name, city, and customer segment.

## 3. Which table should store products?

The **products** table should store product information, including the product name, category, and price.

## 4. Which table should store orders?

The **orders** table should store order information, including which customer placed the order, the order date, status, and sales channel.

## 5. Why should orders not repeat all customer and product details directly?

Repeating customer and product information in every order would create duplicate data. This wastes storage, makes updates harder, and increases the risk of inconsistent information. Instead, orders store IDs that reference the correct customer and product data.

## 6. What is the relationship between customers and orders?

The relationship is **one-to-many**. One customer can place many orders, but each order belongs to only one customer.

## 7. What is the relationship between orders and products?

The relationship is **many-to-many**. One order can contain multiple products, and one product can appear in many different orders.

## 8. Why do we need an order_items table?

The **order_items** table acts as a bridge between orders and products. It allows one order to contain multiple products while also storing the quantity of each product. Without this table, representing many-to-many relationships would be difficult and less organized.
