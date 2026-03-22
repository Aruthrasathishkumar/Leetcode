import csv
import math
import heapq

G = 9.8  # gravitational constant


def parse_csv(filename, filter_bipedal=False):
    """Parse CSV file and return dictionary of relevant data"""
    data = {}
    try:
        with open(filename, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if filter_bipedal and row.get('STANCE') != 'bipedal':
                    continue

                name = row['NAME']

                if 'LEG_LENGTH' in row:
                    data[name] = float(row['LEG_LENGTH'])
                elif 'STRIDE_LENGTH' in row:
                    data[name] = float(row['STRIDE_LENGTH'])

    except FileNotFoundError:
        print(f"Error: File {filename} not found")
        return {}
    except Exception as e:
        print(f"Error reading {filename}: {e}")
        return {}

    return data


def calculate_dinosaur_speeds(file1, file2):
    """Calculate speeds for bipedal dinosaurs and return sorted list"""

    # Parse data files
    leg_lengths = parse_csv(file1)
    stride_lengths = parse_csv(file2, filter_bipedal=True)

    # Calculate speeds using heap for efficient sorting
    speed_heap = []

    for name, stride_length in stride_lengths.items():
        if name in leg_lengths:
            leg_length = leg_lengths[name]

            # Handle edge case
            if leg_length == 0:
                continue

            # Speed formula:
            # ((STRIDE_LENGTH / LEG_LENGTH) - 1) * sqrt(LEG_LENGTH * g)
            ratio = stride_length / leg_length

            if ratio > 1:  # Ensure positive speed
                speed = (ratio - 1) * math.sqrt(leg_length * G)
                heapq.heappush(speed_heap, (-speed, name))

    # Extract sorted results
    result = []
    while speed_heap:
        _, name = heapq.heappop(speed_heap)
        result.append(name)

    return result


# Scalability version for large files
def process_large_files(file1, file2, chunk_size=1000):
    """Process large CSV files efficiently"""

    leg_data = {}
    bipedal_dinos = set()

    # First pass: identify bipedal dinosaurs
    with open(file2, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['STANCE'] == 'bipedal':
                bipedal_dinos.add(row['NAME'])

    # Second pass: get leg lengths only for bipedal dinosaurs
    with open(file1, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['NAME'] in bipedal_dinos:
                leg_data[row['NAME']] = float(row['LEG_LENGTH'])

    