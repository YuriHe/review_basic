SELECT 
    player_id,
    MIN(event_date) AS first_login
From Activity
GROUP BY player_id;