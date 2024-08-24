#2469. Convert the Temperature
class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        K = celsius + 273.15
        F = celsius * 1.8 + 32.0
        return [K, F]
