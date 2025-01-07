import csv
import time


def add_job(file_name):
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["pending"])  # Dodaje nową pracę o statusie "pending"
        print("Dodano nową pracę do kolejki.")


if __name__ == "__main__":
    filename = "jobs.csv"

    # Tworzy plik, jeśli nie istnieje
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["status"])  # Nagłówek pliku

    while True:
        add_job(filename)
        time.sleep(5)  # Dodawanie nowej pracy co 5 sekund
