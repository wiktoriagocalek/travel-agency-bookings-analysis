import pandas as pd

df = pd.read_csv("archive_reservations.csv", sep=";", encoding="utf-8")
df_current = pd.read_csv("all_reservations.csv", sep=";", encoding="utf-8")
df_all = pd.concat([df, df_current], ignore_index=True)

df_confirmed = df_all[df_all["status"] == "OK"]
df_confirmed = df_confirmed.drop_duplicates(subset = "bookingNr")
df_confirmed["price"] = df_confirmed["price"].str.replace(",", ".").astype(float)

import sqlite3

conn = sqlite3.connect("bookings.db")
df_confirmed.to_sql("bookings", conn, if_exists="replace", index=False)

revenue_by_country = pd.read_sql("SELECT country, sum(price) as total_revenue FROM bookings GROUP BY country ORDER BY total_revenue DESC", conn)

print(f"\n The table presented below shows total income grouped by destinations: \n\n  {revenue_by_country}")

booking_by_operator = pd.read_sql("SELECT operator, COUNT(operator) as bookings_count from bookings GROUP BY operator ORDER BY bookings_count DESC ", conn)
print(f"\n The table presented below shows numbers of booking grouped by tour operators: \n\n  {booking_by_operator}")
