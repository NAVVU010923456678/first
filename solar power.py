from prophet import Prophet

# Load solar data (irradiance vs time)
solar_data = pd.read_csv("solar_power.csv")
solar_data.rename(columns={'timestamp':'ds','power':'y'}, inplace=True)

model = Prophet()
model.fit(solar_data)

future = model.make_future_dataframe(periods=24, freq='H')
forecast = model.predict(future)

# Forecast solar power
def forecast_solar_next_hours(hours=6):
    return forecast[['ds','yhat']].tail(hours)
