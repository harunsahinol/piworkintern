UPDATE daily_vaccinations d1
SET daily_vaccinations = (
  SELECT MEDIAN(d2.daily_vaccinations)
  FROM daily_vaccinations d2
  WHERE d2.country = d1.country
WHERE daily_vaccinations IS NULL;
