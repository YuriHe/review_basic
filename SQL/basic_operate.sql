/*
757. Recyclable and Low Fat Products
Return primary id that have value from categories
*/
SELECT product_id from Products where low_fats = "Y" and recyclable = "Y"