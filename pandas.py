import pandas as pd
# Department DataFrame
departments = pd.DataFrame({
    'Department_ID': [1, 2, 3, 4],
    'Department_Name': ['HR', 'Finance', 'IT', 'Marketing'],
    'Location': ['New York', 'Chicago', 'San Francisco', 'Boston']
})
# Employee DataFrame
employees = pd.DataFrame({
    'Employee_ID': [101, 102, 103, 104, 105],
    
    'Name': ['John', 'Jane', 'Sam', 'Anna', 'Mike'],
    'Department_ID': [1, 2, 3, 3, 1],
    'Salary': [50000, 60000, 75000, 50000, 55000]
})
joined=pd.merge(departments,employees)
print(joined)