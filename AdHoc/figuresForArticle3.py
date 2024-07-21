import plotly.graph_objects as go
from plotly.subplots import make_subplots

from ReportProcessing.intradayDetailReport import read_intraday_details
from Util.datesAndTimestamps import timestamp
from Util.pathsAndStockSets import set_stock_set, StockSet

set_stock_set(StockSet.SP500)

# Show two (successful) examples of Higher Highs; Lower Lows
if True:
    intraday_details = read_intraday_details(timestamp('2024-06-03'))
    triggered_cases = [('PODD', '09:35:00', '09:45:00'), ('MRNA', '09:30:00', '09:40:00')]
    fig = make_subplots(rows=1, cols=len(triggered_cases))
    for i, triggered_case in enumerate(triggered_cases):
        figure_details = intraday_details[(intraday_details['symbol'] == triggered_case[0])
                                          & (intraday_details['time'] >= triggered_case[1])
                                          & (intraday_details['time'] <= triggered_case[2])]
        candlestick = go.Candlestick(x=figure_details['timestamp'], open=figure_details['open'],
                                     high=figure_details['high'], low=figure_details['low'],
                                     close=figure_details['close'], name=triggered_case[0])
        fig.add_trace(candlestick, row=1, col=i+1)
    fig.show()

# Show those examples of Higher Highs; Lower Lows over a longer time window
if True:
    intraday_details = read_intraday_details(timestamp('2024-06-03'))
    triggered_cases = [('PODD', '09:30:00', '10:30:00', timestamp('2024-06-03 09:47:30')),
                       ('MRNA', '09:30:00', '10:30:00', timestamp('2024-06-03 09:42:30'))]
    fig = make_subplots(rows=1, cols=len(triggered_cases))
    for i, triggered_case in enumerate(triggered_cases):
        figure_details = intraday_details[(intraday_details['symbol'] == triggered_case[0])
                                          & (intraday_details['time'] >= triggered_case[1])
                                          & (intraday_details['time'] <= triggered_case[2])]
        candlestick = go.Candlestick(x=figure_details['timestamp'], open=figure_details['open'],
                                     high=figure_details['high'], low=figure_details['low'],
                                     close=figure_details['close'], name=triggered_case[0])
        fig.add_trace(candlestick, row=1, col=i+1)
        fig.add_vline(triggered_case[3], row=1, col=i+1)
    fig.show()
