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
st.markdown("shows which attack (eg:ransomware, phishing) is most common")

#Bar chart - attack vector frequeny
fig2=px.bar(df,x='Attack_Vector', y='Previous_Incidents',
                  title='attack vector frequency',
                  labels={'Company_Name':'company'},
                  color_discrete_sequence=['#F39C12'],
                  template='plotly_dark'
)
st.plotly_chart(fig2)
st.markdown("highlights weak entry points like email,web apps,unpatched systems.")


#stacked bar chart - industry vs attack type
fig3=px.bar(df, x='Industry',y='Previous_Incidents',
                 title='country wise attack',
                 color='Attack_Type',barmode='stack',
                 template='plotly_dark'
)
st.plotly_chart(fig3)
st.markdown("shows which industries are most affected by which attacks.")


#timeline
fig4=px.line(df,x='Date_Reported',y='Previous_Incidents',
                 title='incidents by date_reported'
)
st.plotly_chart(fig4)

#records compromised by industry
fig5=px.bar(df,x='Industry',y='Records_Compromised',
      title='records compromised by industry',
)
st.plotly_chart(fig5)
st.markdown("reveals which industries leak the most customer data")

#ransom amount vs recovery time
fig6=px.scatter(df,x='Ransom_Amount_USD',y='Recovery_Time_Days',
                color='Attack_Type',
                size='Recovery_Time_Days'
)
st.plotly_chart(fig6)

#barchart incident severity and records compromised
fig7=px.bar(df,x='Incident_Severity',y='Records_Compromised',
            title='incident severity vs records compromised',
)
st.plotly_chart(fig7)


#bar chart patch status vs average severity
fig8=px.bar(df,x='Patch_Status',y='Incident_Severity',
            title='patch status vs average severity',
)
st.plotly_chart(fig8)


fig9=px.bar(df,x='Incident_Severity',y='Records_Compromised',
            title='incident severity vs records compromised',
)



fig10=px.bar(df,x='Incident_Severity',y='Records_Compromised',
            title='incident severity vs records compromised',
)




fig11=px.bar(df,x='Incident_Severity',y='Records_Compromised',
            title='incident severity vs records compromised',
)



