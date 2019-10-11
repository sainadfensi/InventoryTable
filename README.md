# Inventory_table
The aim is to merge the stock-in table, stock-out table, and initial storage table based on the id of product.
## Format of Files
###ini_storage.txt
The ini_storage.txt consists of two columns that are the IDs of products and their storage at the beginning of the month.
###stock_in.txt
The stock_in.txt consists of two columns that are the IDs of products and the numbers of the products put in the storage during the month. The order of the IDs can be different from the IDs in the ini_storage.txt. If there are new product input this month, the new IDs should be added into the ini_storage.txt and their initial storage are zero.
###stock_out.txt
The stock_out.txt consists of two columns that are the IDs of products and the numbers of the products sold during the month. The order of the IDs can be different from the IDs in the ini_storage.txt. 
