def calculate_total_units_sold(units_sold):
    return sum(units_sold)

def find_highest_sales(flower_names, units_sold):
    max_sales_index = units_sold.index(max(units_sold))
    return flower_names[max_sales_index]

def find_above_average_reviews(flower_names, customer_reviews):
    above_avg = []
    for i in range(len(flower_names)):
        if customer_reviews[i] > 3:
            above_avg.append(flower_names[i])
    return above_avg

def average_review_score(customer_reviews):
    return sum(customer_reviews) / len(customer_reviews)

def below_average_sales(flower_names, units_sold, customer_reviews):
    below_avg = []
    avg_sales = sum(units_sold) / len(units_sold)
    for i in range(len(flower_names)):
        if units_sold[i] < avg_sales:
            below_avg.append((flower_names[i], units_sold[i], customer_reviews[i]))
    return below_avg

# Dataset of flower names, units sold, and customer reviews
flower_names = ["Orchid", "Tulip", "Daisy", "Sunflower", "Rose", "Carnation", "Daffodil", "Peony", "Lily",
                "Cactus", "Lotus", "Camellia", "Jasmine", "Chrysanthemum", "Marigold", "Anemone", "Pansy",
                "Lavender", "Dahlia", "Hibiscus",]

units_sold = [170, 180, 90, 60, 250, 150, 110, 80, 150, 130, 50, 160, 70, 140, 130, 180, 190, 70, 60, 150]

customer_reviews = [4.3, 3.1, 3.9, 4.1, 4.2, 3.8, 4.0, 4.4, 4.6, 3.4, 4.5, 3.9, 4.3, 3.5, 4.1, 3.8, 4.0, 4.2, 4.3, 4.3]

# Calculate total units sold
print("\nTotal Units Sold:", calculate_total_units_sold(units_sold))

# Find flowers with the highest sales
print("\nFlower with Highest Sales:", find_highest_sales(flower_names, units_sold))

# Find flowers with above-average customer reviews
print("\nFlowers with Above-Average Customer Reviews:")
above_avg_reviews = find_above_average_reviews(flower_names, customer_reviews)
for flower in above_avg_reviews:
    print(flower)

print("\nAverage Customer Review Score:", average_review_score(customer_reviews))

print("\nFlowers with Below-Average Sales:")
below_avg_sales = below_average_sales(flower_names, units_sold, customer_reviews)
for flower in below_avg_sales:
    print("Name:", flower[0], "| Units Sold:", flower[1], "| Customer Reviews:", flower[2])
