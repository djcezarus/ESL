@echo off
REM This script runs the payroll processing Python program
REM Usage: run_payroll.bat employees.csv

python process_payroll.py %1
