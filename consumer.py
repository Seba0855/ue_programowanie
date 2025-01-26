import csv
import time


def consume_jobs(file_name):
    while True:
        with open(file_name, mode='r') as file:
            reader = csv.reader(file)
            jobs = list(reader)

        for i in range(1, len(jobs)):  # Pomija nagłówek
            if jobs[i][0] == "pending":
                print("Rozpoczynam pracę...")
                jobs[i][0] = "in_progress"

                with open(file_name, mode='w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerows(jobs)

                time.sleep(30)  # Symuluje czas wykonywania pracy

                jobs[i][0] = "done"
                with open(file_name, mode='w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerows(jobs)

                print("Praca zakończona.")

        time.sleep(5)  # Sprawdza co 5 sekund


if __name__ == "__main__":
    filename = "jobs.csv"
    consume_jobs(filename)
