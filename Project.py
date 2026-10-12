#A Computer Engineering laboratory wants a small monitoring program for simulated device-temperature readings. The program must store the readings, accept additional valid readings, classify each reading, compute a numerical summary, and decide the overall device status. The program must be modular.

readings = [28, 31, 35, 37, 29]
def get_initial_readings(readings):
    return readings

def classify_reading(reading):
    """Classify a temperature reading"""
    if reading < 30:
        return "NORMAL" 
    elif reading <= 35:
        return "WARNING"
    else:
        return "CRITICAL"














