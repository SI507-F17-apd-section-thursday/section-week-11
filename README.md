## Section Week 11: Variations in Select Queries

### Steps

1. Chinook Database Schema  
   ![](ChinookDatabaseSchema.png)
1. Create a database named `507_Section_11`
1. Run this command
    - Mac Users: `psql 507_Section_11 -f Chinook_PostgreSql.sql`
    - Windows Users: `psql 507_Section_11 -U postgresql -f Chinook_PostgreSql.sql`
1. Edit a step in `chinook_database.py`, run the file, and repeat
    - Some questions to consider:
        - What table(s) do you need to get data from?
        - What fields in each table do you need to get data from?


### References
1. SELECT: https://www.postgresql.org/docs/10/static/sql-select.html
1. Aggregate Functions: https://www.postgresql.org/docs/current/static/functions-aggregate.html
1. String Functions: https://www.postgresql.org/docs/current/static/functions-string.html
1. Pattern Matching: https://www.postgresql.org/docs/8.0/static/functions-matching.html

### Attributions:
- Chinook_PostgreSQl.sql from [Chinook Database](https://github.com/lerocha/chinook-database)
- Chinook Database Schema from [Chinook Database Documentation](https://chinookdatabase.codeplex.com/wikipage?title=Chinook_Schema&referringTitle=Documentation)
