import pandas as pd

csvfile = pd.read_csv('Employee_Data.csv', encoding='cp1252')



'''
Removes record of employees who have left
Saves updated dataframe
Removes the 'Exit Date' column
'''
csvfile = csvfile[csvfile['Exit Date'].isna()]
csvfile.to_csv('Employee_Data-removed_former_employees', index=False, mode='w')
csvfile = csvfile.drop(columns=['Exit Date'])



'''
Remove employees with 'Hire Date' below 2018
Save the updated DataFrame to a new CSV file
'''
csvfile = csvfile[pd.to_datetime(csvfile['Hire Date'], format='%d/%m/%Y', errors='coerce').dt.year >= 2018]
csvfile.to_csv('Employee_Data-removed_employees_hired_from_2018_above', index=False, mode='w')




'''
Convert the salary column from $ to £ to nearest penny
Replace USD value with GBP value
Save the updated DataFrame to a new CSV file
'''
exchange_rate_usd_to_gbp = 0.79
csvfile['Annual Salary'] = (csvfile['Annual Salary'].replace('[\$,]', '', regex=True)
                            .astype(float) * exchange_rate_usd_to_gbp).round(2)
csvfile.rename(columns={'Annual Salary': 'Annual Salary GBP'}, inplace=True)

csvfile.to_csv('Employee_Data-converted_USD_to_GBP', index=False, mode='w')



'''
Convert 'Hire Date' column to datetime format
Format date back to source format
Save the updated DataFrame to a new CSV file
'''
formattedDate = pd.to_datetime(csvfile['Hire Date'], format='%m/%d/%Y', errors='coerce')
csvfile['Hire Date'] = formattedDate.dt.strftime("%d/%m/%Y")
csvfile.to_csv('Employee_Data-reformatted_date', index=False, mode='w')




