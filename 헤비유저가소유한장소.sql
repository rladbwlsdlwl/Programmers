-- 코드를 입력하세요
# select id, name, p1.host_id from places as p1
#     join (select host_id, count(host_id) as cnt from places group by host_id) as p2
#     on p1.host_id = p2.host_id
# where cnt > 1 
# order by id;

select * from places
    where host_id in 
    (select host_id 
    from places group by host_id having count(host_id) > 1);
