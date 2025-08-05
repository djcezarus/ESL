import csv
import sys

def calculate_pay(hours, rate):
    """Calculate total pay, tax deduction (20%), and net pay."""
    total = hours * rate
    tax = total * 0.2
    net = total - tax
    return total, tax, net

def process_file(input_file, output_file):
    """Process payroll from input CSV and write results to output CSV."""
    try:
        with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
            reader = csv.DictReader(infile)
            fieldnames = ['Name', 'Total Pay', 'Tax Deduction', 'Net Pay']
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()

            for row in reader:
                name = row['Name']
                hours = float(row['Hours Worked'])
                rate = float(row['Hourly Rate'])
                total, tax, net = calculate_pay(hours, rate)
                writer.writerow({
                    'Name': name,
                    'Total Pay': f"{total:.2f}",
                    'Tax Deduction': f"{tax:.2f}",
                    'Net Pay': f"{net:.2f}"
                })
        print("Processing complete. Output saved to", output_file)
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python process_payroll.py <input_file.csv>")
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = "output.csv"
    process_file(input_path, output_path)
