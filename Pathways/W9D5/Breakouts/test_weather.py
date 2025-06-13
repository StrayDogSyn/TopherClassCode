#!/usr/bin/env python3
"""
Simple test script to verify the weather data analysis works
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Test loading the data
print("Loading weather data...")
weather_data = pd.read_csv(r'c:\Users\Petro\repos\python\TPS25\Pathways\W5D5\Breakouts\weather_data.csv')

print("First 5 rows:")
print(weather_data.head())

print("\nDataset shape:", weather_data.shape)
print("Column names:", list(weather_data.columns))

print("\nScript completed successfully!")
