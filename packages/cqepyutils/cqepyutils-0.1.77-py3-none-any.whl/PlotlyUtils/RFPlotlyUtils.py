import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
from robot.api.deco import keyword
from robot.api import logger


@keyword('Visualize Data')
def visualize_data(*dataframes, x_col: str, y_col: str,
                   plot_type: str = 'bar', titles: list = None, plot_name: str = 'Trace') -> None:
    """
    Visualizes query results as a plot and displays them as a DataFrame.

    Args:
        *dataframes (pd.DataFrame): Variable number of Pandas DataFrames.
        x_col (str): The name of the column to use for the x-axis of the plot.
        y_col (str): The name of the column to use for the y-axis of the plot.
        plot_type (str, optional): The type of plot to use. Default is 'bar', but can be 'line', 'scatter', etc.
        titles (list, optional): A list of titles for each table. Default is None.
        plot_name (str, optional): The name of the trace in the plot. Default is 'Trace'.

    Examples:
        | *Keyword*          | *Arguments*                                                               |
        | `Visualize Data`   | dataframe=x, dataframe2=y, x_col=column_name_1, y_col=column_name_2, plot_type='bar', titles=['Table 1', 'Table 2'], plot_name='Trace' |
        | `Visualize Data`   | dataframe=x, dataframe2=y, x_col=column_name_3, y_col=column_name_4, plot_type='scatter', titles=['Table A', 'Table B'], plot_name='Data' |
        | `Visualize Data`   | dataframe=x, dataframe2=y, x_col=column_name_5, y_col=column_name_6, plot_type='line', titles=['Table X', 'Table Y'], plot_name='Line Data' |
    """

    num_dataframes = len(dataframes)

    if titles is None or len(titles) != num_dataframes:
        titles = ['Table {}'.format(i + 1) for i in range(num_dataframes)]

    logger.info(f'Step - 1: Starting data visualization for {num_dataframes} dataframes.')

    if num_dataframes == 1:
        # If only one dataframe is provided, display it in the center
        fig = go.Figure(data=[go.Table(
            header=dict(values=[col.replace('_', ' ').capitalize() for col in dataframes[0].columns],  # Modify headers
                        fill_color='rgb(30, 53, 76)',
                        font=dict(color='white')),
            cells=dict(values=dataframes[0].T.applymap(lambda x: f'<b>{x}</b>').values.tolist(),  # Center-align values
                       fill_color=[[['#f2f2e8', '#ffffff'][i % 2] for i in range(len(dataframes[0]))]],
                       font=dict(color='black'))
        )])
        fig.update_layout(title=titles[0])
    else:
        # If multiple dataframes are provided, create subplots in a grid layout
        num_rows = (num_dataframes + 1) // 2
        fig = make_subplots(rows=num_rows, cols=2, specs=[[{'type': 'domain'}, {'type': 'domain'}]] * num_rows)

        for i, (dataframe, title) in enumerate(zip(dataframes, titles)):
            row = (i // 2) + 1
            col = (i % 2) + 1

            table = go.Table(
                header=dict(values=[col.replace('_', ' ').capitalize() for col in dataframe.columns],  # Modify headers
                            fill_color='rgb(30, 53, 76)',
                            font=dict(color='white')),
                cells=dict(values=dataframe.T.applymap(lambda x: f'<b>{x}</b>').values.tolist(),  # Center-align values
                           fill_color=[[['#f2f2e8', '#ffffff'][i % 2] for i in range(len(dataframe))]],
                           font=dict(color='black'))
            )

            fig.add_trace(table, row=row, col=col)
            fig.update_xaxes(title_text=title, row=row, col=col)  # Update x-axis title
            fig.update_yaxes(title_text='', row=row, col=col)  # Remove y-axis title

    # Update layout
    fig.update_layout(
        height=500 * ((num_dataframes + 1) // 2) if num_dataframes > 1 else 500,
        margin=dict(t=50, l=50, r=50),
    )
    fig.show()
    logger.info(f'Step - 2: Data visualization complete for {num_dataframes} dataframes.')


@keyword('Visualize Charts with Tables')
def visualize_charts_with_tables(*dataframes, x_col: str, y_col: str, chart_title: str = 'Chart', table_title: str = 'Table') -> None:
    """
    Visualizes charts and displays corresponding DataFrames side by side.

    Args:
        *dataframes (pd.DataFrame): Variable number of Pandas DataFrames.
        x_col (str): The name of the column to use for the x-axis of the chart.
        y_col (str): The name of the column to use for the y-axis of the chart.
        chart_title (str, optional): The title of the chart. Default is 'Chart'.
        table_title (str, optional): The title of the table. Default is 'Table'.
    """

    num_dataframes = len(dataframes)

    # Create subplots for charts
    fig = make_subplots(rows=1, cols=num_dataframes, subplot_titles=[f'Chart {i + 1}' for i in range(num_dataframes)])

    for i, dataframe in enumerate(dataframes):
        chart = px.bar(dataframe, x=x_col, y=y_col, title=f'Chart {i + 1}')
        fig.add_trace(chart.data[0], row=1, col=i + 1)

    # Create subplots for tables
    table_fig = make_subplots(rows=1, cols=num_dataframes, subplot_titles=[f'Table {i + 1}' for i in range(num_dataframes)])

    for i, dataframe in enumerate(dataframes):
        table = go.Figure(data=[go.Table(
            header=dict(values=[col.replace('_', ' ').capitalize() for col in dataframe.columns],
                        fill_color='rgb(30, 53, 76)',
                        font=dict(color='white')),
            cells=dict(values=dataframe.T.applymap(lambda x: f'<b>{x}</b>').values.tolist(),
                       fill_color=[[['#f2f2e8', '#ffffff'][i % 2] for i in range(len(dataframe))]],
                       font=dict(color='black'))
        )])

        table_fig.add_trace(table.data[0], row=1, col=i + 1)

    # Update layout
    fig.update_layout(title_text=chart_title, showlegend=False)
    table_fig.update_layout(title_text=table_title, showlegend=False)

    # Display figures
    fig.show()
    table_fig.show()

    logger.info('Charts and tables visualization complete.')
