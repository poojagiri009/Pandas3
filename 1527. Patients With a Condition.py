import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    result = []
    for i in range(len(patients)):
        name = patients['patient_name'][i]
        pid = patients['patient_id'][i]
        conditions = patients['conditions'][i]
        for condition in conditions.split():
            if(condition.startswith('DIAB1')):
                result.append([pid,name,conditions])
                break
    return pd.DataFrame(result,columns=['patient_id','patient_name','conditions'])

	#using contains

import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    df = patients[(patients['conditions'].str.startswith('DIAB1')) | (patients['conditions'].str.contains(' DIAB1'))]
    return df

	
	#another way using regex \b => space
	import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    return patients[(patients['conditions'].str.contains(r'\bDIAB1'))]
	
	
	
	