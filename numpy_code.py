import numpy as np
import csv
python_scores=[]
sql_scores=[]
aptitude_scores=[]
communication_scores=[]
with open("placement_readiness.csv","r",encoding="utf-8") as file:
    reader=csv.DictReader(file)
    for row in reader:
        python_scores.append((int)(row["Python_Score"]))
        sql_scores.append((int)(row["SQL_Score"]))
        aptitude_scores.append((int)(row["Aptitude_Score"]))
        communication_scores.append((int)(row["Communication_Score"]))
    python_array=np.array(python_scores)
    sql_array=np.array(sql_scores)
    aptitude_array=np.array(aptitude_scores)
    communication_array=np.array(communication_scores)
    #Average Python Score
    avg_py_score=python_array.mean()
    print(f"Avergae Python Score is {avg_py_score:.2f}")
    #Highest and Lowest Aptitude Scores
    highest_apt_score=aptitude_array.max()
    lowest_apt_score=aptitude_array.min()
    print(f"Highest Aptitude Score is {highest_apt_score} and lowest aptitude score is {lowest_apt_score}")
    #How many students scored above 70 in Communication
    communication_above_70=(communication_array>70).sum()
    print(f"No of Students scored above 70 in communication are {communication_above_70}")
    #for every student gap between their best and worst skill
    scores=np.array([python_array,sql_array,aptitude_array,communication_array])
    scores=scores.T
    print(scores)
    best_scores=scores.max(axis=1)
    worst_scores=scores.min(axis=1)
    gap=best_scores-worst_scores
    print(f"for every student gap between their best and worst skill is {gap}")