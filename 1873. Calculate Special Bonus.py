#Using list
import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    mylist= []
    for i in range(len(employees)):
        e_id = employees['employee_id'][i]
        name = employees['name'][i]
        if((e_id % 2 != 0) & (name[0] != 'M')):
            mylist.append([e_id,employees['salary'][i]])
        else:
            mylist.append([e_id,0])

    return pd.DataFrame(mylist, columns=['employee_id','bonus']).sort_values(['employee_id'])


#Another way using df

import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    for i in range(len(employees)):
        e_id = employees['employee_id'][i]
        name = employees['name'][i]
        if((e_id % 2 == 0) or (name[0] == 'M')):
            employees['salary'][i] = 0
    return employees[['employee_id','salary']].rename(columns={'salary':'bonus'}).sort_values(['employee_id'])
	
#Using lambda - vectorization

import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = employees.apply(lambda x : x['salary']
    if (x['employee_id'] % 2) and not (x['name'].startswith('M'))
    else 0, axis=1)
    return employees[['employee_id','bonus']].sort_values(by =['employee_id'])
