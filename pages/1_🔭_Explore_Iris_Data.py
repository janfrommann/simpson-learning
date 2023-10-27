import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from sklearn.datasets import load_iris
from sklearn.linear_model import LinearRegression

def create_plots(sample_sizes):
    # Load and prepare data
    iris = load_iris()
    data = pd.DataFrame(data=np.c_[iris['data'], iris['target']], columns=iris['feature_names'] + ['target'])
    data['species'] = data['target'].map({0: 'setosa', 1: 'versicolor', 2: 'virginica'})

    # Sample data based on the slider values
    sampled_data = pd.DataFrame()
    for target, species in enumerate(['setosa', 'versicolor', 'virginica']):
        sampled_data = pd.concat([sampled_data, data[data['species'] == species].sample(sample_sizes[species])])

    # For total view
    fig_total = px.scatter(sampled_data, x='sepal width (cm)', y='petal width (cm)', color='species',
                           labels={'species': 'Species'}, title='Aggregate View')

    X_total = sampled_data['sepal width (cm)'].values.reshape(-1, 1)
    y_total = sampled_data['petal width (cm)']
    model_total = LinearRegression().fit(X_total, y_total)
    line_x = np.linspace(X_total.min(), X_total.max(), 100)
    line_y = model_total.predict(line_x.reshape(-1, 1))
    fig_total.add_scatter(x=line_x, y=line_y, mode='lines', name='Total Regression', line=dict(color="royalblue"))

    # For subcategory view
    fig_subcat = px.scatter(sampled_data, x='sepal width (cm)', y='petal width (cm)', color='species',
                            labels={'species': 'Species'}, title='Disaggregate View')
    for target, species in enumerate(['setosa', 'versicolor', 'virginica']):
        X_sub = sampled_data[sampled_data['species'] == species]['sepal width (cm)'].values.reshape(-1, 1)
        y_sub = sampled_data[sampled_data['species'] == species]['petal width (cm)']
        model_sub = LinearRegression().fit(X_sub, y_sub)
        line_y_sub = model_sub.predict(X_sub)
        fig_subcat.add_scatter(x=X_sub.reshape(-1,), y=line_y_sub, mode='lines',
                               name=f'{species} Regression', line=dict(dash='dash'))

    return fig_total, fig_subcat

# Streamlit app starts here
st.title('Iris Flower Data Explorer')

st.write("""
Explore the Iris Flower dataset with different sample sizes for each species.
Below you can see two views: The total view with aggregate data and the subcategory (disaggregate) view with data divided by the three Iris species.
""")

# Slider to select sample sizes
st.sidebar.header('Set Sample Sizes')
sample_sizes = {
    'setosa': st.sidebar.slider('Setosa sample size', 1, 50, 50),
    'versicolor': st.sidebar.slider('Versicolor sample size', 1, 50, 50),
    'virginica': st.sidebar.slider('Virginica sample size', 1, 50, 50)
}

# Generate and display the plots based on current settings
fig_total, fig_subcat = create_plots(sample_sizes)
st.plotly_chart(fig_total)
st.plotly_chart(fig_subcat)
