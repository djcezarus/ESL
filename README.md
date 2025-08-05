# ESL
payroll_project Python
# Payroll Processing Program

This project is a simple Python-based data processing program developed as part of a university assignment. It reads employee data from a CSV file, performs payroll calculations, and outputs the processed data to a new CSV file.

## Features

- Read employee name, hours worked, and hourly rate from a CSV file
- Calculate:
  - Total Pay
  - Tax Deduction (20%)
  - Net Pay
- Output results to a new CSV file
- Run from the command line with a batch script

## Project Structure

```
📁 payroll_project/
├── process_payroll.py       # Main Python script
├── run_payroll.bat          # Batch script to execute the program
├── employees.csv            # Sample input data
├── output.csv               # Output (generated after running)
```

## Usage

1. Ensure you have Python installed.
2. Open a Command Prompt in the project directory.
3. Run the following command:

```bash
run_payroll.bat employees.csv
```

This will create `output.csv` with calculated payroll information.

## Sample Input (`employees.csv`)

```
Name,Hours Worked,Hourly Rate
Alice,40,15
Bob,38,20
Charlie,45,18
```

## Output (`output.csv`)

```
Name,Total Pay,Tax Deduction,Net Pay
Alice,600.00,120.00,480.00
Bob,760.00,152.00,608.00
Charlie,810.00,162.00,648.00
```

## Author

Your Name – [your-university-email@example.com](mailto:your-university-email@example.com)

## License

This project is for academic purposes only.
