# Write your MySQL query statement below
select l.book_id, l.title, l.author, l.genre, l.publication_year, l.total_copies as current_borrowers from library_books l join borrowing_records b 
USING (book_id)
WHERE b.return_date IS NULL 
GROUP BY l.book_id 
HAVING COUNT(*) = l.total_copies 
ORDER BY current_borrowers DESC, l.title;

