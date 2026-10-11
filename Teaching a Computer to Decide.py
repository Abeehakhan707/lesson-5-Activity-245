import matplotlib.pyplot as plt

weights = [2.5, 3.0, 4.5, 5.0, 6.5, 7.0, 8.0, 9.5]
height = [20, 22, 25, 27, 40, 42, 45, 48]
labels = ["cat", "cat", "cat", "cat", "dog", "dog", "dog", "dog"]

for w, h, l in zip(weights, height, labels):
    print(f"Weight: {w} kg, Height: {h} cm, Label: {l}")

def rule_based_classifier(weight, height):
    if weight < 6.0 and height < 30:
        return "cat"
    else:
        return "dog" 

print(rule_based_classifier(5.0, 25))
print(rule_based_classifier(7.0, 45))

cat_height_avg = (20 + 22 + 25 + 27) / 4
dog_height_avg = (40 + 42 + 45 + 48) / 4

print(f"Average height of cats: {cat_height_avg} cm")
print(f"Average height of dogs: {dog_height_avg} cm")

cat_weight_avg = (2.5 + 3.0 + 4.5 + 5.0) / 4
dog_weight_avg = (6.5 + 7.0 + 8.0 + 9.5) / 4

print(f"Average weight of cats: {cat_weight_avg} kg")
print(f"Average weight of dogs: {dog_weight_avg} kg")

def ai_classifier(weight, height):
    distance_to_cat = abs((weight - cat_weight_avg) ** 2 + (height - cat_height_avg) ** 2) ** 0.5
    distance_to_dog = abs((weight - dog_weight_avg) ** 2 + (height - dog_height_avg) ** 2) ** 0.5

    if distance_to_cat < distance_to_dog:
        return "cat"
    else:
        return "dog"

new_animal = [(5.2, 29),(6.8,33),(4.8,31)]    
for w,h in new_animal:
    rule_prediction = rule_based_classifier(w,h)
    ai_prediction = ai_classifier(w,h)
    print(f"Weight: {w} kg, Height: {h} cm, Rule-based: {rule_prediction}, AI-based: {ai_prediction}")
    plt.figure(figsize=(6, 5))
    colors = ['steelblue' if label == 'cat' else 'orange' for label in labels]
    plt.scatter(weights, height, c=colors, s=80, label='training data')

for w, h in new_animal:
    plt.scatter(w, h, c="red", marker='x', s=100)
plt.xlabel('weight (kg)')    
plt.ylabel('height (cm)')
plt.title('Animal Classification')
plt.legend()
plt.show()