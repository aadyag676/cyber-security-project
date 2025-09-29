import streamlit as st
import pandas as pd
import plotly.express as px

st.title("explore the insight of cybersecurity incident and data data breaches")

df=pd.read_csv("cybersecurity incident.csv")
df

#bar chart - attack type distribution
fig1=px.bar(df,x='Attack_Type', y='Previous_Incidents',
           title='attack type distribution',
           labels={'Attack_Type':'incident','Count of Incidents':'industry wise'},
           template='plotly_dark'
)
st.plotly_chart(fig1) 
st.subheader("shows which attack (eg:ransomware, phishing) is most common")

#Bar chart - attack vector frequeny
fig2=px.bar(df,x='Attack_Vector', y='Previous_Incidents',
                  title='attack vector frequency',
                  labels={'Company_Name':'company'},
                  color_discrete_sequence=["#F3EB0A"],
                  template='plotly_dark'
)
st.plotly_chart(fig2)
st.subheader("highlights weak entry points like email,web apps,unpatched systems.")


#stacked bar chart - industry vs attack type
fig3=px.bar(df, x='Industry',y='Previous_Incidents',
                 title='country wise attack',
                 color='Attack_Type',barmode='stack',
                 template='plotly_dark'
)
st.plotly_chart(fig3)
st.subheader("shows which industries are most affected by which attacks.")


#timeline
fig4=px.line(df,x='Date_Reported',y='Previous_Incidents',
                 title='incidents by date_reported'
)
st.plotly_chart(fig4)
st.subheader("identifies spikes in attacks during specific months.")


#records compromised by industry
fig5=px.bar(df,x='Industry',y='Records_Compromised',
            title='records compromised by industry',
            color_discrete_sequence=["#E97777"],
            template='plotly_dark'
)
st.plotly_chart(fig5)
st.subheader("reveals which industries leak the most customer data")

fig6=px.box(df, x='Attack_Type', y='Financial_Impact_Million_USD'
)
st.plotly_chart(fig6)
st.subheader("compares how costly diffrent types of attacks are.")


#avearge recovery time by industry
fig7=px.bar(df,x='Industry',y='Recovery_Time_Days',
            title='incident severity vs records compromised',
            color_discrete_sequence=["#008779"],
)
st.plotly_chart(fig7)
st.subheader("shows which sectors recover quickly vs take longest")


#ransom amount vs recovery time
fig8=px.scatter(df,x='Ransom_Amount_USD',y='Recovery_Time_Days',
                color='Attack_Type',
                size='Recovery_Time_Days'
)
st.plotly_chart(fig8)
st.subheader("check if higher ransom demands correlate with longer downtime.")


#barchart incident severity and records compromised
fig9=px.bar(df,x='Incident_Severity',y='Records_Compromised',
            title='incident severity vs records compromised',
            color_discrete_sequence=["#008779"],
)
st.plotly_chart(fig9)
st.subheader("higher severity more record stolen.")


#bar chart patch status vs average severity
fig10=px.bar(df,x='Patch_Status',y='Incident_Severity',
            title='patch status vs average severity',
            color_discrete_sequence=["#CA12F3"],
)
st.plotly_chart(fig10)
st.subheader("confirms wheather poor patching increases severity.")


# MFA enabled vs incident severity
fig11=px.bar(df,x='MFA_Enabled',y='Incident_Severity',
            title='MFA enabled vs incident severity',
            template='plotly_dark',
            color_discrete_sequence=["#C51989"],
)
st.plotly_chart(fig11)
st.subheader("shows if MFA adoption reduces severity.")


#scatter plot security budget vs financial impact
fig12=px.scatter(df, x='Security_Budget_Million_USD',y='Financial_Impact_Million_USD',
                 color='Industry',
                 size='Recovery_Time_Days'
)
st.plotly_chart(fig12)
st.subheader("checks if bigger budgets actually reduce costs of incidents.")


#barchart ciso prescence vs recovery time
fig13=px.bar(df,x='CISO_Present',y='Recovery_Time_Days',
            title='incident severity vs records compromised',
            labels={'CISO_Present':'incident','Recovery_Time_Days':'count'},
             color_discrete_sequence=["#c51245"],
             template='plotly_dark'
)
st.plotly_chart(fig13)
st.subheader("reveals if having a CISO shortens recovery")


#scatter plot - training hours vs customer churn
fig14=px.scatter(df,x='Security_Training_Hours',y='Customer_Churn_Percent',
      color='Country',
       size='Security_Training_Hours'
)
st.plotly_chart(fig14)
st.subheader("higher training - lower chunk or not ")


#bar chart - regulatory fines by industry
fig15=px.bar(df,x='Industry',y='Regulatory_Fine_Million_USD',
            title='regulatory fines by industry',
            labels={'Industry':'Industry','Regulatory_Fine_Million_USD':'Regulatory_Fine_Million_USD'},
             color_discrete_sequence=["#c57d12"],
             template='plotly_dark'
)
st.plotly_chart(fig15)
st.subheader("shows which sector face the heaviest penalties.")


#scatter plot - stock impact % vs inancial impact
fig16=px.scatter(df,x='Financial_Impact_Million_USD',y='Stock_Impact_Percent',
             color='Attack_Vector',
             size='Security_Training_Hours'
)
st.plotly_chart(fig16)
st.subheader("does financial loss lead to stock price drops ?")



#bar chart- customer churn % by attack type
fig17=px.bar(df,x='Attack_Type',y='Customer_Churn_Percent',
            title='incident severity vs records compromised',
            labels={'Attack_Type':'Attack_Type','Customer_Churn_Percent':'Average Customer_Churn_Percent'},
             color_discrete_sequence=["#c51245"],
             template='plotly_dark'
)
st.plotly_chart(fig17)
st.subheader("reveals which attack type customer away most. ")


#reputation score changes by industry
fig18=px.bar(df, x='Industry',y='Reputation_Score_Change',
            title='incident severity vs records compromised',
            labels={'Industry':'Industry','Reputation_Score_Change':'Reputation_Score_Change'},
            color_discrete_sequence=["#a1c512"],
            template='plotly_dark'
)
st.plotly_chart(fig18)
st.subheader("negative values = brand damage")


