# Travel Bookings ETL Pipeline

Which destinations bring the most revenue, and which tour operators are used most often?

A small ETL pipeline that loads travel agency booking data with Pandas, cleans it (deduplication, status filtering, price formatting), loads it into a SQLite database, and runs SQL queries to answer business questions — total revenue by destination country, and booking counts by tour operator.

**Note on data:** the original CSV files contain real booking data and are excluded from this repository for privacy reasons (see `.gitignore`). To run this project, supply your own CSV files with at least these columns: bookingNr, status, price, country, operator.

## Example Output

**Total revenue by destination:**

| Country | Total Revenue |
|---|---|
| Egypt | 152,340.00 |
| Greece | 128,910.50 |
| Spain | 119,275.00 |
| Turkey | 94,680.20 |
| Maldives | 38,200.00 |
| Thailand | 31,450.75 |

**Bookings by tour operator:**

| Operator | Bookings Count |
|---|---|
| Operator A | 34 |
| Operator B | 17 |
| Operator C | 14 |
| Operator D | 7 |
| Operator E | 4 |


## Pipeline

Two CSV files → Pandas (merge, clean, deduplicate) → SQLite → SQL queries → report

## Tech Stack
- Python — `pandas`
- SQL — `sqlite3`