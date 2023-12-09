select web_name, total_points, now_cost*0.1 as now_cost
from elements_summary
where id=60;

select *
from fixtures;

select 
	concat(es.first_name, " ", es.second_name) as palyer,
    gw.total_points,
    gw.event_id
from gameweek_stats gw
left join elements_summary es
on gw.id = es.id
where gw.minutes > 0;