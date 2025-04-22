-- For each date_id and make_name, find the number of distinct lead_id's and distinct partner_id's.
SELECT 
    date_id, 
    make_name, 
    COUNT(DISTINCT lead_id) AS unique_leads,      -- Correct: Counts unique leads
    COUNT(DISTINCT partner_id) AS unique_partners -- Correct: Counts unique partners
FROM DailySales 
GROUP BY date_id, make_name;