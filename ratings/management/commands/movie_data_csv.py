import csv
import os
from django.core.management.base import BaseCommand
from ratings.models import MOVIE


class Command(BaseCommand):
    help = 'Imports movie data from a CSV file.'

    def handle(self, *args, **options):
        # Construct the absolute path to the CSV file
        csv_file_path = os.path.join(os.path.dirname(__file__), 'update_movies_720.csv')

        try:
            with open(csv_file_path, 'r', encoding='utf-8') as file:
                reader = csv.reader(file)
                next(reader)  # Skip the header row
                count = 1
                for row in reader:
                    try:
                        MOVIE.objects.create(
                            movie_id=count,
                            poster=row[0],
                            title=row[1],
                            genre=row[5],
                            released_year=int(row[2]),
                            ratings=float(row[6]),
                            overview=row[7],
                            director=row[9]
                        )
                    except (IndexError, ValueError) as e:
                        # Log the error for better debugging
                        self.stderr.write(f"Skipping row due to data error: {e}")
                        continue
                    count += 1
                self.stdout.write(self.style.SUCCESS(f'Successfully imported {count - 1} movies.'))
        except FileNotFoundError:
            self.stderr.write(self.style.ERROR(f'CSV file not found at: {csv_file_path}'))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f'An unexpected error occurred: {e}'))