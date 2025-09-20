# 1 liter diesel ≈ 2.68 kg CO2
DIESEL_CO2_FACTOR = 2.68  

def calculate_carbon_credits(saved_energy_kwh, diesel_efficiency_l_kwh):
    diesel_saved = saved_energy_kwh / diesel_efficiency_l_kwh
    carbon_saved = diesel_saved * DIESEL_CO2_FACTOR
    return carbon_saved
