# Travel Bookings ETL Pipeline

Which destinations bring the most revenue, and which tour operators are used most often?

A small ETL pipeline that loads travel agency booking data with Pandas, cleans it (deduplication, status filtering, price formatting), loads it into a SQLite database, and runs SQL queries to answer business questions — total revenue by destination country, and booking counts by tour operator.

**Note on data:** the original CSV files contain real booking data and are excluded from this repository for privacy reasons (see `.gitignore`). To run this project, supply your own booking data in the same column structure (see the column list in `main.py`).

## Example Output

Total revenue grouped by destination:
country  total_revenue
0    Egypt      177784.41
1   Greece      151462.37
...

Bookings grouped by tour operator:
operator  bookings_count
0      VITX              36
1      WEZY              19
...



## Pipeline

Two CSV files → Pandas (merge, clean, deduplicate) → SQLite → SQL queries → report

## Tech Stack
- Python — `pandas`
- SQL — `sqlite3`