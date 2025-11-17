# 1->> scatter plotly

import plotly.express as px
import pandas as pd

df =pd.DataFrame({
    "age" : [23,44,55,66,77,88],
    "salary" : [4000,5000,6000,7000,8000,9000]
})

chart=px.scatter(df,x="age",y="salary",title="age vs salary")
chart.show()

import pandas as pd
import plotly.express as px

data=pd.DataFrame({
    'length' : [20,30,40,50,60,70],
    'width' : [20,11,37,13,44,15],
    'shape' : ["box","rectangle","box","box","rectangle","rectangle"]
})

fig=px.scatter(data,x="length",y="width",color="shape",title="scatter with color")
fig.show()

scat = px.scatter(data,x="length",y="width",size="width",hover_data=["length",'width','shape'],title="hight vs width by size and hover")
scat.show()

import pandas as pd
import plotly.express as px

data=pd.DataFrame({
    'length' : [20,30,40,50],
    'width' : [20,30,40,50],
    'shape' : ["box","box","rectangle","rectangle"]
})



scat = px.scatter_3d(data,x="length",y="width",z="shape",size="width",color="shape")
scat.show()




# 2->> line plot

import plotly.express as px
import pandas as pd
salary = [20000,30000,40000,50000]
age= [20,21,22,23]
fig = px.line(x=age,y=salary,title="age vs salary")
fig.show()

epochs = [1, 2, 3, 4, 5]
accuracy = [0.5, 0.6, 0.7, 0.75, 0.8]
fig = px.line(x=epochs, y=accuracy, labels={'x':'Epoch', 'y':'Accuracy'}, title='Model Accuracy')
fig.show()

epochs = [1, 2, 3, 4, 5]
accuracy_1 = [0.5, 0.6, 0.7, 0.75, 0.8]
accuracy_2 = [0.3,0.5,0.9,0.7,0.4]
fig = px.line(x=epochs, y=[accuracy_1,accuracy_2],labels={'x':'Epoch', 'y':'Accuracy'}, title='Model Accuracy')
fig.show()



# 3->> bar chart

import plotly.express as px
import pandas as pd
data = pd.DataFrame({
    "fruits" : ['banana','apple','mango','orange'],
    "prices" : [400,600,800,230]
})
fig=px.bar(data,x="fruits",y="prices",title="fruits vs prices ")
fig.show()

import plotly.express as px
import pandas as pd
data = pd.DataFrame({
    "fruits" : ['banana','apple','mango','orange'],
    "prices" : [400,600,800,230],
    "region" : ["east","west","west","east"]
})
fig=px.bar(data,x="fruits",y="prices",color="region",title="fruits vs prices ")
fig.show()



# 3->> histogram
import plotly.express as px
import pandas as pd

data = pd.DataFrame({
    "fruits" : ['banana','apple','mango','orange'],
    "prices" : [400,600,800,230]
})

fig=px.histogram(data,x="fruits",y="prices",title="fruits vs prices ")
fig.show()

import plotly.express as px
import pandas as pd

data = pd.DataFrame({
    "fruits" : ['banana','apple','mango','orange'],
    "prices" : [400,600,800,230]
})

fig=px.histogram(data,x="fruits",color="prices",nbins=3,title="fruits vs prices ")
fig.show()

#4->>  pie

import plotly.express as px
import pandas as pd

data = pd.DataFrame({
    "fruits" : ['banana','apple','mango','orange','grapes'],
    "prices" : [40,60,80,20,90]
})

fig=px.pie(data,names="fruits",values="prices",title="fruits vs prices ")
fig.show()

# 5-->> box
import plotly.express as px
import pandas as pd

data = pd.DataFrame({
    "fruits" : ['banana','apple','mango','orange','grapes'],
    "prices" : [40,60,80,20,90]
})

fig=px.box(data,x="fruits",y="prices",title="fruits vs prices ")
fig.show()

