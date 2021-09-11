import pandas as pd
import numpy as np 

#### Insert and concat

df_1 = pd.read_csv('D:/@Test/#Sale_Inside/# Raw/20Q2.csv')
df_2 = pd.read_csv('D:/@Test/#Sale_Inside/# Raw/20Q3.csv')
df_3 = pd.read_csv('D:/@Test/#Sale_Inside/# Raw/20Q4.csv')
df_4 = pd.read_csv('D:/@Test/#Sale_Inside/# Raw/21Q1.csv')
df_5 = pd.read_csv('D:/@Test/#Sale_Inside/# Raw/21Q2.csv')
df_6 = pd.read_csv('D:/@Test/#Sale_Inside/# Raw/21Q3.csv')


frames = [df_1,df_2,df_3,df_4,df_5,df_6]
all_data_df = pd.concat(frames, axis=0)
print(all_data_df['Detail'].head(3))

#### Pivot function

# sale_df = pd.pivot_table(all_data_df, index = ['AM','Report SKUs'], columns = ['Năm','Tháng'], values = ['Total'], aggfunc  = 'sum').reset_index()

sale_df = pd.pivot_table(all_data_df, index = ['Tỉnh/thành phố','Mã KH','Năm','Tháng'], values = ['Total'], aggfunc  = 'sum').reset_index()

# # region = sale_df['Region'].unique().tolist()

# # print(region)

# # tháng = sale_df['Tháng'].unique().tolist()

# # print(tháng)

# # sale_df['Count_Active_Detail'] = sale_df['Mã NPP'].astype(str)+sale_df['Năm'].astype(str)+sale_df['Tháng'].astype(str)+" "+sale_df['Detail'].astype(str)
# # sale_df['Count_Active_SKUs'] = sale_df['Mã NPP'].astype(str)+sale_df['Năm'].astype(str)+sale_df['Tháng'].astype(str)+" "+sale_df['SKUs'].astype(str)
# sale_df['Count_Active_Report_SKUs'] = sale_df['Mã NPP'].astype(str)+sale_df['Năm'].astype(str)+sale_df['Tháng'].astype(str)+" "+sale_df['Report SKUs'].astype(str)
# # sale_df['Count_Active_TTL_FC'] = sale_df['Mã NPP'].astype(str)+sale_df['Năm'].astype(str)+sale_df['Tháng'].astype(str)

sale_df_new = sale_df[sale_df['Tỉnh/thành phố'].isin(['Tỉnh Đồng Nai','Tỉnh Bình Dương'])]

# # print(sale_df)

# # value_count_Active_Detail = sale_df['Count_Active_Detail'].value_counts()
# # value_count_Active_SKUs = sale_df['Count_Active_SKUs'].value_counts()
# value_count_Active_Report_SKUs = sale_df['Count_Active_Report_SKUs'].value_counts()
# # value_count_Active_TTL_FC = sale_df['Count_Active_TTL_FC'].value_counts()

# # print(value_count_Active_Detail)
# # print(value_count_Active_SKUs)
# # print(value_count_Active_Report_SKUs)
# # print(value_count_Active_TTL_FC)

print(sale_df_new)

# sale_df_new.to_excel('AM Dụng.xlsx')

# value_count_Active_Report_SKUs.to_excel('Active_Report_SKUs.xlsx')

