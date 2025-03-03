# -*- coding: utf-8 -*-
"""visual_analysis.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1TiRjl5mVnP2Rvhzro3WJV8oG2Ol2coau
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load processed dataset
df = pd.read_csv("/content/processed_datafile.csv")

# Create directories if they don’t exist
os.makedirs("Analysis/results", exist_ok=True)

# Open analysis file to store insights
with open("Analysis/analysisfile.txt", "w") as analysis_file:

    # **Bar Plot: Average Scores by Gender**
    plt.figure(figsize=(8, 5))
    avg_scores_gender = df.groupby('gender')[['math score', 'reading score', 'writing score']].mean()
    avg_scores_gender.plot(kind='bar', ax=plt.gca())
    plt.title("Average Scores by Gender")
    plt.xlabel("Gender (0 = Male, 1 = Female)")  # Added label to indicate scale
    plt.ylabel("Average Score")
    plt.xticks(rotation=0)
    plt.legend(title='Subjects')
    plt.tight_layout()
    plt.savefig("Analysis/results/bar_plot_1.png")
    plt.close()

    insight_1 = "Insight 1: Females outperform males in reading and writing, while males slightly outperform females in math.\n"
    analysis_file.write(insight_1)
    print(insight_1)
    # **Bar Plot: Average Scores by Parental Education Level**
    plt.figure(figsize=(10, 5))
    avg_scores_parent_edu = df.groupby('parental level of education')[['math score', 'reading score', 'writing score']].mean()
    avg_scores_parent_edu.plot(kind='bar', ax=plt.gca())
    plt.title("Average Scores by Parental Education Level")
    plt.xlabel("Parental Education Level")
    plt.ylabel("Average Score")
    plt.xticks(rotation=45)
    plt.legend(title='Subjects')
    plt.tight_layout()
    plt.savefig("Analysis/results/bar_plot_2.png")
    plt.close()

    insight_2 = "Insight 2: Higher parental education levels are associated with higher student scores across all subjects.\n"
    analysis_file.write(insight_2)
    print(insight_2)

    # **Bar Plot: Average Scores by Lunch Type**
    plt.figure(figsize=(8, 5))
    avg_scores_lunch = df.groupby('lunch')[['math score', 'reading score', 'writing score']].mean()
    avg_scores_lunch.plot(kind='bar', ax=plt.gca())
    plt.title("Average Scores by Lunch Type")
    plt.xlabel("Lunch Type")
    plt.ylabel("Average Score")
    plt.xticks(rotation=0)
    plt.legend(title='Subjects')
    plt.tight_layout()
    plt.savefig("Analysis/results/bar_plot_3.png")
    plt.close()

    insight_3 = "Insight 3: Students with standard lunch types score higher on average compared to those with free/reduced lunch.\n"
    analysis_file.write(insight_3)
    print(insight_3)

    # **Bar Plot: Average Scores by Test Preparation Course Completion**
    plt.figure(figsize=(8, 5))
    avg_scores_test_prep = df.groupby('test preparation course')[['math score', 'reading score', 'writing score']].mean()
    avg_scores_test_prep.plot(kind='bar', ax=plt.gca())
    plt.title("Average Scores by Test Preparation Course Completion")
    plt.xlabel("Test Preparation Course")
    plt.ylabel("Average Score")
    plt.xticks(rotation=0)
    plt.legend(title='Subjects')
    plt.tight_layout()
    plt.savefig("Analysis/results/bar_plot_4.png")
    plt.close()

    insight_4 = "Insight 4: Students who completed the test preparation course scored higher across all subjects.\n"
    analysis_file.write(insight_4)
    print(insight_4)

    #  **Bar Plot: Average Scores by Ethnicity Group**
    plt.figure(figsize=(10, 5))
    avg_scores_ethnicity = df.groupby('race/ethnicity')[['math score', 'reading score', 'writing score']].mean()
    avg_scores_ethnicity.plot(kind='bar', ax=plt.gca())
    plt.title("Average Scores by Ethnicity Group")
    plt.xlabel("Ethnicity Group")
    plt.ylabel("Average Score")
    plt.xticks(rotation=0)
    plt.legend(title='Subjects')
    plt.tight_layout()
    plt.savefig("Analysis/results/bar_plot_5.png")
    plt.close()

    insight_5 = "Insight 5: There are observable differences in average scores among different ethnicity groups, indicating potential cultural or socioeconomic factors influencing performance.\n"
    analysis_file.write(insight_5)
    print(insight_5)

print("\n Analysis complete. Check 'Analysis/results/' for visualizations and 'Analysis/analysisfile.txt' for insights.")