# Write a SQL query to delete all duplicate email entries in a table named Person, keeping only unique emails based on its smallest Id.

delete p
from Person p, Person q
where p.Email = q.Email and p.Id > q.Id
