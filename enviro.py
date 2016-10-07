from envirophat import light, weather

def get_environment():
    return {'temp': weather.temperature(), 'atm': weather.pressure(), 'light': light.light()}

if __name__ == '__main__':
    print get_environment()
