# q9; print new version of given str that ends just before word 'house'
advice = "Few things in life are as important as house training your pet dinosaur."
# ==> 'Few things in life are as important as'

print(advice[:advice.find('house')])

# actual solution used advice.split("house")[0]