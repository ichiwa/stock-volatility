import datetime
import jsm
import warnings
import math

warnings.filterwarnings('ignore')


def get_stock_info(code, start, end):
  q = jsm.Quotes()
  histories = []
  api_result = q.get_historical_prices(code, jsm.MONTHLY, start, end)
  api_result.reverse()
  forVariance = 0

  # print('{0}, {1}, {2}'.format('日時', '終値', '収益率'))
  for index, priceData in enumerate(api_result):
    if (index != 0):
      oldPriceData = api_result[index-1]
      rateChange = round(((priceData.close / oldPriceData.close) * 100) - 100, 2)
      forVariance += pow(rateChange, 2)
      histories.append({
        'datetime': priceData.date.strftime('%Y/%m'),
        'close': int(round(priceData.close, 2)),
        'rateChange': rateChange,
      })

  variance = forVariance/len(api_result)
  volatility = round(math.sqrt(variance), 2)
  # print('volatlity: {0}%'.format(volatility))
  histories.reverse()
  return {
    'volatility': volatility,
    'histories': histories,
  }


if __name__ == "__main__":
  print("called")
