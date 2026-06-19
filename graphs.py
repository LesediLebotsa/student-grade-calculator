from matplotlib import pyplot as plt
from services.student_analytics import module_averages

def show_module_chart():
    averages = module_averages()

    plt.figure(figsize=(8, 5))
    plt.bar(
        averages.keys(),
        averages.values()
    )
    plt.title("Average Grade per module")
    plt.ylabel("Average Grade")
    plt.xticks(rotation=30, ha="right")

    plt.tight_layout()
    plt.show()

    average = dict(
        sorted(
            averages.items(),
            key=lambda x: x[1],
            reverse=True
        )
    )



