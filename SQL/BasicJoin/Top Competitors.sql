select h.hacker_id, h.name
FROM SUBMISSIONS s inner join Challenges c on c.challenge_id = s.challenge_id
inner join difficulty d on c.difficulty_level = d.difficulty_level 
inner join hackers h on h.hacker_id = s.hacker_id
where s.score = d.score and c.difficulty_level = d.difficulty_level
group by h.hacker_id, h.name
having count(s.hacker_id) > 1
order by count(s.hacker_id) desc, h.hacker_id asc
