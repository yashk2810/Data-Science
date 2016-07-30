## 2. Adding columns ##

alter table facts add leader text;

## 6. Creating a table with relations ##

CREATE TABLE factbook.states(
    id integer PRIMARY KEY,
    name text,
    area integer,
    country integer,
    FOREIGN KEY(country) REFERENCES facts(id)
);

## 7. Querying across foreign keys ##

select * from landmarks inner join facts on landmarks.country==facts.id;

## 8. Types of joins ##

select * from landmarks left outer join facts on landmarks.country==facts.id;