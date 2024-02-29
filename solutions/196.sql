# I had to find https://stackoverflow.com/a/9843719 to go around an annoying MySQL limitation.

DELETE FROM Person P WHERE id NOT IN (
    SELECT MIN_ID FROM (
        SELECT MIN(Person2.id) AS MIN_ID FROM Person AS Person2 WHERE Person2.email = P.email
    ) as C
)
