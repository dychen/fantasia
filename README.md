#NBA Stats

#Queries

* Contests + result counts
```
SELECT c.*, COUNT(p.payout) AS payouts, rcount.count AS contestants
FROM nba_dkcontest AS c JOIN
    (
    SELECT c.id AS cid, COUNT(r.id) AS count
    FROM nba_dkcontest AS c LEFT JOIN nba_dkresult AS r ON c.id=r.contest_id
    GROUP BY c.id
    ) AS rcount
    ON c.id=rcount.cid
LEFT JOIN nba_dkcontestpayout AS p ON c.id=p.contest_id
GROUP BY c.id, rcount.count
ORDER BY c.date DESC;
```

* Stats

```
SELECT p.first_name, p.last_name, g.date, gs.*
FROM nba_player AS p JOIN nba_gamestats AS gs ON p.id=gs.player_id
    JOIN nba_game AS g ON g.id=gs.game_id
WHERE p.first_name='<FIRST>' AND p.last_name='<LAST>'
ORDER BY g.date DESC;
```

* Injuries

```
SELECT p.first_name, p.last_name, t.name, i.status, i.date, i.comment
FROM nba_player AS p JOIN nba_injury AS i ON p.id=i.player_id
    JOIN nba_team AS t ON p.team_id=t.id
WHERE date='today' OR date='yesterday'
ORDER BY p.first_name, p.last_name, i.date DESC;
```

#Contest Result URLs
```
Moved to the database
```
