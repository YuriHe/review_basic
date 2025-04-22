# Write your MySQL query statement below
# truncate table
SELECT 
    DISTINCT author_id as id 
FROM Views
WHERE viewer_id = author_id
order by author_id ASC;