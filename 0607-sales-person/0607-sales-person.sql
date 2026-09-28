SELECT name
from SalesPerson 
where name not in (
    select s.name 
    from SalesPerson s
    left join orders o on s.sales_id = o.sales_id
    left join Company c on o.com_id = c.com_id
    where c.name = 'red'
)