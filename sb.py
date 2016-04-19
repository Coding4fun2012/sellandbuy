import tushare as ts
import pandas as pd

df= ts.get_tick_data('002268',date='2016-04-19').sort_index(ascending=False)
dff = df[df.change != "--"]
dffu = dff[dff.change.astype(float) > 0.05]
dffd = dff[dff.change.astype(float) < -0.05]
dffu.to_csv("odffu.csv")
dffd.to_csv("odffd.csv")
print(dffu[2:].change.astype(float).sum())
print(dffd.change.astype(float).sum())
#print(pd.rolling_sum(dffu[:-1].change.astype(float),100))
#pd.rolling_sum(dffu[:-1].change.astype(float),100).to_excel("1.excel")
pdu = pd.DataFrame(pd.rolling_sum(dffu[2:].change.astype(float),100), columns=['change'])
pdu.to_csv("dffu.csv")

pdd = pd.DataFrame(pd.rolling_sum(dffd[2:].change.astype(float),100), columns=['change'])
pdd.to_csv("dffd.csv")

pdf = pd.DataFrame(pd.rolling_sum(dff[2:].change.astype(float),100), columns=['change'])
pdf.to_csv("dff.csv")

df.to_csv("df.csv")
