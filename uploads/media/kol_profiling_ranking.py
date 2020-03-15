import pandas as pd
import os 
dir_path = os.path.dirname(os.path.realpath(__file__))
excelfile_path = "%s\\profiling_data.xlsx" %dir_path
# Reading excel file "Profiling_data.xlsx", Sheet Name="Bio" with dataframe name as 'kol'  
kol = pd.read_excel(excelfile_path, "Bio")
kol_name = kol['KOL Name'].unique() #storing all unique names from the excel to a list name 'kol_name'

#opening and reading "input_profiling.txt"file
file_path = "%s\\input_profiling.txt" %dir_path
file = open(file_path, "r")

#Initializing some lists to store different column values in the output ranking file
kol_score =                    [0]*len(kol_name)
Congress_Count =               [0]*len(kol_name)
Breast_Cancer_Congress_Count = [0]*len(kol_name)         
Clinical_trial_Count =         [0]*len(kol_name)         
Breast_Cancer_Trials_Count =   [0]*len(kol_name)   
Principal_Investigator =       [0]*len(kol_name)         
Publication_Count =            [0]*len(kol_name)         
First_Author_Pubs_Count =      [0]*len(kol_name)         
Breast_Cancer_Pubs_Count =     [0]*len(kol_name)         
ACADEMIC_Count =               [0]*len(kol_name)
Journal_Count =                [0]*len(kol_name)
ASSOCIATION_Count =            [0]*len(kol_name)         #not known
GUIDELINE_Count =              [0]*len(kol_name)         #not known
HOSPITAL_Count =               [0]*len(kol_name)
PATIENT_GROUP_Count =          [0]*len(kol_name)         #not known
Social_Media =                 [0]*len(kol_name)         #not known

Congress_Count_aggregate =               [0]*len(kol_name)
Breast_Cancer_Congress_Count_aggregate = [0]*len(kol_name)         
Clinical_trial_Count_aggregate =         [0]*len(kol_name)         
Breast_Cancer_Trials_Count_aggregate =   [0]*len(kol_name)   
Principal_Investigator_aggregate =       [0]*len(kol_name)         
Publication_Count_aggregate =            [0]*len(kol_name)         
First_Author_Pubs_Count_aggregate =      [0]*len(kol_name)         
Breast_Cancer_Pubs_Count_aggregate =     [0]*len(kol_name)         
ACADEMIC_Count_aggregate =               [0]*len(kol_name)
Journal_Count_aggregate =                [0]*len(kol_name)
ASSOCIATION_Count_aggregate =            [0]*len(kol_name)         #not known
GUIDELINE_Count_aggregate =              [0]*len(kol_name)         #not known
HOSPITAL_Count_aggregate =               [0]*len(kol_name)
PATIENT_GROUP_Count_aggregate =          [0]*len(kol_name)         #not known
Social_Media_aggregate =                 [0]*len(kol_name)         #not known


data_list = []  #Intializing list for storing data present in the file line wise 
for line in file:
    data = list(line.strip().split(','))    #Splitting the data present in line by comma(,)  
    data_len = len(data)-1
     
    column_name = [0]*len(data)
    attribute = [0]*len(data)
    
    # Taking the first value(i.e.Sheet name) from the list named 'data' :
    filename = data[0]
    
    # Passing the Sheet name to read the data from
    kol = pd.read_excel(excelfile_path, filename)
    
    eventcount = []
    
    # Started a loop from 1 to data_len and increasing value by 2 everytime,    i=1, 3, 5,.., :
    for i in range(1, data_len, 2):
        # Adding data column_names into "column_name" and attributes into "attribute" :
        column_name[i] = data[i]
        attribute[i] = data[i+1]
        if i==1:
            # storing the rows according to given (column name and attribute) result :
            extracting = (kol[column_name[i]] == attribute[i])
        elif i!=0 and column_name[i] == "Author Position":
            extracting = ((extracting) & (kol[column_name[i]] == int(attribute[i])))
        else:
            extracting = ((extracting) & (kol[column_name[i]] == attribute[i]))
            
    for i in kol_name:
        # Appending the count of rows according to given (column name and attribute) result :
        eventcount.append(len(kol[(extracting) & (kol['KOL Name'] == i)]))     
        
    max_eventcount = max(eventcount) 
    kol_score_event = []
    
    aggregate_eventcount = []
                              
                              
    for k in range(len(eventcount)):
        try:
            aggregate = eventcount[k]/max_eventcount
            aggregate_eventcount.append(float("%.2f" %aggregate))
        except:
            aggregate_eventcount = [0]*len(eventcount)
                              
        # Obtaining the aggregate event count and appending it :
        aggregate_eventcount.append(aggregate)
        
        # weightage = last value in list named 'data' :
        weightage_eventcount = int(data[-1])   
        kol_score_each = aggregate*weightage_eventcount
        kol_score_event.append(float("%.2f" %kol_score_each))
        
        # Appending the kol_score count in list named 'kol_score_event' :
        kol_score[k] += float("%.2f" %kol_score_event[k])

    # Storing the eventcount into the list initialized earlier, according to the following conditions:-  
    if attribute[1] == "Congress" and attribute[3] == 0:
        Congress_Count = eventcount
        Congress_Count_aggregate = aggregate_eventcount
            
    elif attribute[1] == "Congress" and attribute[3] == "Breast Cancer":
        Breast_Cancer_Congress_Count = eventcount
        Breast_Cancer_Congress_Count_aggregate = aggregate_eventcount
            
    elif column_name[1] == "Trial Type" and attribute[1] == "Interventional":
        Clinical_trial_Count = eventcount
        Clinical_trial_Count_aggregate = aggregate_eventcount
        
    elif column_name[1] == "Trial Type" and attribute[3] == "Breast Cancer":
        Breast_Cancer_Trials_Count = eventcount
        Breast_Cancer_Trials_Count_aggregate = aggregate_eventcount
        
    elif column_name[1]=="Role" and attribute[1] == "Principal Investigator":
        Principal_Investigator = eventcount
        Principal_Investigator_aggregate = aggregate_eventcount
        
    elif column_name[1]=="Publication_Type" and attribute[1] =="Journal":
        Publication_Count = eventcount
        Publication_Count_aggregate = aggregate_eventcount
        
    elif column_name[1] == "Author Position" and attribute[1] == 1: 
        First_Author_Pubs_Count=eventcount
        First_Author_Pubs_Count_aggregate = aggregate_eventcount
        
    elif column_name[1] == "Publication_Type" and attribute[3] == "Breast Cancer":
        Breast_Cancer_Pubs_Count = eventcount
        Breast_Cancer_Pubs_Count_aggregate = aggregate_eventcount
        
    elif column_name[1] == "Organization_Type" and  attribute[1] == "Academic":        
        ACADEMIC_Count = eventcount
        ACADEMIC_Count_aggregate = aggregate_eventcount
        
    elif attribute[1] == "Association":
        ASSOCIATION_Count = eventcount
        ASSOCIATION_Count_aggregate = aggregate_eventcount
        
    elif attribute[1] == "Guideline":
        GUIDELINE_Count = eventcount
        GUIDELINE_Count_aggregate = aggregate_eventcount
        
    elif column_name[1] == "Organization_Type" and  attribute[1] == "Hospital":
        HOSPITAL_Count = eventcount
        HOSPITAL_Count_aggregate = aggregate_eventcount
        
    elif column_name[1] == "Publication_Type" and attribute[1] == "Journal":
        Journal_Count = eventcount 
        Journal_Count_aggregate = aggregate_eventcount
        
    elif attribute[1] == "Patient Group":
        PATIENT_GROUP_Count = eventcount
        PATIENT_GROUP_Count_aggregate = aggregate_eventcount
        
    elif attribute[1] == "Social Media":
        Social_Media = eventcount
        Social_Media_aggregate = aggregate_eventcount
                              
kol = pd.read_excel(excelfile_path, "Bio")

kol['Vlookup Name']=['(Blank)']*len(kol_name)

kol_df = pd.DataFrame(list(zip(kol['KOL ID'], kol['Vlookup Name'], kol['Last_Name'], kol['First_Name'], kol_name, kol['Suffix'], kol['Tier Classifications'], Congress_Count, Breast_Cancer_Congress_Count, Clinical_trial_Count, Breast_Cancer_Trials_Count, Principal_Investigator, Publication_Count, First_Author_Pubs_Count, Breast_Cancer_Pubs_Count, ACADEMIC_Count, ASSOCIATION_Count, GUIDELINE_Count, HOSPITAL_Count, Journal_Count, PATIENT_GROUP_Count, Social_Media, Congress_Count_aggregate, Breast_Cancer_Congress_Count_aggregate, Clinical_trial_Count_aggregate, Breast_Cancer_Trials_Count_aggregate, Principal_Investigator_aggregate, Publication_Count_aggregate, First_Author_Pubs_Count_aggregate, Breast_Cancer_Pubs_Count_aggregate, ACADEMIC_Count_aggregate, ASSOCIATION_Count_aggregate, GUIDELINE_Count_aggregate, HOSPITAL_Count_aggregate, Journal_Count_aggregate, PATIENT_GROUP_Count_aggregate, Social_Media_aggregate, kol_score)),
                     columns = ['KOL ID', 'Vlookup Name', 'Last Name', 'First Name', 'Kol Full Name', 'Suffix', 'Tier Classifications', 'Congress_Count','Breast_Cancer_Congress_Count','Clinical_trial_Count','Breast_Cancer_Trials_Count', 'Principal_Investigator', 'Publication_Count','First_Author_Pubs_Count', 'Breast_Cancer_Pubs_Count', 'ACADEMIC_Count','ASSOCIATION_Count', 'GUIDELINE_Count', 'HOSPITAL_Count', 'Journal_Count','PATIENT_GROUP_Count', 'Social_Media', 'Congress_Count_aggregate', 'Breast_Cancer_Congress_Count_aggregate', 'Clinical_trial_Count_aggregate', 'Breast_Cancer_Trials_Count_aggregate', 'Principal_Investigator_aggregate', 'Publication_Count_aggregate', 'First_Author_Pubs_Count_aggregate', 'Breast_Cancer_Pubs_Count_aggregate', 'ACADEMIC_Count_aggregate', 'ASSOCIATION_Count_aggregate', 'GUIDELINE_Count_aggregate', 'HOSPITAL_Count_aggregate', 'Journal_Count_aggregate', 'PATIENT_GROUP_Count_aggregate', 'Social_Media_aggregate', 'Kol Score'])
kol_df["Kol Rank"] = kol_df["Kol Score"].rank(method='first', ascending=False)


kol_df['Therapeutic Area'] = ['(Blank)']*len(kol_name)
try:
    kol_df["Specialty"] = kol['Specialty'][:len(kol_name)]
except:
    kol_df["Specialty"] = ['(Blank)']*len(kol_name)
try:
    kol_df["Salutation"] = kol['Salutation'][:len(kol_name)]
except:
    kol_df["Salutation"] = ['(Blank)']*len(kol_name)
try:
    kol_df["Affilation"] = kol['Affiliation'][:len(kol_name)]
except:
    kol_df["Affiliation"] = ['(Blank)']*len(kol_name)
try:
    kol_df["Department"] = kol['Department'][:len(kol_name)]
except:
    kol_df["Department"] = ['(Blank)']*len(kol_name)
try:
    kol_df["Designation"] = kol['Title'][:len(kol_name)]
except:
    kol_df["Designation"] = ['(Blank)']*len(kol_name)
try:
    kol_df["Address"] = kol['Address1'][:len(kol_name)]
except:
    kol_df["Address"] = ['(Blank)']*len(kol_name)
try:
    kol_df["City"] = kol['City'][:len(kol_name)]
except:
    kol_df["City"] = ['(Blank)']*len(kol_name)
try:
    kol_df["State"] = kol['State'][:len(kol_name)] 
except:
    kol_df["State"] = ['(Blank)']*len(kol_name)
try:
    kol_df["Country"] = kol['Country'][:len(kol_name)]
except:
    kol_df["Country"] = ['(Blank)']*len(kol_name)
try:
    kol_df["Email"] = kol['Primary_Email'][:len(kol_name)]
except:
    kol_df["Email"] = ['(Blank)']*len(kol_name)
try:
    kol_df["Phone"] = kol['Phone'][:len(kol_name)]
except:
    kol_df["Phone"] = ['(Blank)']*len(kol_name)
try:
    kol_df["Fax"] = kol['Fax'][:len(kol_name)]
except:
    kol_df["Fax"] = ['(Blank)']*len(kol_name)
try:
    kol_df["Brief profile"] = kol['Bio_Summary'][:len(kol_name)]                                                                                       
except:    
    kol_df["Brief profile"] = ['(Blank)']*len(kol_name)
    
kol_df['Reference1']=['(Blank)']*len(kol_name)
kol_df['Reference2']=['(Blank)']*len(kol_name)
kol_df['Reference3']=['(Blank)']*len(kol_name)
    
kol_df = kol_df.sort_values("Kol Rank")
outputfile_path = "%s\\profiling_output_rank.xlsx" %dir_path
kol_df.to_excel(outputfile_path, index=False)
