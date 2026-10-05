select u.name, sum(t.amount) as balance
from transactions t
left join users u
on u.account = t.account
group by t.account
having sum(t.amount) > 10000
