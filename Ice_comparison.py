import pandas as pd
import matplotlib.pyplot as plt
import os


"""Column searching functions"""
def id(csv, keywords):
    """
    Filter DataFrame columns case-insensitively based on specified keywords in the column headers.

    Parameters:
        csv (pd.DataFrame): The DataFrame to filter.
        keywords (list): List of keywords to search for in column headers.

    Returns:
        pd.DataFrame: A new DataFrame containing the filtered columns.
    """
    keywords=[keywords]

    # Convert the keywords to lowercase for case-insensitive matching
    lower_keywords = [keyword.lower() for keyword in keywords]

    # Filter columns by checking if any keyword is present in a case-insensitive manner
    filtered_columns = [col for col in csv.columns if any(keyword in col.lower() for keyword in lower_keywords)][0]

    # Create a new DataFrame with the filtered columns
    new_csv = csv[filtered_columns]

    return new_csv


"""Plotting funcions"""


xlsx=pd.read_excel("data.xlsx",skiprows=1)
labels="Experiment Hann","Fensap Hann","Clean RG15 Airfoil"
for i in range(3):
    if i >= 2:
        plt.plot(xlsx.iloc[:, 2 * i], xlsx.iloc[:, 2 * i + 1], label=labels[i])
    else:
        plt.fill_between(xlsx.iloc[:, 2 * i], xlsx.iloc[:, 2 * i + 1], label=labels[i], marker=".")

file_names = [i for i in os.listdir(os.curdir) if i.endswith('.csv')]  # Search for files ending with .csv automatically
print(file_names)
for j in range(len(file_names)):#len(file_names)
	file_name=file_names[j]
	print(file_name)	
	csv = pd.read_csv(file_name,skiprows=5)#,delimiter=',',sheet_name=0
	
	y=id(csv,"Y")
	x=id(csv,"X")
	plt.scatter(x,y,label=file_name[:len(file_name)-4],marker=".")
plt.ylabel('Y [ m ]')
plt.xlabel('X [ m ]')

plt.grid()
plt.legend()
plt.axis('equal')
plt.xlim(-0.05,0.1)
plt.savefig('Ice_shape.pdf',bbox_inches='tight', pad_inches=0)
plt.show()


