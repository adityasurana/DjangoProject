import pandas as pd
list_column = []
kol_excel = pd.read_excel("C://Users//hi//django_project//uploads//media//raw_data.xlsx", "Raw Data")
for i in kol_excel.iloc[0]:
    list_column.append(i)
kol_excel.columns = list_column
kol_excel.drop(kol_excel.index[:1], inplace=True)

kol_excel.to_csv("C://Users//hi//django_project//uploads//media//kol_data_commasep.txt", sep=',', index=False)
file_name = 'C://Users//hi//django_project//uploads//media//kol_data_commasep.txt'
kol = pd.read_csv(file_name, sep=',')

kol_name = kol['Full Name'].unique()
kol_score = [0]*len(kol_name)

Congress_Count =               [0]*len(kol_name)
Breast_Cancer_Congress_Count = [0]*len(kol_name)         #not known
Clinical_trial_Count =         [0]*len(kol_name)         
Breast_Cancer_Trials_Count =   [0]*len(kol_name)         #not known
Principal_Investigator =       [0]*len(kol_name)        
Publication_Count =            [0]*len(kol_name)         
First_Author_Pubs_Count =      [0]*len(kol_name)         
Breast_Cancer_Pubs_Count =     [0]*len(kol_name)         #not known
ACADEMIC_Count =               [0]*len(kol_name)
Journal_Count =                [0]*len(kol_name)
ASSOCIATION_Count =            [0]*len(kol_name)
GUIDELINE_Count =              [0]*len(kol_name)
HOSPITAL_Count =               [0]*len(kol_name)
PATIENT_GROUP_Count =          [0]*len(kol_name)
Social_Media =                 [0]*len(kol_name)          #not known

Congress_Count_aggregate =               [0]*len(kol_name)
Breast_Cancer_Congress_Count_aggregate = [0]*len(kol_name)         #not known
Clinical_trial_Count_aggregate =         [0]*len(kol_name)         
Breast_Cancer_Trials_Count_aggregate =   [0]*len(kol_name)         #not known
Principal_Investigator_aggregate =       [0]*len(kol_name)        
Publication_Count_aggregate =            [0]*len(kol_name)         
First_Author_Pubs_Count_aggregate =      [0]*len(kol_name)         
Breast_Cancer_Pubs_Count_aggregate =     [0]*len(kol_name)         #not known
ACADEMIC_Count_aggregate =               [0]*len(kol_name)
ASSOCIATION_Count_aggregate =            [0]*len(kol_name)
GUIDELINE_Count_aggregate =              [0]*len(kol_name)
HOSPITAL_Count_aggregate =               [0]*len(kol_name)
Journal_Count_aggregate =                [0]*len(kol_name)
PATIENT_GROUP_Count_aggregate =          [0]*len(kol_name)
Social_Media_aggregate =                 [0]*len(kol_name)          #not known


file = open("C://Users//hi//django_project//uploads//media//input_raw_data.txt", "r")
data_list = []
for line in file:
    data = list(line.strip().split(','))
    data_len = len(data)-1
    column_name = [0]*len(data)
    attribute = [0]*len(data)
    
    eventcount = []
    
    # Started a loop from 0 to data_len and increasing value by 2 everytime,    i=0, 2, 4,.., :
    for i in range(0, data_len, 2):
        # Adding data column_names into "column_name" and attributes into "attribute" :
        column_name[i] = data[i]
        attribute[i] = data[i+1]
        if i==0:
            # storing the rows according to given (column name and attribute) result :
            extracting = (kol[column_name[i]] == attribute[i])
            
        elif i!=0 and column_name[i] == "First Author":
            extracting = ((extracting) & (kol[column_name[i]] == int(attribute[i])))
            
        else:
            extracting = ((extracting) & (kol[column_name[i]] == attribute[i]))  
            
        
    for j in kol_name:
        eventcount.append(len(kol[(extracting) & (kol['Full Name'] == j)]))    
        
    max_eventcount = max(eventcount)        
    kol_score_event = []
    aggregate_eventcount = []
    
    for k in range(len(eventcount)):
        try:
            aggregate=eventcount[k]/max_eventcount
            aggregate_eventcount.append(float("%.2f" %aggregate))
        except:
            aggregate_eventcount = [0]*len(eventcount)
            aggregate = 0
        weightage_eventcount = int(data[-1])   
        kol_score_each = aggregate*weightage_eventcount
        kol_score_event.append(float("%.2f" %kol_score_each)) 
        kol_score[k] += float("%.2f" %kol_score_event[k])
        
    #print(attribute[0], attribute[2], column_name[0], column_name[2])
    
    if (attribute[0] == "CONGRESS" or attribute[0] == "EVENTS") and attribute[2]==0:
        Congress_Count = eventcount
        Congress_Count_aggregate = aggregate_eventcount
            
    elif attribute[0] == "CONGRESS" and attribute[2] == "Breast Cancer":
        Breast_Cancer_Congress_Count = eventcount
        Breast_Cancer_Congress_Count_aggregate = aggregate_eventcount
            
    elif (attribute[0] == "TRIAL_Breast Cancer" or attribute[0] == "TRIALS") and attribute[2]==0:
        Clinical_trial_Count = eventcount
        Clinical_trial_Count_aggregate = aggregate_eventcount
            
    elif attribute[0] == "TRIALS" and attribute[2] == "Breast Cancer":
        Breast_Cancer_Trials_Count = eventcount
        Breast_Cancer_Trials_Count_aggregate = aggregate_eventcount
            
    elif attribute[0] == "Principal Investigator" and column_name[0] == "Role":
        Principal_Investigator = eventcount
        Principal_Investigator_aggregate = aggregate_eventcount
            
    elif attribute[0] == "PUBLICATIONS" and attribute[2]==0:
        Publication_Count = eventcount
        Publication_Count_aggregate = aggregate_eventcount
            
    elif column_name[0] == "First Author":
        First_Author_Pubs_Count = eventcount
        First_Author_Pubs_Count_aggregate = aggregate_eventcount
        
    elif attribute[0] == "PUBLICATIONS" and attribute[2] == "Breast Cancer":
        Breast_Cancer_Pubs_Count = eventcount
        Breast_Cancer_Pubs_Count_aggregate = aggregate_eventcount
            
    elif attribute[0] == "ACADEMIC":
        ACADEMIC_Count = eventcount
        ACADEMIC_Count_aggregate = aggregate_eventcount
            
    elif attribute[0] == "ASSOCIATION":
        ASSOCIATION_Count = eventcount
        ASSOCIATION_Count_aggregate = aggregate_eventcount
            
    elif attribute[0] == "GUIDELINE":
        GUIDELINE_Count = eventcount
        GUIDELINE_Count_aggregate = aggregate_eventcount
            
    elif attribute[0] == "HOSPITAL":
        HOSPITAL_Count = eventcount
        HOSPITAL_Count_aggregate = aggregate_eventcount
            
    elif attribute[0] == "JOURNAL":
        Journal_Count = eventcount
        Journal_Count_aggregate = aggregate_eventcount
              
    elif attribute[0] == "PATIENT GROUP":
        PATIENT_GROUP_Count = eventcount
        PATIENT_GROUP_Count_aggregate = aggregate_eventcount
            
    elif column_name[0] == "Social Media" or attribute[0] == "Social Media":
        Social_Media = eventcount
        Social_Media_aggregate = aggregate_eventcount
    else:
        continue
        
kol = pd.read_csv('C://Users//hi//django_project//uploads//media//kol_data_commasep.txt', sep=',')

vlookup=[]
kol_id=[]
last_name=[]
first_name=[]
suffix=[]
tier=[]

for i in kol_name:
    try:
        vlookup.append(kol[kol['Full Name']==i]['Vlookup Name'].unique()[0])
        kol_id.append(kol[kol['Full Name']==i]['KOL ID'].unique()[0])
        last_name.append(kol[kol['Full Name']==i]['Last Name'].unique()[0])
        first_name.append(kol[kol['Full Name']==i]['First Name'].unique()[0])
        suffix.append(kol[kol['Full Name']==i]['Suffix'].unique()[0])                #not known
        tier.append(kol[kol['Full Name']==i]['Tier Classifications'].unique()[0])    #not known
    except:
        suffix.append('')
        tier.append('')
        
        
kol_df = pd.DataFrame(list(zip(kol_id, vlookup, last_name, first_name, kol_name, suffix, tier, Congress_Count, Breast_Cancer_Congress_Count, Clinical_trial_Count, Breast_Cancer_Trials_Count, Principal_Investigator, Publication_Count, First_Author_Pubs_Count, Breast_Cancer_Pubs_Count, ACADEMIC_Count, ASSOCIATION_Count, GUIDELINE_Count, HOSPITAL_Count, Journal_Count, PATIENT_GROUP_Count, Social_Media, Congress_Count_aggregate, Breast_Cancer_Congress_Count_aggregate, Clinical_trial_Count_aggregate, Breast_Cancer_Trials_Count_aggregate, Principal_Investigator_aggregate, Publication_Count_aggregate, First_Author_Pubs_Count_aggregate, Breast_Cancer_Pubs_Count_aggregate, ACADEMIC_Count_aggregate, ASSOCIATION_Count_aggregate, GUIDELINE_Count_aggregate, HOSPITAL_Count_aggregate, Journal_Count_aggregate, PATIENT_GROUP_Count_aggregate, Social_Media_aggregate, kol_score)),
                     columns = ['KOL ID', 'Vlookup Name', 'Last Name', 'First Name', 'Kol Full Name', 'Suffix', 'Tier Classifications', 'Congress_Count','Breast_Cancer_Congress_Count','Clinical_trial_Count','Breast_Cancer_Trials_Count', 'Principal_Investigator', 'Publication_Count','First_Author_Pubs_Count', 'Breast_Cancer_Pubs_Count', 'ACADEMIC_Count','ASSOCIATION_Count', 'GUIDELINE_Count', 'HOSPITAL_Count', 'Journal_Count','PATIENT_GROUP_Count', 'Social_Media', 'Congress_Count_aggregate', 'Breast_Cancer_Congress_Count_aggregate', 'Clinical_trial_Count_aggregate', 'Breast_Cancer_Trials_Count_aggregate', 'Principal_Investigator_aggregate', 'Publication_Count_aggregate', 'First_Author_Pubs_Count_aggregate', 'Breast_Cancer_Pubs_Count_aggregate', 'ACADEMIC_Count_aggregate', 'ASSOCIATION_Count_aggregate', 'GUIDELINE_Count_aggregate', 'HOSPITAL_Count_aggregate', 'Journal_Count_aggregate', 'PATIENT_GROUP_Count_aggregate', 'Social_Media_aggregate', 'Kol Score'])
kol_df["Kol Rank"] = kol_df["Kol Score"].rank(method='first', ascending=False)

kol_df['Therapeutic Area'] = ['(Blank)']*len(kol_name)

Salutation=[]
Affilation=[]
Department=[]
Position=[]
City=[]
Country=[]
State=[]
E_mail=[]
Contact=[]

Specialty=[]
Address=[]
Fax=[]
Bio=[]

for i in kol_name:
    try:
        Salutation.append(kol[kol['Full Name']==i]['Salutation'].unique()[0])
        Affilation.append(kol[kol['Full Name']==i]['Affilation'].unique()[0])
        Department.append(kol[kol['Full Name']==i]['Department'].unique()[0])
        Position.append(kol[kol['Full Name']==i]['Position'].unique()[0])
        City.append(kol[kol['Full Name']==i]['City'].unique()[0])
        Country.append(kol[kol['Full Name']==i]['Country'].unique()[0])
        E_mail.append(kol[kol['Full Name']==i]['E_mail'].unique()[0])
        Contact.append(kol[kol['Full Name']==i]['Contact Info'].unique()[0])
        
        Specialty.append(kol[kol['Full Name']==i]['Specialty'].unique()[0])          #not known
        Address.append(kol[kol['Full Name']==i]['Address'].unique()[0])              #not known       check this once
        State.append(kol[kol['Full Name']==i]['State'].unique()[0])                  #not known
        Fax.append(kol[kol['Full Name']==i]['Fax'].unique()[0])                      #not known
        Bio.append(kol[kol['Full Name']==i]['Bio_Summary'].unique()[0])              #not known
                
    except:
        Specialty.append('')
        Address.append('')
        State.append('')
        Fax.append('')
        Bio.append('')

try:
    kol_df["Specialty"] = Specialty[:len(kol_name)]                     #not known
except:
    kol_df["Specialty"] = ['(Blank)']*len(kol_name)
try:
    kol_df["Salutation"] = Salutation[:len(kol_name)]
except:
    kol_df["Salutation"] = ['(Blank)']*len(kol_name)
try:
    kol_df["Affilation"] = Affilation[:len(kol_name)]
except:
    kol_df["Affiliation"] = ['(Blank)']*len(kol_name)
try:
    kol_df["Department"] = Department[:len(kol_name)]
except:
    kol_df["Department"] = ['(Blank)']*len(kol_name)
try:
    kol_df["Designation"] = Position[:len(kol_name)]
except:
    kol_df["Designation"] = ['(Blank)']*len(kol_name)
try:
    kol_df["Address"] = Address[:len(kol_name)]                        #not known
except:
    kol_df["Address"] = ['(Blank)']*len(kol_name)
try:
    kol_df["City"] = City[:len(kol_name)]
except:
    kol_df["City"] = ['(Blank)']*len(kol_name)
try:
    kol_df["State"] = State[:len(kol_name)]                             #not known
except:
    kol_df["State"] = ['(Blank)']*len(kol_name)
try:
    kol_df["Country"] = Country[:len(kol_name)]
except:
    kol_df["Country"] = ['(Blank)']*len(kol_name)
try:
    kol_df["Email"] = E_mail[:len(kol_name)]
except:
    kol_df["Email"] = ['(Blank)']*len(kol_name)
try:
    kol_df["Phone"] = Contact[:len(kol_name)]
except:
    kol_df["Phone"] = ['(Blank)']*len(kol_name)
try:
    kol_df["Fax"] = Fax[:len(kol_name)]                                #not known
except:
    kol_df["Fax"] = ['(Blank)']*len(kol_name)
try:
    kol_df["Brief profile"] = Bio[:len(kol_name)]             #not known                                                                                   
except:    
    kol_df["Brief profile"] = ['(Blank)']*len(kol_name)
        
kol_df['Reference1']=['(Blank)']*len(kol_name)
kol_df['Reference2']=['(Blank)']*len(kol_name)
kol_df['Reference3']=['(Blank)']*len(kol_name)

kol_df = kol_df.sort_values("Kol Rank")
kol_df.to_excel("C://Users//hi//django_project//uploads//media//rawdata_output_rank.xlsx", index=False)
