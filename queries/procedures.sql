delimiter //

create procedure get_price_changes_by_date(in date varchar(255))
begin
	select e.web_name, round(c.now_cost_live*0.1,1) as now_cost, c.cost_difference as changes, c.date_change as date
	from elements_cost_changes c
	left join elements_summary e
	on c.id = e.id
    where c.date_change = date
	order by c.cost_difference desc;
end //

delimiter ;



delimiter //

create procedure kill_processes(in user varchar(255))
begin
	select concat('KILL ',id,';') as killer from information_schema.processlist where user=user;
end //

delimiter ;