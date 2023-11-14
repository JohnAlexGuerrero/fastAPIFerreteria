drop database if exists soluciones_ferreteras;

create database soluciones_ferreteras;

use soluciones_ferreteras;

show tables;


/* triggers */
delimiter $$
create trigger update_stock_product
before insert on inventory
for each row
	begin
		update product 
        set amount = new.amount + amount, cost = new.price, updatedAt = new.createdAt
        where id=new.product_id;
    end $$
delimiter ;

delimiter $$
create trigger add_item_inventory
before insert on shoppingdetail
for each row
	begin
		insert into inventory(product_id, amount, price, createdAt)
        values(
			new.product_id, new.amount, new.price, new.createdAt
        );
    end $$
delimiter ;

drop trigger add_item_inventory;
